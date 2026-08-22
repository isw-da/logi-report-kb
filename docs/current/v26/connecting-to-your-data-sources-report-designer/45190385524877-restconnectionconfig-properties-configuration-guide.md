---
title: "RestConnectionConfig.properties Configuration Guide"
id: 45190385524877
section: "Connecting to Your Data Sources - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190385524877-RestConnectionConfig-properties-Configuration-Guide
updated_at: 2026-04-30T15:11:51Z
source_host: logi-report-v26.insightsoftware.com
---
# RestConnectionConfig.properties Configuration Guide

The RestConnectionConfig.properties file is used to configure connection parameters for JReport when accessing XML/JSON data sources via REST API. Proper configuration can improve system reliability, performance, and resource efficiency, while maintaining backward compatibility.

## File Location

This file is located in the bin directory under the installation root:

<install_root>\bin\RestConnectionConfig.properties

Edit this file in the specified directory. Please restart the JReport service after making any changes for them to take effect.

## Parameter Descriptions

| Parameter | Description | Example/Default |
| --- | --- | --- |
| ConnectTimeout | Specifies the maximum timeout (in milliseconds) for the HTTP client (JReport server) to establish a connection to the data server. If the client cannot establish a TCP connection to the target data server within this time (e.g., the server does not respond, the network is unreachable, or the port is closed), a connection timeout exception will be thrown. | 10000 |
| ReadTimeout | The maximum time (in milliseconds) to wait for reading data after the connection is established. If no data is available to read within this time (e.g., the server is slow to respond or the network is blocked), a timeout exception will be thrown. | 60000 |
| MaxRetries | The maximum number of automatic retries allowed when a connection or data read fails and an exception occurs. For example, MaxRetries=3 means up to 3 retries (a total of 4 attempts including the initial request). | 2 |
| RetryInterval | The waiting time (in milliseconds) between each retry attempt. For example, RetryInterval=2000 means waiting 2 seconds before each retry. | 1000 |

## Parameter Priority

The order of precedence for parameters is as follows:

- 
URL-specific parameters take highest priority
If a URL-specific parameter is set (for example: ConnectTimeout_URL1), it will be used for the matched URL.

- 
Global parameters are used next
If no URL-specific parameter is set, the global parameter (for example: ConnectTimeout) will be used.

- 
System default values are used last
If neither is set, the system's built-in default value will be used.

For example

# URL-specific parameters
URL1=http://10.72.224.56:5555/api/v1/customers
ConnectTimeout_URL1=10000
ReadTimeout_URL1=0
MaxRetries_URL1=1
RetryInterval_URL1=1000

# Global parameters (applied to all URLs not specifically configured)
ConnectTimeout=5000
ReadTimeout=60000
MaxRetries=2
RetryInterval=1000

Note: Please restart the JReport service after modifying any option for changes to take effect.

## Configuration Best Practices

- 
Improve reliability: Set appropriate MaxRetries and RetryInterval to automatically handle temporary network issues and reduce failures caused by transient errors.

- 
Enhance performance: Set suitable ConnectTimeout and ReadTimeout to avoid long waits for unresponsive servers and improve overall response speed.

- 
Resource efficiency: Use reasonable timeout and retry settings to prevent resources from being occupied by invalid requests, increasing system throughput.

- 
Backward compatibility: If a parameter is not configured, it will automatically fall back to the global or system default value, ensuring compatibility with older configurations.
