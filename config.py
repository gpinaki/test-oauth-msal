class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # TODO: Enter your client secret from Azure AD below
    CLIENT_SECRET = "W9KJ~99GBu12jcc52eBgu-rkgGxh_lO3s." 

    #AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    AUTHORITY = "https://login.microsoftonline.com/f361aa85-dea5-43b7-b416-9fc9b06229a8"

    # TODO: Enter your application client ID here
    CLIENT_ID = "d0fe709e-c968-4857-90c4-7818dd9ead64"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAtoken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session