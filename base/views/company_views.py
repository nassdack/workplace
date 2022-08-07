import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from base.models import Company
from . import mixins

class IndexListView(mixins.MonthCalendarMixin,ListView):
    model = Company
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'pages/company.html'

class MonthCalendar(mixins.MonthCalendarMixin,TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'snippets/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

class WeekCalendar(mixins.WeekCalendarMixin,TemplateView):
    """週間カレンダーを表示するビュー"""
    template_name = 'snippets/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context