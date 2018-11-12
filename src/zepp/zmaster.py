import logging

from pika.exceptions import AMQPError

from zepp import zclient
from zepp import zerrors

logger = logging.getLogger(__name__)


def domain_check(domain_name, raise_errors=False, return_string=False, return_response=False, ):
    """
    Return True (domain exist), False (domain not exist), None (if error) or string (with error message).
    If return_response==True always return EPP response as dictionary.
    If raise_errors==True always raise exceptions in case of errors.
    If return_string==True always return error message as string in case of errors.
    """
    try:
        check = zclient.cmd_domain_check([domain_name, ], )
    except AMQPError as exc:
        if raise_errors:
            raise zerrors.EPPCommandFailed(str(exc))
        if return_string:
            return 'request failed, connection broken: %s' % exc
        return None
    except Exception as exc:
        if raise_errors:
            raise zerrors.EPPCommandFailed(str(exc))
        if return_string:
            return 'request failed, unknown error: %s' % exc
        return None
    try:
        if check['epp']['response']['result']['@code'] != '1000':
            if raise_errors:
                raise zerrors.EPPCommandFailed('EPP domain_check failed with error code: %s' % (
                    check['epp']['response']['result']['@code'], ))
            if return_response:
                return check
            if return_string:
                return 'request failed, error code: %s' % check['epp']['response']['result']['@code']
            return None
        if check['epp']['response']['resData']['chkData']['cd']['name']['@avail'] == '1':
            if return_response:
                return check
            if return_string:
                return 'not exist'
            return False
    except KeyError as exc:
        if return_response:
            return check
        if return_string:
            return 'request failed, unexpected field in response: %s' % exc
        return False
    if return_response:
        return check
    if return_string:
        return 'exist'
    return True


def domain_info(domain_name, auth_info=None, raise_errors=False, return_string=False):
    """
    Send domain_info EPP command and returns result response.
    """
    try:
        info = zclient.cmd_domain_info(domain_name, auth_info=auth_info)
    except AMQPError as exc:
        if raise_errors:
            raise zerrors.EPPCommandFailed(str(exc))
        if return_string:
            return 'domain info request failed, connection broken: %s' % exc
        return None
    except Exception as exc:
        if raise_errors:
            raise zerrors.EPPCommandFailed(str(exc))
        if return_string:
            return 'domain info request failed, unknown error: %s' % exc
        return None
    if info['epp']['response']['result']['@code'] != '1000':
        if raise_errors:
            raise zerrors.EPPCommandFailed('EPP domain_info failed with error code: %s' % (
                info['epp']['response']['result']['@code'], ))
        if return_string:
            return 'domain info request failed with error code: %s' % info['epp']['response']['result']['@code']
        return None
    # TODO: ...
    return {}
        

def domain_register(domain_name):
    """
    """
