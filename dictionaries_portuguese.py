 # coding=utf-8
 
import calendar

days_of_week_pt=['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira','sexta-feira','sábado','domingo']
days_of_month_pt=['janeiro','fevereiro', 'março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

days_of_month_en=[month for month in calendar.month_name]
days_of_week_en=[day for day in calendar.day_name]

days_of_month=dict(zip(days_of_month_pt, days_of_month_en[1:]))
days_of_week=dict(zip(days_of_week_pt, days_of_week_en))

