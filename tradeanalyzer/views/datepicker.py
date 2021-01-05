from datetime import datetime

class DatePicker:
    now_year  = 1999
    now_month = 1
    now_day   = 1
    
    def __init__(self):
        pass
    
    def __now__(self, context):
        now = datetime.now()

        self.now_year   = now.year
        self.now_month  = now.month
        self.now_day    = now.day
        context['now_year']   = self.now_year
        context['now_month']  = self.now_month
        context['now_day']    = self.now_day
        context['day_list']   = range(1,31)
        context['year_list']  = range(1990, 2025)
        context['month_list'] = range(1,12)
        
        print('year  = ' + str(self.now_year))
        print('month = ' + str(self.now_month))
        print('day   = ' + str(self.now_day))

    def __str__(self):
        print('year(' + now_year + 
              '),month(' + now_month +
              '),day(' + now_day + ')')
