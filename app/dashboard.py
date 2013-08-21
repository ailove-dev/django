# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.Group(
            title= 'Administration',
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    title='Users',
                    models=('django.contrib.*',)
                )
            ]
        ))

        self.children.append(modules.LinkList(
            'Media',
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=True,
            column=3,
        ))
