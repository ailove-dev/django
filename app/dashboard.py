# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(modules.Group(
            title='Administration',
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
            title='Media',
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
            title=_('Recent Actions'),
            limit=5,
            collapsible=True,
            column=3,
        ))
