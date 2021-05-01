from datetime import datetime, timedelta

# dt =datetime.now()
# start = dt - timedelta(days=dt.isoweekday())
# start = start.replace(hour = 0, minute=0, second=0, microsecond=0).astimezone().isoformat()
# print(start)

from pandas import *
df = DataFrame({'foo1' : np.random.randn(2), 'foo2' : np.random.randn(2)})
html = df.to_html()
print(html)