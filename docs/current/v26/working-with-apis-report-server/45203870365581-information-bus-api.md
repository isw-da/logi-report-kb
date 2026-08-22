---
title: "Information Bus API"
id: 45203870365581
section: "Working with APIs Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203870365581-Information-Bus-API
updated_at: 2026-04-30T14:07:47Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Information Bus API

You can use the Information Bus API to access information container and get or put information in the container. This topic describes the interfaces of the Information Bus API.

- InformationBus
                
    It is used to transmit information in Report Server. It contains three kinds of information containers, global level, organization level, and user level, and you can get or put information in the containers. 

- InformationBusManager
                
    It is used to get the Information Bus instance from the Information Bus Manager. 

- InformationContainer
                
    It is used to store user information of the following types:
    
- LONG_TIME -    The information exists in the container until it is removed or the container it belongs to is removed. 

- SPECIFIED_TIME- The information exists in the container until the time you specify arrives or you remove it, or the container it belongs to is removed. 

- ONCE_TIME -       The information will be removed from the container once you get or remove it, or the container it belongs to is removed. 

- InfoLifeCycleType
                
    It is used to specify the life cycle type of the information, which can be LONG_TIME, SPECIFIED_TIME OR ONCE_TIME.
