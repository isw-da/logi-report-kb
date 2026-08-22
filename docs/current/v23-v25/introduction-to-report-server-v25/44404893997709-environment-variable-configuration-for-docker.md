---
title: "Environment Variable Configuration for Docker"
id: 44404893997709
section: "Introduction to Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/44404893997709-Environment-Variable-Configuration-for-Docker
updated_at: 2026-03-18T19:57:51Z
source_host: docs-report.zendesk.com
---
# 
        Environment Variable Configuration for Docker
      

      
        This topic describes how to configure environment variables when
        you run containers from a Server Docker image.
      

      
        User ID and License Key
      

      
| Environment Variable | Description | Default Value | Configuration File |
| --- | --- | --- | --- |
| USERKEY | To specify the license's User ID |  | jslc.dat |
| USERPASSWORD | To specify the license's License Key |  |  |

      
        Heap Size Settings and Extra Java Options
      

      
| Environment Variable | Description | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_INIT_HEAP_SIZE | Set the initial java heap size | 512m | JRServer.sh |
| LGRPT_MAX_HEAP_SIZE | Set the maximum java heap size | 1400m |  |
| LGRPT_JAVA_OPTS | Set extra java options Example: SSO auth class (-Djrs.httpExternalAuthorized=CustomHttpExternalAuthorized) can be set by using this configuration item. |  |  |

      
        CSRF White List
      

      
        This list can be set by the -D java property in JRServer.sh script
        under $REPORTHOME/bin/ folder.
      

      
| Environment Variable | Configuration Item | Default Value | Configuration Files |
| --- | --- | --- | --- |
| LGRPT_CSRF_WHITE_LIST | o specify the CSRF white list. Property name: jreport.server.csrf.whitelist Valid value: semicolon seperated domain names - example1.com;example2.org |  | JRServer.sh |

      
        Log Level Configuration -> Log Configuration
      

      
        All the following log levels can be set to one of these values: OFF,
        ERROR, WARN, INFO, DEBUG, or TRACE.
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_LOGGER_ENGINE_LEVEL | logger.Engine.level | ERROR | LogConfig.properties |
| LGRPT_LOGGER_DHTML_LEVEL | logger.DHTML.level | ERROR |  |
| LGRPT_LOGGER_DESIGNER_LEVEL | logger.Designer.level | ERROR |  |
| LGRPT_LOGGER_EVENT_LEVEL | logger.Event.level | ERROR |  |
| LGRPT_LOGGER_ERROR_LEVEL | logger.Error.level | ERROR |  |
| LGRPT_LOGGER_ACCESS_LEVEL | logger.Access.level | ERROR |  |
| LGRPT_LOGGER_MANAGE_LEVEL | logger.Manage.level | ERROR |  |
| LGRPT_LOGGER_DEBUG_LEVEL | logger.Debug.level | ERROR |  |
| LGRPT_LOGGER_PERFORMANCE_LEVEL | logger.Performance.level | ERROR |  |
| LGRPT_LOGGER_DUMP_LEVEL | logger.Dump.level | ERROR |  |

      
        Streaming Server Logs to Docker Logs Console
      

      
        In the standalone installation of Logi Report Server, all Server
        logs are written to log files under $REPORTHOME/logs/ folder. When
        it needs to investigate issues, the log files need to be archived
        and send back to our teams for further check. However in the docker
        container environment, this will be very inconvenient to grab all
        these log files. So, streaming the Server logs directly to the docker
        logs console will be very important for the convenience of issue
        checkings.
      

      
        To acheive this goal, $REPORTHOME/bin/LogConfig.properties file need
        to be customized when running a docker container. Here are what need
        to do in the docker entrypoint script before actually starting the
        Report Server main thread:
      

      
        - 
          
            Add following configuration lines into LogConfig.properties
            file
          

          
            logger.Engine.appenderRef.stdout.ref = EngineConsole

            logger.DHTML.appenderRef.stdout.ref = DHTMLConsole

            logger.Designer.appenderRef.stdout.ref = EngineConsole

            logger.Event.appenderRef.stdout.ref = EventConsole

            logger.Error.appenderRef.stdout.ref = ErrorConsole

            logger.Access.appenderRef.stdout.ref = AccessConsole

            logger.Manage.appenderRef.stdout.ref = ManageConsole

            logger.Debug.appenderRef.stdout.ref = DebugConsole

            
              logger.Performance.appenderRef.stdout.ref = PerformanceConsole
            

            logger.Dump.appenderRef.stdout.ref = DumpConsole

          

        

        - 
          
            Customize following configuration for better distinguishing
            different log types in the docker logs console
          

          
            # The original configuration

            
              appender.EngineConsole.layout.pattern = %m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.DHTMLConsole.layout.pattern = %m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.LogiReportConsole_designer.layout.pattern =
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.EventConsole.layout.pattern = %m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.ErrorConsole.layout.pattern =%m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.AccessConsole.layout.pattern = %m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.ManageConsole.layout.pattern = %m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.DebugConsole.layout.pattern = %m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.PerformanceConsole.layout.pattern = %m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            
              appender.DumpConsole.layout.pattern = %m [%t][%p][%d{dd
              MMM yyyy HH:mm:ss,SSS}]%n
            

            # Customized configuration

            
              appender.EngineConsole.layout.pattern = [EnigneLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<EnigneLog]%n
            

            
              appender.DHTMLConsole.layout.pattern = [DHTMLLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<DHTMLLog]%n
            

            
              appender.LogiReportConsole_designer.layout.pattern =
              [DesignerLog>> %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}]
              <<DesignerLog]%n
            

            
              appender.EventConsole.layout.pattern = [EventLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<EventLog]%n
            

            
              appender.ErrorConsole.layout.pattern = [ErrorLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<ErrorLog]%n
            

            
              appender.AccessConsole.layout.pattern = [AccessLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<AccessLog]%n
            

            
              appender.ManageConsole.layout.pattern = [ManageLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<ManageLog]%n
            

            
              appender.DebugConsole.layout.pattern = [DebugLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<DebugLog]%n
            

            
              appender.PerformanceConsole.layout.pattern = [PerformanceLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<PerformanceLog]%n
            

            
              appender.DumpConsole.layout.pattern = [DumpLog>>
              %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] <<DumpLog]%n
            

          

        

      
      
        The configuration items in step 1 will only be added into LogConfig.properties
        file when the this environment variable has been set: LGRPT_ENABLE_CONSOLE_LOGS_DESTINATION=true.
        The console patterns described in step 2 can be customized by environment
        variables LGRPT_LOGGER_XXXX_CONSOLE_PATTERN where XXXX is representing
        to different log types.
      

      Environment Variable-Property Mapping

      
| Environment Variable | Configuration Item | Default Value |
| --- | --- | --- |
| LGRPT_ENABLE_CONSOLE_LOGS_DESTINATION | N/A |  |
| LGRPT_LOGGER_ENGINE_CONSOLE_PATTERN | appender.EngineConsole.layout.pattern | [EnigneLog>> %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] > %m [%t][%p][%d{dd MMM yyyy HH:mm:ss,SSS}] 
        System Environment Configuration
      

      
        Service
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_ADMIN_USERNAME | Admin user name | admin | install.server.properties |
| LGRPT_ADMIN_PASSWORD | Admin password | admin |  |
| LGRPT_HTTPSERVER_PORT | httpserver.port | 8888 | server.properties |
| LGRPT_HTTPSERVER_MAX_HANDLERS | httpserver.max.handlers | 50 |  |
| LGRPT_HTTPSERVER_MAX_CONNECTIONS | httpserver.max.connections | 1000 |  |
| LGRPT_HTTPSERVER_TIMEOUT | httpserver.timeout | 500 |  |
| LGRPT_SECURE_COOKIES_HTTPS_ONLY | server.http.only_https_apply_cookie_settings | Valid values are true or false true | server.properties |
| LGRPT_HTTPSERVER_SSL_PORT | httpserver.ssl.port | 6888 |  |
| LGRPT_HTTPSERVER_SSL_PROTOCOL | httpserver.ssl.protocol | SSL |  |
| LGRPT_HTTPSERVER_SSL_ALGORITHM | httpserver.ssl.algorithm | sunx509 |  |
| LGRPT_HTTPSERVER_SSL_KEYSTORE | httpserver.ssl.keystore | $REPORTHOME/bin/keystore |  |
| LGRPT_HTTPSERVER_SSL_KEYSTORE_PASSWD | httpserver.ssl.keystore.npassword |  |  |
| LGRPT_HTTPSERVER_SSL_KEYSTORE_TYPE | httpserver.ssl.keystore.type | JKS |  |
| LGRPT_HTTPSERVER_SSL_TRUSTSTORE_PASSWD | httpserver.ssl.truststore.npassword |  |  |
| LGRPT_HTTPSERVER_HOST_NAME | httpserver.host.name |  |  |
| LGRPT_HTTPSERVER_SOCKET_TIMEOUT | httpserver.socket.timeout | 0 |  |

      
        Cluster
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_CLUSTER_ENABLE | cluster.enable | false | server.properties |
| LGRPT_CLUSTER_NAME | cluster.name | Report Cluster |  |
| LGRPT_PROPERTIES_DIRECTORY | resource.share.properties.dir |  |  |
| LGRPT_REALM_DIRECTORY | resource.share.realm.dir |  |  |
| LGRPT_RESOURCE_ROOT | resource.root |  |  |
| LGRPT_HISTORY_DIRECTORY | resource.share.hist.dir |  |  |
| LGRPT_TEMPORARY_FILES_DIRECTORY | resource.share.temp.dir |  |  |
| LGRPT_SERVER_RMI_HOST | server.rmi.host |  |  |
| LGRPT_SERVER_RMI_PORT | server.rmi.port | 1129 |  |

      
        Email
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_SMTP_SERVER | smtp.server |  | mailconfig.properties |
| LGRPT_SMTP_SERVER_PORT | smtp.server.port | 25 |  |
| LGRPT_SMTP_AUTHENTICATION | smtp.authentication | false |  |
| LGRPT_SMTP_USER | smtp.user |  |  |
| LGRPT_SMTP_NPASSWORD | smtp.password |  |  |
| LGRPT_SMTP_SSL | smtp.SSL | false |  |
| LGRPT_SMTP_TLS | smtp.TLS | false |  |
| LGRPT_MAIL_ENCODING | mail.encoding | ASCII |  |
| LGRPT_MAILBOX | mailbox |  |  |
| LGRPT_DEFAULT_EMAIL_FORMAT | default.format | 0 |  |
| LGRPT_COMPRESS_MAIL | compress.mail | false |  |
| LGRPT_TAG_MAX_MAIL_SIZE | Tag_MaxMailSize | -1 |  |
| LGRPT_TAG_MAX_MAIL_PAGE | Tag_MaxMailPage | -1 |  |

      
        Cache
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_CACHE_LOADED_CATALOGS | performance.cachecat | true | server.properties |
| LGRPT_CACHE_LOADED_REPORTS | performance.cacherpt | true |  |

      
        Configuration Items
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_SVR_CRD_MEM_USAGE | Maximum Memory Usage Property name: server.crd.memory.usage | 4 MB | server.properties |
| LGRPT_SVR_AUTOCACHE_ENABLED | Turn on/off Automatic Cache Property name: server.autocache.enabled |  |  |
| LGRPT_SVR_AUTOCACHE_MAX_DISK_USAGE | The maximum hard disk space that can be used for automatic data cache Property name: server.autocache.max.disk.usage |  |  |
| LGRPT_SVR_AUTOCACHE_NEVER_EXPIRE | Never expire auto cache Property name: server.autocache.never.expire |  |  |
| LGRPT_SVR_AUTOCACHE_EXPIRED_TIME | Sets the expiration time for how long to keep the cached data Property name: server.autocache.expired.time |  |  |
| LGRPT_SVR_AUTOCACHE_CONNSTREAM_ENABLED | Turn on/off automatic cache JSON/XML stream Property name: server.autocache.connstream.enabled |  |  |
| LGRPT_SVR_AUTOCACHE_CONNSTREAM_EXPIRE_IN_TASK_SESSION | Expire in task session Property name: server.autocache.connstream.expire_in_task_session |  |  |
| LGRPT_SVR_AUTOCACHE_CONNSTREAM_MAX_DISK_USAGE | The maximum hard disk space that can be used for automatic JSON/XML stream cache Property name: server.autocache.connstream.max.disk.usage |  |  |
| LGRPT_SVR_AUTOCACHE_CONNSTREAM_NEVER_EXPIRE | Never expire auto JSON/XML stream cache Property name: server.autocache.connstream.never.expire |  |  |
| LGRPT_SVR_AUTOCACHE_CONNSTREAM_EXPIRE_TIME | Sets the expiration time for how long to keep the cached data Property name: server.autocache.connstream.expired.time |  |  |

      
        Security Cache Properties
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_SECURITY_USER_CACHE_SIZE | Number of User Objects Property name: server.security.user.cache.size | 1000 | server.properties |
| LGRPT_SECURITY_ROLE_CACHE_SIZE | Number of Role Objects Property name: server.security.role.cache.size | 50 |  |
| LGRPT_SECURITY_GROUP_CACHE_SIZE | Number of Group Objects Property name: server.security.group.cache.size | 50 |  |
| LGRPT_SECURITY_PROTECTION_CACHE_SIZE | Number of ACL Objects Property name: server.security.protection.cache.size | 100 |  |
| LGRPT_SECURITY_USER_CACHE_EXPIRETIME | Expiration Time (seconds) Property name: server.security.user.cache.expiretime | 180 |  |

      
        Performance
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_PRELOAD_CATALOG_REFERRED_CLASSES | performance.preloadcatcls | true | server.properties |
| LGRPT_PRELOAD_PAGE_REPORT_REFERRED_CLASSES | performance.preloadrptcls | true |  |
| LGRPT_PRELOAD_ENGINE_REFERRED_CLASSES | performance.preloadenginecls | true |  |
| LGRPT_PRELOAD_FONTS | performance.loadfont | false |  |
| LGRPT_COMPRESS_SWAP_FILES | performance.compressio | false |  |

      
        Demo
      

      
        This configuration controls whether
        Report Server
        installs the built-in demo reports.
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_INSTALL_DEMO | install.demo.reports | true | server.properties |

      
        Advanced
      

      
| Environment Variable | Configuration Item | Default Value |
| --- | --- | --- |
| LGRPT_USER_SESSION_TIMEOUT | server.session.timeout | 1800000 (unit: seconds) |
| LGRPT_TIME_LIMIT_BEFORE_MOVING_TO_BACKGROUND | web.timeouts.report_wait | 170 (unit: seconds) |
| LGRPT_TEMPORARY_FILE_LIFE | resource.result.life | 86400 (unit: seconds) |
| LGRPT_ENGINE_PRIORITY | engine.priority | 2 (Normal Priority) |
| LGRPT_ENGINE_DEFAULT_LAGUAGE | engine.default_language | en |
| LGRPT_SECURITY_CHECK | server.security | true |
| LGRPT_ENABLE_PUBLISH_TO_VERSIONING_SYSTEM_FOR_ON_DEMAND_VIEW | server.version.from.temp | false |
| LGRPT_KEEP_CONNECTION_ALIVE | server.connection.keepalive | true |
| LGRPT_ENABLE_MULTIPLE_USERS_TO_LOGIN_USING_THE_SAME_USER_NAME | server.enableMultipleLogin | true |
| LGRPT_ENABLE_RESOURCE_FROM_REAL_PATHS | server.enableDynamicResource | false |
| LGRPT_PUBLIC_REPORTS_REAL_PATH | server.publicReportsRealPath |  |
| LGRPT_PUBLIC_COMPONENTS_REAL_PATH | server.publicComponentsRealPath |  |
| LGRPT_ENABLE_MONITOR_SERVER_TO_CHECK_THE_STATUS_OF_LOGI_REPORT_SERVER | server.rmimonitor.enable | true |
| LGRPT_ENABLE_REMOTE_SERVER_API_TO_CALL_LOGI_REPORT_SERVER | server.rmiserver.enable | false |
| LGRPT_ENABLE_PROFILING_TO_RECORD_REPORT_RUN_PERFORMANCE_INFORMATION | server.profiling.enable | false |

      
        System Database Configuration
      

      
        System Database Type
      

      
| Environment Variable | Configuration Item | Default Value |
| --- | --- | --- |
| LGRPT_SYSDB_TYP | Set the system database type. Valid values are: Trial Production It only makes sense to configure environment variables (see the following sections) of the chosen type of database, otherwise the non-relevant configuration items will be just ignored. | Trial |

      
        Trial Database
      

      
        Report Server
        has built-in derby database as its system database.
      

      
| Environment Variable | Configuration Item | Default Value | Configuration File |
| --- | --- | --- | --- |
| LGRPT_DERBY_DB_PORT | Set the built-in derby db port | 8886 | dbconfig.xml derby.properties |

      
        Production Database
      

      
| Environment Variable | Configuration Item | Configuration File |
| --- | --- | --- |
| LGRPT_SYSDB_TYP | Set the system database type to Production. | dbconfig.xml |
| LGRPT_SYSDB_JDBC_URL | Set the system database JDBC URL. |  |
| LGRPT_SYSDB_JDBC_DRIVER_CLASSNAME | Set the system database JDBC driver class name. |  |
| LGRPT_SYSDB_JDBC_DRIVER_PATH | Set the system database JDBC driver path. |  |
| LGRPT_SYSDB_USERNAME | Set the system database user name. |  |
| LGRPT_SYSDB_PASSWORD | Set the system database password. |  |

      
        Select JDK
      

      
        Report Server
        Docker images were built and published to Docker hub for one version
        with several JDKs. These can be pulled by specifying different Docker
        image types.
      

      
        The following table shows the relationship between JDK selections
        and Docker image tags:
      

      
| Desired JDK Version | Docker Image | Tag Docker Pull Command (taking V23.1 for Example) |
| --- | --- | --- |
| 8 | 23.1-jdk8 | docker pull logianalytics/logireport-server:23.1-jdk8 |
| 11 | 23.1 | docker pull logianalytics/logireport-server:23.1 |
| 17 | 23.1-jdk17 | docker pull logianalytics/logireport-server:23.1-jdk17 |

      
        Additional Class Path
      

      
        Mount a host directory which contains additional libraries to the
        /var/lib/logi-report/additional-lib folder in container, then Docker
        entry point will automatically add them into ADDCLASSPATH variable
        in setenv.sh and CLASSPATH variable in JRServer.sh.
      

      Response Headers Customization

      
        For setting any custom response headers for accessing web pages.
        Refer to this link for more information about response headers.
      

      
        To set a response header name/value pair using environment variable,
        set it as this format: LGRPT_RESPONSE_HEADER_Header_name=Header_value.
        If the header name contains “-” characters, please convert them to
        “_” characters. Following will show some examples.
      

      Response Header Environment Variable Examples

      
| Environment Variable Name/Value Pair | Response Header Name/Value Pair | Configuration Files |
| --- | --- | --- |
| LGRPT_RESPONSE_HEADER_X_Content_Type_Options=nosniff | X-Content-Type-Options: nosniff | responseHeaders.properties |
| LGRPT_RESPONSE_HEADER_Content_Security_Policy="script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; worker-src blob:; report-uri http://localhost:8888/apidemo/cspReport.jsp" | Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; worker-src blob:; report-uri http://localhost:8888/apidemo/cspReport.jsp |  |
| LGRPT_RESPONSE_HEADER_X_XSS_Protection='1; mode=block;' | X-XSS-Protection: 1; mode=block; |  |
| LGRPT_RESPONSE_HEADER_access_control_allow_origin='*' | access-control-allow-origin: * |  |
| LGRPT_RESPONSE_HEADER_vary=origin | vary: origin |  |

      
        Usage Examples
      

      
        CSRF Whitelist
      

      
        docker run
      

      
        
          docker run --rm --name report_server -it -p 8888:8888 -p 6443:6443
          \
        

        -e LGRPT_CSRF_WHITE_LIST="example1.com;example2.org" \

        -e LGRPT_SECURE_COOKIES_HTTPS_ONLY=false \

        -e LGRPT_HTTPSERVER_SSL_PORT=6443 \

        -e LGRPT_HTTPSERVER_SOCKET_TIMEOUT=800 \

        -e LGRPT_SECURITY_USER_CACHE_SIZE=1024 \

        -e LGRPT_SECURITY_USER_CACHE_EXPIRETIME=512 \

        
          -e LGRPT_RESPONSE_HEADER_Content_Security_Policy="script-src
          'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline';
          worker-src blob:; report-uri http://localhost:8888/apidemo/cspReport.jsp"
          \
        

        -e LGRPT_ENABLE_CONSOLE_LOGS_DESTINATION=true \

        logianalytics/logireport-server-nightly-build:24140.Latest

      

      
        docker compose
      

      
        services:

        # other services ...

        server:

        environment:

        - LGRPT_CSRF_WHITE_LIST=example1.com;example2.org

        - LGRPT_SECURE_COOKIES_HTTPS_ONLY=false

        - LGRPT_HTTPSERVER_SSL_PORT=6443

        - LGRPT_HTTPSERVER_SOCKET_TIMEOUT=800

        - LGRPT_SECURITY_USER_CACHE_SIZE=1024

        - LGRPT_SECURITY_USER_CACHE_EXPIRETIME=512

        
          - LGRPT_RESPONSE_HEADER_Content_Security_Policy=script-src 'self'
          'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline';
          worker-src blob:; report-uri http://localhost:8888/apidemo/cspReport.jsp
        

        - LGRPT_ENABLE_CONSOLE_LOGS_DESTINATION=true

        
          image: logianalytics/logireport-server-nightly-build:24140.Latest
        

        ports:

        - "8888:8888"

        - "6443:6443"

        # other services ...

      

      
        Set License UID and Key
      

       

      docker run
docker run --rm --name report_server -it -p 8888:8888 \
-e USERKEY=********* \
-e USERPASSWORD=************************************* \
logianalytics/logireport-server-nightly-build:23200.Latest

docker compose
services:
    # other services ...
    server:
        environment:
            - USERKEY=**********
            - USERPASSWORD=*****************
        image: logianalytics/logireport-server-nightly-build:23200.Latest
        ports:
            - "8888:8888"
    # other services ...
       

      
        For USERKEY and USERPASSWORD or other security sensitive credentials,
        we strongly recommend using credential manager (e.g Jenkins credential
        manager) to inject them into docker run or docker-compose.yml at
        runtime. Otherwise, everyone will see your credentials once they
        have been pushed to source code version management systems.
      

      
        Set Heapsize and Extra Java Options
      

       

      docker run
docker run --rm --name report_server -it -p 8888:8888 \
-e LGRPT_INIT_HEAP_SIZE=700m \
-e LGRPT_MAX_HEAP_SIZE=4g \
-e LGRPT_JAVA_OPTS="-Xlog:gc*=debug:file=gcLogs/gc.log -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=error/heapdump.hprof" \
logianalytics/logireport-server-nightly-build:23200.Latest

docker compose
services:
    # other services ...
    server:
        environment:
            - LGRPT_INIT_HEAP_SIZE=700m
            - LGRPT_MAX_HEAP_SIZE=4g
            - LGRPT_JAVA_OPTS=-Xlog:gc*=debug:file=../logs/gc.log -
XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=../logs/heapdump.hprof
            image: logianalytics/logireport-server-nightly-build:23200.Latest
        ports:
            - "8888:8888"
    # other services ...
       

      
        Set Admin Username and Password
      

       

      docker run
docker run --rm --name report_server -it -p 8888:8888 \
-e LGRPT_ADMIN_USERNAME=******** \
-e LGRPT_ADMIN_PASSWORD="********" \
logianalytics/logireport-server-nightly-build:23200.Latest

docker compose
services:
    # other services ...
    server:
        environment:
            - LGRPT_ADMIN_USERNAME=********
            - LGRPT_ADMIN_PASSWORD="************"
        image: logianalytics/logireport-server-nightly-build:23200.Latest
        ports:
            - "8888:8888"
    # other services ...
       

      
        For LGRPT_ADMIN_USERNAME and LGRPT_ADMIN_PASSWORD or other security
        sensitive credentials, we strongly recommend using credential manager
        (e.g Jenkins credential manager) to inject them into docker run or
        docker-compose.yml at runtime. Otherwise, everyone will see your
        credentials once they have been pushed to source code version management
        systems.
      

      
        HTTP Server Relevant Settings
      

       

      docker run
docker run --rm --name report_server -it -p 9543:9543 \
-e LGRPT_HTTPSERVER_PORT=9543 \
-e LGRPT_HTTPSERVER_MAX_HANDLERS=64 \
-e LGRPT_HTTPSERVER_MAX_CONNECTIONS=1024 \
-e LGRPT_HTTPSERVER_TIMEOUT=512 \
logianalytics/logireport-server-nightly-build:23200.Latest

docker compose
services:
    # other services ...
    server:
        environment:
            - LGRPT_HTTPSERVER_PORT=9543
            - LGRPT_HTTPSERVER_MAX_HANDLERS=64
            - LGRPT_HTTPSERVER_MAX_CONNECTIONS=1024
            - LGRPT_HTTPSERVER_TIMEOUT=512
        image: logianalytics/logireport-server-nightly-build:23200.Latest
        ports:
            - "9543:9543"
    # other services ...
       

      
        System Database Settings
      

       

      docker run
# Create a network for server container and its backend database container
docker network create report_network

# Run the backend database container and connect it to the previously created network
docker run --name system-database -itd -p 3306:3306 \
--network report_network \
-e MARIADB_RANDOM_ROOT_PASSWORD=yes \
-e MARIADB_DATABASE=LogiReportSystem \
-e MARIADB_USER=****** \
-e MARIADB_PASSWORD=******* \
--character-set-server=utf8 \
--collation-server=utf8_unicode_ci \
--lower-case-table-names=1

# Run Logi Report Server container and connect it to the previously created network.
# Make sure that the db user/password are identical to ones previously set in the backend database container.
docker run --rm --name report_server -it -p 8888:8888 \
--network report_network \
-e LGRPT_SYSDB_TYP=Production \
-e LGRPT_SYSDB_JDBC_URL=jdbc:mariadb://system-database:3306/LogiReportSystem \
-e LGRPT_SYSDB_JDBC_DRIVER_CLASSNAME=org.mariadb.jdbc.Driver \
-e LGRPT_SYSDB_JDBC_DRIVER_PATH=/var/lib/logi-report/additional-lib/mariadb-java-client-3.1.3.jar \
-e LGRPT_SYSDB_USERNAME=******** \
-e LGRPT_SYSDB_PASSWORD=******** \
-v /host/path/to/mariadb-java-client-3.1.3.jar:/var/lib/logi-report/additional-lib/mariadb-java-client-3.1.3.jar \
logianalytics/logireport-server-nightly-build:23200.Latest

docker compose
services:
    # other services ...
    system-database:
        command: [ '--character-set-server=utf8', '--collation-server=utf8_unicode_ci', '--lower-case-table-names=1' ]
        environment:
            - MARIADB_RANDOM_ROOT_PASSWORD=yes
            - MARIADB_DATABASE=LogiReportSystem
            - MARIADB_USER=*******
            - MARIADB_PASSWORD=*****
        image: mariadb:latest
        ports:
            - "3306:3306"
    report-server:
        depends_on:
            - system-database
        environment:
            - LGRPT_SYSDB_TYP=Production
            - LGRPT_SYSDB_JDBC_URL=jdbc:mariadb://system-database:3306/LogiReportSystem
            - LGRPT_SYSDB_JDBC_DRIVER_CLASSNAME=org.mariadb.jdbc.Driver
            - LGRPT_SYSDB_JDBC_DRIVER_PATH=/var/lib/logi-report/additional-lib/mariadb-java-client-3.1.3.jar
            - LGRPT_SYSDB_USERNAME=*********
            - LGRPT_SYSDB_PASSWORD=**********
        image: logianalytics/logireport-server-nightly-build:23200.Latest
        ports:
            - "8888:8888"
        volumes:
            - "/host/path/to/mariadb-java-client-3.1.3.jar:/var/lib/logi-report/additional-lib/mariadb-java-client-3.1.3.jar"
    # other services ...
       

      
        For database username and password or other security sensitive credentials,
        we strongly recommend using credential manager (e.g Jenkins credential
        manager) to inject them into docker run or docker-compose.yml at
        runtime. Otherwise, everyone will see your credentials once they
        have been pushed to source code version management systems.
      

      
        Set Additional Class Path
      

       

      docker run
docker run --rm --name report_server -it -p 8888:8888 \
-v /host/path/to/addlibs:/var/lib/logi-report/additional-lib \
logianalytics/logireport-server-nightly-build:23200.Latest

docker compose
services:
    # other services ...
    server:
        image: logianalytics/logireport-server-nightly-build:23200.Latest
        volumes:
            - /host/path/to/addlibs:/var/lib/logi-report/additional-lib
        ports:
            - "8888:8888"
    # other services ...
       

       

      
        Previous Topic  Next Topic
