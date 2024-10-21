from datetime import date, time, datetime, timedelta, timezone
import zoneinfo, dateutil.tz
timezone.utc 

print(datetime.now(timezone.utc))