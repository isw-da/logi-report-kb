---
title: "Date Range Functions"
id: 1500009568202
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568202-Date-Range-Functions
updated_at: 2021-07-24T05:54:38Z
---

# Date Range Functions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589501-Array-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589521-Date-Time-Functions)

# Date Range Functions

Below is a list of the date ranges used in Logi JReport Designer:

> * [Aged0To30Days()](#Aged0To30Days)
> * [Aged31To60Days()](#Aged31To60Days)
> * [Aged61To90Days()](#Aged61To90Days)
> * [AllDatesFromToday()](#AllDatesFromToday)
> * [AllDatesFromTomorrow()](#AllDatesFromTomorrow)
> * [AllDatesToToday()](#AllDatesToToday)
> * [AllDatesToYesterday()](#AllDatesToYesterday)
> * [Calendar1stHalf()](#Calendar1stHalf)
> * [Calendar1stQtr()](#Calendar1stQtr)
> * [Calendar2ndHalf()](#Calendar2ndHalf)
> * [Calendar2ndQtr()](#Calendar2ndQtr)
> * [Calendar3rdQtr()](#Calendar3rdQtr)
> * [Calendar4thQtr()](#Calendar4thQtr)
> * [Last4WeeksToSun()](#Last4WeeksToSun)
> * [Last7Days()](#Last7Days)
> * [LastFullMonth()](#LastFullMonth)
> * [LastFullWeek()](#LastFullWeek)
> * [LastYearMTD()](#LastYearMTD)
> * [LastYearYTD()](#LastYearYTD)
> * [MonthToDate()](#MonthToDate)
> * [Next30Days()](#Next30Days)
> * [Next31To60Days()](#Next31To60Days)
> * [Next61To90Days()](#Next61To90Days)
> * [Next91To365Days()](#Next91To365Days)
> * [Over90Days()](#Over90Days)
> * [WeekToDateFromSun()](#WeekToDateFromSun)
> * [YearToDate()](#YearToDate)
>
> Note that all the functions here cannot be used to return a value singly.

## Aged0To30Days()

This function returns a range of Data values that is within the previous 30 days from today. For example, if today is 10/14/99, the return range is from 09/15/99 to 10/14/99.

**Example**

The return value of the following statement is Not Expired.

|  |
| --- |
| ``` if (ToDate(1999,9,20) in Aged0To30Days())   return "Not Expired" else   return "Expired" ``` |

## Aged31To60Days()

This function returns a range of Data values that is within the previous 31 to 60 days from today date. For example, if today is 10/13/99, the return range is from 08/12/99 to 09/13/99.

**Example**

If today is 10/13/99, the return value of the following statement is false.

`return ToDate(1998, 4, 20) in Aged31To60Days()`

## Aged61To90Days()

This function returns a range of Data values that is within the previous 61 to 90 days from today date. For example, if today is 10/13/99, the return range is from 07/13/99 to 08/11/99.

**Example**

If today is 10/13/99, the return value of the following statement is false.

`return ToDate(1998, 4, 20) in Aged61To90Days()`

## AllDatesFromToday()

This function returns a range of Data values that include any date from the present day to a date about 10000 years in the future Data value. For example, if today is 04/15/98, the return range is from 04/15/98 to the future.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1998, 4, 20) in AllDatesFromToday()`

## AllDatesFromTomorrow()

This function returns a range of Data values that include any date from tomorrow to any future Data value. For example, if today is 04/15/98, the return range is from 04/16/98 to the future.

**Example**

If today is 10/10/99, the return of the following statement is false.

`return ToDate(1998, 4, 20) in AllDatesFromTomorrow()`

## AllDatesToToday()

This function returns a range of Data values that include all dates up through the present day. For example, if today is 4/15/98, the return range is from the past to 04/15/1998.

**Example**

If today is 10/10/99, the return value of the following statement is true.

`return ToDate(1998, 4, 20) in AllDatesToToday()`

## AllDatesToYesterday()

This function returns a range of Data values that include all dates up through the previous day. For example, if today is 4/15/98, the return range is from the past to 04/14/1998.

**Example**

If today is 10/10/99, the return value of the following statement is true.

`return ToDate(1998, 4, 20) in AllDatesToYesterday()`

## Calendar1stHalf()

This function returns a range of Data values that include all dates from January 1st through June 30th.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return Today() in Calendar1stHalf()`

## Calendar1stQtr()

This function returns a range of Data values that include all dates from January 1st through to March 31st.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return Today() in Calendar1stQtr()`

## Calendar2ndHalf()

This function returns a range of Data values that include all dates from July 1st through to December 31st.

**Example**

If today is 10/10/99, the return value of the following statement is true.

`return Today() in Calendar2ndHalf()`

## Calendar2ndQtr()

This function returns a range of Data values that include all dates from April 1st through to June 30th.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return Today() in Calendar2ndQtr()`

## Calendar3rdQtr()

This function returns a range of Data values that include all dates from July 1st through to September 30th.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return Today() in Calendar3rdQtr()`

## Calendar4thQtr()

This function returns a range of Data values that include all dates from October 1st through December 31st.

**Example**

If today is 10/10/99, the return value of the following statement is true.

`return Today() in Calendar4thQtr()`

## Last4WeeksToSun()

This function returns a range of Data values that include the four weeks previous to last Sunday. For example, if today is 4/15/95, the return range is from 3/13/95 to 4/9/95.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 4, 20) in Last4WeeksToSun()`

## Last7Days()

This function returns a range of Data values that include all dates from seven days ago to today (including today). For example, if today is 04/15/98, the return range is from (include) 04/09/98 to 04/15/98.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 4, 20) in Last7Days()`

## LastFullMonth()

This function returns a range of Data values that include all dates from the first to the last day of the previous month. For example, if today is 04/15/98, the return range is from 03/01/98 to 03/31/98.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 4, 20) in LastFullMonth()`

## LastFullWeek()

This function returns a range of Data values that include all dates from the Sunday to the Saturday of the previous week. For example, if today is 04/10/95, the return range is from 04/02/95 to 04/08/95.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 4, 20) in LastFullWeek()`

## LastYearMTD()

This function returns a range of Data values that fall on any date in the current month last year, up to the current date last year. For example, if today is 04/15/98, the return range is from 04/01/97 to 04/15/97.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 4, 20) in LastYearMTD()`

## LastYearYTD()

This function returns a range of Data values that include all dates in the last year, up to the current date last year. For example, if today is 04/15/98, the return range is from 01/01/97 to 04/15/97

**Example**

If today is 10/10/99, the return value of the following statement is true.

`return ToDate(1998, 4, 20) in LastYearYTD()`

## MonthToDate()

This function returns a range of Data values that include all dates from the first day of the month to today. For example, if today is 04/15/98, the return range is from 04/01/98 to 04/15/98.

**Example**

If today is 10/10/99, the return value of the following statement is true.

`return ToDate(1999, 10, 2) in MonthToDate()`

## Next30Days()

This function returns a range of Data values that include all days in the next 30 days starting from today (including today). For example, if today is 04/15/98, the return range is from 04/15/98 to 05/15/98.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 10, 2) in Next30Days()`

## Next31To60Days()

This function returns a range of Data values that include all days in the next 31 to 60 days starting from today. For example, if today is 04/15/98, the return range is from 05/16/98 to 06/14/98.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 10, 2) in Next31To60Days()`

## Next61To90Days()

This function returns a range of Data values that include all days in the next 61 to 90 days starting from today. For example, if today is 04/15/98, the return range is from 06/15/98 to 07/14/98.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 4, 20) in Next61To90Days()`

## Next91To365Days()

This function Returns a range of Data values that include all days in the next 91 to 365 days starting from today. For example, if today is 04/15/98, the return range is from 07/15/98 to 04/15/99.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 4, 20) in Next91To365Days()`

## Over90Days()

This function returns a range of Data values that include all days that are more than 90 days older than the current date. For example, if today is 04/15/98, the return range is from the past to 01/14/98.

**Example**

If today is 10/10/99, the return value of the following statement is true.

`return ToDate(1999, 4, 20) in Over90Days()`

## WeekToDateFromSun()

This function returns a range of Data values that include all days from last Sunday to today (including today). For example, if today is 04/13/95, the return range is from 04/09/95 to 04/13/95.

**Example**

If today is 10/10/99, the return value of the following statement is false.

`return ToDate(1999, 4, 20) in WeekToDateFromSun()`

## YearToDate()

This function returns a range of Data values that include all days from the first day of the calendar year to today (including today). For example, if today is 04/15/98, the return range is from 01/01/98 to 04/15/98.

**Example**

If today is 10/10/99, the return value of the following statement is true.

`return ToDate(1999, 4, 20) in YearToDate(`)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589501-Array-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589521-Date-Time-Functions)
