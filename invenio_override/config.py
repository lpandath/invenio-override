# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Shared RDM.
#
# invenio_override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for sharedRDM theme."""

from invenio_i18n import gettext as _

INVENIO_OVERRIDE_DEFAULT_VALUE = _("TU Graz Repository")
"""Default value for the application."""

INVENIO_OVERRIDE_BASE_TEMPLATE = "invenio_override/base.html"
"""TU Graz Default base template"""

INVENIO_OVERRIDE_ACCOUNT_BASE = "invenio_override/accounts/accounts_base.html"
"""TU Graz Default account base template"""

INVENIO_OVERRIDE_ICON = "images/icon_use.png"
"""icon used in login page"""

THEME_TUGRAZ_CONTACT_FORM = False
"""Enable/Disable Contact form."""

THEME_TUGRAZ_PRODUCTION = False
"""Production environment.

    Can also be set as an environment variable in a .env file. Then the name
    has to be 'INVENIO_OVERRIDE_PRODUCTION'.
"""

# Invenio-theme
# ============
# See https://invenio-theme.readthedocs.io/en/latest/configuration.html
#

THEME_SEARCHBAR = False
"""Enable or disable the header search bar."""

THEME_HEADER_TEMPLATE = "invenio_override/header.html"
"""TU Graz header template"""

THEME_FRONTPAGE = False
"""Use default frontpage."""

THEME_HEADER_LOGIN_TEMPLATE = "invenio_override/accounts/header_login.html"
"""login page header"""

THEME_FOOTER_TEMPLATE = "invenio_override/footer.html"
"""footer template"""

THEME_FRONTPAGE_TITLE = _("TU Graz Repository")
"""Frontpage title."""

THEME_SITENAME = _("Repository")
"""Site name."""

# Invenio-accounts
# ============
# See https://invenio-accounts.readthedocs.io/en/latest/configuration.html

# COVER_TEMPLATE = 'invenio_override/accounts/accounts_base.html'
"""Cover page template for login and sign up pages."""

SECURITY_LOGIN_USER_TEMPLATE = "invenio_override/accounts/login_user.html"
"""Login template"""

SECURITY_REGISTER_USER_TEMPLATE = "invenio_override/accounts/register_user.html"
"""Sigup template"""

# Invenio-app-rdm
# =============
# See https://invenio-app-rdm.readthedocs.io/en/latest/configuration.html
SEARCH_UI_HEADER_TEMPLATE = "invenio_override/header.html"
"""Search page's header template."""

DEPOSITS_HEADER_TEMPLATE = "invenio_override/header.html"
"""Deposits header page's template."""


# Invenio-rdm-records
# =============
# See https://invenio-rdm-records.readthedocs.io/en/latest/configuration.html
# Uncomment below to override records landingpage.
# from invenio_rdm_records.config import RECORDS_UI_ENDPOINTS
# RECORDS_UI_ENDPOINTS["recid"].update(
#     template="invenio_override/record_landing_page.html"
# )
"""override the default record landing page"""

# Invenio-search-ui
# =============
# See https://invenio-search-ui.readthedocs.io/en/latest/configuration.html
# SEARCH_UI_SEARCH_TEMPLATE = "invenio_override/search.html"
# """override the default search page"""

TUG_ROUTES = {
    "index": "/",
    "comingsoon": "/comingsoon",
}


##############################################################################

INVENIO_OVERRIDE_LOGO = "images/TUG.png"
"""override logo"""

# TODO: fix it
INVENIO_OVERRIDE_FAVICON = "favicon.ico"
"""override favicon"""

INVENIO_OVERRIDE_SHIBBOLETH = False
"""Set True if SAML is configured"""

# Invenio-I18N
# ============
# See https://invenio-i18n.readthedocs.io/en/latest/configuration.html
BABEL_DEFAULT_LOCALE = "en"
# Default time zone
BABEL_DEFAULT_TIMEZONE = "Europe/Vienna"
# Other supported languages (do not include BABEL_DEFAULT_LOCALE in list).
I18N_LANGUAGES = [("de", _("German"))]
