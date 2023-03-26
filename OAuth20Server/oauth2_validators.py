from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):
    pass
    # Set `oidc_claim_scope = None` to ignore scopes that limit which claims to return,
    # otherwise the OIDC standard scopes are used.
    # oidc_claim_scope = None

    # def get_additional_claims(self, request):
    #     return {
    #         "given_name": request.user.first_name,
    #         "family_name": request.user.last_name,
    #         "name": ' '.join([request.user.first_name, request.user.last_name]),
    #         "preferred_username": request.user.username,
    #         "email": request.user.email,
    #     }
