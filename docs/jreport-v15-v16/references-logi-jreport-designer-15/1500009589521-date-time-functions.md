---
title: "Date/Time Functions"
id: 1500009589521
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589521-Date-Time-Functions
updated_at: 2021-07-24T05:54:38Z
---

# Date/Time Functions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568202-Date-Range-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568222-Financial-Functions)

# Date/Time Functions

Date functions allow you to convert numbers to dates and dates to numbers.

Below is a list of the date/time functions used in Logi JReport Designer:

> * [CurrentDate()](#CurrentDate)
> * [CurrentDateTime()](#CurrentDateTime)
> * [CurrentTime()](#CurrentTime)
> * [DateAdd()](#DateAdd)
> * [DateDiff()](#DateDiff)
> * [DatePart()](#DatePart)
> * [DateTimeTo2000()](#DateTimeTo2000)
> * [DateTimeToDate()](#DateTimeToDate)
> * [DateTimeToSeconds()](#DateTimeToSeconds)
> * [DateTimeToTime()](#DateTimeToTime)
> * [DateTo2000()](#DateTo2000)
> * [Day()](#Day)
> * [DayOfWeek()](#DayOfWeek)
> * [DayOfYear()](#DayOfYear)
> * [DTSTo2000()](#DTSTo2000)
> * [DTSToSeconds()](#DTSToSeconds)
> * [FirstDayOfMonth()](#FirstDayOfMonth)
> * [FirstDayOfQuarter()](#FirstDayOfQuarter)
> * [FirstDayOfWeek()](#FirstDayOfWeek)
> * [FirstDayOfYear()](#FirstDayOfYear)
> * [FirstSundayOfMonth()](#FirstSundayOfMonth)
> * [FirstSundayOfYear()](#FirstSundayOfYear)
> * [ForEachDay()](#ForEachDay)
> * [ForEachHalfMonth()](#ForEachHalfMonth)
> * [ForEachHalfYear()](#ForEachHalfYear)
> * [ForEachMonth()](#ForEachMonth)
> * [ForEachQuarter()](#ForEachQuarter)
> * [ForEachWeek()](#ForEachWeek)
> * [ForEachYear()](#ForEachYear)
> * [Hour()](#Hour)
> * [IsDate()](#IsDate)
> * [IsDateTime()](#IsDateTime)
> * [IsTime()](#IsTime)
> * [Minute()](#Minute)
> * [Month()](#Month)
> * [MonthName()](#MonthName)
> * [Now()](#Now)
> * [Quarter()](#Quarter)
> * [Second()](#Second)
> * [SelectedDate()](#SelectedDate)
> * [Timer()](#Timer)
> * [ToDate()](#ToDate)
> * [ToDateTime()](#ToDateTime)
> * [Today()](#Today)
> * [ToTime()](#ToTime)
> * [WeekdayName()](#WeekdayName)
> * [WeekFrom1970()](#WeekFrom1970)
> * [WeekOfMonth()](#WeekOfMonth)
> * [WeekOfYear()](#WeekOfYear)
> * [Year()](#Year)

## CurrentDate()

This function returns the current date on a report.

**Return value**

The return value is a date.

**Example**

If today is Oct. 6,1999, the return value of the following statement is 10/06/99.

`CurrentDate()`

## CurrentDateTime()

This function returns the current date and time on a report.

**Return value**

The return value is a DateTime.

**Example**

If today is Oct.6,1999, the current time is 5:10:27 p.m., the return value of the following statement is 1999-10-06 05:10:27 PM.

`CurrentDateTime()`

## CurrentTime()

This function returns the current time on a report.

**Return value**

The return value is a Time.

**Example**

If the current time is 5:10:27 p.m., the return value of the following statement is 05:10:27 PM.

`CurrentTime()`

## DateAdd(intervalType, nIntervals, startDateTime)

Returns a DateTime value to which a specified number of time intervals have been added.

This function is used to add interval of time to a DateTime. Its main feature is that the DateTime returned will always be valid. For example, the function takes into account such factors as the number of days in a month and leap years. If you want to add or subtract days to a DateTime, you could use the addition and subtraction operators instead of the function with the "d" parameter. However, this function also handles other types of intervals such as adding months or hours to a DateTime.

**Parameters**

* intervalType - A String expression specifying the interval of time to be added.

  | IntervalType value | Description |
  | --- | --- |
  | yyyy | Year |
  | q | Quarter (3-month period) |
  | m | Month |
  | y | Day of year |
  | d | Day |
  | w | Weekday |
  | ww | Week (7-day period) |
  | h | Hour |
  | n | Minute |
  | s | Second |
* nIntervals - A Number or numeric expression specifying the number of intervals to be added. It can be positive (to get DateTimes from the future), or negative (to get DateTimes from the past).
* startDateTime - The DateTime value to which the intervals are to be added.

**Return value**

A DateTime value.

**Examples**

* `DateAdd("yyyy",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus one year.
* `DateAdd("q",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus three months.
* `DateAdd("m",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus one month.
* `DateAdd("y",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus one day.
* `DateAdd("d",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus one day.
* `DateAdd("w",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus one day.
* `DateAdd("ww",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus seven days.
* `DateAdd("h",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus one hour.
* `DateAdd("n",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus one minute.
* `DateAdd("s",1,CurrentDateTime())` - Returns the DateTime value for current datetime plus one second.
* `DateAdd("d",-32,ToDateTime(1999,9,28))` - Returns the DateTime value 1999-8-27 00:00:00.
* `DateAdd("m",1,ToDateTime(1996,1,31))` - Returns the DateTime value 1996-2-29 00:00:00. Notice that DateAdd will not return the invalid value 1996-2-31 00:00:00.
* `DateAdd("q",17,ToDateTime(1999,9,28))` - Returns the DateTime value 2003-12-28 00:00:00.
* `DateAdd("h",-400,ToDateTime(1999,9,28))` - Returns the DateTime value 1999-9-11 08:00:00. In other words, this is the result of subtracting 400 hours from 1999-9-28 00:00:00.

**Notes**:

* To add days to a DateTime, you can use any of the interval type parameters "y", "d" or "w". They all have the same effect for DateAdd.
* DateAdd returns a DateTime value and not a Date value. However, you may need to convert this DateTime value to a Date value in certain situations (such as if you wanted to assign the value returned by DateAdd to a Date type variable). To convert to a Date value, use DateAdd in combination with the ToDate type conversion function. For example, the following returns the Date value for October 6, 1997.

  `ToDate(DateAdd("yyyy",-2,ToDateTime(1999,10,6)))`

## DateDiff(intervalType, startDateTime, endDateTime, firstDayOfWeek)

Returns a number of time intervals between two specified dates.

**Overload**

* DateDiff(intervalType, startDateTime, endDateTime)
* DateDiff(intervalType, startDateTime, endDateTime, firstDayOfWeek)

**Parameters**

* intervalType - A string expression that is the interval of time you use to calculate the difference between startDateTime and endDateTime. Possible values can be:
    

  | IntervalType value | Description |
  | --- | --- |
  | Yyyy | Year |
  | Q | Quarter |
  | M | Month |
  | Y | Day of year |
  | D | Day (both "y" and "d" find the difference in days) |
  | W | Number of weeks between startDateTime and endDateTime |
  | Ww | Number of firstDayOfWeek's between startDateTime and endDateTime |
  | H | Hour |
  | N | Minute |
  | S | Second |
* startDateTime - The first DateTime value used in calculating the difference.
* endDateTime - The second DateTime value used in calculating the difference.
* firstDayOfWeek - An optional constant specifying the first day of the week. If not specified, jrSunday will be used.
    

  | Constant | Description |
  | --- | --- |
  | jrUseSystem | 0 (Use the current system date) |
  | jrSunday | 1 |
  | jrMonday | 2 |
  | jrTuesday | 3 |
  | jrWednesday | 4 |
  | jrThursday | 5 |
  | jrFriday | 6 |
  | jrSaturday | 7 |

**Return value**

A Number value.

**Examples**

* Use DateDiff with the "d" or "y" interval type parameter to find the number of days between two dates.

  `DateDiff("d", ToDateTime(1999,10,7), ToDateTime(1999,10,10))` - Returns 3
* Use DateDiff with the "yyyy" interval type parameter to find the number of years difference between two dates. This use of DateDiff is the same as finding the difference between the year of endDateTime and the year of startDateTime.
  + `DateDiff("yyyy", ToDateTime(1999,10,7), ToDateTime(2005,2,10))` - Returns 6.
  + `DateDiff("yyyy", ToDateTime(1999,12,31), ToDateTime(2000,1,1))` - Returns 1 (a 1 year difference), even though there is only a 1 day difference between the dates.
  + `DateDiff("yyyy", ToDateTime(1999,1,1), ToDateTime(1999,12,31))` - Returns 0 (a 0 year difference), even though there is a 364 days difference.

  Suppose that for the above examples, the first date is the date that you bought a mutual fund, and the second date is the date you sold it. The mutual fund company must send you an annual report for every year in which you owned units in the fund. You would then get 7, 2 and 1 annual reports respectively, in the above cases.
* Use DateDiff with the "q" parameter to find the number of quarters (3 month periods) difference between two dates.
  + `DateDiff("q", ToDateTime(1999,10,6), ToDateTime(2003,5,20))` - Returns 14.
  + `DateDiff("q", ToDateTime(1999,3,31), ToDateTime(1999,4,1))` - Returns 1. The two dates are in adjacent quarters.
  + `DateDiff("q", ToDateTime(1999,1,1), ToDateTime(1999,3,31))` - Returns 0. The two dates are in the same quarter.

  Suppose the mutual fund company in the "yyyy" example mailed out quarterly reports. It would need to mail out 15, 2 and 1 quarterly reports respectively, in the above cases.
* Use DateDiff with the "m" parameter to find the number of months difference between two dates.

  `DateDiff("m", ToDateTime(1999,3,15), ToDateTime(1999,7,13))` - Returns 4.
* Use DateDiff with the "w" parameter to calculate the number of weeks between two dates. For example, if startDateTime is on a Tuesday, DateDiff counts the number of Tuesdays between startDateTime and endDateTime not including the initial Tuesday of startDateTime. Note however that it counts endDateTime if endDateTime is on a Tuesday.
  + `DateDiff("w", ToDateTime(1999,10,19), ToDateTime(1999,10,25))` - Returns 0.
  + `DateDiff("w", ToDateTime(1999,10,19), ToDateTime(1999, 10,26))` - Returns 1.

## DatePart(intervalType, inputDateTime, firstDayOfWeek, firstWeekOfYear)

Returns a number that specifies a given part of a given date.

**Overloads**

* DatePart(intervalType, inputDateTime)
* DatePart(intervalType, inputDateTime, firstDayOfWeek)
* DatePart(intervalType, inputDateTime, firstDayOfWeek, firstWeekOfYear)
* DatePart(intervalType, inputTime)
* DatePart(intervalType, inputTime, firstDayOfWeek)
* DatePart(intervalType, inputTime, firstDayOfWeek, firstWeekOfYear)

**Parameters**

* intervalType - A String expression that specifies the part of a date to be returned. Possible values can be:

  | IntervalType value | Description |
  | --- | --- |
  | Yyyy | Extracts the year |
  | Q | Quarter (the result is 1, 2, 3 or 4) |
  | M | Month (the result is from 1 to 12) |
  | Y | Day of year (1 to 365 or 366 in a leap year) |
  | D | Day part of the date (1 to 31)   Year |
  | W | Day of week (1 to 7 with the result depending on firstDayOfWeek) |
  | Ww | Week of year (1 to 53 with firstDayOfWeek and firstWeekOfYear determining the exact days of the first calendar week of the year) |
  | H | Extracts the hour part of the given DateTime (0 to 23) |
  | N | Minute part (0 to 59) |
  | S | Second part (0 to 59) |
* inputDateTime - The DateTime value whose part will be extracted.
* FirstDayOfWeek - An optional constant used to specify the first day of the week. If not specified, jrSunday will be used.

  | Constant | Description |
  | --- | --- |
  | jrUseSystem | 0 (Use the current system date) |
  | jrSunday | 1 |
  | jrMonday | 2 |
  | jrTuesday | 3 |
  | jrWednesday | 4 |
  | jrThursday | 5 |
  | jrFriday | 6 |
  | jrSaturday | 7 |
* firstWeekOfYear - An optional constant specifying the first week of the year. If not specified, the first week is assumed to be the one in which Jan. 1 occurs (jrFirstJan1).

  | Constant | Value | Description |
  | --- | --- | --- |
  | jrUseSystem | 0 | Start with week in which system date occurs |
  | jrFirstJan1 | 1 | Start with week in which January 1 occurs (default) |
  | jrFirstFourDays | 2 | Start with the first week that has at least four days in the new year |
  | jrFirstFullWeek | 3 | Start with first full week of the year |

**Examples**

* `DatePart("d", ToDateTime(1999,8,15))` - Returns 15.
* `DatePart("m", ToDateTime(1999,8,15))` - Returns 8.
* `DatePart("n", ToDateTime(1999,8,15,10,35,0))` - Returns 35.
* `DatePart("q", ToDateTime(1999, 9,29))` - Returns 3 since September 29 is in the third quarter of the year.
* `DatePart("ww", ToDateTime(1997, 9,14))` - Returns 38 since 1997-9-14 is in the 38th week of 1997.

**Notes:**

* The DatePart function with "yyyy" intervalType parameter is the same as the Year function. Similarly, the DatePart function with "m", "d", "w", "h", "n" and "s" intervalType argument is the same as the functions Month, Day, Weekday (or DayOfWeek), Hour, Minute and Second respectively. On the other hand, there is no easy alternative to using the DatePart function for the "q", "y" and "ww" intervalType parameters.
* The firstDayOfWeek parameter affects the DatePart function when the interval type parameter is "w" or "ww". For all other intervalType parameter values, it is ignored.
* The firstWeekOfYear parameter affects the DatePart function only when the intervalType argument is "ww". For all other intervalType argument values, it is ignored.

## DateTimeTo2000(Datetime, Number)

* **2 digit years(xx)**  
   If the Year value is greater than the windowing number, 19 is appended before the 2 digits (19xx). If the Year value is less than or equal to the windowing number, 20 is appended (20xx).
* **4 digit years(19xx)**  
   If the last two digits in the Year value are greater than the windowing number, the Year is retained as found in the Date field (19xx). If the two digits in the Year value are less than or equal to the windowing number, the first two digits are changed to 20 (20xx). If the first two digits in the year field are 20, the Year is retained as found in the Date field (20xx).

  **Note:** If the year is less than or equal to 1899, and greater than or equal to 100, there will be no change to the date.

**Parameters**

* DateTime - Accepts only valid DateTime fields, with either 2 digit or 4 digit years.
* Number - A number between 0 and 99 corresponding with the desired windowing year.

**Return value**

A Date field with a four digit year.

**Examples**

* Here the window value is greater than the year, and so the year is changed to 20XX.

  `DateTimeTo2000(ToDateTime(1998, 12, 12, 3, 2, 1), 99)` - Returns 2098-12-12 3:02:01.
* Here the window value is less than the year, and so it will not change the year.

  `DateTimeTo2000(ToDateTime(1995, 1, 2, 3, 2, 1), 94)` - Returns 1995-01-02 3:02:01.
* These are examples of dates that will not be affected by this function.
  + `DateTimeTo2000(ToDateTime(1899, 12, 12, 5, 6, 7), 99)` - Returns 1899-12-12 5:06:07.
  + `DateTimeTo2000(ToDateTime(999, 12, 12, 5, 6, 7), 99)` - Returns 999-12-12 5:06:07.
* Some databases maintain the year of a Date as a two-digit field. These samples simulate that Date field.
  + `DateTimeTo2000(ToDateTime(93, 12, 12, 5, 6, 7), 96)` - Returns 2093-12-12 5:06:07.
  + `DateTimeTo2000(ToDateTime(98, 12, 12, 5, 6, 7), 50)` - Returns 1998-12-12 5:06:07.

## DateTimeToDate(Datetime a)

This function evaluates the specified TimeStamp value and returns only the date.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is a date.

**Example**

If the current date is Oct. 17, 1999 and the current time is 12:27:15, the return value of the following statement is 10/17/99.

`DateTimeToDate(CurrentDateTime())`

## DateTimeToSeconds(Datetime a)

This function evaluates the specified value and converts the time to the number of seconds from 00:00:00 to the specified time.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

If the current date is Oct. 17, 1999 and the current time is 12:27:15, the return value of the following statement is 44835.

`DateTimeToSeconds(CurrentDateTime())`

## DateTimeToTime(Datetime a)

This function evaluates the specified TimeStamp value and returns only the time.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is a Time.

**Example**

If the current date is Oct. 17, 1999 and the current time is 12:27:15, the return value of the following statement is 12:27:15.

`DateTimeToTime(CurrentDateTime())`

## DateTo2000(date, number)

* 2 digit years(xx)  
   If the Year value is greater than the windowing number, 19 is appended before the 2 digits (19xx). If the Year value is less than or equal to the windowing number, 20 is appended (20xx).
* 4 digit years(19xx)  
   If the last two digits in the Year value are greater than the windowing number, the Year is preserved as found in the date field (19xx). If the last two digits in the Year value are less than or equal to the windowing number, the first two digits are changed to 20 (20xx). If the first two digits in the year field are 20, the Year is preserved as found in the date field (20xx).

**Parameters**

* date - Accepts only valid Date fields, with either 2 digit or 4 digit years.
* number - A number between 0 and 99 corresponding with the desired windowing year.

**Return value**

A Date field with a four digit year.

**Examples**

* `DateTo2000(ToDate(1993,12,12), 99)`- Returns 2093/12/12 because the window value is greater than the year, and so the date will be changed to 20XX.
* `DateTo2000(ToDate(1993,12,12), 92)`- Returns 1993/12/12 because the window value is less than the year, and so the year will not be changed.
* This is an example of a date that is not affected by this function:

  `DateTo2000(ToDate(1899,12,12), 99)`- Returns 1899/12/12.
* This is an example of a date that is not affected by this function.

  `DateTo2000(ToDate(100,12,12), 99)`- Returns 100/12/12.
* Some databases maintain the year of a date as a two-digit field. The following simulates this type of date field.
  + `DateTo2000(ToDate (98,12,12), 99)`- Returns 2098/12/12.
  + `DateTo2000(ToDate (98,12,12), 97)`- Returns 1998/12/12.
  + `DateTo2000(ToDate (9,12,12), 10)`- Returns 2009/12/12.
  + `DateTo2000(ToDate (1,12,12), 0)`- Returns 1901/12/12.

**Notes:**

* If the year is less than or equal to 1899 and greater or equal to 100, there will be no change to the date.
* Whether your database dates are interpreted as two digit years or 4 digit years (19xx) is dependent on the database driver you are using. The result of the formula will be the same in either case.

## Day()

### Day()

This function returns the day of the month.

**Return value**

The return value is an Integer.

**Example**

If today is Oct. 17, 1999, the return value of the following statement is 17.

`Day()`

### Day(Date a)

This function extracts the day portion of a specified Date value.

**Parameter**

a - A Date value.

**Return value**

The return value is an Integer.

**Example**

If the current date is Oct. 17, 1999, the return value of the following statement is 17.

`Day(CurrentDate())`

### Day(Datetime a)

This function extracts the day portion of a specified Date value.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

If the current date is Oct. 17, 1999 and the current time is 12:27:15, the return value of the following statement is 17.

`Day(CurrentDateTime())`

## DayOfWeek()

### DayOfWeek()

This function returns the day of the week.

**Return value**

The return value is an Integer.

**Example**

If today is Thursday, the return value of the following statement is 5.

`DayOfWeek()`

### DayOfWeek(Date a)

This function extracts the day portion of a specified Date value, and indicates which day of the week.

**Parameter**

a - A Date value.

**Return value**

The return value is an Integer.

**Example**

If today is Oct. 17, 1999 and today is Sunday, the return value of the following statement is 1.

`DayOfWeek(CurrentDate())`

### DayOfWeek(Datetime a)

This function extracts the day portion of a specified Date value, and indicates which day of the week.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

If the current date is Oct. 17, 1999, current time is 12:27:15 and today is Sunday, the return value of the following statement is 1 (Sunday is the first day of the week).

`DayOfWeek(CurrentDateTime())`

## DayOfYear()

This function returns the day of the year.

**Return value**

The return value is an Integer.

**Example**

If today is Oct. 17, 1999, the return value of the following statement is 290.

`DayOfYear()`

## DTSTo2000(DateString, Number)

* **2 digit years(xx)**  
  If the Year value is greater than the windowing number, 19 is appended before the 2 digits(19xx). If the Year value is less than or equal to the windowing number, 20 is appended (20xx).
* **4 digit years(19xx)**  
  If the last two digits in the Year value are greater than the windowing number, the Year is retained as found in the Date field (19xx). If the two digits in the Year value are less than or equal to the windowing number, the first two digits are changed to 20 (20xx). If the first two digits in the year field are 20, the Year is retained as found in the Date field (20xx).

  **Note:** If the year is less than or equal to 1899 and greater than or equal to 100, there will be no change to the date.

**Parameters**

* Date String - Accepts only valid Date fields, with either 2 digit or 4 digit years. A DateTime string entered in the format: "yyyy/MM/dd HH: mm: ss.00" or "yy/MM/dd HH:mm:ss:00". For example, "1997/04/11 12:12:12.00" or "97/04/11 12:12:12.00".
* Number - A number between 0 and 99 corresponding with the desired windowing year.

**Return value**

A DateTime string with a four digit year.

**Examples**

* `DTSTo2000("1988-12-12 12:12:12", 90)`- Returns 2088-12-12 12:12:12 because the window value is greater than the year, and so the year will be changed to 20XX.
* `DTSTo2000("1988-12-12 12:12:12", 85)`- Returns 1988-12-12 12:12:12 because the window value is less than the year, and so the year will not change.
* These are examples of a date that will not be affected by the function:
  + `DTSTo2000("1899/12/12 1:2:3am", 99)`- Returns 1899/12/12 1:2:3am.
  + `DTSTo2000("100/12/12 1:02:03AM", 99)`- Returns 100/12/12 1:02:03AM.
* Some databases maintain the year of a date as a two-digit field and so these samples will simulate that date field:  
  + `DTSTo2000("98/12/12 1:02:03AM", 99)`- Returns 2098/12/12 1:02:03AM.
  + `DTSTo2000("98/12/12 1:02:03", 97)`- Returns 1998/12/12 1:02:03AM.
  + `DTSTo2000("9/12/12 1:02:03AM", 10)`- Returns 2009/12/12 1:02:03AM.
  + `DTSTo2000("1/12/12 1:02:03AM", 0)`- Returns 1901/12/12 1:02:03AM.

## DTSToSeconds(string)

Evaluates the specified string, and converts the Time value to the number of seconds from 00:00:00 (12:00 midnight) to the specified time.

**Parameter**

string - A String which includes a Date and a Time value.

**Return value**

Whole number.

**Example**

`DTSToSeconds("2004/06/11 13:42:15")`- Returns 49335.

## FirstDayOfMonth(Date a)

This function returns the first day of the month.

**Parameter**

a - A Date value.

**Return value**

The return value is a Date.

**Example**

If the current date is 11/24/2008, the return value of the following statement is 11/01/2008.

`FirstDayOfMonth(CurrentDate())`

## FirstDayOfQuarter(Date a)

This function returns the first day of the quarter.

**Parameter**

a - A Date value.

**Return value**

The return value is a Date.

**Example**

The return value of the following statement is 10/01/2008.

`FirstDayOfQuarter(ToDate("11/24/2008"))`

## FirstDayOfWeek(Date a)

This function returns the first day of the week.

**Parameter**

a - A Date value.

**Return value**

The return value is a Date.

**Example**

The return value of the following statement is 11/23/2008.

`FirstDayOfWeek(ToDate("11/24/2008"))`

## FirstDayOfYear(Date a)

This function returns the first day of the year.

**Parameter**

a - A Date value.

**Return value**

The return value is a Date.

**Example**

The return value of the following statement is 01/01/2008.

`FirstDayOfYear(ToDate("11/24/2008"))`

## FirstSundayOfMonth(Date a)

This function returns the first Sunday of the month.

**Parameter**

a - A Date value.

**Return value**

The return value is a Date.

**Example**

The return value of the following statement is 11/02/2008.

`FirstSundayOfMonth(ToDate("11/24/2008"))`

## FirstSundayOfYear(Date a)

This function returns the first Sunday of the year.

**Parameter**

a - A Date value.

**Return value**

The return value is a Date.

**Example**

The return value of the following statement is 01/06/2008.

`FirstSundayOfYear(ToDate("11/24/2008"))`

## ForEachDay(Datetime a)

This function returns the Date portion of a specified DateTime value.

**Parameter**

a - A DateTime value.

**Return value**

The return value is a Date.

**Example**

If the DateTime is Dec.25,1999 20:12:50, the return value of the following statement is 12/25/99.

`ForEachDay(ToDateTime(1999, 12, 25, 20, 12, 50))`

## ForEachHalfMonth(DateTime a)

If the day in the DateTime is less than 15, this function will return to the first day of the month. If the day is more than 15, it will return to the 16th day of the month.

**Parameter**

a - A DateTime value.

**Return value**

The return value is a date.

**Examples**

* If the datetime is Sep.13,1999 12:27:15, the return value of the following statement is 09/01/99.

  `ForEachHalfMonth(ToDateTime(1999,9,13,12,27,15))`
* If the datetime is Oct.18,1999 5:21:22, the return value of the following statement is 10/16/99.

  `ForEachHalfMonth(ToDateTime(1999,10,18,5,21,22))`

## ForEachHalfYear(DateTime a)

If the month of a specified DateTime is before July, the function will return to Jan.1 of the year. Otherwise the function will return to July 1 of the year.

**Parameter**

a - A DateTime value.

**Return value**

The return value is a date.

**Examples:**

* If the datetime is May. 28,1999 10:10:25, the return value of the following statement is 01/01/99.

  `ForEachHalfYear(ToDateTime(1999, 5, 28, 10, 10, 25))`
* If the datetime is Nov. 15,1998 11:40:23, the return value of the following statement is 07/01/99.

  `ForEachHalfYear(ToDateTime(1998, 11, 15, 11, 40, 23))`

## ForEachMonth(DateTime a)

This function returns the first day of the month in a specified DateTime value.

**Parameter**

a - A DateTime value.

**Return value**

The return value is a date.

**Example**

If the datetime is Sep.24,1999 12:05:56, the return value of the following statement is 09/01/99.

`ForEachMonth(ToDateTime(1999,9,24,12,5,56))`

## ForEachQuarter(DateTime a)

If the month of a specified DateTime is before April, the function will return to Jan. 1 of the year. If the month is after April but before July, the function will return to April. 1 of the year. If the month is after July but before October, the function will return to July. 1 of the year. If the month is after October, the function will return to Oct.1 of the year.

**Parameter**

a - A DateTime value.

**Return value**

The return value is a date.

**Examples**

* If the datetime is Feb.14,1997 2:10:23, the return value of the following statement is 01/01/97.

  `ForEachQuarter(ToDateTime(1997,2,14,2,10,23))`
* If the datetime is May. 28,1999 10:10:25, the return value of the following statement is 04/01/99.

  `ForEachQuarter(ToDateTime(1999,5,28,10,10,25))`
* If the datetime is Aug. 28,1999 10:10:25, the return value of the following statement is 07/01/99.

  `ForEachQuarter(ToDateTime(1999,8,28,10,10,25))`
* If the datetime is Nov. 11,1998 11:40:23, the return value of the following statement is 10/01/98.

  `ForEachQuarter(ToDateTime(1998,11,11,11,40,23))`

## ForEachWeek(DateTime a)

This function returns the Date of the first day of the week.

**Parameter**

a - A DateTime value.

**Return value**

The return value is a Date.

**Example**

If the DateTime is Oct. 15,1999 5:15:20 and it is Friday, the return value of the following statement is 10/10/99.

`ForEachWeek(ToDateTime(1999, 10, 15, 5, 15, 20))`

## ForEachYear(DateTime a)

This function will return to Jan.1 of the year.

**Parameter**

a - A DateTime value.

**Return value**

The return value is a date.

**Example**

If the datetime is Aug. 28,1999 10:10:25, the return value of the following statement is 01/01/99.

`ForEachYear(ToDateTime(1999, 8, 28, 10, 10, 25))`

## Hour()

### Hour()

This function extracts the hour portion of the current time.

**Return value**

The return value is an integer.

**Example**

If the current time is 8:15:30, the return value of the following statement is 8.

`Hour()`

### Hour(DateTime a)

This function extracts the hour portion of a specified TimeStamp value.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

Suppose the datetime is Oct. 15,1999 9:35:22. The return value of the following statement is 9.

`Hour(ToDateTime(1999,10,15,9,35,22))`

### Hour(Time a)

This function extracts the hour portion of a specified Time value.

**Parameter**

a - A Time value.

**Return value**

The return value is an Integer.

**Example**

Suppose the time is 10:05:26. The return value of the following statement is 10.

`Hour(ToTime(10, 5, 26))`

## IsDate(number or string)

Returns true if the given String or Number value can be converted to a valid Date and returns false otherwise. A valid Date is any Date between 100-1-1 and 9999-12-31.

**Parameters**

* number - A Number value representing the number of days starting from January 1, 1900. It can be positive or negative, and is truncated if fractional.
* string - A text string representing a date and many forms can be accepted. If the string is a right Date value and format, the function returns true, otherwise false.

**Return value**

Boolean value, True or False.

**Examples**

* `IsDate(50)` - Returns true since the number 50 is interpreted as 50 days from Jan. 1, 1900, which is Feb 19, 1900.
* `IsDate(-50)` - Returns true since the number –50 is interpreted as 50 days before Jan 1, 1900, which is Nov 11, 1899.
* `IsDate("Feb 1, 2004")` - Returns true since the string is a right Date value and there is only one blank between 'Feb' and '1,' and '2004'.
* `IsDate("2004 - 2 - 19")` - Returns false since the String format is not right Date format.
* `IsDate("2003/2/29")` - Returns false since 2003 is not leap year.
* `IsDate("2004*2*19")` - Returns false since the String format is not right Date format.

## IsDateTime(number/string)

Returns True if the given Number or String value can be converted to a valid DateTime, and returns False otherwise.

**Parameters**

* number - A Number value or expression to be tested for convertibility to a DateTime value. It can be positive, negative or fractional. It is interpreted as a number of days from Jan 1, 1900.
* string - A String value or expression to be tested for convertibility to a DateTime value. Many forms are accepted. If the given String value and format are right DateTime value and format, the function will return true, otherwise false.

**Return value**

Boolean value, true or false.

**Examples**

* `IsDateTime(15.2)` - Returns true since the given number argument is interpreted as the DateTime value 1900-01-15 04:48:00.
* `IsDateTime("Feb 23, 2004 15:23:25")` - Returns true.
* `IsDateTime("2004-2-23")` - Returns true.
* `IsDateTime("15:23:25")` - Returns true.

## IsTime(number or string)

Returns True if the given Number or String value can be converted to a valid Time, and returns False if otherwise.

**Parameters**

* number - A Number value or expression to be tested for convertibility to a Time value. It can be positive, negative or fractional. It is interpreted as units of 24 hours. If the number makes the Time value between 0:0:0: and 23:59:59, the function will return true, otherwise false.
* string - A String value or expression to be tested for convertibility to a Time value. Many forms are accepted. If the String value and the format are right Time value and format, the function will return true, otherwise false.

**Return value**

Boolean value, true or false.

**Examples**

* `IsTime(0.5)` - Returns true since the given number argument is interpreted as 0.5 units of 24 hours, which is 12:00:00.
* `IsTime(3.8)` - Returns true since the given number is interpreted as 3.8 units of 24 hours, which is 19:12:00.
* `IsTime("8:30:00")` - Returns true since 8:30:00 is right Time value and format.
* `IsTime("8 30:00")` - Returns false since the given string is not right Time format.
* `IsTime("8:30:62")` - Returns false since the given string is not right Time value.

## Minute()

### Minute()

This function returns the minute portion of the current time.

**Return value**

The return value is an Integer.

**Example**

If the current time is 12:41:27, the return value of the following statement is 41.

`Minute()`

### Minute(DateTime a)

This function returns the minute portion of a specified DateTime.

**Parameter**

a - A DateTime value.

**Return value**

The return value is an Integer.

**Example**

Suppose the datetime is Sep. 21,1997 12:20:25. The return value of the following statement is 20.

`Minute(ToDateTime(1997, 9, 21, 12, 20, 25))`

### Minute(Time a)

This function returns the minute portion of a specified time.

**Parameter**

a - A Time value.

**Return value**

The return value is an Integer.

**Example**

Suppose the time is 8:30:27. The return value of the following statement is 30.

`Minute(ToTime(8,30,27))`

## Month()

### Month()

This function adding one returns the current month of the year.

**Return value**

The return value is an Integer, which ranges from 0 to 11.

**Example**

If the current month is September, the return value of the following statement is 8.

`Month()`

### Month(Date a)

This function extracts the month portion from a specified Date value.

**Parameter**

a - A Date value.

**Return value**

The return value is an Integer.

**Example**

If the date is June 15,1999, the return value of the following statement is 6.

`Month(ToDate(1999, 6, 15))`

### Month(DateTime a)

This function extracts the month portion from a specified TimeStamp value.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

If the timestamp is July 15, 1999 10:10:10, the return value of the following statement is 7.

`Month(ToDateTime(1999, 7, 15, 10, 10, 10))`

## MonthName(month, abbreviate)

Returns a String name for the specified month.

**Parameters**

* month - A whole number representing the month of the year, with values between 1 and 12, where 1 represents January.
* abbreviate - An optional Boolean value that indicates if the month name is to be abbreviated. If the abbreviate value is true, the function will return the abbreviated month name. Otherwise the function will return the full month name.

**Return value**

String value.

**Examples**

* `MonthName(4)` - Returns String value "April".
* `MonthName(12, true)` - Returns String value "Dec".
* `MonthName(12, false)` - Returns String value "December".

## Now()

This function prints the current time on a report.

**Return value**

The return value is a Time.

**Example**

If the current time is 1:24:35 in the afternoon, the return value of the following statement is 1:24:35 PM.

`Now()`

## Quarter()

Returns the quarter for the given date (1 for the first quarter).

**Overloads**

* Quarter()
* Quarter(Date,Integer)
* Quarter(Datetime,Integer)

**Parameters**

* Date - A Date value.
* Integer - An Integer value in the range of 1 to 12. It is an optional argument which indicates the beginning month of the first quarter. Specifying the number is useful for fiscal quarter. If b is not specified, the default is 1 which means January is the beginning month of the first quarter as same as the calendar quarter.
* Datetime - A DateStamp value.

**Return value**

Return an integer (1, 2, 3, 4).

**Examples**

* Quarter() - Return 3 if it is September according to the current system date.
* Quarter(ToDate(2006,11,28),4) - Return 3. In this example, the first quarter begins from the 4th month - April, so the 11th month is in the third quarter.
* Quarter(ToDateTime(2006,7,15,10,10,10),4) - Return 2.

## Second()

### Second()

This function extracts the second portion of the current time.

**Return value**

The return value is an Integer.

**Example**

If the current time is 4:55:03, the return value of the following statement is 3.

`Second()`

### Second(Datetime a)

This function extracts the second portion of a specified TimeStamp.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

Suppose the datetime is Oct. 15,1999 10:15:17, the return value of the following statement is 17.

`Second(ToDateTime(1999, 10, 15, 10, 15, 17 ))`

### Second(Time a)

This function extracts the second portion of a specified time.

**Parameter**

a - A Time value.

**Return value**

The return value is an Integer.

**Example**

Suppose the time is 7:51:59, the return value of the following statement is 59.

`Second(ToTime(7, 51, 59))`

## SelectedDate()

Returns the date selected in the calendar or returns today() when no calendar is available for selecting a date.

There is a built-in expression Selected Date in Calendar calling this function. The expression can be found in the Name drop-down list of the Calendar dialog.

**Return value**

Date value.

**Example**

If the calendar date is March 12, 2012, the function returns 03/12/2012.

## Timer()

Returns the number of seconds elapsed since midnight.

**Return value**

Number value.

**Example**

If the current time is 9:28:30am, the function returns 34110.

## ToDate()

### ToDate(number or string)

Uses the function IsDate(number or string) to check whether the number/string is right or not. If the number/string is right, the function returns a Date value between 100-1-1 and 9999-12-31. If the number/string is wrong, it returns null.

**Parameters**

* number - A value representing the number of days starting from January 1, 1900. It can be positive or negative, and is truncated if fractional.
* string - A text string representing a date and many forms can be accepted.

**Return value**

Date value or null.

**Examples**

* `ToDate(50.5)` - Returns 1900-2-19 since fraction is truncated.
* `ToDate(-50)` - Returns 1970-01-01.
* `ToDate(22222222)` - Returns 1970-01-01.
* `ToDate("2004 2 19")` - Returns 2004-2-19.
* `ToDate("99-5")` - Returns 1999-5-1.
* `ToDate("1999-2-29")` - Returns null since 1999 is not leap year.

### ToDate(Date a)

This function returns the specified date.

**Parameter**

a - A Date value.

**Return value**

The return value is a Date.

**Example**

Suppose the date is July 15, 1999, the return of the following statement is 07/15/99.

`ToDate(ToDate(1999, 7, 15))`

### ToDate(Datetime a)

This function extracts the date portion of a specified DateTime.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is a Date value.

**Example**

Suppose the DateTime is July 15,1999 12:20:30, the return value of the following statement is 07/15/99.

`ToDate(ToDateTime(1999, 7, 15, 12, 20, 30 ) )`

### ToDate(integer d)

This function converts the argument d (A milliseconds value represents the number of milliseconds that have passed since January 1, 1970 00:00:00.000 GMT) to a data value.

**Parameter**

d - A Milliseconds value, a DBField value or a parameter. It should be a long integer.

**Return value**

The return value is a Date.

**Example**

The return value of the following statement is 01/02/70.

`ToDate(72000000)`

**Note:** When the milliseconds value is larger than 2³², you should use DBField or parameter instead.

### ToDate(integer y, Integer m, Integer d)

This function creates a Date value from arguments y, m and d.

**Parameters**

* y - A BigInt value indicating year.
* m - A BigInt value indicating month.
* d - A BigInt value indicating day.

**Return value**

The return value is a Date.

**Example**

The return value of the following statement is 07/15/99.

`ToDate(1999, 7, 15)`

## ToDateTime()

### ToDateTime(number or string)

Use the function IsDateTime to check whether the number/string is right or not. If it is right, the function returns a DateTime value between 100-1-1 and 9999-12-31, otherwise the function returns null.

**Parameters**

* number - A Number value or expression to be tested for convertibility to a DateTime value. It can be positive, negative or fractional. It is interpreted as a number of days from Jan 1, 1900.
* string - A String value or expression to be tested for convertibility to a DateTime value. Many forms are accepted.

**Return value**

DateTime value or null.

**Examples**

* `ToDateTime(255.35)` - Returns 1900-09-12 08:23:59.
* `ToDateTime("Jan 3, 2004")` - Returns 2004-01-03 00:00:00.
* `ToDateTime("5:25:26pm")` - Returns 2004-02-23 17:25:26 because the current date is 2004-2-23.
* `ToDateTime("2003-2-29 15:26:25")` - Returns null because the given String value is not right DateTime value.
* `ToDateTime("2004 *2 *29 15:26:25")` - Returns null because the given String format is not right DateTime format.

### ToDateTime(date a)

Returns a DateTime value.

**Parameter**

a - A Date value that can be converted to a DateTime type value by this function.

**Example**

`ToDateTime(ToDate("2004-2-23"))` - Returns 2004-02-23 00:00:00.

### ToDateTime(Date a, Time b)

This function creates a TimeStamp value from arguments a and b.

**Parameters**

* a - A Date value.
* b - A Time value.

**Return value**

The return value is a DateTime.

**Example**

Suppose the date is July 15,1999 and the time is 12:20:30, the return value of the following statement is 1999-07-15 12:20:30.

`ToDateTime(ToDate(1999, 7, 15), ToTime(12, 20, 30))`

### ToDateTime(Integer d)

This function converts the argument d (A milliseconds value represents the number of milliseconds that have passed since January 1, 1970 00:00:00.000 GMT) to a TimeStamp value. The function calculating is based on the time zone. You must adjust argument d to reflect your desired time zone.

**Parameter**

d - A Milliseconds value, a DBField value or a parameter. It should be a long integer.

**Return value**

The return value is a DateTime.

**Examples**

* The time zone is UTC+08:00. The return value of the following statement is 11/9/2016 3:10:17 AM.

  `Integer i = 1478632217;  
  Integer j = 1000;  
    
  ToDateTime(I * j)`
* The time zone is UTC+08:00. The return value of the following statement is 1/2/1970 04:00:00 AM.

  `ToDateTime(72000000)`

**Notes:**

* In this function, you can decide the display format by selecting the format from the Report Inspector. The format of the example above is yyyy-mm-dd hh:mm:ss.
* When the milliseconds value is larger than 2³² (4294967296), you should use DBField, parameter or assign integers to variables.

### ToDateTime(Integer y, Integer m, Integer d)

This function creates a TimeStamp value from arguments y, m and d.

**Parameters**

* y - A BigInt value indicating year.
* m - A BigInt value indicating month.
* d - A BigInt value indicating day.

**Return value**

The return value is a DateTime.

**Example**

Suppose the date is July 15,1999, the return value of the following statement is 1999-07-15 12:00:00.

`ToDateTime(1999, 7, 15)`

**Note:** In this function, because you only input year, month and day, the system will output 12:00:00 as the default time. Also you can decide the display format by selecting the format from the Report Inspector. The format of the example above is yyyy-mm-dd hh:mm:ss.

### ToDateTime(Integer y, Integer m, Integer d, Integer h, Integer i, Integer s)

This function creates a TimeStamp value from arguments y, m, d, h, i and s.

**Parameters**

* y - A BigInt value indicating year.
* m - A BigInt value indicating month.
* d - A BigInt value indicating day.
* h - A BigInt value indicating hour.
* i - A BigInt value indicating minute.
* s - a BigInt value indicating second.

**Return value**

The return value is a DateTime.

**Example**

Suppose the date is July 15,1999 and time is 8:05:30, the return value of the following statement is 1999-07-15 08:05:30.

`ToDateTime(1999, 7, 15, 8, 5, 30)`

## Today()

This function returns the current date on a report.

**Return value**

The return value is a date.

**Example**

If the current date is Oct. 11, 1999, the return value of the following statement is 10/11/99.

`Today()`

## ToTime()

### ToTime(number or string)

Use the function IsTime to check whether the number/string is right or not. If the number/string is right, the function returns a Time value between 00:00:00 and 23:59:59, otherwise it will return null.

**Parameters**

* number - A Number value or expression to be tested for convertibility to a Time value. It can be positive, negative or fractional. It is interpreted as units of 24 hours.
* string - A String value or expression to be tested for convertibility to a Time value. Many forms are accepted.

**Return value**

Time value or null.

**Examples**

* `ToTime(0.2)` - Returns 04:48:00.
* `ToTime(-0.2)` - Returns 19:12:00.
* `ToTime(50)` - Returns 00:00:00.
* `ToTime("10:34:25")` - Returns 10:34:25.
* `ToTime("2:25pm")` - Returns 02:25:00.
* `ToTime("2004-2-20")` - Returns 00:00:00.
* `ToTime("24:25:23")` - Returns 00:25:23.
* `ToTime("20*23:25")` - Returns null since the given String format is not time format.

### ToTime(DateTime a)

This function extracts the time portion from a specified TimeStamp value.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is a Time.

**Example**

Suppose the date is July 15,1999 and time is 10:55:45. The return value of the following statement is 10:55:45.

`ToTime(ToDateTime(1999, 7, 15, 10, 55, 45 ))`

### ToTime(Integer t)

This function converts the argument t (A milliseconds value represents the number of milliseconds that have passed since January 1, 1970 00:00:00.000 GMT) to a Time value.

**Parameter**

t - A milliseconds value, a DBField value or a parameter. It should be a long integer.

**Return value**

The return value is a Time.

**Example**

The return value of the following statement is 08:00:01.

`ToTime(1000)`

**Note:** When the milliseconds value is larger than 2³², you should use DBField or parameter instead.

### ToTime(Integer a, Integer b, Integer c)

This function creates a Time value from argument a, b and c.

**Parameters**

* a - A BigInt value, indicating hours.
* b - A BigInt value, indicating minutes.
* c - A BigInt value, indicating seconds.

**Return value**

The return value is a Time.

**Example**

The return value of the following statement is 10:10:10.

`ToTime(10, 10, 10)`

## WeekdayName(weekday, abbreviate, firstDayOfWeek)

WeekdayName returns a string indicating the name of the specified day of the week.

**Overloads**

* WeekdayName(weekday)
* WeekdayName(weekday, abbreviate)
* WeekdayName(weekday, abbreviate, firstDayOfWeek)

**Parameters**

* Weekday - The numeric designation for the day of the week.
* abbreviate - An optional Boolean value that indicates whether or not the weekday name is to be abbreviated.
* FirstDayOfWeek - An optional number indicating the first day of the week.

  | Constant | Description |
  | --- | --- |
  | jrUseSystem | 0 (Use the current system date) |
  | jrSunday | 1 |
  | jrMonday | 2 |
  | jrTuesday | 3 |
  | jrWednesday | 4 |
  | jrThursday | 5 |
  | jrFriday | 6 |
  | jrSaturday | 7 |

**Return value**

String value.

**Examples**

* `WeekdayName (2)` - Returns String value Monday.
* `WeekdayName (1)` - Returns String value Sunday.
* `WeekdayName (4, true)` - Returns String value Wed.
* `WeekdayName (4, false)` - Returns String value Wednesday.
* `WeekdayName (3, true, "jrMonday")` - Returns Wed, since abbreviation is selected and the first day of the week is specified to be Monday.
* `WeekdayName (3, true, "jrUseSystem")` - If the current day is Friday, the function returns Sun, since the first day of week is specified to the current day, and the third day from Friday is Sunday.

## WeekFrom1970()

### WeekFrom1970()

This function computes the total number of weeks from 1970 to the current date.

**Return value**

The return value is an Integer.

**Example**

If the current date is Oct. 13,1999, the return value of the following statement is 1554.

`WeekFrom1970()`

### WeekFrom1970(Date, a)

This function computes the total number of weeks from 1970 to a specified date.

**Parameter**

a - A Date value.

**Return value**

The return value is an Integer.

**Example**

Suppose the date is July 8,1995. The return value of the following statement is 1331.

`WeekFrom1970(ToDate(1995, 7, 8))`

### WeekFrom1970(DateTime, a)

This function computes the total number of weeks from 1970 to a specified DateTime.

**Parameter**

a - A DateTime value.

**Return value**

The return value is an Integer.

**Example**

Suppose the DateTime is Jan. 2,1988 10:40:50. The return value of the following statement is 940.

`WeekFrom1970(ToDateTime(1988, 1, 2, 10, 40, 50))`

## WeekOfMonth()

### WeekOfMonth()

This function returns the week of the current month.

**Return value**

The return value is an Integer.

**Example**

If the current date is Oct. 13,1999, the return value of the following statement is 3.

`WeekOfMonth()`

### WeekOfMonth(Date a)

This function returns the week of the month of a specified date.

**Parameter**

a - A Date value.

**Return value**

The return value is an Integer.

**Example**

If the current date is Oct. 13,1999, the return value of the following statement is 3.

`WeekOfMonth(ToDate(1999, 10, 13))`

### WeekOfMonth(DateTime a)

This function evaluates the week of the month of a specified TimeStamp.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

Suppose the timestamp is Jan. 20,1999 10:40:50. The return value of the following statement is 4.

`WeekOfMonth(ToDateTime(1999, 1, 20, 10, 40, 50))`

## WeekOfYear()

### WeekOfYear()

This function returns the week of the current year.

**Return value**

The return value is an Integer.

**Example**

If the current date is Oct. 13,1999, the return value of the following statement is 42.

`WeekOfYear()`

### WeekOfYear(Date a)

This function returns the week of the year in a specified date.

**Parameter**

a - A Data value.

**Return value**

The return value is an Integer.

**Example**

Suppose the date is July 8,1999. The return value of the following statement is 28.

`WeekOfYear(ToDate(1999, 7, 8))`

### WeekOfYear(DateTime a)

This function returns the week of the year in a specified TimeStamp.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

Suppose the timestamp is Feb. 4,1999 10:40:50. The return value of the following statement is 6.

`WeekOfYear(ToDateTime(1999, 2, 4, 10, 40, 50))`

## Year()

### Year()

This function returns the current year.

**Return value**

The return value is an Integer.

**Example**

If the current year is 1999, the return value of the following statement is 1999.

`Year()`

### Year(Date a)

This function extracts the year portion of a specified date.

**Parameter**

a - A Data value.

**Return value**

The return value is an Integer.

**Example**

Suppose the date is Jan.15,1995. The return value of the following statement is 1995.

`Year(ToDate(1995, 1, 15))`

### Year(DateTime a)

This function extracts the year portion of a specified TimeStamp value.

**Parameter**

a - A TimeStamp value.

**Return value**

The return value is an Integer.

**Example**

Suppose the timestamp is July 15,1988 10:40:50. The return value of the following statement is 1988.

`Year(ToDateTime(1988, 7, 15, 10, 40, 50))`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568202-Date-Range-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568222-Financial-Functions)
