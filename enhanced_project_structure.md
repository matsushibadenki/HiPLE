# Project Analysis: 

## Project Summary

- **Total Python files**: 53
- **Total lines of code**: 4,368
- **Main modules**: main.py
- **Test files**: 5
- **Config files**: 10800

### Largest Files
- `enhanced_python_analyzer.py`: 23,016 bytes
- `orchestrator/hiple_orchestrator.py`: 22,927 bytes
- `agents/planner_agent.py`: 11,881 bytes
- `agents/generator_agent.py`: 10,668 bytes
- `agents/tool_router_agent.py`: 6,228 bytes

## 1. Project Directory Structure

```

├── .DS_Store
├── .env
├── .mypy_cache
│   ├── .gitignore
│   ├── 3.10
│   │   ├── @plugins_snapshot.json
│   │   ├── PIL
│   │   │   ├── ExifTags.data.json
│   │   │   ├── ExifTags.meta.json
│   │   │   ├── GimpGradientFile.data.json
│   │   │   ├── GimpGradientFile.meta.json
│   │   │   ├── GimpPaletteFile.data.json
│   │   │   ├── GimpPaletteFile.meta.json
│   │   │   ├── Image.data.json
│   │   │   ├── Image.meta.json
│   │   │   ├── ImageCms.data.json
│   │   │   ├── ImageCms.meta.json
│   │   │   ├── ImageColor.data.json
│   │   │   ├── ImageColor.meta.json
│   │   │   ├── ImageDraw.data.json
│   │   │   ├── ImageDraw.meta.json
│   │   │   ├── ImageDraw2.data.json
│   │   │   ├── ImageDraw2.meta.json
│   │   │   ├── ImageFile.data.json
│   │   │   ├── ImageFile.meta.json
│   │   │   ├── ImageFilter.data.json
│   │   │   ├── ImageFilter.meta.json
│   │   │   ├── ImageFont.data.json
│   │   │   ├── ImageFont.meta.json
│   │   │   ├── ImageMode.data.json
│   │   │   ├── ImageMode.meta.json
│   │   │   ├── ImageOps.data.json
│   │   │   ├── ImageOps.meta.json
│   │   │   ├── ImagePalette.data.json
│   │   │   ├── ImagePalette.meta.json
│   │   │   ├── ImagePath.data.json
│   │   │   ├── ImagePath.meta.json
│   │   │   ├── ImageQt.data.json
│   │   │   ├── ImageQt.meta.json
│   │   │   ├── PaletteFile.data.json
│   │   │   ├── PaletteFile.meta.json
│   │   │   ├── TiffImagePlugin.data.json
│   │   │   ├── TiffImagePlugin.meta.json
│   │   │   ├── TiffTags.data.json
│   │   │   ├── TiffTags.meta.json
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _binary.data.json
│   │   │   ├── _binary.meta.json
│   │   │   ├── _deprecate.data.json
│   │   │   ├── _deprecate.meta.json
│   │   │   ├── _imaging.data.json
│   │   │   ├── _imaging.meta.json
│   │   │   ├── _imagingcms.data.json
│   │   │   ├── _imagingcms.meta.json
│   │   │   ├── _imagingft.data.json
│   │   │   ├── _imagingft.meta.json
│   │   │   ├── _typing.data.json
│   │   │   ├── _typing.meta.json
│   │   │   ├── _util.data.json
│   │   │   ├── _util.meta.json
│   │   │   ├── _version.data.json
│   │   │   ├── _version.meta.json
│   │   │   ├── features.data.json
│   │   │   └── features.meta.json
│   │   ├── __future__.data.json
│   │   ├── __future__.meta.json
│   │   ├── __main__
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── _ast.data.json
│   │   ├── _ast.meta.json
│   │   ├── _asyncio.data.json
│   │   ├── _asyncio.meta.json
│   │   ├── _bisect.data.json
│   │   ├── _bisect.meta.json
│   │   ├── _blake2.data.json
│   │   ├── _blake2.meta.json
│   │   ├── _bz2.data.json
│   │   ├── _bz2.meta.json
│   │   ├── _codecs.data.json
│   │   ├── _codecs.meta.json
│   │   ├── _collections_abc.data.json
│   │   ├── _collections_abc.meta.json
│   │   ├── _compat_pickle.data.json
│   │   ├── _compat_pickle.meta.json
│   │   ├── _compression.data.json
│   │   ├── _compression.meta.json
│   │   ├── _contextvars.data.json
│   │   ├── _contextvars.meta.json
│   │   ├── _csv.data.json
│   │   ├── _csv.meta.json
│   │   ├── _ctypes.data.json
│   │   ├── _ctypes.meta.json
│   │   ├── _decimal.data.json
│   │   ├── _decimal.meta.json
│   │   ├── _frozen_importlib.data.json
│   │   ├── _frozen_importlib.meta.json
│   │   ├── _frozen_importlib_external.data.json
│   │   ├── _frozen_importlib_external.meta.json
│   │   ├── _hashlib.data.json
│   │   ├── _hashlib.meta.json
│   │   ├── _heapq.data.json
│   │   ├── _heapq.meta.json
│   │   ├── _io.data.json
│   │   ├── _io.meta.json
│   │   ├── _locale.data.json
│   │   ├── _locale.meta.json
│   │   ├── _lsprof.data.json
│   │   ├── _lsprof.meta.json
│   │   ├── _markupbase.data.json
│   │   ├── _markupbase.meta.json
│   │   ├── _multibytecodec.data.json
│   │   ├── _multibytecodec.meta.json
│   │   ├── _operator.data.json
│   │   ├── _operator.meta.json
│   │   ├── _pickle.data.json
│   │   ├── _pickle.meta.json
│   │   ├── _queue.data.json
│   │   ├── _queue.meta.json
│   │   ├── _random.data.json
│   │   ├── _random.meta.json
│   │   ├── _sitebuiltins.data.json
│   │   ├── _sitebuiltins.meta.json
│   │   ├── _socket.data.json
│   │   ├── _socket.meta.json
│   │   ├── _ssl.data.json
│   │   ├── _ssl.meta.json
│   │   ├── _stat.data.json
│   │   ├── _stat.meta.json
│   │   ├── _struct.data.json
│   │   ├── _struct.meta.json
│   │   ├── _thread.data.json
│   │   ├── _thread.meta.json
│   │   ├── _typeshed
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── importlib.data.json
│   │   │   └── importlib.meta.json
│   │   ├── _warnings.data.json
│   │   ├── _warnings.meta.json
│   │   ├── _weakref.data.json
│   │   ├── _weakref.meta.json
│   │   ├── _weakrefset.data.json
│   │   ├── _weakrefset.meta.json
│   │   ├── abc.data.json
│   │   ├── abc.meta.json
│   │   ├── agents
│   │   │   ├── base_agent.data.json
│   │   │   ├── base_agent.meta.json
│   │   │   ├── consultant_agent.data.json
│   │   │   ├── consultant_agent.meta.json
│   │   │   ├── critic_agent.data.json
│   │   │   ├── critic_agent.meta.json
│   │   │   ├── generator_agent.data.json
│   │   │   ├── generator_agent.meta.json
│   │   │   ├── metacognition_agent.data.json
│   │   │   ├── metacognition_agent.meta.json
│   │   │   ├── planner_agent.data.json
│   │   │   ├── planner_agent.meta.json
│   │   │   ├── rag_agent.data.json
│   │   │   ├── rag_agent.meta.json
│   │   │   ├── reporter_agent.data.json
│   │   │   ├── reporter_agent.meta.json
│   │   │   ├── reviewer_agent.data.json
│   │   │   ├── reviewer_agent.meta.json
│   │   │   ├── router_agent.data.json
│   │   │   ├── router_agent.meta.json
│   │   │   ├── safety_director_agent.data.json
│   │   │   ├── safety_director_agent.meta.json
│   │   │   ├── tool_router_agent.data.json
│   │   │   ├── tool_router_agent.meta.json
│   │   │   ├── web_browser_agent.data.json
│   │   │   ├── web_browser_agent.meta.json
│   │   │   ├── wikipedia_agent.data.json
│   │   │   ├── wikipedia_agent.meta.json
│   │   │   ├── worker.data.json
│   │   │   └── worker.meta.json
│   │   ├── agents.data.json
│   │   ├── agents.meta.json
│   │   ├── aiohappyeyeballs
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _staggered.data.json
│   │   │   ├── _staggered.meta.json
│   │   │   ├── impl.data.json
│   │   │   ├── impl.meta.json
│   │   │   ├── types.data.json
│   │   │   ├── types.meta.json
│   │   │   ├── utils.data.json
│   │   │   └── utils.meta.json
│   │   ├── aiohttp
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _cookie_helpers.data.json
│   │   │   ├── _cookie_helpers.meta.json
│   │   │   ├── _websocket
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── helpers.data.json
│   │   │   │   ├── helpers.meta.json
│   │   │   │   ├── models.data.json
│   │   │   │   ├── models.meta.json
│   │   │   │   ├── reader.data.json
│   │   │   │   ├── reader.meta.json
│   │   │   │   ├── reader_py.data.json
│   │   │   │   ├── reader_py.meta.json
│   │   │   │   ├── writer.data.json
│   │   │   │   └── writer.meta.json
│   │   │   ├── abc.data.json
│   │   │   ├── abc.meta.json
│   │   │   ├── base_protocol.data.json
│   │   │   ├── base_protocol.meta.json
│   │   │   ├── client.data.json
│   │   │   ├── client.meta.json
│   │   │   ├── client_exceptions.data.json
│   │   │   ├── client_exceptions.meta.json
│   │   │   ├── client_middleware_digest_auth.data.json
│   │   │   ├── client_middleware_digest_auth.meta.json
│   │   │   ├── client_middlewares.data.json
│   │   │   ├── client_middlewares.meta.json
│   │   │   ├── client_proto.data.json
│   │   │   ├── client_proto.meta.json
│   │   │   ├── client_reqrep.data.json
│   │   │   ├── client_reqrep.meta.json
│   │   │   ├── client_ws.data.json
│   │   │   ├── client_ws.meta.json
│   │   │   ├── compression_utils.data.json
│   │   │   ├── compression_utils.meta.json
│   │   │   ├── connector.data.json
│   │   │   ├── connector.meta.json
│   │   │   ├── cookiejar.data.json
│   │   │   ├── cookiejar.meta.json
│   │   │   ├── formdata.data.json
│   │   │   ├── formdata.meta.json
│   │   │   ├── hdrs.data.json
│   │   │   ├── hdrs.meta.json
│   │   │   ├── helpers.data.json
│   │   │   ├── helpers.meta.json
│   │   │   ├── http.data.json
│   │   │   ├── http.meta.json
│   │   │   ├── http_exceptions.data.json
│   │   │   ├── http_exceptions.meta.json
│   │   │   ├── http_parser.data.json
│   │   │   ├── http_parser.meta.json
│   │   │   ├── http_websocket.data.json
│   │   │   ├── http_websocket.meta.json
│   │   │   ├── http_writer.data.json
│   │   │   ├── http_writer.meta.json
│   │   │   ├── log.data.json
│   │   │   ├── log.meta.json
│   │   │   ├── multipart.data.json
│   │   │   ├── multipart.meta.json
│   │   │   ├── payload.data.json
│   │   │   ├── payload.meta.json
│   │   │   ├── payload_streamer.data.json
│   │   │   ├── payload_streamer.meta.json
│   │   │   ├── resolver.data.json
│   │   │   ├── resolver.meta.json
│   │   │   ├── streams.data.json
│   │   │   ├── streams.meta.json
│   │   │   ├── tcp_helpers.data.json
│   │   │   ├── tcp_helpers.meta.json
│   │   │   ├── tracing.data.json
│   │   │   ├── tracing.meta.json
│   │   │   ├── typedefs.data.json
│   │   │   ├── typedefs.meta.json
│   │   │   ├── web.data.json
│   │   │   ├── web.meta.json
│   │   │   ├── web_app.data.json
│   │   │   ├── web_app.meta.json
│   │   │   ├── web_exceptions.data.json
│   │   │   ├── web_exceptions.meta.json
│   │   │   ├── web_fileresponse.data.json
│   │   │   ├── web_fileresponse.meta.json
│   │   │   ├── web_log.data.json
│   │   │   ├── web_log.meta.json
│   │   │   ├── web_middlewares.data.json
│   │   │   ├── web_middlewares.meta.json
│   │   │   ├── web_protocol.data.json
│   │   │   ├── web_protocol.meta.json
│   │   │   ├── web_request.data.json
│   │   │   ├── web_request.meta.json
│   │   │   ├── web_response.data.json
│   │   │   ├── web_response.meta.json
│   │   │   ├── web_routedef.data.json
│   │   │   ├── web_routedef.meta.json
│   │   │   ├── web_runner.data.json
│   │   │   ├── web_runner.meta.json
│   │   │   ├── web_server.data.json
│   │   │   ├── web_server.meta.json
│   │   │   ├── web_urldispatcher.data.json
│   │   │   ├── web_urldispatcher.meta.json
│   │   │   ├── web_ws.data.json
│   │   │   ├── web_ws.meta.json
│   │   │   ├── worker.data.json
│   │   │   └── worker.meta.json
│   │   ├── aiosignal
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── annotated_types
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── anyio
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _core
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _eventloop.data.json
│   │   │   │   ├── _eventloop.meta.json
│   │   │   │   ├── _exceptions.data.json
│   │   │   │   ├── _exceptions.meta.json
│   │   │   │   ├── _fileio.data.json
│   │   │   │   ├── _fileio.meta.json
│   │   │   │   ├── _resources.data.json
│   │   │   │   ├── _resources.meta.json
│   │   │   │   ├── _signals.data.json
│   │   │   │   ├── _signals.meta.json
│   │   │   │   ├── _sockets.data.json
│   │   │   │   ├── _sockets.meta.json
│   │   │   │   ├── _streams.data.json
│   │   │   │   ├── _streams.meta.json
│   │   │   │   ├── _subprocesses.data.json
│   │   │   │   ├── _subprocesses.meta.json
│   │   │   │   ├── _synchronization.data.json
│   │   │   │   ├── _synchronization.meta.json
│   │   │   │   ├── _tasks.data.json
│   │   │   │   ├── _tasks.meta.json
│   │   │   │   ├── _tempfile.data.json
│   │   │   │   ├── _tempfile.meta.json
│   │   │   │   ├── _testing.data.json
│   │   │   │   ├── _testing.meta.json
│   │   │   │   ├── _typedattr.data.json
│   │   │   │   └── _typedattr.meta.json
│   │   │   ├── abc
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _eventloop.data.json
│   │   │   │   ├── _eventloop.meta.json
│   │   │   │   ├── _resources.data.json
│   │   │   │   ├── _resources.meta.json
│   │   │   │   ├── _sockets.data.json
│   │   │   │   ├── _sockets.meta.json
│   │   │   │   ├── _streams.data.json
│   │   │   │   ├── _streams.meta.json
│   │   │   │   ├── _subprocesses.data.json
│   │   │   │   ├── _subprocesses.meta.json
│   │   │   │   ├── _tasks.data.json
│   │   │   │   ├── _tasks.meta.json
│   │   │   │   ├── _testing.data.json
│   │   │   │   └── _testing.meta.json
│   │   │   ├── from_thread.data.json
│   │   │   ├── from_thread.meta.json
│   │   │   ├── lowlevel.data.json
│   │   │   ├── lowlevel.meta.json
│   │   │   ├── streams
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── memory.data.json
│   │   │   │   ├── memory.meta.json
│   │   │   │   ├── stapled.data.json
│   │   │   │   ├── stapled.meta.json
│   │   │   │   ├── tls.data.json
│   │   │   │   └── tls.meta.json
│   │   │   ├── to_thread.data.json
│   │   │   └── to_thread.meta.json
│   │   ├── argparse.data.json
│   │   ├── argparse.meta.json
│   │   ├── array.data.json
│   │   ├── array.meta.json
│   │   ├── ast.data.json
│   │   ├── ast.meta.json
│   │   ├── async_timeout
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── asyncio
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── base_events.data.json
│   │   │   ├── base_events.meta.json
│   │   │   ├── coroutines.data.json
│   │   │   ├── coroutines.meta.json
│   │   │   ├── events.data.json
│   │   │   ├── events.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── futures.data.json
│   │   │   ├── futures.meta.json
│   │   │   ├── locks.data.json
│   │   │   ├── locks.meta.json
│   │   │   ├── mixins.data.json
│   │   │   ├── mixins.meta.json
│   │   │   ├── protocols.data.json
│   │   │   ├── protocols.meta.json
│   │   │   ├── queues.data.json
│   │   │   ├── queues.meta.json
│   │   │   ├── runners.data.json
│   │   │   ├── runners.meta.json
│   │   │   ├── selector_events.data.json
│   │   │   ├── selector_events.meta.json
│   │   │   ├── streams.data.json
│   │   │   ├── streams.meta.json
│   │   │   ├── subprocess.data.json
│   │   │   ├── subprocess.meta.json
│   │   │   ├── tasks.data.json
│   │   │   ├── tasks.meta.json
│   │   │   ├── threads.data.json
│   │   │   ├── threads.meta.json
│   │   │   ├── transports.data.json
│   │   │   ├── transports.meta.json
│   │   │   ├── unix_events.data.json
│   │   │   └── unix_events.meta.json
│   │   ├── atexit.data.json
│   │   ├── atexit.meta.json
│   │   ├── attr
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _cmp.data.json
│   │   │   ├── _cmp.meta.json
│   │   │   ├── _typing_compat.data.json
│   │   │   ├── _typing_compat.meta.json
│   │   │   ├── _version_info.data.json
│   │   │   ├── _version_info.meta.json
│   │   │   ├── converters.data.json
│   │   │   ├── converters.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── filters.data.json
│   │   │   ├── filters.meta.json
│   │   │   ├── setters.data.json
│   │   │   ├── setters.meta.json
│   │   │   ├── validators.data.json
│   │   │   └── validators.meta.json
│   │   ├── attrs
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── av
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _core.data.json
│   │   │   ├── _core.meta.json
│   │   │   ├── about.data.json
│   │   │   ├── about.meta.json
│   │   │   ├── audio
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── codeccontext.data.json
│   │   │   │   ├── codeccontext.meta.json
│   │   │   │   ├── fifo.data.json
│   │   │   │   ├── fifo.meta.json
│   │   │   │   ├── format.data.json
│   │   │   │   ├── format.meta.json
│   │   │   │   ├── frame.data.json
│   │   │   │   ├── frame.meta.json
│   │   │   │   ├── layout.data.json
│   │   │   │   ├── layout.meta.json
│   │   │   │   ├── plane.data.json
│   │   │   │   ├── plane.meta.json
│   │   │   │   ├── resampler.data.json
│   │   │   │   ├── resampler.meta.json
│   │   │   │   ├── stream.data.json
│   │   │   │   └── stream.meta.json
│   │   │   ├── bitstream.data.json
│   │   │   ├── bitstream.meta.json
│   │   │   ├── buffer.data.json
│   │   │   ├── buffer.meta.json
│   │   │   ├── codec
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── codec.data.json
│   │   │   │   ├── codec.meta.json
│   │   │   │   ├── context.data.json
│   │   │   │   ├── context.meta.json
│   │   │   │   ├── hwaccel.data.json
│   │   │   │   └── hwaccel.meta.json
│   │   │   ├── container
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── core.data.json
│   │   │   │   ├── core.meta.json
│   │   │   │   ├── input.data.json
│   │   │   │   ├── input.meta.json
│   │   │   │   ├── output.data.json
│   │   │   │   ├── output.meta.json
│   │   │   │   ├── streams.data.json
│   │   │   │   └── streams.meta.json
│   │   │   ├── descriptor.data.json
│   │   │   ├── descriptor.meta.json
│   │   │   ├── error.data.json
│   │   │   ├── error.meta.json
│   │   │   ├── filter
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── context.data.json
│   │   │   │   ├── context.meta.json
│   │   │   │   ├── filter.data.json
│   │   │   │   ├── filter.meta.json
│   │   │   │   ├── graph.data.json
│   │   │   │   ├── graph.meta.json
│   │   │   │   ├── link.data.json
│   │   │   │   ├── link.meta.json
│   │   │   │   ├── loudnorm.data.json
│   │   │   │   ├── loudnorm.meta.json
│   │   │   │   ├── pad.data.json
│   │   │   │   └── pad.meta.json
│   │   │   ├── format.data.json
│   │   │   ├── format.meta.json
│   │   │   ├── frame.data.json
│   │   │   ├── frame.meta.json
│   │   │   ├── logging.data.json
│   │   │   ├── logging.meta.json
│   │   │   ├── option.data.json
│   │   │   ├── option.meta.json
│   │   │   ├── packet.data.json
│   │   │   ├── packet.meta.json
│   │   │   ├── plane.data.json
│   │   │   ├── plane.meta.json
│   │   │   ├── sidedata
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── motionvectors.data.json
│   │   │   │   ├── motionvectors.meta.json
│   │   │   │   ├── sidedata.data.json
│   │   │   │   └── sidedata.meta.json
│   │   │   ├── stream.data.json
│   │   │   ├── stream.meta.json
│   │   │   ├── subtitles
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── codeccontext.data.json
│   │   │   │   ├── codeccontext.meta.json
│   │   │   │   ├── stream.data.json
│   │   │   │   ├── stream.meta.json
│   │   │   │   ├── subtitle.data.json
│   │   │   │   └── subtitle.meta.json
│   │   │   └── video
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── codeccontext.data.json
│   │   │       ├── codeccontext.meta.json
│   │   │       ├── format.data.json
│   │   │       ├── format.meta.json
│   │   │       ├── frame.data.json
│   │   │       ├── frame.meta.json
│   │   │       ├── plane.data.json
│   │   │       ├── plane.meta.json
│   │   │       ├── stream.data.json
│   │   │       └── stream.meta.json
│   │   ├── base64.data.json
│   │   ├── base64.meta.json
│   │   ├── bdb.data.json
│   │   ├── bdb.meta.json
│   │   ├── binascii.data.json
│   │   ├── binascii.meta.json
│   │   ├── bisect.data.json
│   │   ├── bisect.meta.json
│   │   ├── bs4
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _deprecation.data.json
│   │   │   ├── _deprecation.meta.json
│   │   │   ├── _typing.data.json
│   │   │   ├── _typing.meta.json
│   │   │   ├── _warnings.data.json
│   │   │   ├── _warnings.meta.json
│   │   │   ├── builder
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _html5lib.data.json
│   │   │   │   ├── _html5lib.meta.json
│   │   │   │   ├── _htmlparser.data.json
│   │   │   │   ├── _htmlparser.meta.json
│   │   │   │   ├── _lxml.data.json
│   │   │   │   └── _lxml.meta.json
│   │   │   ├── css.data.json
│   │   │   ├── css.meta.json
│   │   │   ├── dammit.data.json
│   │   │   ├── dammit.meta.json
│   │   │   ├── element.data.json
│   │   │   ├── element.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── filter.data.json
│   │   │   ├── filter.meta.json
│   │   │   ├── formatter.data.json
│   │   │   └── formatter.meta.json
│   │   ├── builtins.data.json
│   │   ├── builtins.meta.json
│   │   ├── bz2.data.json
│   │   ├── bz2.meta.json
│   │   ├── cProfile.data.json
│   │   ├── cProfile.meta.json
│   │   ├── calendar.data.json
│   │   ├── calendar.meta.json
│   │   ├── charset_normalizer
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── api.data.json
│   │   │   ├── api.meta.json
│   │   │   ├── cd.data.json
│   │   │   ├── cd.meta.json
│   │   │   ├── constant.data.json
│   │   │   ├── constant.meta.json
│   │   │   ├── legacy.data.json
│   │   │   ├── legacy.meta.json
│   │   │   ├── md.data.json
│   │   │   ├── md.meta.json
│   │   │   ├── models.data.json
│   │   │   ├── models.meta.json
│   │   │   ├── utils.data.json
│   │   │   ├── utils.meta.json
│   │   │   ├── version.data.json
│   │   │   └── version.meta.json
│   │   ├── cmath.data.json
│   │   ├── cmath.meta.json
│   │   ├── cmd.data.json
│   │   ├── cmd.meta.json
│   │   ├── codecs.data.json
│   │   ├── codecs.meta.json
│   │   ├── collections
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── abc.data.json
│   │   │   └── abc.meta.json
│   │   ├── colorsys.data.json
│   │   ├── colorsys.meta.json
│   │   ├── concurrent
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   └── futures
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── _base.data.json
│   │   │       ├── _base.meta.json
│   │   │       ├── process.data.json
│   │   │       ├── process.meta.json
│   │   │       ├── thread.data.json
│   │   │       └── thread.meta.json
│   │   ├── config
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── configparser.data.json
│   │   ├── configparser.meta.json
│   │   ├── container
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── contextlib.data.json
│   │   ├── contextlib.meta.json
│   │   ├── contextvars.data.json
│   │   ├── contextvars.meta.json
│   │   ├── copy.data.json
│   │   ├── copy.meta.json
│   │   ├── copyreg.data.json
│   │   ├── copyreg.meta.json
│   │   ├── csv.data.json
│   │   ├── csv.meta.json
│   │   ├── ctypes
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _endian.data.json
│   │   │   ├── _endian.meta.json
│   │   │   ├── util.data.json
│   │   │   ├── util.meta.json
│   │   │   ├── wintypes.data.json
│   │   │   └── wintypes.meta.json
│   │   ├── cycler
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── dataclasses.data.json
│   │   ├── dataclasses.meta.json
│   │   ├── datetime.data.json
│   │   ├── datetime.meta.json
│   │   ├── decimal.data.json
│   │   ├── decimal.meta.json
│   │   ├── dependency_injector
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── containers.data.json
│   │   │   ├── containers.meta.json
│   │   │   ├── providers.data.json
│   │   │   ├── providers.meta.json
│   │   │   ├── resources.data.json
│   │   │   └── resources.meta.json
│   │   ├── difflib.data.json
│   │   ├── difflib.meta.json
│   │   ├── diffusers
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── callbacks.data.json
│   │   │   ├── callbacks.meta.json
│   │   │   ├── configuration_utils.data.json
│   │   │   ├── configuration_utils.meta.json
│   │   │   ├── dependency_versions_check.data.json
│   │   │   ├── dependency_versions_check.meta.json
│   │   │   ├── dependency_versions_table.data.json
│   │   │   ├── dependency_versions_table.meta.json
│   │   │   ├── hooks
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── faster_cache.data.json
│   │   │   │   ├── faster_cache.meta.json
│   │   │   │   ├── group_offloading.data.json
│   │   │   │   ├── group_offloading.meta.json
│   │   │   │   ├── hooks.data.json
│   │   │   │   ├── hooks.meta.json
│   │   │   │   ├── layerwise_casting.data.json
│   │   │   │   ├── layerwise_casting.meta.json
│   │   │   │   ├── pyramid_attention_broadcast.data.json
│   │   │   │   └── pyramid_attention_broadcast.meta.json
│   │   │   ├── image_processor.data.json
│   │   │   ├── image_processor.meta.json
│   │   │   ├── loaders
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── ip_adapter.data.json
│   │   │   │   ├── ip_adapter.meta.json
│   │   │   │   ├── lora_base.data.json
│   │   │   │   ├── lora_base.meta.json
│   │   │   │   ├── lora_conversion_utils.data.json
│   │   │   │   ├── lora_conversion_utils.meta.json
│   │   │   │   ├── lora_pipeline.data.json
│   │   │   │   ├── lora_pipeline.meta.json
│   │   │   │   ├── peft.data.json
│   │   │   │   ├── peft.meta.json
│   │   │   │   ├── single_file.data.json
│   │   │   │   ├── single_file.meta.json
│   │   │   │   ├── single_file_model.data.json
│   │   │   │   ├── single_file_model.meta.json
│   │   │   │   ├── single_file_utils.data.json
│   │   │   │   ├── single_file_utils.meta.json
│   │   │   │   ├── textual_inversion.data.json
│   │   │   │   ├── textual_inversion.meta.json
│   │   │   │   ├── transformer_flux.data.json
│   │   │   │   ├── transformer_flux.meta.json
│   │   │   │   ├── transformer_sd3.data.json
│   │   │   │   ├── transformer_sd3.meta.json
│   │   │   │   ├── unet.data.json
│   │   │   │   ├── unet.meta.json
│   │   │   │   ├── unet_loader_utils.data.json
│   │   │   │   ├── unet_loader_utils.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── models
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── activations.data.json
│   │   │   │   ├── activations.meta.json
│   │   │   │   ├── adapter.data.json
│   │   │   │   ├── adapter.meta.json
│   │   │   │   ├── attention.data.json
│   │   │   │   ├── attention.meta.json
│   │   │   │   ├── attention_flax.data.json
│   │   │   │   ├── attention_flax.meta.json
│   │   │   │   ├── attention_processor.data.json
│   │   │   │   ├── attention_processor.meta.json
│   │   │   │   ├── auto_model.data.json
│   │   │   │   ├── auto_model.meta.json
│   │   │   │   ├── autoencoders
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── autoencoder_asym_kl.data.json
│   │   │   │   │   ├── autoencoder_asym_kl.meta.json
│   │   │   │   │   ├── autoencoder_dc.data.json
│   │   │   │   │   ├── autoencoder_dc.meta.json
│   │   │   │   │   ├── autoencoder_kl.data.json
│   │   │   │   │   ├── autoencoder_kl.meta.json
│   │   │   │   │   ├── autoencoder_kl_allegro.data.json
│   │   │   │   │   ├── autoencoder_kl_allegro.meta.json
│   │   │   │   │   ├── autoencoder_kl_cogvideox.data.json
│   │   │   │   │   ├── autoencoder_kl_cogvideox.meta.json
│   │   │   │   │   ├── autoencoder_kl_cosmos.data.json
│   │   │   │   │   ├── autoencoder_kl_cosmos.meta.json
│   │   │   │   │   ├── autoencoder_kl_hunyuan_video.data.json
│   │   │   │   │   ├── autoencoder_kl_hunyuan_video.meta.json
│   │   │   │   │   ├── autoencoder_kl_ltx.data.json
│   │   │   │   │   ├── autoencoder_kl_ltx.meta.json
│   │   │   │   │   ├── autoencoder_kl_magvit.data.json
│   │   │   │   │   ├── autoencoder_kl_magvit.meta.json
│   │   │   │   │   ├── autoencoder_kl_mochi.data.json
│   │   │   │   │   ├── autoencoder_kl_mochi.meta.json
│   │   │   │   │   ├── autoencoder_kl_temporal_decoder.data.json
│   │   │   │   │   ├── autoencoder_kl_temporal_decoder.meta.json
│   │   │   │   │   ├── autoencoder_kl_wan.data.json
│   │   │   │   │   ├── autoencoder_kl_wan.meta.json
│   │   │   │   │   ├── autoencoder_oobleck.data.json
│   │   │   │   │   ├── autoencoder_oobleck.meta.json
│   │   │   │   │   ├── autoencoder_tiny.data.json
│   │   │   │   │   ├── autoencoder_tiny.meta.json
│   │   │   │   │   ├── consistency_decoder_vae.data.json
│   │   │   │   │   ├── consistency_decoder_vae.meta.json
│   │   │   │   │   ├── vae.data.json
│   │   │   │   │   ├── vae.meta.json
│   │   │   │   │   ├── vq_model.data.json
│   │   │   │   │   └── vq_model.meta.json
│   │   │   │   ├── cache_utils.data.json
│   │   │   │   ├── cache_utils.meta.json
│   │   │   │   ├── controlnets
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── controlnet.data.json
│   │   │   │   │   ├── controlnet.meta.json
│   │   │   │   │   ├── controlnet_flax.data.json
│   │   │   │   │   ├── controlnet_flax.meta.json
│   │   │   │   │   ├── controlnet_flux.data.json
│   │   │   │   │   ├── controlnet_flux.meta.json
│   │   │   │   │   ├── controlnet_hunyuan.data.json
│   │   │   │   │   ├── controlnet_hunyuan.meta.json
│   │   │   │   │   ├── controlnet_sana.data.json
│   │   │   │   │   ├── controlnet_sana.meta.json
│   │   │   │   │   ├── controlnet_sd3.data.json
│   │   │   │   │   ├── controlnet_sd3.meta.json
│   │   │   │   │   ├── controlnet_sparsectrl.data.json
│   │   │   │   │   ├── controlnet_sparsectrl.meta.json
│   │   │   │   │   ├── controlnet_union.data.json
│   │   │   │   │   ├── controlnet_union.meta.json
│   │   │   │   │   ├── controlnet_xs.data.json
│   │   │   │   │   ├── controlnet_xs.meta.json
│   │   │   │   │   ├── multicontrolnet.data.json
│   │   │   │   │   ├── multicontrolnet.meta.json
│   │   │   │   │   ├── multicontrolnet_union.data.json
│   │   │   │   │   └── multicontrolnet_union.meta.json
│   │   │   │   ├── downsampling.data.json
│   │   │   │   ├── downsampling.meta.json
│   │   │   │   ├── embeddings.data.json
│   │   │   │   ├── embeddings.meta.json
│   │   │   │   ├── embeddings_flax.data.json
│   │   │   │   ├── embeddings_flax.meta.json
│   │   │   │   ├── lora.data.json
│   │   │   │   ├── lora.meta.json
│   │   │   │   ├── model_loading_utils.data.json
│   │   │   │   ├── model_loading_utils.meta.json
│   │   │   │   ├── modeling_flax_pytorch_utils.data.json
│   │   │   │   ├── modeling_flax_pytorch_utils.meta.json
│   │   │   │   ├── modeling_flax_utils.data.json
│   │   │   │   ├── modeling_flax_utils.meta.json
│   │   │   │   ├── modeling_outputs.data.json
│   │   │   │   ├── modeling_outputs.meta.json
│   │   │   │   ├── modeling_pytorch_flax_utils.data.json
│   │   │   │   ├── modeling_pytorch_flax_utils.meta.json
│   │   │   │   ├── modeling_utils.data.json
│   │   │   │   ├── modeling_utils.meta.json
│   │   │   │   ├── normalization.data.json
│   │   │   │   ├── normalization.meta.json
│   │   │   │   ├── resnet.data.json
│   │   │   │   ├── resnet.meta.json
│   │   │   │   ├── resnet_flax.data.json
│   │   │   │   ├── resnet_flax.meta.json
│   │   │   │   ├── transformers
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── auraflow_transformer_2d.data.json
│   │   │   │   │   ├── auraflow_transformer_2d.meta.json
│   │   │   │   │   ├── cogvideox_transformer_3d.data.json
│   │   │   │   │   ├── cogvideox_transformer_3d.meta.json
│   │   │   │   │   ├── consisid_transformer_3d.data.json
│   │   │   │   │   ├── consisid_transformer_3d.meta.json
│   │   │   │   │   ├── dit_transformer_2d.data.json
│   │   │   │   │   ├── dit_transformer_2d.meta.json
│   │   │   │   │   ├── dual_transformer_2d.data.json
│   │   │   │   │   ├── dual_transformer_2d.meta.json
│   │   │   │   │   ├── hunyuan_transformer_2d.data.json
│   │   │   │   │   ├── hunyuan_transformer_2d.meta.json
│   │   │   │   │   ├── latte_transformer_3d.data.json
│   │   │   │   │   ├── latte_transformer_3d.meta.json
│   │   │   │   │   ├── lumina_nextdit2d.data.json
│   │   │   │   │   ├── lumina_nextdit2d.meta.json
│   │   │   │   │   ├── pixart_transformer_2d.data.json
│   │   │   │   │   ├── pixart_transformer_2d.meta.json
│   │   │   │   │   ├── prior_transformer.data.json
│   │   │   │   │   ├── prior_transformer.meta.json
│   │   │   │   │   ├── sana_transformer.data.json
│   │   │   │   │   ├── sana_transformer.meta.json
│   │   │   │   │   ├── stable_audio_transformer.data.json
│   │   │   │   │   ├── stable_audio_transformer.meta.json
│   │   │   │   │   ├── t5_film_transformer.data.json
│   │   │   │   │   ├── t5_film_transformer.meta.json
│   │   │   │   │   ├── transformer_2d.data.json
│   │   │   │   │   ├── transformer_2d.meta.json
│   │   │   │   │   ├── transformer_allegro.data.json
│   │   │   │   │   ├── transformer_allegro.meta.json
│   │   │   │   │   ├── transformer_chroma.data.json
│   │   │   │   │   ├── transformer_chroma.meta.json
│   │   │   │   │   ├── transformer_cogview3plus.data.json
│   │   │   │   │   ├── transformer_cogview3plus.meta.json
│   │   │   │   │   ├── transformer_cogview4.data.json
│   │   │   │   │   ├── transformer_cogview4.meta.json
│   │   │   │   │   ├── transformer_cosmos.data.json
│   │   │   │   │   ├── transformer_cosmos.meta.json
│   │   │   │   │   ├── transformer_easyanimate.data.json
│   │   │   │   │   ├── transformer_easyanimate.meta.json
│   │   │   │   │   ├── transformer_flux.data.json
│   │   │   │   │   ├── transformer_flux.meta.json
│   │   │   │   │   ├── transformer_hidream_image.data.json
│   │   │   │   │   ├── transformer_hidream_image.meta.json
│   │   │   │   │   ├── transformer_hunyuan_video.data.json
│   │   │   │   │   ├── transformer_hunyuan_video.meta.json
│   │   │   │   │   ├── transformer_hunyuan_video_framepack.data.json
│   │   │   │   │   ├── transformer_hunyuan_video_framepack.meta.json
│   │   │   │   │   ├── transformer_ltx.data.json
│   │   │   │   │   ├── transformer_ltx.meta.json
│   │   │   │   │   ├── transformer_lumina2.data.json
│   │   │   │   │   ├── transformer_lumina2.meta.json
│   │   │   │   │   ├── transformer_mochi.data.json
│   │   │   │   │   ├── transformer_mochi.meta.json
│   │   │   │   │   ├── transformer_omnigen.data.json
│   │   │   │   │   ├── transformer_omnigen.meta.json
│   │   │   │   │   ├── transformer_sd3.data.json
│   │   │   │   │   ├── transformer_sd3.meta.json
│   │   │   │   │   ├── transformer_temporal.data.json
│   │   │   │   │   ├── transformer_temporal.meta.json
│   │   │   │   │   ├── transformer_wan.data.json
│   │   │   │   │   ├── transformer_wan.meta.json
│   │   │   │   │   ├── transformer_wan_vace.data.json
│   │   │   │   │   └── transformer_wan_vace.meta.json
│   │   │   │   ├── unets
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── unet_1d.data.json
│   │   │   │   │   ├── unet_1d.meta.json
│   │   │   │   │   ├── unet_1d_blocks.data.json
│   │   │   │   │   ├── unet_1d_blocks.meta.json
│   │   │   │   │   ├── unet_2d.data.json
│   │   │   │   │   ├── unet_2d.meta.json
│   │   │   │   │   ├── unet_2d_blocks.data.json
│   │   │   │   │   ├── unet_2d_blocks.meta.json
│   │   │   │   │   ├── unet_2d_blocks_flax.data.json
│   │   │   │   │   ├── unet_2d_blocks_flax.meta.json
│   │   │   │   │   ├── unet_2d_condition.data.json
│   │   │   │   │   ├── unet_2d_condition.meta.json
│   │   │   │   │   ├── unet_2d_condition_flax.data.json
│   │   │   │   │   ├── unet_2d_condition_flax.meta.json
│   │   │   │   │   ├── unet_3d_blocks.data.json
│   │   │   │   │   ├── unet_3d_blocks.meta.json
│   │   │   │   │   ├── unet_3d_condition.data.json
│   │   │   │   │   ├── unet_3d_condition.meta.json
│   │   │   │   │   ├── unet_i2vgen_xl.data.json
│   │   │   │   │   ├── unet_i2vgen_xl.meta.json
│   │   │   │   │   ├── unet_kandinsky3.data.json
│   │   │   │   │   ├── unet_kandinsky3.meta.json
│   │   │   │   │   ├── unet_motion_model.data.json
│   │   │   │   │   ├── unet_motion_model.meta.json
│   │   │   │   │   ├── unet_spatio_temporal_condition.data.json
│   │   │   │   │   ├── unet_spatio_temporal_condition.meta.json
│   │   │   │   │   ├── unet_stable_cascade.data.json
│   │   │   │   │   ├── unet_stable_cascade.meta.json
│   │   │   │   │   ├── uvit_2d.data.json
│   │   │   │   │   └── uvit_2d.meta.json
│   │   │   │   ├── upsampling.data.json
│   │   │   │   ├── upsampling.meta.json
│   │   │   │   ├── vae_flax.data.json
│   │   │   │   ├── vae_flax.meta.json
│   │   │   │   ├── vq_model.data.json
│   │   │   │   └── vq_model.meta.json
│   │   │   ├── optimization.data.json
│   │   │   ├── optimization.meta.json
│   │   │   ├── pipelines
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── allegro
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_allegro.data.json
│   │   │   │   │   ├── pipeline_allegro.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── amused
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_amused.data.json
│   │   │   │   │   ├── pipeline_amused.meta.json
│   │   │   │   │   ├── pipeline_amused_img2img.data.json
│   │   │   │   │   ├── pipeline_amused_img2img.meta.json
│   │   │   │   │   ├── pipeline_amused_inpaint.data.json
│   │   │   │   │   └── pipeline_amused_inpaint.meta.json
│   │   │   │   ├── animatediff
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_animatediff.data.json
│   │   │   │   │   ├── pipeline_animatediff.meta.json
│   │   │   │   │   ├── pipeline_animatediff_controlnet.data.json
│   │   │   │   │   ├── pipeline_animatediff_controlnet.meta.json
│   │   │   │   │   ├── pipeline_animatediff_sdxl.data.json
│   │   │   │   │   ├── pipeline_animatediff_sdxl.meta.json
│   │   │   │   │   ├── pipeline_animatediff_sparsectrl.data.json
│   │   │   │   │   ├── pipeline_animatediff_sparsectrl.meta.json
│   │   │   │   │   ├── pipeline_animatediff_video2video.data.json
│   │   │   │   │   ├── pipeline_animatediff_video2video.meta.json
│   │   │   │   │   ├── pipeline_animatediff_video2video_controlnet.data.json
│   │   │   │   │   ├── pipeline_animatediff_video2video_controlnet.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── audioldm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_audioldm.data.json
│   │   │   │   │   └── pipeline_audioldm.meta.json
│   │   │   │   ├── audioldm2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── modeling_audioldm2.data.json
│   │   │   │   │   ├── modeling_audioldm2.meta.json
│   │   │   │   │   ├── pipeline_audioldm2.data.json
│   │   │   │   │   └── pipeline_audioldm2.meta.json
│   │   │   │   ├── aura_flow
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_aura_flow.data.json
│   │   │   │   │   └── pipeline_aura_flow.meta.json
│   │   │   │   ├── auto_pipeline.data.json
│   │   │   │   ├── auto_pipeline.meta.json
│   │   │   │   ├── blip_diffusion
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── blip_image_processing.data.json
│   │   │   │   │   ├── blip_image_processing.meta.json
│   │   │   │   │   ├── modeling_blip2.data.json
│   │   │   │   │   ├── modeling_blip2.meta.json
│   │   │   │   │   ├── modeling_ctx_clip.data.json
│   │   │   │   │   ├── modeling_ctx_clip.meta.json
│   │   │   │   │   ├── pipeline_blip_diffusion.data.json
│   │   │   │   │   └── pipeline_blip_diffusion.meta.json
│   │   │   │   ├── chroma
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_chroma.data.json
│   │   │   │   │   ├── pipeline_chroma.meta.json
│   │   │   │   │   ├── pipeline_chroma_img2img.data.json
│   │   │   │   │   ├── pipeline_chroma_img2img.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── cogvideo
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_cogvideox.data.json
│   │   │   │   │   ├── pipeline_cogvideox.meta.json
│   │   │   │   │   ├── pipeline_cogvideox_fun_control.data.json
│   │   │   │   │   ├── pipeline_cogvideox_fun_control.meta.json
│   │   │   │   │   ├── pipeline_cogvideox_image2video.data.json
│   │   │   │   │   ├── pipeline_cogvideox_image2video.meta.json
│   │   │   │   │   ├── pipeline_cogvideox_video2video.data.json
│   │   │   │   │   ├── pipeline_cogvideox_video2video.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── cogview3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_cogview3plus.data.json
│   │   │   │   │   ├── pipeline_cogview3plus.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── cogview4
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_cogview4.data.json
│   │   │   │   │   ├── pipeline_cogview4.meta.json
│   │   │   │   │   ├── pipeline_cogview4_control.data.json
│   │   │   │   │   ├── pipeline_cogview4_control.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── consisid
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_consisid.data.json
│   │   │   │   │   ├── pipeline_consisid.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── consistency_models
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_consistency_models.data.json
│   │   │   │   │   └── pipeline_consistency_models.meta.json
│   │   │   │   ├── controlnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── multicontrolnet.data.json
│   │   │   │   │   ├── multicontrolnet.meta.json
│   │   │   │   │   ├── pipeline_controlnet.data.json
│   │   │   │   │   ├── pipeline_controlnet.meta.json
│   │   │   │   │   ├── pipeline_controlnet_blip_diffusion.data.json
│   │   │   │   │   ├── pipeline_controlnet_blip_diffusion.meta.json
│   │   │   │   │   ├── pipeline_controlnet_img2img.data.json
│   │   │   │   │   ├── pipeline_controlnet_img2img.meta.json
│   │   │   │   │   ├── pipeline_controlnet_inpaint.data.json
│   │   │   │   │   ├── pipeline_controlnet_inpaint.meta.json
│   │   │   │   │   ├── pipeline_controlnet_inpaint_sd_xl.data.json
│   │   │   │   │   ├── pipeline_controlnet_inpaint_sd_xl.meta.json
│   │   │   │   │   ├── pipeline_controlnet_sd_xl.data.json
│   │   │   │   │   ├── pipeline_controlnet_sd_xl.meta.json
│   │   │   │   │   ├── pipeline_controlnet_sd_xl_img2img.data.json
│   │   │   │   │   ├── pipeline_controlnet_sd_xl_img2img.meta.json
│   │   │   │   │   ├── pipeline_controlnet_union_inpaint_sd_xl.data.json
│   │   │   │   │   ├── pipeline_controlnet_union_inpaint_sd_xl.meta.json
│   │   │   │   │   ├── pipeline_controlnet_union_sd_xl.data.json
│   │   │   │   │   ├── pipeline_controlnet_union_sd_xl.meta.json
│   │   │   │   │   ├── pipeline_controlnet_union_sd_xl_img2img.data.json
│   │   │   │   │   ├── pipeline_controlnet_union_sd_xl_img2img.meta.json
│   │   │   │   │   ├── pipeline_flax_controlnet.data.json
│   │   │   │   │   └── pipeline_flax_controlnet.meta.json
│   │   │   │   ├── controlnet_hunyuandit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_hunyuandit_controlnet.data.json
│   │   │   │   │   └── pipeline_hunyuandit_controlnet.meta.json
│   │   │   │   ├── controlnet_sd3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_3_controlnet.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_3_controlnet.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_3_controlnet_inpainting.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_3_controlnet_inpainting.meta.json
│   │   │   │   ├── controlnet_xs
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_controlnet_xs.data.json
│   │   │   │   │   ├── pipeline_controlnet_xs.meta.json
│   │   │   │   │   ├── pipeline_controlnet_xs_sd_xl.data.json
│   │   │   │   │   └── pipeline_controlnet_xs_sd_xl.meta.json
│   │   │   │   ├── cosmos
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_cosmos2_text2image.data.json
│   │   │   │   │   ├── pipeline_cosmos2_text2image.meta.json
│   │   │   │   │   ├── pipeline_cosmos2_video2world.data.json
│   │   │   │   │   ├── pipeline_cosmos2_video2world.meta.json
│   │   │   │   │   ├── pipeline_cosmos_text2world.data.json
│   │   │   │   │   ├── pipeline_cosmos_text2world.meta.json
│   │   │   │   │   ├── pipeline_cosmos_video2world.data.json
│   │   │   │   │   ├── pipeline_cosmos_video2world.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── dance_diffusion
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_dance_diffusion.data.json
│   │   │   │   │   └── pipeline_dance_diffusion.meta.json
│   │   │   │   ├── ddim
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_ddim.data.json
│   │   │   │   │   └── pipeline_ddim.meta.json
│   │   │   │   ├── ddpm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_ddpm.data.json
│   │   │   │   │   └── pipeline_ddpm.meta.json
│   │   │   │   ├── deepfloyd_if
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_if.data.json
│   │   │   │   │   ├── pipeline_if.meta.json
│   │   │   │   │   ├── pipeline_if_img2img.data.json
│   │   │   │   │   ├── pipeline_if_img2img.meta.json
│   │   │   │   │   ├── pipeline_if_img2img_superresolution.data.json
│   │   │   │   │   ├── pipeline_if_img2img_superresolution.meta.json
│   │   │   │   │   ├── pipeline_if_inpainting.data.json
│   │   │   │   │   ├── pipeline_if_inpainting.meta.json
│   │   │   │   │   ├── pipeline_if_inpainting_superresolution.data.json
│   │   │   │   │   ├── pipeline_if_inpainting_superresolution.meta.json
│   │   │   │   │   ├── pipeline_if_superresolution.data.json
│   │   │   │   │   ├── pipeline_if_superresolution.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── safety_checker.data.json
│   │   │   │   │   ├── safety_checker.meta.json
│   │   │   │   │   ├── timesteps.data.json
│   │   │   │   │   ├── timesteps.meta.json
│   │   │   │   │   ├── watermark.data.json
│   │   │   │   │   └── watermark.meta.json
│   │   │   │   ├── deprecated
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── alt_diffusion
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── modeling_roberta_series.data.json
│   │   │   │   │   │   ├── modeling_roberta_series.meta.json
│   │   │   │   │   │   ├── pipeline_alt_diffusion.data.json
│   │   │   │   │   │   ├── pipeline_alt_diffusion.meta.json
│   │   │   │   │   │   ├── pipeline_alt_diffusion_img2img.data.json
│   │   │   │   │   │   ├── pipeline_alt_diffusion_img2img.meta.json
│   │   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   │   ├── audio_diffusion
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── mel.data.json
│   │   │   │   │   │   ├── mel.meta.json
│   │   │   │   │   │   ├── pipeline_audio_diffusion.data.json
│   │   │   │   │   │   └── pipeline_audio_diffusion.meta.json
│   │   │   │   │   ├── latent_diffusion_uncond
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── pipeline_latent_diffusion_uncond.data.json
│   │   │   │   │   │   └── pipeline_latent_diffusion_uncond.meta.json
│   │   │   │   │   ├── pndm
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── pipeline_pndm.data.json
│   │   │   │   │   │   └── pipeline_pndm.meta.json
│   │   │   │   │   ├── repaint
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── pipeline_repaint.data.json
│   │   │   │   │   │   └── pipeline_repaint.meta.json
│   │   │   │   │   ├── score_sde_ve
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── pipeline_score_sde_ve.data.json
│   │   │   │   │   │   └── pipeline_score_sde_ve.meta.json
│   │   │   │   │   ├── spectrogram_diffusion
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── continuous_encoder.data.json
│   │   │   │   │   │   ├── continuous_encoder.meta.json
│   │   │   │   │   │   ├── midi_utils.data.json
│   │   │   │   │   │   ├── midi_utils.meta.json
│   │   │   │   │   │   ├── notes_encoder.data.json
│   │   │   │   │   │   ├── notes_encoder.meta.json
│   │   │   │   │   │   ├── pipeline_spectrogram_diffusion.data.json
│   │   │   │   │   │   └── pipeline_spectrogram_diffusion.meta.json
│   │   │   │   │   ├── stable_diffusion_variants
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── pipeline_cycle_diffusion.data.json
│   │   │   │   │   │   ├── pipeline_cycle_diffusion.meta.json
│   │   │   │   │   │   ├── pipeline_stable_diffusion_inpaint_legacy.data.json
│   │   │   │   │   │   ├── pipeline_stable_diffusion_inpaint_legacy.meta.json
│   │   │   │   │   │   ├── pipeline_stable_diffusion_model_editing.data.json
│   │   │   │   │   │   ├── pipeline_stable_diffusion_model_editing.meta.json
│   │   │   │   │   │   ├── pipeline_stable_diffusion_paradigms.data.json
│   │   │   │   │   │   ├── pipeline_stable_diffusion_paradigms.meta.json
│   │   │   │   │   │   ├── pipeline_stable_diffusion_pix2pix_zero.data.json
│   │   │   │   │   │   └── pipeline_stable_diffusion_pix2pix_zero.meta.json
│   │   │   │   │   ├── stochastic_karras_ve
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── pipeline_stochastic_karras_ve.data.json
│   │   │   │   │   │   └── pipeline_stochastic_karras_ve.meta.json
│   │   │   │   │   ├── versatile_diffusion
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── modeling_text_unet.data.json
│   │   │   │   │   │   ├── modeling_text_unet.meta.json
│   │   │   │   │   │   ├── pipeline_versatile_diffusion.data.json
│   │   │   │   │   │   ├── pipeline_versatile_diffusion.meta.json
│   │   │   │   │   │   ├── pipeline_versatile_diffusion_dual_guided.data.json
│   │   │   │   │   │   ├── pipeline_versatile_diffusion_dual_guided.meta.json
│   │   │   │   │   │   ├── pipeline_versatile_diffusion_image_variation.data.json
│   │   │   │   │   │   ├── pipeline_versatile_diffusion_image_variation.meta.json
│   │   │   │   │   │   ├── pipeline_versatile_diffusion_text_to_image.data.json
│   │   │   │   │   │   └── pipeline_versatile_diffusion_text_to_image.meta.json
│   │   │   │   │   └── vq_diffusion
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── pipeline_vq_diffusion.data.json
│   │   │   │   │       └── pipeline_vq_diffusion.meta.json
│   │   │   │   ├── dit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_dit.data.json
│   │   │   │   │   └── pipeline_dit.meta.json
│   │   │   │   ├── easyanimate
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_easyanimate.data.json
│   │   │   │   │   ├── pipeline_easyanimate.meta.json
│   │   │   │   │   ├── pipeline_easyanimate_control.data.json
│   │   │   │   │   ├── pipeline_easyanimate_control.meta.json
│   │   │   │   │   ├── pipeline_easyanimate_inpaint.data.json
│   │   │   │   │   ├── pipeline_easyanimate_inpaint.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── flux
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── modeling_flux.data.json
│   │   │   │   │   ├── modeling_flux.meta.json
│   │   │   │   │   ├── pipeline_flux.data.json
│   │   │   │   │   ├── pipeline_flux.meta.json
│   │   │   │   │   ├── pipeline_flux_control.data.json
│   │   │   │   │   ├── pipeline_flux_control.meta.json
│   │   │   │   │   ├── pipeline_flux_control_img2img.data.json
│   │   │   │   │   ├── pipeline_flux_control_img2img.meta.json
│   │   │   │   │   ├── pipeline_flux_control_inpaint.data.json
│   │   │   │   │   ├── pipeline_flux_control_inpaint.meta.json
│   │   │   │   │   ├── pipeline_flux_controlnet.data.json
│   │   │   │   │   ├── pipeline_flux_controlnet.meta.json
│   │   │   │   │   ├── pipeline_flux_controlnet_image_to_image.data.json
│   │   │   │   │   ├── pipeline_flux_controlnet_image_to_image.meta.json
│   │   │   │   │   ├── pipeline_flux_controlnet_inpainting.data.json
│   │   │   │   │   ├── pipeline_flux_controlnet_inpainting.meta.json
│   │   │   │   │   ├── pipeline_flux_fill.data.json
│   │   │   │   │   ├── pipeline_flux_fill.meta.json
│   │   │   │   │   ├── pipeline_flux_img2img.data.json
│   │   │   │   │   ├── pipeline_flux_img2img.meta.json
│   │   │   │   │   ├── pipeline_flux_inpaint.data.json
│   │   │   │   │   ├── pipeline_flux_inpaint.meta.json
│   │   │   │   │   ├── pipeline_flux_prior_redux.data.json
│   │   │   │   │   ├── pipeline_flux_prior_redux.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── free_init_utils.data.json
│   │   │   │   ├── free_init_utils.meta.json
│   │   │   │   ├── free_noise_utils.data.json
│   │   │   │   ├── free_noise_utils.meta.json
│   │   │   │   ├── hidream_image
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_hidream_image.data.json
│   │   │   │   │   ├── pipeline_hidream_image.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── hunyuan_video
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_hunyuan_skyreels_image2video.data.json
│   │   │   │   │   ├── pipeline_hunyuan_skyreels_image2video.meta.json
│   │   │   │   │   ├── pipeline_hunyuan_video.data.json
│   │   │   │   │   ├── pipeline_hunyuan_video.meta.json
│   │   │   │   │   ├── pipeline_hunyuan_video_framepack.data.json
│   │   │   │   │   ├── pipeline_hunyuan_video_framepack.meta.json
│   │   │   │   │   ├── pipeline_hunyuan_video_image2video.data.json
│   │   │   │   │   ├── pipeline_hunyuan_video_image2video.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── hunyuandit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_hunyuandit.data.json
│   │   │   │   │   └── pipeline_hunyuandit.meta.json
│   │   │   │   ├── i2vgen_xl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_i2vgen_xl.data.json
│   │   │   │   │   └── pipeline_i2vgen_xl.meta.json
│   │   │   │   ├── kandinsky
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_kandinsky.data.json
│   │   │   │   │   ├── pipeline_kandinsky.meta.json
│   │   │   │   │   ├── pipeline_kandinsky_combined.data.json
│   │   │   │   │   ├── pipeline_kandinsky_combined.meta.json
│   │   │   │   │   ├── pipeline_kandinsky_img2img.data.json
│   │   │   │   │   ├── pipeline_kandinsky_img2img.meta.json
│   │   │   │   │   ├── pipeline_kandinsky_inpaint.data.json
│   │   │   │   │   ├── pipeline_kandinsky_inpaint.meta.json
│   │   │   │   │   ├── pipeline_kandinsky_prior.data.json
│   │   │   │   │   ├── pipeline_kandinsky_prior.meta.json
│   │   │   │   │   ├── text_encoder.data.json
│   │   │   │   │   └── text_encoder.meta.json
│   │   │   │   ├── kandinsky2_2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_kandinsky2_2.data.json
│   │   │   │   │   ├── pipeline_kandinsky2_2.meta.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_combined.data.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_combined.meta.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_controlnet.data.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_controlnet.meta.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_controlnet_img2img.data.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_controlnet_img2img.meta.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_img2img.data.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_img2img.meta.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_inpainting.data.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_inpainting.meta.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_prior.data.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_prior.meta.json
│   │   │   │   │   ├── pipeline_kandinsky2_2_prior_emb2emb.data.json
│   │   │   │   │   └── pipeline_kandinsky2_2_prior_emb2emb.meta.json
│   │   │   │   ├── kandinsky3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_kandinsky3.data.json
│   │   │   │   │   ├── pipeline_kandinsky3.meta.json
│   │   │   │   │   ├── pipeline_kandinsky3_img2img.data.json
│   │   │   │   │   └── pipeline_kandinsky3_img2img.meta.json
│   │   │   │   ├── kolors
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_kolors.data.json
│   │   │   │   │   ├── pipeline_kolors.meta.json
│   │   │   │   │   ├── pipeline_kolors_img2img.data.json
│   │   │   │   │   ├── pipeline_kolors_img2img.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── text_encoder.data.json
│   │   │   │   │   ├── text_encoder.meta.json
│   │   │   │   │   ├── tokenizer.data.json
│   │   │   │   │   └── tokenizer.meta.json
│   │   │   │   ├── latent_consistency_models
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_latent_consistency_img2img.data.json
│   │   │   │   │   ├── pipeline_latent_consistency_img2img.meta.json
│   │   │   │   │   ├── pipeline_latent_consistency_text2img.data.json
│   │   │   │   │   └── pipeline_latent_consistency_text2img.meta.json
│   │   │   │   ├── latent_diffusion
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_latent_diffusion.data.json
│   │   │   │   │   ├── pipeline_latent_diffusion.meta.json
│   │   │   │   │   ├── pipeline_latent_diffusion_superresolution.data.json
│   │   │   │   │   └── pipeline_latent_diffusion_superresolution.meta.json
│   │   │   │   ├── latte
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_latte.data.json
│   │   │   │   │   └── pipeline_latte.meta.json
│   │   │   │   ├── ledits_pp
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_leditspp_stable_diffusion.data.json
│   │   │   │   │   ├── pipeline_leditspp_stable_diffusion.meta.json
│   │   │   │   │   ├── pipeline_leditspp_stable_diffusion_xl.data.json
│   │   │   │   │   ├── pipeline_leditspp_stable_diffusion_xl.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── ltx
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── modeling_latent_upsampler.data.json
│   │   │   │   │   ├── modeling_latent_upsampler.meta.json
│   │   │   │   │   ├── pipeline_ltx.data.json
│   │   │   │   │   ├── pipeline_ltx.meta.json
│   │   │   │   │   ├── pipeline_ltx_condition.data.json
│   │   │   │   │   ├── pipeline_ltx_condition.meta.json
│   │   │   │   │   ├── pipeline_ltx_image2video.data.json
│   │   │   │   │   ├── pipeline_ltx_image2video.meta.json
│   │   │   │   │   ├── pipeline_ltx_latent_upsample.data.json
│   │   │   │   │   ├── pipeline_ltx_latent_upsample.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── lumina
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_lumina.data.json
│   │   │   │   │   └── pipeline_lumina.meta.json
│   │   │   │   ├── lumina2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_lumina2.data.json
│   │   │   │   │   └── pipeline_lumina2.meta.json
│   │   │   │   ├── marigold
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── marigold_image_processing.data.json
│   │   │   │   │   ├── marigold_image_processing.meta.json
│   │   │   │   │   ├── pipeline_marigold_depth.data.json
│   │   │   │   │   ├── pipeline_marigold_depth.meta.json
│   │   │   │   │   ├── pipeline_marigold_intrinsics.data.json
│   │   │   │   │   ├── pipeline_marigold_intrinsics.meta.json
│   │   │   │   │   ├── pipeline_marigold_normals.data.json
│   │   │   │   │   └── pipeline_marigold_normals.meta.json
│   │   │   │   ├── mochi
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_mochi.data.json
│   │   │   │   │   ├── pipeline_mochi.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   └── pipeline_output.meta.json
│   │   │   │   ├── musicldm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_musicldm.data.json
│   │   │   │   │   └── pipeline_musicldm.meta.json
│   │   │   │   ├── omnigen
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_omnigen.data.json
│   │   │   │   │   ├── pipeline_omnigen.meta.json
│   │   │   │   │   ├── processor_omnigen.data.json
│   │   │   │   │   └── processor_omnigen.meta.json
│   │   │   │   ├── onnx_utils.data.json
│   │   │   │   ├── onnx_utils.meta.json
│   │   │   │   ├── pag
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pag_utils.data.json
│   │   │   │   │   ├── pag_utils.meta.json
│   │   │   │   │   ├── pipeline_pag_controlnet_sd.data.json
│   │   │   │   │   ├── pipeline_pag_controlnet_sd.meta.json
│   │   │   │   │   ├── pipeline_pag_controlnet_sd_inpaint.data.json
│   │   │   │   │   ├── pipeline_pag_controlnet_sd_inpaint.meta.json
│   │   │   │   │   ├── pipeline_pag_controlnet_sd_xl.data.json
│   │   │   │   │   ├── pipeline_pag_controlnet_sd_xl.meta.json
│   │   │   │   │   ├── pipeline_pag_controlnet_sd_xl_img2img.data.json
│   │   │   │   │   ├── pipeline_pag_controlnet_sd_xl_img2img.meta.json
│   │   │   │   │   ├── pipeline_pag_hunyuandit.data.json
│   │   │   │   │   ├── pipeline_pag_hunyuandit.meta.json
│   │   │   │   │   ├── pipeline_pag_kolors.data.json
│   │   │   │   │   ├── pipeline_pag_kolors.meta.json
│   │   │   │   │   ├── pipeline_pag_pixart_sigma.data.json
│   │   │   │   │   ├── pipeline_pag_pixart_sigma.meta.json
│   │   │   │   │   ├── pipeline_pag_sana.data.json
│   │   │   │   │   ├── pipeline_pag_sana.meta.json
│   │   │   │   │   ├── pipeline_pag_sd.data.json
│   │   │   │   │   ├── pipeline_pag_sd.meta.json
│   │   │   │   │   ├── pipeline_pag_sd_3.data.json
│   │   │   │   │   ├── pipeline_pag_sd_3.meta.json
│   │   │   │   │   ├── pipeline_pag_sd_3_img2img.data.json
│   │   │   │   │   ├── pipeline_pag_sd_3_img2img.meta.json
│   │   │   │   │   ├── pipeline_pag_sd_animatediff.data.json
│   │   │   │   │   ├── pipeline_pag_sd_animatediff.meta.json
│   │   │   │   │   ├── pipeline_pag_sd_img2img.data.json
│   │   │   │   │   ├── pipeline_pag_sd_img2img.meta.json
│   │   │   │   │   ├── pipeline_pag_sd_inpaint.data.json
│   │   │   │   │   ├── pipeline_pag_sd_inpaint.meta.json
│   │   │   │   │   ├── pipeline_pag_sd_xl.data.json
│   │   │   │   │   ├── pipeline_pag_sd_xl.meta.json
│   │   │   │   │   ├── pipeline_pag_sd_xl_img2img.data.json
│   │   │   │   │   ├── pipeline_pag_sd_xl_img2img.meta.json
│   │   │   │   │   ├── pipeline_pag_sd_xl_inpaint.data.json
│   │   │   │   │   └── pipeline_pag_sd_xl_inpaint.meta.json
│   │   │   │   ├── paint_by_example
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── image_encoder.data.json
│   │   │   │   │   ├── image_encoder.meta.json
│   │   │   │   │   ├── pipeline_paint_by_example.data.json
│   │   │   │   │   └── pipeline_paint_by_example.meta.json
│   │   │   │   ├── pia
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_pia.data.json
│   │   │   │   │   └── pipeline_pia.meta.json
│   │   │   │   ├── pipeline_flax_utils.data.json
│   │   │   │   ├── pipeline_flax_utils.meta.json
│   │   │   │   ├── pipeline_loading_utils.data.json
│   │   │   │   ├── pipeline_loading_utils.meta.json
│   │   │   │   ├── pipeline_utils.data.json
│   │   │   │   ├── pipeline_utils.meta.json
│   │   │   │   ├── pixart_alpha
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_pixart_alpha.data.json
│   │   │   │   │   ├── pipeline_pixart_alpha.meta.json
│   │   │   │   │   ├── pipeline_pixart_sigma.data.json
│   │   │   │   │   └── pipeline_pixart_sigma.meta.json
│   │   │   │   ├── sana
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── pipeline_sana.data.json
│   │   │   │   │   ├── pipeline_sana.meta.json
│   │   │   │   │   ├── pipeline_sana_controlnet.data.json
│   │   │   │   │   ├── pipeline_sana_controlnet.meta.json
│   │   │   │   │   ├── pipeline_sana_sprint.data.json
│   │   │   │   │   ├── pipeline_sana_sprint.meta.json
│   │   │   │   │   ├── pipeline_sana_sprint_img2img.data.json
│   │   │   │   │   └── pipeline_sana_sprint_img2img.meta.json
│   │   │   │   ├── semantic_stable_diffusion
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── pipeline_semantic_stable_diffusion.data.json
│   │   │   │   │   └── pipeline_semantic_stable_diffusion.meta.json
│   │   │   │   ├── shap_e
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── camera.data.json
│   │   │   │   │   ├── camera.meta.json
│   │   │   │   │   ├── pipeline_shap_e.data.json
│   │   │   │   │   ├── pipeline_shap_e.meta.json
│   │   │   │   │   ├── pipeline_shap_e_img2img.data.json
│   │   │   │   │   ├── pipeline_shap_e_img2img.meta.json
│   │   │   │   │   ├── renderer.data.json
│   │   │   │   │   └── renderer.meta.json
│   │   │   │   ├── stable_audio
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── modeling_stable_audio.data.json
│   │   │   │   │   ├── modeling_stable_audio.meta.json
│   │   │   │   │   ├── pipeline_stable_audio.data.json
│   │   │   │   │   └── pipeline_stable_audio.meta.json
│   │   │   │   ├── stable_cascade
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_cascade.data.json
│   │   │   │   │   ├── pipeline_stable_cascade.meta.json
│   │   │   │   │   ├── pipeline_stable_cascade_combined.data.json
│   │   │   │   │   ├── pipeline_stable_cascade_combined.meta.json
│   │   │   │   │   ├── pipeline_stable_cascade_prior.data.json
│   │   │   │   │   └── pipeline_stable_cascade_prior.meta.json
│   │   │   │   ├── stable_diffusion
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── clip_image_project_model.data.json
│   │   │   │   │   ├── clip_image_project_model.meta.json
│   │   │   │   │   ├── pipeline_flax_stable_diffusion.data.json
│   │   │   │   │   ├── pipeline_flax_stable_diffusion.meta.json
│   │   │   │   │   ├── pipeline_flax_stable_diffusion_img2img.data.json
│   │   │   │   │   ├── pipeline_flax_stable_diffusion_img2img.meta.json
│   │   │   │   │   ├── pipeline_flax_stable_diffusion_inpaint.data.json
│   │   │   │   │   ├── pipeline_flax_stable_diffusion_inpaint.meta.json
│   │   │   │   │   ├── pipeline_onnx_stable_diffusion.data.json
│   │   │   │   │   ├── pipeline_onnx_stable_diffusion.meta.json
│   │   │   │   │   ├── pipeline_onnx_stable_diffusion_img2img.data.json
│   │   │   │   │   ├── pipeline_onnx_stable_diffusion_img2img.meta.json
│   │   │   │   │   ├── pipeline_onnx_stable_diffusion_inpaint.data.json
│   │   │   │   │   ├── pipeline_onnx_stable_diffusion_inpaint.meta.json
│   │   │   │   │   ├── pipeline_onnx_stable_diffusion_upscale.data.json
│   │   │   │   │   ├── pipeline_onnx_stable_diffusion_upscale.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_depth2img.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_depth2img.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_image_variation.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_image_variation.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_img2img.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_img2img.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_inpaint.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_inpaint.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_instruct_pix2pix.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_instruct_pix2pix.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_latent_upscale.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_latent_upscale.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_upscale.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_upscale.meta.json
│   │   │   │   │   ├── pipeline_stable_unclip.data.json
│   │   │   │   │   ├── pipeline_stable_unclip.meta.json
│   │   │   │   │   ├── pipeline_stable_unclip_img2img.data.json
│   │   │   │   │   ├── pipeline_stable_unclip_img2img.meta.json
│   │   │   │   │   ├── safety_checker.data.json
│   │   │   │   │   ├── safety_checker.meta.json
│   │   │   │   │   ├── safety_checker_flax.data.json
│   │   │   │   │   ├── safety_checker_flax.meta.json
│   │   │   │   │   ├── stable_unclip_image_normalizer.data.json
│   │   │   │   │   └── stable_unclip_image_normalizer.meta.json
│   │   │   │   ├── stable_diffusion_3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_3.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_3.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_3_img2img.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_3_img2img.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_3_inpaint.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_3_inpaint.meta.json
│   │   │   │   ├── stable_diffusion_attend_and_excite
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_attend_and_excite.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_attend_and_excite.meta.json
│   │   │   │   ├── stable_diffusion_diffedit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_diffedit.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_diffedit.meta.json
│   │   │   │   ├── stable_diffusion_gligen
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_gligen.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_gligen.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_gligen_text_image.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_gligen_text_image.meta.json
│   │   │   │   ├── stable_diffusion_k_diffusion
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_k_diffusion.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_k_diffusion.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl_k_diffusion.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_xl_k_diffusion.meta.json
│   │   │   │   ├── stable_diffusion_ldm3d
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_ldm3d.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_ldm3d.meta.json
│   │   │   │   ├── stable_diffusion_panorama
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_panorama.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_panorama.meta.json
│   │   │   │   ├── stable_diffusion_safe
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_safe.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_safe.meta.json
│   │   │   │   │   ├── safety_checker.data.json
│   │   │   │   │   └── safety_checker.meta.json
│   │   │   │   ├── stable_diffusion_sag
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_sag.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_sag.meta.json
│   │   │   │   ├── stable_diffusion_xl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_flax_stable_diffusion_xl.data.json
│   │   │   │   │   ├── pipeline_flax_stable_diffusion_xl.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl_img2img.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl_img2img.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl_inpaint.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl_inpaint.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl_instruct_pix2pix.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl_instruct_pix2pix.meta.json
│   │   │   │   │   ├── watermark.data.json
│   │   │   │   │   └── watermark.meta.json
│   │   │   │   ├── stable_video_diffusion
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_video_diffusion.data.json
│   │   │   │   │   └── pipeline_stable_video_diffusion.meta.json
│   │   │   │   ├── t2i_adapter
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_adapter.data.json
│   │   │   │   │   ├── pipeline_stable_diffusion_adapter.meta.json
│   │   │   │   │   ├── pipeline_stable_diffusion_xl_adapter.data.json
│   │   │   │   │   └── pipeline_stable_diffusion_xl_adapter.meta.json
│   │   │   │   ├── text_to_video_synthesis
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── pipeline_text_to_video_synth.data.json
│   │   │   │   │   ├── pipeline_text_to_video_synth.meta.json
│   │   │   │   │   ├── pipeline_text_to_video_synth_img2img.data.json
│   │   │   │   │   ├── pipeline_text_to_video_synth_img2img.meta.json
│   │   │   │   │   ├── pipeline_text_to_video_zero.data.json
│   │   │   │   │   ├── pipeline_text_to_video_zero.meta.json
│   │   │   │   │   ├── pipeline_text_to_video_zero_sdxl.data.json
│   │   │   │   │   └── pipeline_text_to_video_zero_sdxl.meta.json
│   │   │   │   ├── transformers_loading_utils.data.json
│   │   │   │   ├── transformers_loading_utils.meta.json
│   │   │   │   ├── unclip
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_unclip.data.json
│   │   │   │   │   ├── pipeline_unclip.meta.json
│   │   │   │   │   ├── pipeline_unclip_image_variation.data.json
│   │   │   │   │   ├── pipeline_unclip_image_variation.meta.json
│   │   │   │   │   ├── text_proj.data.json
│   │   │   │   │   └── text_proj.meta.json
│   │   │   │   ├── unidiffuser
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── modeling_text_decoder.data.json
│   │   │   │   │   ├── modeling_text_decoder.meta.json
│   │   │   │   │   ├── modeling_uvit.data.json
│   │   │   │   │   ├── modeling_uvit.meta.json
│   │   │   │   │   ├── pipeline_unidiffuser.data.json
│   │   │   │   │   └── pipeline_unidiffuser.meta.json
│   │   │   │   ├── visualcloze
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_visualcloze_combined.data.json
│   │   │   │   │   ├── pipeline_visualcloze_combined.meta.json
│   │   │   │   │   ├── pipeline_visualcloze_generation.data.json
│   │   │   │   │   ├── pipeline_visualcloze_generation.meta.json
│   │   │   │   │   ├── visualcloze_utils.data.json
│   │   │   │   │   └── visualcloze_utils.meta.json
│   │   │   │   ├── wan
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pipeline_output.data.json
│   │   │   │   │   ├── pipeline_output.meta.json
│   │   │   │   │   ├── pipeline_wan.data.json
│   │   │   │   │   ├── pipeline_wan.meta.json
│   │   │   │   │   ├── pipeline_wan_i2v.data.json
│   │   │   │   │   ├── pipeline_wan_i2v.meta.json
│   │   │   │   │   ├── pipeline_wan_vace.data.json
│   │   │   │   │   ├── pipeline_wan_vace.meta.json
│   │   │   │   │   ├── pipeline_wan_video2video.data.json
│   │   │   │   │   └── pipeline_wan_video2video.meta.json
│   │   │   │   └── wuerstchen
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── modeling_paella_vq_model.data.json
│   │   │   │       ├── modeling_paella_vq_model.meta.json
│   │   │   │       ├── modeling_wuerstchen_common.data.json
│   │   │   │       ├── modeling_wuerstchen_common.meta.json
│   │   │   │       ├── modeling_wuerstchen_diffnext.data.json
│   │   │   │       ├── modeling_wuerstchen_diffnext.meta.json
│   │   │   │       ├── modeling_wuerstchen_prior.data.json
│   │   │   │       ├── modeling_wuerstchen_prior.meta.json
│   │   │   │       ├── pipeline_wuerstchen.data.json
│   │   │   │       ├── pipeline_wuerstchen.meta.json
│   │   │   │       ├── pipeline_wuerstchen_combined.data.json
│   │   │   │       ├── pipeline_wuerstchen_combined.meta.json
│   │   │   │       ├── pipeline_wuerstchen_prior.data.json
│   │   │   │       └── pipeline_wuerstchen_prior.meta.json
│   │   │   ├── quantizers
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── auto.data.json
│   │   │   │   ├── auto.meta.json
│   │   │   │   ├── base.data.json
│   │   │   │   ├── base.meta.json
│   │   │   │   ├── bitsandbytes
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── bnb_quantizer.data.json
│   │   │   │   │   ├── bnb_quantizer.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   ├── gguf
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── gguf_quantizer.data.json
│   │   │   │   │   ├── gguf_quantizer.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   ├── quantization_config.data.json
│   │   │   │   ├── quantization_config.meta.json
│   │   │   │   ├── quanto
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── quanto_quantizer.data.json
│   │   │   │   │   ├── quanto_quantizer.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   └── torchao
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── torchao_quantizer.data.json
│   │   │   │       └── torchao_quantizer.meta.json
│   │   │   ├── schedulers
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── deprecated
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── scheduling_karras_ve.data.json
│   │   │   │   │   ├── scheduling_karras_ve.meta.json
│   │   │   │   │   ├── scheduling_sde_vp.data.json
│   │   │   │   │   └── scheduling_sde_vp.meta.json
│   │   │   │   ├── scheduling_amused.data.json
│   │   │   │   ├── scheduling_amused.meta.json
│   │   │   │   ├── scheduling_consistency_decoder.data.json
│   │   │   │   ├── scheduling_consistency_decoder.meta.json
│   │   │   │   ├── scheduling_consistency_models.data.json
│   │   │   │   ├── scheduling_consistency_models.meta.json
│   │   │   │   ├── scheduling_cosine_dpmsolver_multistep.data.json
│   │   │   │   ├── scheduling_cosine_dpmsolver_multistep.meta.json
│   │   │   │   ├── scheduling_ddim.data.json
│   │   │   │   ├── scheduling_ddim.meta.json
│   │   │   │   ├── scheduling_ddim_cogvideox.data.json
│   │   │   │   ├── scheduling_ddim_cogvideox.meta.json
│   │   │   │   ├── scheduling_ddim_flax.data.json
│   │   │   │   ├── scheduling_ddim_flax.meta.json
│   │   │   │   ├── scheduling_ddim_inverse.data.json
│   │   │   │   ├── scheduling_ddim_inverse.meta.json
│   │   │   │   ├── scheduling_ddim_parallel.data.json
│   │   │   │   ├── scheduling_ddim_parallel.meta.json
│   │   │   │   ├── scheduling_ddpm.data.json
│   │   │   │   ├── scheduling_ddpm.meta.json
│   │   │   │   ├── scheduling_ddpm_flax.data.json
│   │   │   │   ├── scheduling_ddpm_flax.meta.json
│   │   │   │   ├── scheduling_ddpm_parallel.data.json
│   │   │   │   ├── scheduling_ddpm_parallel.meta.json
│   │   │   │   ├── scheduling_ddpm_wuerstchen.data.json
│   │   │   │   ├── scheduling_ddpm_wuerstchen.meta.json
│   │   │   │   ├── scheduling_deis_multistep.data.json
│   │   │   │   ├── scheduling_deis_multistep.meta.json
│   │   │   │   ├── scheduling_dpm_cogvideox.data.json
│   │   │   │   ├── scheduling_dpm_cogvideox.meta.json
│   │   │   │   ├── scheduling_dpmsolver_multistep.data.json
│   │   │   │   ├── scheduling_dpmsolver_multistep.meta.json
│   │   │   │   ├── scheduling_dpmsolver_multistep_flax.data.json
│   │   │   │   ├── scheduling_dpmsolver_multistep_flax.meta.json
│   │   │   │   ├── scheduling_dpmsolver_multistep_inverse.data.json
│   │   │   │   ├── scheduling_dpmsolver_multistep_inverse.meta.json
│   │   │   │   ├── scheduling_dpmsolver_sde.data.json
│   │   │   │   ├── scheduling_dpmsolver_sde.meta.json
│   │   │   │   ├── scheduling_dpmsolver_singlestep.data.json
│   │   │   │   ├── scheduling_dpmsolver_singlestep.meta.json
│   │   │   │   ├── scheduling_edm_dpmsolver_multistep.data.json
│   │   │   │   ├── scheduling_edm_dpmsolver_multistep.meta.json
│   │   │   │   ├── scheduling_edm_euler.data.json
│   │   │   │   ├── scheduling_edm_euler.meta.json
│   │   │   │   ├── scheduling_euler_ancestral_discrete.data.json
│   │   │   │   ├── scheduling_euler_ancestral_discrete.meta.json
│   │   │   │   ├── scheduling_euler_discrete.data.json
│   │   │   │   ├── scheduling_euler_discrete.meta.json
│   │   │   │   ├── scheduling_euler_discrete_flax.data.json
│   │   │   │   ├── scheduling_euler_discrete_flax.meta.json
│   │   │   │   ├── scheduling_flow_match_euler_discrete.data.json
│   │   │   │   ├── scheduling_flow_match_euler_discrete.meta.json
│   │   │   │   ├── scheduling_flow_match_heun_discrete.data.json
│   │   │   │   ├── scheduling_flow_match_heun_discrete.meta.json
│   │   │   │   ├── scheduling_flow_match_lcm.data.json
│   │   │   │   ├── scheduling_flow_match_lcm.meta.json
│   │   │   │   ├── scheduling_heun_discrete.data.json
│   │   │   │   ├── scheduling_heun_discrete.meta.json
│   │   │   │   ├── scheduling_ipndm.data.json
│   │   │   │   ├── scheduling_ipndm.meta.json
│   │   │   │   ├── scheduling_k_dpm_2_ancestral_discrete.data.json
│   │   │   │   ├── scheduling_k_dpm_2_ancestral_discrete.meta.json
│   │   │   │   ├── scheduling_k_dpm_2_discrete.data.json
│   │   │   │   ├── scheduling_k_dpm_2_discrete.meta.json
│   │   │   │   ├── scheduling_karras_ve_flax.data.json
│   │   │   │   ├── scheduling_karras_ve_flax.meta.json
│   │   │   │   ├── scheduling_lcm.data.json
│   │   │   │   ├── scheduling_lcm.meta.json
│   │   │   │   ├── scheduling_lms_discrete.data.json
│   │   │   │   ├── scheduling_lms_discrete.meta.json
│   │   │   │   ├── scheduling_lms_discrete_flax.data.json
│   │   │   │   ├── scheduling_lms_discrete_flax.meta.json
│   │   │   │   ├── scheduling_pndm.data.json
│   │   │   │   ├── scheduling_pndm.meta.json
│   │   │   │   ├── scheduling_pndm_flax.data.json
│   │   │   │   ├── scheduling_pndm_flax.meta.json
│   │   │   │   ├── scheduling_repaint.data.json
│   │   │   │   ├── scheduling_repaint.meta.json
│   │   │   │   ├── scheduling_sasolver.data.json
│   │   │   │   ├── scheduling_sasolver.meta.json
│   │   │   │   ├── scheduling_scm.data.json
│   │   │   │   ├── scheduling_scm.meta.json
│   │   │   │   ├── scheduling_sde_ve.data.json
│   │   │   │   ├── scheduling_sde_ve.meta.json
│   │   │   │   ├── scheduling_sde_ve_flax.data.json
│   │   │   │   ├── scheduling_sde_ve_flax.meta.json
│   │   │   │   ├── scheduling_tcd.data.json
│   │   │   │   ├── scheduling_tcd.meta.json
│   │   │   │   ├── scheduling_unclip.data.json
│   │   │   │   ├── scheduling_unclip.meta.json
│   │   │   │   ├── scheduling_unipc_multistep.data.json
│   │   │   │   ├── scheduling_unipc_multistep.meta.json
│   │   │   │   ├── scheduling_utils.data.json
│   │   │   │   ├── scheduling_utils.meta.json
│   │   │   │   ├── scheduling_utils_flax.data.json
│   │   │   │   ├── scheduling_utils_flax.meta.json
│   │   │   │   ├── scheduling_vq_diffusion.data.json
│   │   │   │   └── scheduling_vq_diffusion.meta.json
│   │   │   ├── training_utils.data.json
│   │   │   ├── training_utils.meta.json
│   │   │   ├── utils
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── accelerate_utils.data.json
│   │   │   │   ├── accelerate_utils.meta.json
│   │   │   │   ├── constants.data.json
│   │   │   │   ├── constants.meta.json
│   │   │   │   ├── deprecation_utils.data.json
│   │   │   │   ├── deprecation_utils.meta.json
│   │   │   │   ├── doc_utils.data.json
│   │   │   │   ├── doc_utils.meta.json
│   │   │   │   ├── dummy_bitsandbytes_objects.data.json
│   │   │   │   ├── dummy_bitsandbytes_objects.meta.json
│   │   │   │   ├── dummy_flax_and_transformers_objects.data.json
│   │   │   │   ├── dummy_flax_and_transformers_objects.meta.json
│   │   │   │   ├── dummy_flax_objects.data.json
│   │   │   │   ├── dummy_flax_objects.meta.json
│   │   │   │   ├── dummy_gguf_objects.data.json
│   │   │   │   ├── dummy_gguf_objects.meta.json
│   │   │   │   ├── dummy_note_seq_objects.data.json
│   │   │   │   ├── dummy_note_seq_objects.meta.json
│   │   │   │   ├── dummy_onnx_objects.data.json
│   │   │   │   ├── dummy_onnx_objects.meta.json
│   │   │   │   ├── dummy_optimum_quanto_objects.data.json
│   │   │   │   ├── dummy_optimum_quanto_objects.meta.json
│   │   │   │   ├── dummy_pt_objects.data.json
│   │   │   │   ├── dummy_pt_objects.meta.json
│   │   │   │   ├── dummy_torch_and_librosa_objects.data.json
│   │   │   │   ├── dummy_torch_and_librosa_objects.meta.json
│   │   │   │   ├── dummy_torch_and_scipy_objects.data.json
│   │   │   │   ├── dummy_torch_and_scipy_objects.meta.json
│   │   │   │   ├── dummy_torch_and_torchsde_objects.data.json
│   │   │   │   ├── dummy_torch_and_torchsde_objects.meta.json
│   │   │   │   ├── dummy_torch_and_transformers_and_k_diffusion_objects.data.json
│   │   │   │   ├── dummy_torch_and_transformers_and_k_diffusion_objects.meta.json
│   │   │   │   ├── dummy_torch_and_transformers_and_onnx_objects.data.json
│   │   │   │   ├── dummy_torch_and_transformers_and_onnx_objects.meta.json
│   │   │   │   ├── dummy_torch_and_transformers_and_opencv_objects.data.json
│   │   │   │   ├── dummy_torch_and_transformers_and_opencv_objects.meta.json
│   │   │   │   ├── dummy_torch_and_transformers_and_sentencepiece_objects.data.json
│   │   │   │   ├── dummy_torch_and_transformers_and_sentencepiece_objects.meta.json
│   │   │   │   ├── dummy_torch_and_transformers_objects.data.json
│   │   │   │   ├── dummy_torch_and_transformers_objects.meta.json
│   │   │   │   ├── dummy_torchao_objects.data.json
│   │   │   │   ├── dummy_torchao_objects.meta.json
│   │   │   │   ├── dummy_transformers_and_torch_and_note_seq_objects.data.json
│   │   │   │   ├── dummy_transformers_and_torch_and_note_seq_objects.meta.json
│   │   │   │   ├── dynamic_modules_utils.data.json
│   │   │   │   ├── dynamic_modules_utils.meta.json
│   │   │   │   ├── export_utils.data.json
│   │   │   │   ├── export_utils.meta.json
│   │   │   │   ├── hub_utils.data.json
│   │   │   │   ├── hub_utils.meta.json
│   │   │   │   ├── import_utils.data.json
│   │   │   │   ├── import_utils.meta.json
│   │   │   │   ├── loading_utils.data.json
│   │   │   │   ├── loading_utils.meta.json
│   │   │   │   ├── logging.data.json
│   │   │   │   ├── logging.meta.json
│   │   │   │   ├── outputs.data.json
│   │   │   │   ├── outputs.meta.json
│   │   │   │   ├── peft_utils.data.json
│   │   │   │   ├── peft_utils.meta.json
│   │   │   │   ├── pil_utils.data.json
│   │   │   │   ├── pil_utils.meta.json
│   │   │   │   ├── remote_utils.data.json
│   │   │   │   ├── remote_utils.meta.json
│   │   │   │   ├── state_dict_utils.data.json
│   │   │   │   ├── state_dict_utils.meta.json
│   │   │   │   ├── torch_utils.data.json
│   │   │   │   ├── torch_utils.meta.json
│   │   │   │   ├── typing_utils.data.json
│   │   │   │   ├── typing_utils.meta.json
│   │   │   │   ├── versions.data.json
│   │   │   │   └── versions.meta.json
│   │   │   ├── video_processor.data.json
│   │   │   └── video_processor.meta.json
│   │   ├── dis.data.json
│   │   ├── dis.meta.json
│   │   ├── domain
│   │   │   ├── evaluation.data.json
│   │   │   ├── evaluation.meta.json
│   │   │   ├── model_manager.data.json
│   │   │   ├── model_manager.meta.json
│   │   │   ├── schemas.data.json
│   │   │   └── schemas.meta.json
│   │   ├── domain.data.json
│   │   ├── domain.meta.json
│   │   ├── dotenv
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── main.data.json
│   │   │   ├── main.meta.json
│   │   │   ├── parser.data.json
│   │   │   ├── parser.meta.json
│   │   │   ├── variables.data.json
│   │   │   └── variables.meta.json
│   │   ├── einops
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _backends.data.json
│   │   │   ├── _backends.meta.json
│   │   │   ├── _torch_specific.data.json
│   │   │   ├── _torch_specific.meta.json
│   │   │   ├── einops.data.json
│   │   │   ├── einops.meta.json
│   │   │   ├── layers
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _einmix.data.json
│   │   │   │   ├── _einmix.meta.json
│   │   │   │   ├── keras.data.json
│   │   │   │   ├── keras.meta.json
│   │   │   │   ├── oneflow.data.json
│   │   │   │   ├── oneflow.meta.json
│   │   │   │   ├── paddle.data.json
│   │   │   │   ├── paddle.meta.json
│   │   │   │   ├── tensorflow.data.json
│   │   │   │   ├── tensorflow.meta.json
│   │   │   │   ├── torch.data.json
│   │   │   │   └── torch.meta.json
│   │   │   ├── packing.data.json
│   │   │   ├── packing.meta.json
│   │   │   ├── parsing.data.json
│   │   │   └── parsing.meta.json
│   │   ├── email
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _policybase.data.json
│   │   │   ├── _policybase.meta.json
│   │   │   ├── charset.data.json
│   │   │   ├── charset.meta.json
│   │   │   ├── contentmanager.data.json
│   │   │   ├── contentmanager.meta.json
│   │   │   ├── errors.data.json
│   │   │   ├── errors.meta.json
│   │   │   ├── feedparser.data.json
│   │   │   ├── feedparser.meta.json
│   │   │   ├── header.data.json
│   │   │   ├── header.meta.json
│   │   │   ├── message.data.json
│   │   │   ├── message.meta.json
│   │   │   ├── parser.data.json
│   │   │   ├── parser.meta.json
│   │   │   ├── policy.data.json
│   │   │   ├── policy.meta.json
│   │   │   ├── utils.data.json
│   │   │   └── utils.meta.json
│   │   ├── encodings
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── aliases.data.json
│   │   │   └── aliases.meta.json
│   │   ├── enum.data.json
│   │   ├── enum.meta.json
│   │   ├── errno.data.json
│   │   ├── errno.meta.json
│   │   ├── exceptiongroup
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _catch.data.json
│   │   │   ├── _catch.meta.json
│   │   │   ├── _exceptions.data.json
│   │   │   ├── _exceptions.meta.json
│   │   │   ├── _formatting.data.json
│   │   │   ├── _formatting.meta.json
│   │   │   ├── _suppress.data.json
│   │   │   ├── _suppress.meta.json
│   │   │   ├── _version.data.json
│   │   │   └── _version.meta.json
│   │   ├── fastapi
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _compat.data.json
│   │   │   ├── _compat.meta.json
│   │   │   ├── applications.data.json
│   │   │   ├── applications.meta.json
│   │   │   ├── background.data.json
│   │   │   ├── background.meta.json
│   │   │   ├── concurrency.data.json
│   │   │   ├── concurrency.meta.json
│   │   │   ├── datastructures.data.json
│   │   │   ├── datastructures.meta.json
│   │   │   ├── dependencies
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── models.data.json
│   │   │   │   ├── models.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── encoders.data.json
│   │   │   ├── encoders.meta.json
│   │   │   ├── exception_handlers.data.json
│   │   │   ├── exception_handlers.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── logger.data.json
│   │   │   ├── logger.meta.json
│   │   │   ├── openapi
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── constants.data.json
│   │   │   │   ├── constants.meta.json
│   │   │   │   ├── docs.data.json
│   │   │   │   ├── docs.meta.json
│   │   │   │   ├── models.data.json
│   │   │   │   ├── models.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── param_functions.data.json
│   │   │   ├── param_functions.meta.json
│   │   │   ├── params.data.json
│   │   │   ├── params.meta.json
│   │   │   ├── requests.data.json
│   │   │   ├── requests.meta.json
│   │   │   ├── responses.data.json
│   │   │   ├── responses.meta.json
│   │   │   ├── routing.data.json
│   │   │   ├── routing.meta.json
│   │   │   ├── security
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── api_key.data.json
│   │   │   │   ├── api_key.meta.json
│   │   │   │   ├── base.data.json
│   │   │   │   ├── base.meta.json
│   │   │   │   ├── http.data.json
│   │   │   │   ├── http.meta.json
│   │   │   │   ├── oauth2.data.json
│   │   │   │   ├── oauth2.meta.json
│   │   │   │   ├── open_id_connect_url.data.json
│   │   │   │   ├── open_id_connect_url.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── types.data.json
│   │   │   ├── types.meta.json
│   │   │   ├── utils.data.json
│   │   │   ├── utils.meta.json
│   │   │   ├── websockets.data.json
│   │   │   └── websockets.meta.json
│   │   ├── faulthandler.data.json
│   │   ├── faulthandler.meta.json
│   │   ├── fcntl.data.json
│   │   ├── fcntl.meta.json
│   │   ├── filecmp.data.json
│   │   ├── filecmp.meta.json
│   │   ├── filelock
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _api.data.json
│   │   │   ├── _api.meta.json
│   │   │   ├── _error.data.json
│   │   │   ├── _error.meta.json
│   │   │   ├── _soft.data.json
│   │   │   ├── _soft.meta.json
│   │   │   ├── _unix.data.json
│   │   │   ├── _unix.meta.json
│   │   │   ├── _util.data.json
│   │   │   ├── _util.meta.json
│   │   │   ├── _windows.data.json
│   │   │   ├── _windows.meta.json
│   │   │   ├── asyncio.data.json
│   │   │   ├── asyncio.meta.json
│   │   │   ├── version.data.json
│   │   │   └── version.meta.json
│   │   ├── fnmatch.data.json
│   │   ├── fnmatch.meta.json
│   │   ├── fractions.data.json
│   │   ├── fractions.meta.json
│   │   ├── frozenlist
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── functools.data.json
│   │   ├── functools.meta.json
│   │   ├── gc.data.json
│   │   ├── gc.meta.json
│   │   ├── genericpath.data.json
│   │   ├── genericpath.meta.json
│   │   ├── getpass.data.json
│   │   ├── getpass.meta.json
│   │   ├── gettext.data.json
│   │   ├── gettext.meta.json
│   │   ├── glob.data.json
│   │   ├── glob.meta.json
│   │   ├── gzip.data.json
│   │   ├── gzip.meta.json
│   │   ├── hashlib.data.json
│   │   ├── hashlib.meta.json
│   │   ├── heapq.data.json
│   │   ├── heapq.meta.json
│   │   ├── hmac.data.json
│   │   ├── hmac.meta.json
│   │   ├── hrm_test.data.json
│   │   ├── hrm_test.meta.json
│   │   ├── html
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── entities.data.json
│   │   │   ├── entities.meta.json
│   │   │   ├── parser.data.json
│   │   │   └── parser.meta.json
│   │   ├── http
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── client.data.json
│   │   │   ├── client.meta.json
│   │   │   ├── cookiejar.data.json
│   │   │   ├── cookiejar.meta.json
│   │   │   ├── cookies.data.json
│   │   │   └── cookies.meta.json
│   │   ├── huggingface_hub
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _commit_api.data.json
│   │   │   ├── _commit_api.meta.json
│   │   │   ├── _commit_scheduler.data.json
│   │   │   ├── _commit_scheduler.meta.json
│   │   │   ├── _inference_endpoints.data.json
│   │   │   ├── _inference_endpoints.meta.json
│   │   │   ├── _jobs_api.data.json
│   │   │   ├── _jobs_api.meta.json
│   │   │   ├── _local_folder.data.json
│   │   │   ├── _local_folder.meta.json
│   │   │   ├── _login.data.json
│   │   │   ├── _login.meta.json
│   │   │   ├── _oauth.data.json
│   │   │   ├── _oauth.meta.json
│   │   │   ├── _snapshot_download.data.json
│   │   │   ├── _snapshot_download.meta.json
│   │   │   ├── _space_api.data.json
│   │   │   ├── _space_api.meta.json
│   │   │   ├── _tensorboard_logger.data.json
│   │   │   ├── _tensorboard_logger.meta.json
│   │   │   ├── _upload_large_folder.data.json
│   │   │   ├── _upload_large_folder.meta.json
│   │   │   ├── _webhooks_payload.data.json
│   │   │   ├── _webhooks_payload.meta.json
│   │   │   ├── _webhooks_server.data.json
│   │   │   ├── _webhooks_server.meta.json
│   │   │   ├── commands
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _cli_utils.data.json
│   │   │   │   └── _cli_utils.meta.json
│   │   │   ├── community.data.json
│   │   │   ├── community.meta.json
│   │   │   ├── constants.data.json
│   │   │   ├── constants.meta.json
│   │   │   ├── errors.data.json
│   │   │   ├── errors.meta.json
│   │   │   ├── fastai_utils.data.json
│   │   │   ├── fastai_utils.meta.json
│   │   │   ├── file_download.data.json
│   │   │   ├── file_download.meta.json
│   │   │   ├── hf_api.data.json
│   │   │   ├── hf_api.meta.json
│   │   │   ├── hf_file_system.data.json
│   │   │   ├── hf_file_system.meta.json
│   │   │   ├── hub_mixin.data.json
│   │   │   ├── hub_mixin.meta.json
│   │   │   ├── inference
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _client.data.json
│   │   │   │   ├── _client.meta.json
│   │   │   │   ├── _common.data.json
│   │   │   │   ├── _common.meta.json
│   │   │   │   ├── _generated
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _async_client.data.json
│   │   │   │   │   ├── _async_client.meta.json
│   │   │   │   │   └── types
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── audio_classification.data.json
│   │   │   │   │       ├── audio_classification.meta.json
│   │   │   │   │       ├── audio_to_audio.data.json
│   │   │   │   │       ├── audio_to_audio.meta.json
│   │   │   │   │       ├── automatic_speech_recognition.data.json
│   │   │   │   │       ├── automatic_speech_recognition.meta.json
│   │   │   │   │       ├── base.data.json
│   │   │   │   │       ├── base.meta.json
│   │   │   │   │       ├── chat_completion.data.json
│   │   │   │   │       ├── chat_completion.meta.json
│   │   │   │   │       ├── depth_estimation.data.json
│   │   │   │   │       ├── depth_estimation.meta.json
│   │   │   │   │       ├── document_question_answering.data.json
│   │   │   │   │       ├── document_question_answering.meta.json
│   │   │   │   │       ├── feature_extraction.data.json
│   │   │   │   │       ├── feature_extraction.meta.json
│   │   │   │   │       ├── fill_mask.data.json
│   │   │   │   │       ├── fill_mask.meta.json
│   │   │   │   │       ├── image_classification.data.json
│   │   │   │   │       ├── image_classification.meta.json
│   │   │   │   │       ├── image_segmentation.data.json
│   │   │   │   │       ├── image_segmentation.meta.json
│   │   │   │   │       ├── image_to_image.data.json
│   │   │   │   │       ├── image_to_image.meta.json
│   │   │   │   │       ├── image_to_text.data.json
│   │   │   │   │       ├── image_to_text.meta.json
│   │   │   │   │       ├── image_to_video.data.json
│   │   │   │   │       ├── image_to_video.meta.json
│   │   │   │   │       ├── object_detection.data.json
│   │   │   │   │       ├── object_detection.meta.json
│   │   │   │   │       ├── question_answering.data.json
│   │   │   │   │       ├── question_answering.meta.json
│   │   │   │   │       ├── sentence_similarity.data.json
│   │   │   │   │       ├── sentence_similarity.meta.json
│   │   │   │   │       ├── summarization.data.json
│   │   │   │   │       ├── summarization.meta.json
│   │   │   │   │       ├── table_question_answering.data.json
│   │   │   │   │       ├── table_question_answering.meta.json
│   │   │   │   │       ├── text2text_generation.data.json
│   │   │   │   │       ├── text2text_generation.meta.json
│   │   │   │   │       ├── text_classification.data.json
│   │   │   │   │       ├── text_classification.meta.json
│   │   │   │   │       ├── text_generation.data.json
│   │   │   │   │       ├── text_generation.meta.json
│   │   │   │   │       ├── text_to_audio.data.json
│   │   │   │   │       ├── text_to_audio.meta.json
│   │   │   │   │       ├── text_to_image.data.json
│   │   │   │   │       ├── text_to_image.meta.json
│   │   │   │   │       ├── text_to_speech.data.json
│   │   │   │   │       ├── text_to_speech.meta.json
│   │   │   │   │       ├── text_to_video.data.json
│   │   │   │   │       ├── text_to_video.meta.json
│   │   │   │   │       ├── token_classification.data.json
│   │   │   │   │       ├── token_classification.meta.json
│   │   │   │   │       ├── translation.data.json
│   │   │   │   │       ├── translation.meta.json
│   │   │   │   │       ├── video_classification.data.json
│   │   │   │   │       ├── video_classification.meta.json
│   │   │   │   │       ├── visual_question_answering.data.json
│   │   │   │   │       ├── visual_question_answering.meta.json
│   │   │   │   │       ├── zero_shot_classification.data.json
│   │   │   │   │       ├── zero_shot_classification.meta.json
│   │   │   │   │       ├── zero_shot_image_classification.data.json
│   │   │   │   │       ├── zero_shot_image_classification.meta.json
│   │   │   │   │       ├── zero_shot_object_detection.data.json
│   │   │   │   │       └── zero_shot_object_detection.meta.json
│   │   │   │   ├── _mcp
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── agent.data.json
│   │   │   │   │   ├── agent.meta.json
│   │   │   │   │   ├── constants.data.json
│   │   │   │   │   ├── constants.meta.json
│   │   │   │   │   ├── mcp_client.data.json
│   │   │   │   │   ├── mcp_client.meta.json
│   │   │   │   │   ├── types.data.json
│   │   │   │   │   ├── types.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   └── _providers
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── _common.data.json
│   │   │   │       ├── _common.meta.json
│   │   │   │       ├── black_forest_labs.data.json
│   │   │   │       ├── black_forest_labs.meta.json
│   │   │   │       ├── cerebras.data.json
│   │   │   │       ├── cerebras.meta.json
│   │   │   │       ├── cohere.data.json
│   │   │   │       ├── cohere.meta.json
│   │   │   │       ├── fal_ai.data.json
│   │   │   │       ├── fal_ai.meta.json
│   │   │   │       ├── featherless_ai.data.json
│   │   │   │       ├── featherless_ai.meta.json
│   │   │   │       ├── fireworks_ai.data.json
│   │   │   │       ├── fireworks_ai.meta.json
│   │   │   │       ├── groq.data.json
│   │   │   │       ├── groq.meta.json
│   │   │   │       ├── hf_inference.data.json
│   │   │   │       ├── hf_inference.meta.json
│   │   │   │       ├── hyperbolic.data.json
│   │   │   │       ├── hyperbolic.meta.json
│   │   │   │       ├── nebius.data.json
│   │   │   │       ├── nebius.meta.json
│   │   │   │       ├── novita.data.json
│   │   │   │       ├── novita.meta.json
│   │   │   │       ├── nscale.data.json
│   │   │   │       ├── nscale.meta.json
│   │   │   │       ├── openai.data.json
│   │   │   │       ├── openai.meta.json
│   │   │   │       ├── replicate.data.json
│   │   │   │       ├── replicate.meta.json
│   │   │   │       ├── sambanova.data.json
│   │   │   │       ├── sambanova.meta.json
│   │   │   │       ├── together.data.json
│   │   │   │       └── together.meta.json
│   │   │   ├── inference_api.data.json
│   │   │   ├── inference_api.meta.json
│   │   │   ├── keras_mixin.data.json
│   │   │   ├── keras_mixin.meta.json
│   │   │   ├── lfs.data.json
│   │   │   ├── lfs.meta.json
│   │   │   ├── repocard.data.json
│   │   │   ├── repocard.meta.json
│   │   │   ├── repocard_data.data.json
│   │   │   ├── repocard_data.meta.json
│   │   │   ├── repository.data.json
│   │   │   ├── repository.meta.json
│   │   │   ├── serialization
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _base.data.json
│   │   │   │   ├── _base.meta.json
│   │   │   │   ├── _dduf.data.json
│   │   │   │   ├── _dduf.meta.json
│   │   │   │   ├── _tensorflow.data.json
│   │   │   │   ├── _tensorflow.meta.json
│   │   │   │   ├── _torch.data.json
│   │   │   │   └── _torch.meta.json
│   │   │   └── utils
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── _auth.data.json
│   │   │       ├── _auth.meta.json
│   │   │       ├── _cache_assets.data.json
│   │   │       ├── _cache_assets.meta.json
│   │   │       ├── _cache_manager.data.json
│   │   │       ├── _cache_manager.meta.json
│   │   │       ├── _chunk_utils.data.json
│   │   │       ├── _chunk_utils.meta.json
│   │   │       ├── _datetime.data.json
│   │   │       ├── _datetime.meta.json
│   │   │       ├── _deprecation.data.json
│   │   │       ├── _deprecation.meta.json
│   │   │       ├── _experimental.data.json
│   │   │       ├── _experimental.meta.json
│   │   │       ├── _fixes.data.json
│   │   │       ├── _fixes.meta.json
│   │   │       ├── _git_credential.data.json
│   │   │       ├── _git_credential.meta.json
│   │   │       ├── _headers.data.json
│   │   │       ├── _headers.meta.json
│   │   │       ├── _hf_folder.data.json
│   │   │       ├── _hf_folder.meta.json
│   │   │       ├── _http.data.json
│   │   │       ├── _http.meta.json
│   │   │       ├── _lfs.data.json
│   │   │       ├── _lfs.meta.json
│   │   │       ├── _pagination.data.json
│   │   │       ├── _pagination.meta.json
│   │   │       ├── _paths.data.json
│   │   │       ├── _paths.meta.json
│   │   │       ├── _runtime.data.json
│   │   │       ├── _runtime.meta.json
│   │   │       ├── _safetensors.data.json
│   │   │       ├── _safetensors.meta.json
│   │   │       ├── _subprocess.data.json
│   │   │       ├── _subprocess.meta.json
│   │   │       ├── _telemetry.data.json
│   │   │       ├── _telemetry.meta.json
│   │   │       ├── _typing.data.json
│   │   │       ├── _typing.meta.json
│   │   │       ├── _validators.data.json
│   │   │       ├── _validators.meta.json
│   │   │       ├── _xet.data.json
│   │   │       ├── _xet.meta.json
│   │   │       ├── endpoint_helpers.data.json
│   │   │       ├── endpoint_helpers.meta.json
│   │   │       ├── insecure_hashlib.data.json
│   │   │       ├── insecure_hashlib.meta.json
│   │   │       ├── logging.data.json
│   │   │       ├── logging.meta.json
│   │   │       ├── sha.data.json
│   │   │       ├── sha.meta.json
│   │   │       ├── tqdm.data.json
│   │   │       └── tqdm.meta.json
│   │   ├── idna
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── core.data.json
│   │   │   ├── core.meta.json
│   │   │   ├── idnadata.data.json
│   │   │   ├── idnadata.meta.json
│   │   │   ├── intranges.data.json
│   │   │   ├── intranges.meta.json
│   │   │   ├── package_data.data.json
│   │   │   └── package_data.meta.json
│   │   ├── importlib
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _abc.data.json
│   │   │   ├── _abc.meta.json
│   │   │   ├── _bootstrap.data.json
│   │   │   ├── _bootstrap.meta.json
│   │   │   ├── _bootstrap_external.data.json
│   │   │   ├── _bootstrap_external.meta.json
│   │   │   ├── abc.data.json
│   │   │   ├── abc.meta.json
│   │   │   ├── machinery.data.json
│   │   │   ├── machinery.meta.json
│   │   │   ├── metadata
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _meta.data.json
│   │   │   │   └── _meta.meta.json
│   │   │   ├── readers.data.json
│   │   │   ├── readers.meta.json
│   │   │   ├── resources
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── importlib_metadata
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _adapters.data.json
│   │   │   ├── _adapters.meta.json
│   │   │   ├── _collections.data.json
│   │   │   ├── _collections.meta.json
│   │   │   ├── _compat.data.json
│   │   │   ├── _compat.meta.json
│   │   │   ├── _functools.data.json
│   │   │   ├── _functools.meta.json
│   │   │   ├── _itertools.data.json
│   │   │   ├── _itertools.meta.json
│   │   │   ├── _meta.data.json
│   │   │   ├── _meta.meta.json
│   │   │   ├── _text.data.json
│   │   │   ├── _text.meta.json
│   │   │   ├── _typing.data.json
│   │   │   ├── _typing.meta.json
│   │   │   └── compat
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── py311.data.json
│   │   │       ├── py311.meta.json
│   │   │       ├── py39.data.json
│   │   │       └── py39.meta.json
│   │   ├── inspect.data.json
│   │   ├── inspect.meta.json
│   │   ├── io.data.json
│   │   ├── io.meta.json
│   │   ├── ipaddress.data.json
│   │   ├── ipaddress.meta.json
│   │   ├── itertools.data.json
│   │   ├── itertools.meta.json
│   │   ├── jamba_test.data.json
│   │   ├── jamba_test.meta.json
│   │   ├── jinja2
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _identifier.data.json
│   │   │   ├── _identifier.meta.json
│   │   │   ├── async_utils.data.json
│   │   │   ├── async_utils.meta.json
│   │   │   ├── bccache.data.json
│   │   │   ├── bccache.meta.json
│   │   │   ├── compiler.data.json
│   │   │   ├── compiler.meta.json
│   │   │   ├── debug.data.json
│   │   │   ├── debug.meta.json
│   │   │   ├── defaults.data.json
│   │   │   ├── defaults.meta.json
│   │   │   ├── environment.data.json
│   │   │   ├── environment.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── ext.data.json
│   │   │   ├── ext.meta.json
│   │   │   ├── filters.data.json
│   │   │   ├── filters.meta.json
│   │   │   ├── idtracking.data.json
│   │   │   ├── idtracking.meta.json
│   │   │   ├── lexer.data.json
│   │   │   ├── lexer.meta.json
│   │   │   ├── loaders.data.json
│   │   │   ├── loaders.meta.json
│   │   │   ├── nodes.data.json
│   │   │   ├── nodes.meta.json
│   │   │   ├── optimizer.data.json
│   │   │   ├── optimizer.meta.json
│   │   │   ├── parser.data.json
│   │   │   ├── parser.meta.json
│   │   │   ├── runtime.data.json
│   │   │   ├── runtime.meta.json
│   │   │   ├── sandbox.data.json
│   │   │   ├── sandbox.meta.json
│   │   │   ├── tests.data.json
│   │   │   ├── tests.meta.json
│   │   │   ├── utils.data.json
│   │   │   ├── utils.meta.json
│   │   │   ├── visitor.data.json
│   │   │   └── visitor.meta.json
│   │   ├── json
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── decoder.data.json
│   │   │   ├── decoder.meta.json
│   │   │   ├── encoder.data.json
│   │   │   └── encoder.meta.json
│   │   ├── keyword.data.json
│   │   ├── keyword.meta.json
│   │   ├── linecache.data.json
│   │   ├── linecache.meta.json
│   │   ├── liquids4_test.data.json
│   │   ├── liquids4_test.meta.json
│   │   ├── llama_cpp
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _ctypes_extensions.data.json
│   │   │   ├── _ctypes_extensions.meta.json
│   │   │   ├── _internals.data.json
│   │   │   ├── _internals.meta.json
│   │   │   ├── _logger.data.json
│   │   │   ├── _logger.meta.json
│   │   │   ├── _utils.data.json
│   │   │   ├── _utils.meta.json
│   │   │   ├── llama.data.json
│   │   │   ├── llama.meta.json
│   │   │   ├── llama_cache.data.json
│   │   │   ├── llama_cache.meta.json
│   │   │   ├── llama_chat_format.data.json
│   │   │   ├── llama_chat_format.meta.json
│   │   │   ├── llama_cpp.data.json
│   │   │   ├── llama_cpp.meta.json
│   │   │   ├── llama_grammar.data.json
│   │   │   ├── llama_grammar.meta.json
│   │   │   ├── llama_speculative.data.json
│   │   │   ├── llama_speculative.meta.json
│   │   │   ├── llama_tokenizer.data.json
│   │   │   ├── llama_tokenizer.meta.json
│   │   │   ├── llama_types.data.json
│   │   │   ├── llama_types.meta.json
│   │   │   ├── mtmd_cpp.data.json
│   │   │   └── mtmd_cpp.meta.json
│   │   ├── locale.data.json
│   │   ├── locale.meta.json
│   │   ├── logging
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── markdown_it
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _compat.data.json
│   │   │   ├── _compat.meta.json
│   │   │   ├── _punycode.data.json
│   │   │   ├── _punycode.meta.json
│   │   │   ├── common
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── entities.data.json
│   │   │   │   ├── entities.meta.json
│   │   │   │   ├── html_blocks.data.json
│   │   │   │   ├── html_blocks.meta.json
│   │   │   │   ├── html_re.data.json
│   │   │   │   ├── html_re.meta.json
│   │   │   │   ├── normalize_url.data.json
│   │   │   │   ├── normalize_url.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── helpers
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── parse_link_destination.data.json
│   │   │   │   ├── parse_link_destination.meta.json
│   │   │   │   ├── parse_link_label.data.json
│   │   │   │   ├── parse_link_label.meta.json
│   │   │   │   ├── parse_link_title.data.json
│   │   │   │   └── parse_link_title.meta.json
│   │   │   ├── main.data.json
│   │   │   ├── main.meta.json
│   │   │   ├── parser_block.data.json
│   │   │   ├── parser_block.meta.json
│   │   │   ├── parser_core.data.json
│   │   │   ├── parser_core.meta.json
│   │   │   ├── parser_inline.data.json
│   │   │   ├── parser_inline.meta.json
│   │   │   ├── presets
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── commonmark.data.json
│   │   │   │   ├── commonmark.meta.json
│   │   │   │   ├── default.data.json
│   │   │   │   ├── default.meta.json
│   │   │   │   ├── zero.data.json
│   │   │   │   └── zero.meta.json
│   │   │   ├── renderer.data.json
│   │   │   ├── renderer.meta.json
│   │   │   ├── ruler.data.json
│   │   │   ├── ruler.meta.json
│   │   │   ├── rules_block
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── blockquote.data.json
│   │   │   │   ├── blockquote.meta.json
│   │   │   │   ├── code.data.json
│   │   │   │   ├── code.meta.json
│   │   │   │   ├── fence.data.json
│   │   │   │   ├── fence.meta.json
│   │   │   │   ├── heading.data.json
│   │   │   │   ├── heading.meta.json
│   │   │   │   ├── hr.data.json
│   │   │   │   ├── hr.meta.json
│   │   │   │   ├── html_block.data.json
│   │   │   │   ├── html_block.meta.json
│   │   │   │   ├── lheading.data.json
│   │   │   │   ├── lheading.meta.json
│   │   │   │   ├── list.data.json
│   │   │   │   ├── list.meta.json
│   │   │   │   ├── paragraph.data.json
│   │   │   │   ├── paragraph.meta.json
│   │   │   │   ├── reference.data.json
│   │   │   │   ├── reference.meta.json
│   │   │   │   ├── state_block.data.json
│   │   │   │   ├── state_block.meta.json
│   │   │   │   ├── table.data.json
│   │   │   │   └── table.meta.json
│   │   │   ├── rules_core
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── block.data.json
│   │   │   │   ├── block.meta.json
│   │   │   │   ├── inline.data.json
│   │   │   │   ├── inline.meta.json
│   │   │   │   ├── linkify.data.json
│   │   │   │   ├── linkify.meta.json
│   │   │   │   ├── normalize.data.json
│   │   │   │   ├── normalize.meta.json
│   │   │   │   ├── replacements.data.json
│   │   │   │   ├── replacements.meta.json
│   │   │   │   ├── smartquotes.data.json
│   │   │   │   ├── smartquotes.meta.json
│   │   │   │   ├── state_core.data.json
│   │   │   │   ├── state_core.meta.json
│   │   │   │   ├── text_join.data.json
│   │   │   │   └── text_join.meta.json
│   │   │   ├── rules_inline
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── autolink.data.json
│   │   │   │   ├── autolink.meta.json
│   │   │   │   ├── backticks.data.json
│   │   │   │   ├── backticks.meta.json
│   │   │   │   ├── balance_pairs.data.json
│   │   │   │   ├── balance_pairs.meta.json
│   │   │   │   ├── emphasis.data.json
│   │   │   │   ├── emphasis.meta.json
│   │   │   │   ├── entity.data.json
│   │   │   │   ├── entity.meta.json
│   │   │   │   ├── escape.data.json
│   │   │   │   ├── escape.meta.json
│   │   │   │   ├── fragments_join.data.json
│   │   │   │   ├── fragments_join.meta.json
│   │   │   │   ├── html_inline.data.json
│   │   │   │   ├── html_inline.meta.json
│   │   │   │   ├── image.data.json
│   │   │   │   ├── image.meta.json
│   │   │   │   ├── link.data.json
│   │   │   │   ├── link.meta.json
│   │   │   │   ├── linkify.data.json
│   │   │   │   ├── linkify.meta.json
│   │   │   │   ├── newline.data.json
│   │   │   │   ├── newline.meta.json
│   │   │   │   ├── state_inline.data.json
│   │   │   │   ├── state_inline.meta.json
│   │   │   │   ├── strikethrough.data.json
│   │   │   │   ├── strikethrough.meta.json
│   │   │   │   ├── text.data.json
│   │   │   │   └── text.meta.json
│   │   │   ├── token.data.json
│   │   │   ├── token.meta.json
│   │   │   ├── utils.data.json
│   │   │   └── utils.meta.json
│   │   ├── markupsafe
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _native.data.json
│   │   │   ├── _native.meta.json
│   │   │   ├── _speedups.data.json
│   │   │   └── _speedups.meta.json
│   │   ├── marshal.data.json
│   │   ├── marshal.meta.json
│   │   ├── math.data.json
│   │   ├── math.meta.json
│   │   ├── matplotlib
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _afm.data.json
│   │   │   ├── _afm.meta.json
│   │   │   ├── _api
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── deprecation.data.json
│   │   │   │   └── deprecation.meta.json
│   │   │   ├── _docstring.data.json
│   │   │   ├── _docstring.meta.json
│   │   │   ├── _enums.data.json
│   │   │   ├── _enums.meta.json
│   │   │   ├── _mathtext.data.json
│   │   │   ├── _mathtext.meta.json
│   │   │   ├── _mathtext_data.data.json
│   │   │   ├── _mathtext_data.meta.json
│   │   │   ├── _pylab_helpers.data.json
│   │   │   ├── _pylab_helpers.meta.json
│   │   │   ├── _tri.data.json
│   │   │   ├── _tri.meta.json
│   │   │   ├── artist.data.json
│   │   │   ├── artist.meta.json
│   │   │   ├── axes
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _axes.data.json
│   │   │   │   ├── _axes.meta.json
│   │   │   │   ├── _base.data.json
│   │   │   │   ├── _base.meta.json
│   │   │   │   ├── _secondary_axes.data.json
│   │   │   │   └── _secondary_axes.meta.json
│   │   │   ├── axis.data.json
│   │   │   ├── axis.meta.json
│   │   │   ├── backend_bases.data.json
│   │   │   ├── backend_bases.meta.json
│   │   │   ├── backend_managers.data.json
│   │   │   ├── backend_managers.meta.json
│   │   │   ├── backend_tools.data.json
│   │   │   ├── backend_tools.meta.json
│   │   │   ├── backends
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── registry.data.json
│   │   │   │   └── registry.meta.json
│   │   │   ├── bezier.data.json
│   │   │   ├── bezier.meta.json
│   │   │   ├── cbook.data.json
│   │   │   ├── cbook.meta.json
│   │   │   ├── cm.data.json
│   │   │   ├── cm.meta.json
│   │   │   ├── collections.data.json
│   │   │   ├── collections.meta.json
│   │   │   ├── colorbar.data.json
│   │   │   ├── colorbar.meta.json
│   │   │   ├── colorizer.data.json
│   │   │   ├── colorizer.meta.json
│   │   │   ├── colors.data.json
│   │   │   ├── colors.meta.json
│   │   │   ├── container.data.json
│   │   │   ├── container.meta.json
│   │   │   ├── contour.data.json
│   │   │   ├── contour.meta.json
│   │   │   ├── figure.data.json
│   │   │   ├── figure.meta.json
│   │   │   ├── font_manager.data.json
│   │   │   ├── font_manager.meta.json
│   │   │   ├── ft2font.data.json
│   │   │   ├── ft2font.meta.json
│   │   │   ├── gridspec.data.json
│   │   │   ├── gridspec.meta.json
│   │   │   ├── image.data.json
│   │   │   ├── image.meta.json
│   │   │   ├── inset.data.json
│   │   │   ├── inset.meta.json
│   │   │   ├── layout_engine.data.json
│   │   │   ├── layout_engine.meta.json
│   │   │   ├── legend.data.json
│   │   │   ├── legend.meta.json
│   │   │   ├── legend_handler.data.json
│   │   │   ├── legend_handler.meta.json
│   │   │   ├── lines.data.json
│   │   │   ├── lines.meta.json
│   │   │   ├── markers.data.json
│   │   │   ├── markers.meta.json
│   │   │   ├── mathtext.data.json
│   │   │   ├── mathtext.meta.json
│   │   │   ├── mlab.data.json
│   │   │   ├── mlab.meta.json
│   │   │   ├── offsetbox.data.json
│   │   │   ├── offsetbox.meta.json
│   │   │   ├── patches.data.json
│   │   │   ├── patches.meta.json
│   │   │   ├── path.data.json
│   │   │   ├── path.meta.json
│   │   │   ├── patheffects.data.json
│   │   │   ├── patheffects.meta.json
│   │   │   ├── projections
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── geo.data.json
│   │   │   │   ├── geo.meta.json
│   │   │   │   ├── polar.data.json
│   │   │   │   └── polar.meta.json
│   │   │   ├── pyplot.data.json
│   │   │   ├── pyplot.meta.json
│   │   │   ├── quiver.data.json
│   │   │   ├── quiver.meta.json
│   │   │   ├── rcsetup.data.json
│   │   │   ├── rcsetup.meta.json
│   │   │   ├── scale.data.json
│   │   │   ├── scale.meta.json
│   │   │   ├── spines.data.json
│   │   │   ├── spines.meta.json
│   │   │   ├── stackplot.data.json
│   │   │   ├── stackplot.meta.json
│   │   │   ├── streamplot.data.json
│   │   │   ├── streamplot.meta.json
│   │   │   ├── style
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── core.data.json
│   │   │   │   └── core.meta.json
│   │   │   ├── table.data.json
│   │   │   ├── table.meta.json
│   │   │   ├── texmanager.data.json
│   │   │   ├── texmanager.meta.json
│   │   │   ├── text.data.json
│   │   │   ├── text.meta.json
│   │   │   ├── textpath.data.json
│   │   │   ├── textpath.meta.json
│   │   │   ├── ticker.data.json
│   │   │   ├── ticker.meta.json
│   │   │   ├── transforms.data.json
│   │   │   ├── transforms.meta.json
│   │   │   ├── tri
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _triangulation.data.json
│   │   │   │   ├── _triangulation.meta.json
│   │   │   │   ├── _tricontour.data.json
│   │   │   │   ├── _tricontour.meta.json
│   │   │   │   ├── _trifinder.data.json
│   │   │   │   ├── _trifinder.meta.json
│   │   │   │   ├── _triinterpolate.data.json
│   │   │   │   ├── _triinterpolate.meta.json
│   │   │   │   ├── _tripcolor.data.json
│   │   │   │   ├── _tripcolor.meta.json
│   │   │   │   ├── _triplot.data.json
│   │   │   │   ├── _triplot.meta.json
│   │   │   │   ├── _trirefine.data.json
│   │   │   │   ├── _trirefine.meta.json
│   │   │   │   ├── _tritools.data.json
│   │   │   │   └── _tritools.meta.json
│   │   │   ├── typing.data.json
│   │   │   ├── typing.meta.json
│   │   │   ├── units.data.json
│   │   │   ├── units.meta.json
│   │   │   ├── widgets.data.json
│   │   │   └── widgets.meta.json
│   │   ├── mdurl
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _decode.data.json
│   │   │   ├── _decode.meta.json
│   │   │   ├── _encode.data.json
│   │   │   ├── _encode.meta.json
│   │   │   ├── _format.data.json
│   │   │   ├── _format.meta.json
│   │   │   ├── _parse.data.json
│   │   │   ├── _parse.meta.json
│   │   │   ├── _url.data.json
│   │   │   └── _url.meta.json
│   │   ├── mimetypes.data.json
│   │   ├── mimetypes.meta.json
│   │   ├── mlx
│   │   │   └── core
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── distributed
│   │   │       │   ├── __init__.data.json
│   │   │       │   └── __init__.meta.json
│   │   │       ├── fast
│   │   │       │   ├── __init__.data.json
│   │   │       │   └── __init__.meta.json
│   │   │       ├── fft
│   │   │       │   ├── __init__.data.json
│   │   │       │   └── __init__.meta.json
│   │   │       ├── linalg
│   │   │       │   ├── __init__.data.json
│   │   │       │   └── __init__.meta.json
│   │   │       ├── metal
│   │   │       │   ├── __init__.data.json
│   │   │       │   └── __init__.meta.json
│   │   │       └── random
│   │   │           ├── __init__.data.json
│   │   │           └── __init__.meta.json
│   │   ├── mlx.data.json
│   │   ├── mlx.meta.json
│   │   ├── mmap.data.json
│   │   ├── mmap.meta.json
│   │   ├── multidict
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _abc.data.json
│   │   │   ├── _abc.meta.json
│   │   │   ├── _compat.data.json
│   │   │   ├── _compat.meta.json
│   │   │   ├── _multidict_py.data.json
│   │   │   └── _multidict_py.meta.json
│   │   ├── multiprocessing
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── connection.data.json
│   │   │   ├── connection.meta.json
│   │   │   ├── context.data.json
│   │   │   ├── context.meta.json
│   │   │   ├── managers.data.json
│   │   │   ├── managers.meta.json
│   │   │   ├── pool.data.json
│   │   │   ├── pool.meta.json
│   │   │   ├── popen_fork.data.json
│   │   │   ├── popen_fork.meta.json
│   │   │   ├── popen_forkserver.data.json
│   │   │   ├── popen_forkserver.meta.json
│   │   │   ├── popen_spawn_posix.data.json
│   │   │   ├── popen_spawn_posix.meta.json
│   │   │   ├── popen_spawn_win32.data.json
│   │   │   ├── popen_spawn_win32.meta.json
│   │   │   ├── process.data.json
│   │   │   ├── process.meta.json
│   │   │   ├── queues.data.json
│   │   │   ├── queues.meta.json
│   │   │   ├── reduction.data.json
│   │   │   ├── reduction.meta.json
│   │   │   ├── resource_sharer.data.json
│   │   │   ├── resource_sharer.meta.json
│   │   │   ├── resource_tracker.data.json
│   │   │   ├── resource_tracker.meta.json
│   │   │   ├── shared_memory.data.json
│   │   │   ├── shared_memory.meta.json
│   │   │   ├── sharedctypes.data.json
│   │   │   ├── sharedctypes.meta.json
│   │   │   ├── spawn.data.json
│   │   │   ├── spawn.meta.json
│   │   │   ├── synchronize.data.json
│   │   │   ├── synchronize.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── netrc.data.json
│   │   ├── netrc.meta.json
│   │   ├── numbers.data.json
│   │   ├── numbers.meta.json
│   │   ├── numpy
│   │   │   ├── __config__.data.json
│   │   │   ├── __config__.meta.json
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _array_api_info.data.json
│   │   │   ├── _array_api_info.meta.json
│   │   │   ├── _core
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _asarray.data.json
│   │   │   │   ├── _asarray.meta.json
│   │   │   │   ├── _internal.data.json
│   │   │   │   ├── _internal.meta.json
│   │   │   │   ├── _type_aliases.data.json
│   │   │   │   ├── _type_aliases.meta.json
│   │   │   │   ├── _ufunc_config.data.json
│   │   │   │   ├── _ufunc_config.meta.json
│   │   │   │   ├── arrayprint.data.json
│   │   │   │   ├── arrayprint.meta.json
│   │   │   │   ├── defchararray.data.json
│   │   │   │   ├── defchararray.meta.json
│   │   │   │   ├── einsumfunc.data.json
│   │   │   │   ├── einsumfunc.meta.json
│   │   │   │   ├── fromnumeric.data.json
│   │   │   │   ├── fromnumeric.meta.json
│   │   │   │   ├── function_base.data.json
│   │   │   │   ├── function_base.meta.json
│   │   │   │   ├── multiarray.data.json
│   │   │   │   ├── multiarray.meta.json
│   │   │   │   ├── numeric.data.json
│   │   │   │   ├── numeric.meta.json
│   │   │   │   ├── numerictypes.data.json
│   │   │   │   ├── numerictypes.meta.json
│   │   │   │   ├── records.data.json
│   │   │   │   ├── records.meta.json
│   │   │   │   ├── shape_base.data.json
│   │   │   │   ├── shape_base.meta.json
│   │   │   │   ├── strings.data.json
│   │   │   │   └── strings.meta.json
│   │   │   ├── _expired_attrs_2_0.data.json
│   │   │   ├── _expired_attrs_2_0.meta.json
│   │   │   ├── _globals.data.json
│   │   │   ├── _globals.meta.json
│   │   │   ├── _pytesttester.data.json
│   │   │   ├── _pytesttester.meta.json
│   │   │   ├── _typing
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _add_docstring.data.json
│   │   │   │   ├── _add_docstring.meta.json
│   │   │   │   ├── _array_like.data.json
│   │   │   │   ├── _array_like.meta.json
│   │   │   │   ├── _callable.data.json
│   │   │   │   ├── _callable.meta.json
│   │   │   │   ├── _char_codes.data.json
│   │   │   │   ├── _char_codes.meta.json
│   │   │   │   ├── _dtype_like.data.json
│   │   │   │   ├── _dtype_like.meta.json
│   │   │   │   ├── _extended_precision.data.json
│   │   │   │   ├── _extended_precision.meta.json
│   │   │   │   ├── _nbit.data.json
│   │   │   │   ├── _nbit.meta.json
│   │   │   │   ├── _nbit_base.data.json
│   │   │   │   ├── _nbit_base.meta.json
│   │   │   │   ├── _nested_sequence.data.json
│   │   │   │   ├── _nested_sequence.meta.json
│   │   │   │   ├── _scalars.data.json
│   │   │   │   ├── _scalars.meta.json
│   │   │   │   ├── _shape.data.json
│   │   │   │   ├── _shape.meta.json
│   │   │   │   ├── _ufunc.data.json
│   │   │   │   └── _ufunc.meta.json
│   │   │   ├── _utils
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _convertions.data.json
│   │   │   │   └── _convertions.meta.json
│   │   │   ├── char
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── core
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── ctypeslib.data.json
│   │   │   ├── ctypeslib.meta.json
│   │   │   ├── distutils
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── dtypes.data.json
│   │   │   ├── dtypes.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── f2py
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── fft
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _helper.data.json
│   │   │   │   ├── _helper.meta.json
│   │   │   │   ├── _pocketfft.data.json
│   │   │   │   └── _pocketfft.meta.json
│   │   │   ├── lib
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _array_utils_impl.data.json
│   │   │   │   ├── _array_utils_impl.meta.json
│   │   │   │   ├── _arraypad_impl.data.json
│   │   │   │   ├── _arraypad_impl.meta.json
│   │   │   │   ├── _arraysetops_impl.data.json
│   │   │   │   ├── _arraysetops_impl.meta.json
│   │   │   │   ├── _arrayterator_impl.data.json
│   │   │   │   ├── _arrayterator_impl.meta.json
│   │   │   │   ├── _datasource.data.json
│   │   │   │   ├── _datasource.meta.json
│   │   │   │   ├── _function_base_impl.data.json
│   │   │   │   ├── _function_base_impl.meta.json
│   │   │   │   ├── _histograms_impl.data.json
│   │   │   │   ├── _histograms_impl.meta.json
│   │   │   │   ├── _index_tricks_impl.data.json
│   │   │   │   ├── _index_tricks_impl.meta.json
│   │   │   │   ├── _nanfunctions_impl.data.json
│   │   │   │   ├── _nanfunctions_impl.meta.json
│   │   │   │   ├── _npyio_impl.data.json
│   │   │   │   ├── _npyio_impl.meta.json
│   │   │   │   ├── _polynomial_impl.data.json
│   │   │   │   ├── _polynomial_impl.meta.json
│   │   │   │   ├── _scimath_impl.data.json
│   │   │   │   ├── _scimath_impl.meta.json
│   │   │   │   ├── _shape_base_impl.data.json
│   │   │   │   ├── _shape_base_impl.meta.json
│   │   │   │   ├── _stride_tricks_impl.data.json
│   │   │   │   ├── _stride_tricks_impl.meta.json
│   │   │   │   ├── _twodim_base_impl.data.json
│   │   │   │   ├── _twodim_base_impl.meta.json
│   │   │   │   ├── _type_check_impl.data.json
│   │   │   │   ├── _type_check_impl.meta.json
│   │   │   │   ├── _ufunclike_impl.data.json
│   │   │   │   ├── _ufunclike_impl.meta.json
│   │   │   │   ├── _utils_impl.data.json
│   │   │   │   ├── _utils_impl.meta.json
│   │   │   │   ├── _version.data.json
│   │   │   │   ├── _version.meta.json
│   │   │   │   ├── array_utils.data.json
│   │   │   │   ├── array_utils.meta.json
│   │   │   │   ├── format.data.json
│   │   │   │   ├── format.meta.json
│   │   │   │   ├── introspect.data.json
│   │   │   │   ├── introspect.meta.json
│   │   │   │   ├── mixins.data.json
│   │   │   │   ├── mixins.meta.json
│   │   │   │   ├── npyio.data.json
│   │   │   │   ├── npyio.meta.json
│   │   │   │   ├── scimath.data.json
│   │   │   │   ├── scimath.meta.json
│   │   │   │   ├── stride_tricks.data.json
│   │   │   │   └── stride_tricks.meta.json
│   │   │   ├── linalg
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _linalg.data.json
│   │   │   │   └── _linalg.meta.json
│   │   │   ├── ma
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── core.data.json
│   │   │   │   ├── core.meta.json
│   │   │   │   ├── extras.data.json
│   │   │   │   ├── extras.meta.json
│   │   │   │   ├── mrecords.data.json
│   │   │   │   └── mrecords.meta.json
│   │   │   ├── matlib.data.json
│   │   │   ├── matlib.meta.json
│   │   │   ├── matrixlib
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── defmatrix.data.json
│   │   │   │   └── defmatrix.meta.json
│   │   │   ├── polynomial
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _polybase.data.json
│   │   │   │   ├── _polybase.meta.json
│   │   │   │   ├── _polytypes.data.json
│   │   │   │   ├── _polytypes.meta.json
│   │   │   │   ├── chebyshev.data.json
│   │   │   │   ├── chebyshev.meta.json
│   │   │   │   ├── hermite.data.json
│   │   │   │   ├── hermite.meta.json
│   │   │   │   ├── hermite_e.data.json
│   │   │   │   ├── hermite_e.meta.json
│   │   │   │   ├── laguerre.data.json
│   │   │   │   ├── laguerre.meta.json
│   │   │   │   ├── legendre.data.json
│   │   │   │   ├── legendre.meta.json
│   │   │   │   ├── polynomial.data.json
│   │   │   │   ├── polynomial.meta.json
│   │   │   │   ├── polyutils.data.json
│   │   │   │   └── polyutils.meta.json
│   │   │   ├── random
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _generator.data.json
│   │   │   │   ├── _generator.meta.json
│   │   │   │   ├── _mt19937.data.json
│   │   │   │   ├── _mt19937.meta.json
│   │   │   │   ├── _pcg64.data.json
│   │   │   │   ├── _pcg64.meta.json
│   │   │   │   ├── _philox.data.json
│   │   │   │   ├── _philox.meta.json
│   │   │   │   ├── _sfc64.data.json
│   │   │   │   ├── _sfc64.meta.json
│   │   │   │   ├── bit_generator.data.json
│   │   │   │   ├── bit_generator.meta.json
│   │   │   │   ├── mtrand.data.json
│   │   │   │   └── mtrand.meta.json
│   │   │   ├── rec
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── strings
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── testing
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _private
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   ├── overrides.data.json
│   │   │   │   └── overrides.meta.json
│   │   │   ├── typing
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── version.data.json
│   │   │   └── version.meta.json
│   │   ├── opcode.data.json
│   │   ├── opcode.meta.json
│   │   ├── opentelemetry
│   │   │   ├── attributes
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── context
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── context.data.json
│   │   │   │   └── context.meta.json
│   │   │   ├── environment_variables
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── metrics
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   └── _internal
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── instrument.data.json
│   │   │   │       ├── instrument.meta.json
│   │   │   │       ├── observation.data.json
│   │   │   │       └── observation.meta.json
│   │   │   ├── trace
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── propagation
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── span.data.json
│   │   │   │   ├── span.meta.json
│   │   │   │   ├── status.data.json
│   │   │   │   └── status.meta.json
│   │   │   ├── util
│   │   │   │   ├── _decorator.data.json
│   │   │   │   ├── _decorator.meta.json
│   │   │   │   ├── _importlib_metadata.data.json
│   │   │   │   ├── _importlib_metadata.meta.json
│   │   │   │   ├── _once.data.json
│   │   │   │   ├── _once.meta.json
│   │   │   │   ├── _providers.data.json
│   │   │   │   ├── _providers.meta.json
│   │   │   │   ├── types.data.json
│   │   │   │   └── types.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── opentelemetry.data.json
│   │   ├── opentelemetry.meta.json
│   │   ├── operator.data.json
│   │   ├── operator.meta.json
│   │   ├── orchestrator
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── orjson
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── os
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── path.data.json
│   │   │   └── path.meta.json
│   │   ├── packaging
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _structures.data.json
│   │   │   ├── _structures.meta.json
│   │   │   ├── version.data.json
│   │   │   └── version.meta.json
│   │   ├── pathlib
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── pdb.data.json
│   │   ├── pdb.meta.json
│   │   ├── pickle.data.json
│   │   ├── pickle.meta.json
│   │   ├── pickletools.data.json
│   │   ├── pickletools.meta.json
│   │   ├── pkgutil.data.json
│   │   ├── pkgutil.meta.json
│   │   ├── platform.data.json
│   │   ├── platform.meta.json
│   │   ├── playwright
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _impl
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _accessibility.data.json
│   │   │   │   ├── _accessibility.meta.json
│   │   │   │   ├── _api_structures.data.json
│   │   │   │   ├── _api_structures.meta.json
│   │   │   │   ├── _artifact.data.json
│   │   │   │   ├── _artifact.meta.json
│   │   │   │   ├── _assertions.data.json
│   │   │   │   ├── _assertions.meta.json
│   │   │   │   ├── _async_base.data.json
│   │   │   │   ├── _async_base.meta.json
│   │   │   │   ├── _browser.data.json
│   │   │   │   ├── _browser.meta.json
│   │   │   │   ├── _browser_context.data.json
│   │   │   │   ├── _browser_context.meta.json
│   │   │   │   ├── _browser_type.data.json
│   │   │   │   ├── _browser_type.meta.json
│   │   │   │   ├── _cdp_session.data.json
│   │   │   │   ├── _cdp_session.meta.json
│   │   │   │   ├── _clock.data.json
│   │   │   │   ├── _clock.meta.json
│   │   │   │   ├── _connection.data.json
│   │   │   │   ├── _connection.meta.json
│   │   │   │   ├── _console_message.data.json
│   │   │   │   ├── _console_message.meta.json
│   │   │   │   ├── _dialog.data.json
│   │   │   │   ├── _dialog.meta.json
│   │   │   │   ├── _download.data.json
│   │   │   │   ├── _download.meta.json
│   │   │   │   ├── _driver.data.json
│   │   │   │   ├── _driver.meta.json
│   │   │   │   ├── _element_handle.data.json
│   │   │   │   ├── _element_handle.meta.json
│   │   │   │   ├── _errors.data.json
│   │   │   │   ├── _errors.meta.json
│   │   │   │   ├── _event_context_manager.data.json
│   │   │   │   ├── _event_context_manager.meta.json
│   │   │   │   ├── _fetch.data.json
│   │   │   │   ├── _fetch.meta.json
│   │   │   │   ├── _file_chooser.data.json
│   │   │   │   ├── _file_chooser.meta.json
│   │   │   │   ├── _frame.data.json
│   │   │   │   ├── _frame.meta.json
│   │   │   │   ├── _glob.data.json
│   │   │   │   ├── _glob.meta.json
│   │   │   │   ├── _greenlets.data.json
│   │   │   │   ├── _greenlets.meta.json
│   │   │   │   ├── _har_router.data.json
│   │   │   │   ├── _har_router.meta.json
│   │   │   │   ├── _helper.data.json
│   │   │   │   ├── _helper.meta.json
│   │   │   │   ├── _impl_to_api_mapping.data.json
│   │   │   │   ├── _impl_to_api_mapping.meta.json
│   │   │   │   ├── _input.data.json
│   │   │   │   ├── _input.meta.json
│   │   │   │   ├── _js_handle.data.json
│   │   │   │   ├── _js_handle.meta.json
│   │   │   │   ├── _json_pipe.data.json
│   │   │   │   ├── _json_pipe.meta.json
│   │   │   │   ├── _local_utils.data.json
│   │   │   │   ├── _local_utils.meta.json
│   │   │   │   ├── _locator.data.json
│   │   │   │   ├── _locator.meta.json
│   │   │   │   ├── _map.data.json
│   │   │   │   ├── _map.meta.json
│   │   │   │   ├── _network.data.json
│   │   │   │   ├── _network.meta.json
│   │   │   │   ├── _object_factory.data.json
│   │   │   │   ├── _object_factory.meta.json
│   │   │   │   ├── _page.data.json
│   │   │   │   ├── _page.meta.json
│   │   │   │   ├── _playwright.data.json
│   │   │   │   ├── _playwright.meta.json
│   │   │   │   ├── _selectors.data.json
│   │   │   │   ├── _selectors.meta.json
│   │   │   │   ├── _set_input_files_helpers.data.json
│   │   │   │   ├── _set_input_files_helpers.meta.json
│   │   │   │   ├── _str_utils.data.json
│   │   │   │   ├── _str_utils.meta.json
│   │   │   │   ├── _stream.data.json
│   │   │   │   ├── _stream.meta.json
│   │   │   │   ├── _tracing.data.json
│   │   │   │   ├── _tracing.meta.json
│   │   │   │   ├── _transport.data.json
│   │   │   │   ├── _transport.meta.json
│   │   │   │   ├── _video.data.json
│   │   │   │   ├── _video.meta.json
│   │   │   │   ├── _waiter.data.json
│   │   │   │   ├── _waiter.meta.json
│   │   │   │   ├── _web_error.data.json
│   │   │   │   ├── _web_error.meta.json
│   │   │   │   ├── _writable_stream.data.json
│   │   │   │   └── _writable_stream.meta.json
│   │   │   ├── _repo_version.data.json
│   │   │   ├── _repo_version.meta.json
│   │   │   └── async_api
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── _context_manager.data.json
│   │   │       ├── _context_manager.meta.json
│   │   │       ├── _generated.data.json
│   │   │       └── _generated.meta.json
│   │   ├── posixpath.data.json
│   │   ├── posixpath.meta.json
│   │   ├── pprint.data.json
│   │   ├── pprint.meta.json
│   │   ├── profile.data.json
│   │   ├── profile.meta.json
│   │   ├── propcache
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _helpers.data.json
│   │   │   ├── _helpers.meta.json
│   │   │   ├── _helpers_py.data.json
│   │   │   ├── _helpers_py.meta.json
│   │   │   ├── api.data.json
│   │   │   └── api.meta.json
│   │   ├── pstats.data.json
│   │   ├── pstats.meta.json
│   │   ├── pty.data.json
│   │   ├── pty.meta.json
│   │   ├── pydantic
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _internal
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _config.data.json
│   │   │   │   ├── _config.meta.json
│   │   │   │   ├── _core_metadata.data.json
│   │   │   │   ├── _core_metadata.meta.json
│   │   │   │   ├── _core_utils.data.json
│   │   │   │   ├── _core_utils.meta.json
│   │   │   │   ├── _dataclasses.data.json
│   │   │   │   ├── _dataclasses.meta.json
│   │   │   │   ├── _decorators.data.json
│   │   │   │   ├── _decorators.meta.json
│   │   │   │   ├── _decorators_v1.data.json
│   │   │   │   ├── _decorators_v1.meta.json
│   │   │   │   ├── _discriminated_union.data.json
│   │   │   │   ├── _discriminated_union.meta.json
│   │   │   │   ├── _docs_extraction.data.json
│   │   │   │   ├── _docs_extraction.meta.json
│   │   │   │   ├── _fields.data.json
│   │   │   │   ├── _fields.meta.json
│   │   │   │   ├── _forward_ref.data.json
│   │   │   │   ├── _forward_ref.meta.json
│   │   │   │   ├── _generate_schema.data.json
│   │   │   │   ├── _generate_schema.meta.json
│   │   │   │   ├── _generics.data.json
│   │   │   │   ├── _generics.meta.json
│   │   │   │   ├── _import_utils.data.json
│   │   │   │   ├── _import_utils.meta.json
│   │   │   │   ├── _internal_dataclass.data.json
│   │   │   │   ├── _internal_dataclass.meta.json
│   │   │   │   ├── _known_annotated_metadata.data.json
│   │   │   │   ├── _known_annotated_metadata.meta.json
│   │   │   │   ├── _mock_val_ser.data.json
│   │   │   │   ├── _mock_val_ser.meta.json
│   │   │   │   ├── _model_construction.data.json
│   │   │   │   ├── _model_construction.meta.json
│   │   │   │   ├── _namespace_utils.data.json
│   │   │   │   ├── _namespace_utils.meta.json
│   │   │   │   ├── _repr.data.json
│   │   │   │   ├── _repr.meta.json
│   │   │   │   ├── _schema_gather.data.json
│   │   │   │   ├── _schema_gather.meta.json
│   │   │   │   ├── _schema_generation_shared.data.json
│   │   │   │   ├── _schema_generation_shared.meta.json
│   │   │   │   ├── _serializers.data.json
│   │   │   │   ├── _serializers.meta.json
│   │   │   │   ├── _signature.data.json
│   │   │   │   ├── _signature.meta.json
│   │   │   │   ├── _typing_extra.data.json
│   │   │   │   ├── _typing_extra.meta.json
│   │   │   │   ├── _utils.data.json
│   │   │   │   ├── _utils.meta.json
│   │   │   │   ├── _validate_call.data.json
│   │   │   │   ├── _validate_call.meta.json
│   │   │   │   ├── _validators.data.json
│   │   │   │   └── _validators.meta.json
│   │   │   ├── _migration.data.json
│   │   │   ├── _migration.meta.json
│   │   │   ├── aliases.data.json
│   │   │   ├── aliases.meta.json
│   │   │   ├── annotated_handlers.data.json
│   │   │   ├── annotated_handlers.meta.json
│   │   │   ├── class_validators.data.json
│   │   │   ├── class_validators.meta.json
│   │   │   ├── color.data.json
│   │   │   ├── color.meta.json
│   │   │   ├── config.data.json
│   │   │   ├── config.meta.json
│   │   │   ├── dataclasses.data.json
│   │   │   ├── dataclasses.meta.json
│   │   │   ├── deprecated
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── class_validators.data.json
│   │   │   │   ├── class_validators.meta.json
│   │   │   │   ├── config.data.json
│   │   │   │   ├── config.meta.json
│   │   │   │   ├── copy_internals.data.json
│   │   │   │   ├── copy_internals.meta.json
│   │   │   │   ├── json.data.json
│   │   │   │   ├── json.meta.json
│   │   │   │   ├── parse.data.json
│   │   │   │   ├── parse.meta.json
│   │   │   │   ├── tools.data.json
│   │   │   │   └── tools.meta.json
│   │   │   ├── error_wrappers.data.json
│   │   │   ├── error_wrappers.meta.json
│   │   │   ├── errors.data.json
│   │   │   ├── errors.meta.json
│   │   │   ├── fields.data.json
│   │   │   ├── fields.meta.json
│   │   │   ├── functional_serializers.data.json
│   │   │   ├── functional_serializers.meta.json
│   │   │   ├── functional_validators.data.json
│   │   │   ├── functional_validators.meta.json
│   │   │   ├── json_schema.data.json
│   │   │   ├── json_schema.meta.json
│   │   │   ├── main.data.json
│   │   │   ├── main.meta.json
│   │   │   ├── networks.data.json
│   │   │   ├── networks.meta.json
│   │   │   ├── plugin
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _schema_validator.data.json
│   │   │   │   └── _schema_validator.meta.json
│   │   │   ├── root_model.data.json
│   │   │   ├── root_model.meta.json
│   │   │   ├── schema.data.json
│   │   │   ├── schema.meta.json
│   │   │   ├── type_adapter.data.json
│   │   │   ├── type_adapter.meta.json
│   │   │   ├── types.data.json
│   │   │   ├── types.meta.json
│   │   │   ├── typing.data.json
│   │   │   ├── typing.meta.json
│   │   │   ├── utils.data.json
│   │   │   ├── utils.meta.json
│   │   │   ├── v1
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── annotated_types.data.json
│   │   │   │   ├── annotated_types.meta.json
│   │   │   │   ├── class_validators.data.json
│   │   │   │   ├── class_validators.meta.json
│   │   │   │   ├── color.data.json
│   │   │   │   ├── color.meta.json
│   │   │   │   ├── config.data.json
│   │   │   │   ├── config.meta.json
│   │   │   │   ├── dataclasses.data.json
│   │   │   │   ├── dataclasses.meta.json
│   │   │   │   ├── datetime_parse.data.json
│   │   │   │   ├── datetime_parse.meta.json
│   │   │   │   ├── decorator.data.json
│   │   │   │   ├── decorator.meta.json
│   │   │   │   ├── env_settings.data.json
│   │   │   │   ├── env_settings.meta.json
│   │   │   │   ├── error_wrappers.data.json
│   │   │   │   ├── error_wrappers.meta.json
│   │   │   │   ├── errors.data.json
│   │   │   │   ├── errors.meta.json
│   │   │   │   ├── fields.data.json
│   │   │   │   ├── fields.meta.json
│   │   │   │   ├── json.data.json
│   │   │   │   ├── json.meta.json
│   │   │   │   ├── main.data.json
│   │   │   │   ├── main.meta.json
│   │   │   │   ├── networks.data.json
│   │   │   │   ├── networks.meta.json
│   │   │   │   ├── parse.data.json
│   │   │   │   ├── parse.meta.json
│   │   │   │   ├── schema.data.json
│   │   │   │   ├── schema.meta.json
│   │   │   │   ├── tools.data.json
│   │   │   │   ├── tools.meta.json
│   │   │   │   ├── types.data.json
│   │   │   │   ├── types.meta.json
│   │   │   │   ├── typing.data.json
│   │   │   │   ├── typing.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   ├── utils.meta.json
│   │   │   │   ├── validators.data.json
│   │   │   │   ├── validators.meta.json
│   │   │   │   ├── version.data.json
│   │   │   │   └── version.meta.json
│   │   │   ├── validate_call_decorator.data.json
│   │   │   ├── validate_call_decorator.meta.json
│   │   │   ├── version.data.json
│   │   │   ├── version.meta.json
│   │   │   ├── warnings.data.json
│   │   │   └── warnings.meta.json
│   │   ├── pydantic_core
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _pydantic_core.data.json
│   │   │   ├── _pydantic_core.meta.json
│   │   │   ├── core_schema.data.json
│   │   │   └── core_schema.meta.json
│   │   ├── pydoc.data.json
│   │   ├── pydoc.meta.json
│   │   ├── pyee
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── asyncio.data.json
│   │   │   ├── asyncio.meta.json
│   │   │   ├── base.data.json
│   │   │   └── base.meta.json
│   │   ├── pyexpat
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── errors.data.json
│   │   │   ├── errors.meta.json
│   │   │   ├── model.data.json
│   │   │   └── model.meta.json
│   │   ├── pyparsing
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── actions.data.json
│   │   │   ├── actions.meta.json
│   │   │   ├── common.data.json
│   │   │   ├── common.meta.json
│   │   │   ├── core.data.json
│   │   │   ├── core.meta.json
│   │   │   ├── diagram
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── helpers.data.json
│   │   │   ├── helpers.meta.json
│   │   │   ├── results.data.json
│   │   │   ├── results.meta.json
│   │   │   ├── testing.data.json
│   │   │   ├── testing.meta.json
│   │   │   ├── unicode.data.json
│   │   │   ├── unicode.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── queue.data.json
│   │   ├── queue.meta.json
│   │   ├── rag
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── data_sources.data.json
│   │   │   ├── data_sources.meta.json
│   │   │   ├── retrievers.data.json
│   │   │   └── retrievers.meta.json
│   │   ├── random.data.json
│   │   ├── random.meta.json
│   │   ├── re.data.json
│   │   ├── re.meta.json
│   │   ├── readline.data.json
│   │   ├── readline.meta.json
│   │   ├── reprlib.data.json
│   │   ├── reprlib.meta.json
│   │   ├── requests
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── __version__.data.json
│   │   │   ├── __version__.meta.json
│   │   │   ├── adapters.data.json
│   │   │   ├── adapters.meta.json
│   │   │   ├── api.data.json
│   │   │   ├── api.meta.json
│   │   │   ├── auth.data.json
│   │   │   ├── auth.meta.json
│   │   │   ├── compat.data.json
│   │   │   ├── compat.meta.json
│   │   │   ├── cookies.data.json
│   │   │   ├── cookies.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── hooks.data.json
│   │   │   ├── hooks.meta.json
│   │   │   ├── models.data.json
│   │   │   ├── models.meta.json
│   │   │   ├── packages.data.json
│   │   │   ├── packages.meta.json
│   │   │   ├── sessions.data.json
│   │   │   ├── sessions.meta.json
│   │   │   ├── status_codes.data.json
│   │   │   ├── status_codes.meta.json
│   │   │   ├── structures.data.json
│   │   │   ├── structures.meta.json
│   │   │   ├── utils.data.json
│   │   │   └── utils.meta.json
│   │   ├── resource.data.json
│   │   ├── resource.meta.json
│   │   ├── rich
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── __main__.data.json
│   │   │   ├── __main__.meta.json
│   │   │   ├── _cell_widths.data.json
│   │   │   ├── _cell_widths.meta.json
│   │   │   ├── _emoji_codes.data.json
│   │   │   ├── _emoji_codes.meta.json
│   │   │   ├── _emoji_replace.data.json
│   │   │   ├── _emoji_replace.meta.json
│   │   │   ├── _export_format.data.json
│   │   │   ├── _export_format.meta.json
│   │   │   ├── _extension.data.json
│   │   │   ├── _extension.meta.json
│   │   │   ├── _fileno.data.json
│   │   │   ├── _fileno.meta.json
│   │   │   ├── _log_render.data.json
│   │   │   ├── _log_render.meta.json
│   │   │   ├── _loop.data.json
│   │   │   ├── _loop.meta.json
│   │   │   ├── _null_file.data.json
│   │   │   ├── _null_file.meta.json
│   │   │   ├── _palettes.data.json
│   │   │   ├── _palettes.meta.json
│   │   │   ├── _pick.data.json
│   │   │   ├── _pick.meta.json
│   │   │   ├── _ratio.data.json
│   │   │   ├── _ratio.meta.json
│   │   │   ├── _spinners.data.json
│   │   │   ├── _spinners.meta.json
│   │   │   ├── _stack.data.json
│   │   │   ├── _stack.meta.json
│   │   │   ├── _timer.data.json
│   │   │   ├── _timer.meta.json
│   │   │   ├── _win32_console.data.json
│   │   │   ├── _win32_console.meta.json
│   │   │   ├── _windows.data.json
│   │   │   ├── _windows.meta.json
│   │   │   ├── _windows_renderer.data.json
│   │   │   ├── _windows_renderer.meta.json
│   │   │   ├── _wrap.data.json
│   │   │   ├── _wrap.meta.json
│   │   │   ├── abc.data.json
│   │   │   ├── abc.meta.json
│   │   │   ├── align.data.json
│   │   │   ├── align.meta.json
│   │   │   ├── ansi.data.json
│   │   │   ├── ansi.meta.json
│   │   │   ├── box.data.json
│   │   │   ├── box.meta.json
│   │   │   ├── cells.data.json
│   │   │   ├── cells.meta.json
│   │   │   ├── color.data.json
│   │   │   ├── color.meta.json
│   │   │   ├── color_triplet.data.json
│   │   │   ├── color_triplet.meta.json
│   │   │   ├── columns.data.json
│   │   │   ├── columns.meta.json
│   │   │   ├── console.data.json
│   │   │   ├── console.meta.json
│   │   │   ├── constrain.data.json
│   │   │   ├── constrain.meta.json
│   │   │   ├── containers.data.json
│   │   │   ├── containers.meta.json
│   │   │   ├── control.data.json
│   │   │   ├── control.meta.json
│   │   │   ├── default_styles.data.json
│   │   │   ├── default_styles.meta.json
│   │   │   ├── emoji.data.json
│   │   │   ├── emoji.meta.json
│   │   │   ├── errors.data.json
│   │   │   ├── errors.meta.json
│   │   │   ├── file_proxy.data.json
│   │   │   ├── file_proxy.meta.json
│   │   │   ├── highlighter.data.json
│   │   │   ├── highlighter.meta.json
│   │   │   ├── json.data.json
│   │   │   ├── json.meta.json
│   │   │   ├── jupyter.data.json
│   │   │   ├── jupyter.meta.json
│   │   │   ├── live.data.json
│   │   │   ├── live.meta.json
│   │   │   ├── live_render.data.json
│   │   │   ├── live_render.meta.json
│   │   │   ├── markdown.data.json
│   │   │   ├── markdown.meta.json
│   │   │   ├── markup.data.json
│   │   │   ├── markup.meta.json
│   │   │   ├── measure.data.json
│   │   │   ├── measure.meta.json
│   │   │   ├── padding.data.json
│   │   │   ├── padding.meta.json
│   │   │   ├── pager.data.json
│   │   │   ├── pager.meta.json
│   │   │   ├── palette.data.json
│   │   │   ├── palette.meta.json
│   │   │   ├── panel.data.json
│   │   │   ├── panel.meta.json
│   │   │   ├── pretty.data.json
│   │   │   ├── pretty.meta.json
│   │   │   ├── protocol.data.json
│   │   │   ├── protocol.meta.json
│   │   │   ├── region.data.json
│   │   │   ├── region.meta.json
│   │   │   ├── repr.data.json
│   │   │   ├── repr.meta.json
│   │   │   ├── rule.data.json
│   │   │   ├── rule.meta.json
│   │   │   ├── scope.data.json
│   │   │   ├── scope.meta.json
│   │   │   ├── screen.data.json
│   │   │   ├── screen.meta.json
│   │   │   ├── segment.data.json
│   │   │   ├── segment.meta.json
│   │   │   ├── spinner.data.json
│   │   │   ├── spinner.meta.json
│   │   │   ├── status.data.json
│   │   │   ├── status.meta.json
│   │   │   ├── style.data.json
│   │   │   ├── style.meta.json
│   │   │   ├── styled.data.json
│   │   │   ├── styled.meta.json
│   │   │   ├── syntax.data.json
│   │   │   ├── syntax.meta.json
│   │   │   ├── table.data.json
│   │   │   ├── table.meta.json
│   │   │   ├── terminal_theme.data.json
│   │   │   ├── terminal_theme.meta.json
│   │   │   ├── text.data.json
│   │   │   ├── text.meta.json
│   │   │   ├── theme.data.json
│   │   │   ├── theme.meta.json
│   │   │   ├── themes.data.json
│   │   │   ├── themes.meta.json
│   │   │   ├── traceback.data.json
│   │   │   └── traceback.meta.json
│   │   ├── safetensors
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── flax.data.json
│   │   │   ├── flax.meta.json
│   │   │   ├── numpy.data.json
│   │   │   ├── numpy.meta.json
│   │   │   ├── tensorflow.data.json
│   │   │   ├── tensorflow.meta.json
│   │   │   ├── torch.data.json
│   │   │   └── torch.meta.json
│   │   ├── secrets.data.json
│   │   ├── secrets.meta.json
│   │   ├── select.data.json
│   │   ├── select.meta.json
│   │   ├── selectors.data.json
│   │   ├── selectors.meta.json
│   │   ├── sentence_transformers
│   │   │   ├── LoggingHandler.data.json
│   │   │   ├── LoggingHandler.meta.json
│   │   │   ├── SentenceTransformer.data.json
│   │   │   ├── SentenceTransformer.meta.json
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── backend.data.json
│   │   │   ├── backend.meta.json
│   │   │   ├── cross_encoder
│   │   │   │   ├── CrossEncoder.data.json
│   │   │   │   ├── CrossEncoder.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── data_collator.data.json
│   │   │   │   ├── data_collator.meta.json
│   │   │   │   ├── fit_mixin.data.json
│   │   │   │   ├── fit_mixin.meta.json
│   │   │   │   ├── losses
│   │   │   │   │   ├── BinaryCrossEntropyLoss.data.json
│   │   │   │   │   ├── BinaryCrossEntropyLoss.meta.json
│   │   │   │   │   ├── CachedMultipleNegativesRankingLoss.data.json
│   │   │   │   │   ├── CachedMultipleNegativesRankingLoss.meta.json
│   │   │   │   │   ├── CrossEntropyLoss.data.json
│   │   │   │   │   ├── CrossEntropyLoss.meta.json
│   │   │   │   │   ├── LambdaLoss.data.json
│   │   │   │   │   ├── LambdaLoss.meta.json
│   │   │   │   │   ├── ListMLELoss.data.json
│   │   │   │   │   ├── ListMLELoss.meta.json
│   │   │   │   │   ├── ListNetLoss.data.json
│   │   │   │   │   ├── ListNetLoss.meta.json
│   │   │   │   │   ├── MSELoss.data.json
│   │   │   │   │   ├── MSELoss.meta.json
│   │   │   │   │   ├── MarginMSELoss.data.json
│   │   │   │   │   ├── MarginMSELoss.meta.json
│   │   │   │   │   ├── MultipleNegativesRankingLoss.data.json
│   │   │   │   │   ├── MultipleNegativesRankingLoss.meta.json
│   │   │   │   │   ├── PListMLELoss.data.json
│   │   │   │   │   ├── PListMLELoss.meta.json
│   │   │   │   │   ├── RankNetLoss.data.json
│   │   │   │   │   ├── RankNetLoss.meta.json
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── model_card.data.json
│   │   │   │   ├── model_card.meta.json
│   │   │   │   ├── trainer.data.json
│   │   │   │   ├── trainer.meta.json
│   │   │   │   ├── training_args.data.json
│   │   │   │   ├── training_args.meta.json
│   │   │   │   ├── util.data.json
│   │   │   │   └── util.meta.json
│   │   │   ├── data_collator.data.json
│   │   │   ├── data_collator.meta.json
│   │   │   ├── datasets
│   │   │   │   ├── DenoisingAutoEncoderDataset.data.json
│   │   │   │   ├── DenoisingAutoEncoderDataset.meta.json
│   │   │   │   ├── NoDuplicatesDataLoader.data.json
│   │   │   │   ├── NoDuplicatesDataLoader.meta.json
│   │   │   │   ├── ParallelSentencesDataset.data.json
│   │   │   │   ├── ParallelSentencesDataset.meta.json
│   │   │   │   ├── SentenceLabelDataset.data.json
│   │   │   │   ├── SentenceLabelDataset.meta.json
│   │   │   │   ├── SentencesDataset.data.json
│   │   │   │   ├── SentencesDataset.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── evaluation
│   │   │   │   ├── BinaryClassificationEvaluator.data.json
│   │   │   │   ├── BinaryClassificationEvaluator.meta.json
│   │   │   │   ├── EmbeddingSimilarityEvaluator.data.json
│   │   │   │   ├── EmbeddingSimilarityEvaluator.meta.json
│   │   │   │   ├── InformationRetrievalEvaluator.data.json
│   │   │   │   ├── InformationRetrievalEvaluator.meta.json
│   │   │   │   ├── LabelAccuracyEvaluator.data.json
│   │   │   │   ├── LabelAccuracyEvaluator.meta.json
│   │   │   │   ├── MSEEvaluator.data.json
│   │   │   │   ├── MSEEvaluator.meta.json
│   │   │   │   ├── MSEEvaluatorFromDataFrame.data.json
│   │   │   │   ├── MSEEvaluatorFromDataFrame.meta.json
│   │   │   │   ├── NanoBEIREvaluator.data.json
│   │   │   │   ├── NanoBEIREvaluator.meta.json
│   │   │   │   ├── ParaphraseMiningEvaluator.data.json
│   │   │   │   ├── ParaphraseMiningEvaluator.meta.json
│   │   │   │   ├── RerankingEvaluator.data.json
│   │   │   │   ├── RerankingEvaluator.meta.json
│   │   │   │   ├── SentenceEvaluator.data.json
│   │   │   │   ├── SentenceEvaluator.meta.json
│   │   │   │   ├── SequentialEvaluator.data.json
│   │   │   │   ├── SequentialEvaluator.meta.json
│   │   │   │   ├── SimilarityFunction.data.json
│   │   │   │   ├── SimilarityFunction.meta.json
│   │   │   │   ├── TranslationEvaluator.data.json
│   │   │   │   ├── TranslationEvaluator.meta.json
│   │   │   │   ├── TripletEvaluator.data.json
│   │   │   │   ├── TripletEvaluator.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── fit_mixin.data.json
│   │   │   ├── fit_mixin.meta.json
│   │   │   ├── losses
│   │   │   │   ├── AdaptiveLayerLoss.data.json
│   │   │   │   ├── AdaptiveLayerLoss.meta.json
│   │   │   │   ├── AnglELoss.data.json
│   │   │   │   ├── AnglELoss.meta.json
│   │   │   │   ├── BatchAllTripletLoss.data.json
│   │   │   │   ├── BatchAllTripletLoss.meta.json
│   │   │   │   ├── BatchHardSoftMarginTripletLoss.data.json
│   │   │   │   ├── BatchHardSoftMarginTripletLoss.meta.json
│   │   │   │   ├── BatchHardTripletLoss.data.json
│   │   │   │   ├── BatchHardTripletLoss.meta.json
│   │   │   │   ├── BatchSemiHardTripletLoss.data.json
│   │   │   │   ├── BatchSemiHardTripletLoss.meta.json
│   │   │   │   ├── CachedGISTEmbedLoss.data.json
│   │   │   │   ├── CachedGISTEmbedLoss.meta.json
│   │   │   │   ├── CachedMultipleNegativesRankingLoss.data.json
│   │   │   │   ├── CachedMultipleNegativesRankingLoss.meta.json
│   │   │   │   ├── CachedMultipleNegativesSymmetricRankingLoss.data.json
│   │   │   │   ├── CachedMultipleNegativesSymmetricRankingLoss.meta.json
│   │   │   │   ├── CoSENTLoss.data.json
│   │   │   │   ├── CoSENTLoss.meta.json
│   │   │   │   ├── ContrastiveLoss.data.json
│   │   │   │   ├── ContrastiveLoss.meta.json
│   │   │   │   ├── ContrastiveTensionLoss.data.json
│   │   │   │   ├── ContrastiveTensionLoss.meta.json
│   │   │   │   ├── CosineSimilarityLoss.data.json
│   │   │   │   ├── CosineSimilarityLoss.meta.json
│   │   │   │   ├── DenoisingAutoEncoderLoss.data.json
│   │   │   │   ├── DenoisingAutoEncoderLoss.meta.json
│   │   │   │   ├── DistillKLDivLoss.data.json
│   │   │   │   ├── DistillKLDivLoss.meta.json
│   │   │   │   ├── GISTEmbedLoss.data.json
│   │   │   │   ├── GISTEmbedLoss.meta.json
│   │   │   │   ├── MSELoss.data.json
│   │   │   │   ├── MSELoss.meta.json
│   │   │   │   ├── MarginMSELoss.data.json
│   │   │   │   ├── MarginMSELoss.meta.json
│   │   │   │   ├── Matryoshka2dLoss.data.json
│   │   │   │   ├── Matryoshka2dLoss.meta.json
│   │   │   │   ├── MatryoshkaLoss.data.json
│   │   │   │   ├── MatryoshkaLoss.meta.json
│   │   │   │   ├── MegaBatchMarginLoss.data.json
│   │   │   │   ├── MegaBatchMarginLoss.meta.json
│   │   │   │   ├── MultipleNegativesRankingLoss.data.json
│   │   │   │   ├── MultipleNegativesRankingLoss.meta.json
│   │   │   │   ├── MultipleNegativesSymmetricRankingLoss.data.json
│   │   │   │   ├── MultipleNegativesSymmetricRankingLoss.meta.json
│   │   │   │   ├── OnlineContrastiveLoss.data.json
│   │   │   │   ├── OnlineContrastiveLoss.meta.json
│   │   │   │   ├── SoftmaxLoss.data.json
│   │   │   │   ├── SoftmaxLoss.meta.json
│   │   │   │   ├── TripletLoss.data.json
│   │   │   │   ├── TripletLoss.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── model_card.data.json
│   │   │   ├── model_card.meta.json
│   │   │   ├── model_card_templates.data.json
│   │   │   ├── model_card_templates.meta.json
│   │   │   ├── models
│   │   │   │   ├── BoW.data.json
│   │   │   │   ├── BoW.meta.json
│   │   │   │   ├── CLIPModel.data.json
│   │   │   │   ├── CLIPModel.meta.json
│   │   │   │   ├── CNN.data.json
│   │   │   │   ├── CNN.meta.json
│   │   │   │   ├── Dense.data.json
│   │   │   │   ├── Dense.meta.json
│   │   │   │   ├── Dropout.data.json
│   │   │   │   ├── Dropout.meta.json
│   │   │   │   ├── InputModule.data.json
│   │   │   │   ├── InputModule.meta.json
│   │   │   │   ├── LSTM.data.json
│   │   │   │   ├── LSTM.meta.json
│   │   │   │   ├── LayerNorm.data.json
│   │   │   │   ├── LayerNorm.meta.json
│   │   │   │   ├── Module.data.json
│   │   │   │   ├── Module.meta.json
│   │   │   │   ├── Normalize.data.json
│   │   │   │   ├── Normalize.meta.json
│   │   │   │   ├── Pooling.data.json
│   │   │   │   ├── Pooling.meta.json
│   │   │   │   ├── Router.data.json
│   │   │   │   ├── Router.meta.json
│   │   │   │   ├── StaticEmbedding.data.json
│   │   │   │   ├── StaticEmbedding.meta.json
│   │   │   │   ├── Transformer.data.json
│   │   │   │   ├── Transformer.meta.json
│   │   │   │   ├── WeightedLayerPooling.data.json
│   │   │   │   ├── WeightedLayerPooling.meta.json
│   │   │   │   ├── WordEmbeddings.data.json
│   │   │   │   ├── WordEmbeddings.meta.json
│   │   │   │   ├── WordWeights.data.json
│   │   │   │   ├── WordWeights.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   └── tokenizer
│   │   │   │       ├── PhraseTokenizer.data.json
│   │   │   │       ├── PhraseTokenizer.meta.json
│   │   │   │       ├── WhitespaceTokenizer.data.json
│   │   │   │       ├── WhitespaceTokenizer.meta.json
│   │   │   │       ├── WordTokenizer.data.json
│   │   │   │       ├── WordTokenizer.meta.json
│   │   │   │       ├── __init__.data.json
│   │   │   │       └── __init__.meta.json
│   │   │   ├── peft_mixin.data.json
│   │   │   ├── peft_mixin.meta.json
│   │   │   ├── quantization.data.json
│   │   │   ├── quantization.meta.json
│   │   │   ├── readers
│   │   │   │   ├── InputExample.data.json
│   │   │   │   ├── InputExample.meta.json
│   │   │   │   ├── LabelSentenceReader.data.json
│   │   │   │   ├── LabelSentenceReader.meta.json
│   │   │   │   ├── NLIDataReader.data.json
│   │   │   │   ├── NLIDataReader.meta.json
│   │   │   │   ├── STSDataReader.data.json
│   │   │   │   ├── STSDataReader.meta.json
│   │   │   │   ├── TripletReader.data.json
│   │   │   │   ├── TripletReader.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── sampler.data.json
│   │   │   ├── sampler.meta.json
│   │   │   ├── similarity_functions.data.json
│   │   │   ├── similarity_functions.meta.json
│   │   │   ├── sparse_encoder
│   │   │   │   ├── SparseEncoder.data.json
│   │   │   │   ├── SparseEncoder.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── callbacks
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── splade_callbacks.data.json
│   │   │   │   │   └── splade_callbacks.meta.json
│   │   │   │   ├── data_collator.data.json
│   │   │   │   ├── data_collator.meta.json
│   │   │   │   ├── losses
│   │   │   │   │   ├── CSRLoss.data.json
│   │   │   │   │   ├── CSRLoss.meta.json
│   │   │   │   │   ├── FlopsLoss.data.json
│   │   │   │   │   ├── FlopsLoss.meta.json
│   │   │   │   │   ├── SparseAnglELoss.data.json
│   │   │   │   │   ├── SparseAnglELoss.meta.json
│   │   │   │   │   ├── SparseCoSENTLoss.data.json
│   │   │   │   │   ├── SparseCoSENTLoss.meta.json
│   │   │   │   │   ├── SparseCosineSimilarityLoss.data.json
│   │   │   │   │   ├── SparseCosineSimilarityLoss.meta.json
│   │   │   │   │   ├── SparseDistillKLDivLoss.data.json
│   │   │   │   │   ├── SparseDistillKLDivLoss.meta.json
│   │   │   │   │   ├── SparseMSELoss.data.json
│   │   │   │   │   ├── SparseMSELoss.meta.json
│   │   │   │   │   ├── SparseMarginMSELoss.data.json
│   │   │   │   │   ├── SparseMarginMSELoss.meta.json
│   │   │   │   │   ├── SparseMultipleNegativesRankingLoss.data.json
│   │   │   │   │   ├── SparseMultipleNegativesRankingLoss.meta.json
│   │   │   │   │   ├── SparseTripletLoss.data.json
│   │   │   │   │   ├── SparseTripletLoss.meta.json
│   │   │   │   │   ├── SpladeLoss.data.json
│   │   │   │   │   ├── SpladeLoss.meta.json
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── model_card.data.json
│   │   │   │   ├── model_card.meta.json
│   │   │   │   ├── models
│   │   │   │   │   ├── MLMTransformer.data.json
│   │   │   │   │   ├── MLMTransformer.meta.json
│   │   │   │   │   ├── SparseAutoEncoder.data.json
│   │   │   │   │   ├── SparseAutoEncoder.meta.json
│   │   │   │   │   ├── SparseStaticEmbedding.data.json
│   │   │   │   │   ├── SparseStaticEmbedding.meta.json
│   │   │   │   │   ├── SpladePooling.data.json
│   │   │   │   │   ├── SpladePooling.meta.json
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── trainer.data.json
│   │   │   │   ├── trainer.meta.json
│   │   │   │   ├── training_args.data.json
│   │   │   │   └── training_args.meta.json
│   │   │   ├── trainer.data.json
│   │   │   ├── trainer.meta.json
│   │   │   ├── training_args.data.json
│   │   │   ├── training_args.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── services
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── model_loader.data.json
│   │   │   ├── model_loader.meta.json
│   │   │   ├── plan_evaluation_service.data.json
│   │   │   ├── plan_evaluation_service.meta.json
│   │   │   ├── rag_manager_service.data.json
│   │   │   ├── rag_manager_service.meta.json
│   │   │   ├── retrieval_service.data.json
│   │   │   ├── retrieval_service.meta.json
│   │   │   ├── tool_manager_service.data.json
│   │   │   ├── tool_manager_service.meta.json
│   │   │   ├── vectorization_service.data.json
│   │   │   ├── vectorization_service.meta.json
│   │   │   ├── web_browser_service.data.json
│   │   │   ├── web_browser_service.meta.json
│   │   │   ├── wikipedia_service.data.json
│   │   │   ├── wikipedia_service.meta.json
│   │   │   ├── worker_manager.data.json
│   │   │   └── worker_manager.meta.json
│   │   ├── shlex.data.json
│   │   ├── shlex.meta.json
│   │   ├── shutil.data.json
│   │   ├── shutil.meta.json
│   │   ├── signal.data.json
│   │   ├── signal.meta.json
│   │   ├── simplejson
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── decoder.data.json
│   │   │   ├── decoder.meta.json
│   │   │   ├── encoder.data.json
│   │   │   ├── encoder.meta.json
│   │   │   ├── raw_json.data.json
│   │   │   ├── raw_json.meta.json
│   │   │   ├── scanner.data.json
│   │   │   └── scanner.meta.json
│   │   ├── sniffio
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _impl.data.json
│   │   │   ├── _impl.meta.json
│   │   │   ├── _version.data.json
│   │   │   └── _version.meta.json
│   │   ├── socket.data.json
│   │   ├── socket.meta.json
│   │   ├── soupsieve
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── __meta__.data.json
│   │   │   ├── __meta__.meta.json
│   │   │   ├── css_match.data.json
│   │   │   ├── css_match.meta.json
│   │   │   ├── css_parser.data.json
│   │   │   ├── css_parser.meta.json
│   │   │   ├── css_types.data.json
│   │   │   ├── css_types.meta.json
│   │   │   ├── pretty.data.json
│   │   │   ├── pretty.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── sre_compile.data.json
│   │   ├── sre_compile.meta.json
│   │   ├── sre_constants.data.json
│   │   ├── sre_constants.meta.json
│   │   ├── sre_parse.data.json
│   │   ├── sre_parse.meta.json
│   │   ├── ssl.data.json
│   │   ├── ssl.meta.json
│   │   ├── starlette
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _exception_handler.data.json
│   │   │   ├── _exception_handler.meta.json
│   │   │   ├── _utils.data.json
│   │   │   ├── _utils.meta.json
│   │   │   ├── applications.data.json
│   │   │   ├── applications.meta.json
│   │   │   ├── background.data.json
│   │   │   ├── background.meta.json
│   │   │   ├── concurrency.data.json
│   │   │   ├── concurrency.meta.json
│   │   │   ├── convertors.data.json
│   │   │   ├── convertors.meta.json
│   │   │   ├── datastructures.data.json
│   │   │   ├── datastructures.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── formparsers.data.json
│   │   │   ├── formparsers.meta.json
│   │   │   ├── middleware
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── base.data.json
│   │   │   │   ├── base.meta.json
│   │   │   │   ├── errors.data.json
│   │   │   │   ├── errors.meta.json
│   │   │   │   ├── exceptions.data.json
│   │   │   │   └── exceptions.meta.json
│   │   │   ├── requests.data.json
│   │   │   ├── requests.meta.json
│   │   │   ├── responses.data.json
│   │   │   ├── responses.meta.json
│   │   │   ├── routing.data.json
│   │   │   ├── routing.meta.json
│   │   │   ├── status.data.json
│   │   │   ├── status.meta.json
│   │   │   ├── types.data.json
│   │   │   ├── types.meta.json
│   │   │   ├── websockets.data.json
│   │   │   └── websockets.meta.json
│   │   ├── stat.data.json
│   │   ├── stat.meta.json
│   │   ├── statistics.data.json
│   │   ├── statistics.meta.json
│   │   ├── string
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── struct.data.json
│   │   ├── struct.meta.json
│   │   ├── subprocess.data.json
│   │   ├── subprocess.meta.json
│   │   ├── sys
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── sysconfig.data.json
│   │   ├── sysconfig.meta.json
│   │   ├── tabulate
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── version.data.json
│   │   │   └── version.meta.json
│   │   ├── tarfile.data.json
│   │   ├── tarfile.meta.json
│   │   ├── tempfile.data.json
│   │   ├── tempfile.meta.json
│   │   ├── textwrap.data.json
│   │   ├── textwrap.meta.json
│   │   ├── threading.data.json
│   │   ├── threading.meta.json
│   │   ├── tiktoken
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── core.data.json
│   │   │   ├── core.meta.json
│   │   │   ├── load.data.json
│   │   │   ├── load.meta.json
│   │   │   ├── model.data.json
│   │   │   ├── model.meta.json
│   │   │   ├── registry.data.json
│   │   │   └── registry.meta.json
│   │   ├── time.data.json
│   │   ├── time.meta.json
│   │   ├── timeit.data.json
│   │   ├── timeit.meta.json
│   │   ├── token.data.json
│   │   ├── token.meta.json
│   │   ├── tokenize.data.json
│   │   ├── tokenize.meta.json
│   │   ├── torch
│   │   │   ├── _C
│   │   │   │   ├── _VariableFunctions.data.json
│   │   │   │   ├── _VariableFunctions.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _aoti.data.json
│   │   │   │   ├── _aoti.meta.json
│   │   │   │   ├── _autograd.data.json
│   │   │   │   ├── _autograd.meta.json
│   │   │   │   ├── _cpu.data.json
│   │   │   │   ├── _cpu.meta.json
│   │   │   │   ├── _cudnn.data.json
│   │   │   │   ├── _cudnn.meta.json
│   │   │   │   ├── _cusparselt.data.json
│   │   │   │   ├── _cusparselt.meta.json
│   │   │   │   ├── _distributed_autograd.data.json
│   │   │   │   ├── _distributed_autograd.meta.json
│   │   │   │   ├── _distributed_c10d.data.json
│   │   │   │   ├── _distributed_c10d.meta.json
│   │   │   │   ├── _distributed_rpc.data.json
│   │   │   │   ├── _distributed_rpc.meta.json
│   │   │   │   ├── _dynamo
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── compiled_autograd.data.json
│   │   │   │   │   ├── compiled_autograd.meta.json
│   │   │   │   │   ├── eval_frame.data.json
│   │   │   │   │   ├── eval_frame.meta.json
│   │   │   │   │   ├── guards.data.json
│   │   │   │   │   └── guards.meta.json
│   │   │   │   ├── _export
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── pt2_archive_constants.data.json
│   │   │   │   │   └── pt2_archive_constants.meta.json
│   │   │   │   ├── _functions.data.json
│   │   │   │   ├── _functions.meta.json
│   │   │   │   ├── _functorch.data.json
│   │   │   │   ├── _functorch.meta.json
│   │   │   │   ├── _instruction_counter.data.json
│   │   │   │   ├── _instruction_counter.meta.json
│   │   │   │   ├── _itt.data.json
│   │   │   │   ├── _itt.meta.json
│   │   │   │   ├── _lazy.data.json
│   │   │   │   ├── _lazy.meta.json
│   │   │   │   ├── _lazy_ts_backend.data.json
│   │   │   │   ├── _lazy_ts_backend.meta.json
│   │   │   │   ├── _monitor.data.json
│   │   │   │   ├── _monitor.meta.json
│   │   │   │   ├── _nn.data.json
│   │   │   │   ├── _nn.meta.json
│   │   │   │   ├── _nvtx.data.json
│   │   │   │   ├── _nvtx.meta.json
│   │   │   │   ├── _onnx.data.json
│   │   │   │   ├── _onnx.meta.json
│   │   │   │   ├── _profiler.data.json
│   │   │   │   ├── _profiler.meta.json
│   │   │   │   ├── _verbose.data.json
│   │   │   │   └── _verbose.meta.json
│   │   │   ├── _VF.data.json
│   │   │   ├── _VF.meta.json
│   │   │   ├── __config__.data.json
│   │   │   ├── __config__.meta.json
│   │   │   ├── __future__.data.json
│   │   │   ├── __future__.meta.json
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _appdirs.data.json
│   │   │   ├── _appdirs.meta.json
│   │   │   ├── _awaits
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── _classes.data.json
│   │   │   ├── _classes.meta.json
│   │   │   ├── _compile.data.json
│   │   │   ├── _compile.meta.json
│   │   │   ├── _custom_op
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── autograd.data.json
│   │   │   │   ├── autograd.meta.json
│   │   │   │   ├── impl.data.json
│   │   │   │   └── impl.meta.json
│   │   │   ├── _custom_ops.data.json
│   │   │   ├── _custom_ops.meta.json
│   │   │   ├── _decomp
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── decompositions.data.json
│   │   │   │   ├── decompositions.meta.json
│   │   │   │   ├── decompositions_for_rng.data.json
│   │   │   │   └── decompositions_for_rng.meta.json
│   │   │   ├── _dispatch
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── python.data.json
│   │   │   │   └── python.meta.json
│   │   │   ├── _dynamo
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _trace_wrapped_higher_order_op.data.json
│   │   │   │   ├── _trace_wrapped_higher_order_op.meta.json
│   │   │   │   ├── backends
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── common.data.json
│   │   │   │   │   ├── common.meta.json
│   │   │   │   │   ├── debugging.data.json
│   │   │   │   │   ├── debugging.meta.json
│   │   │   │   │   ├── distributed.data.json
│   │   │   │   │   ├── distributed.meta.json
│   │   │   │   │   ├── registry.data.json
│   │   │   │   │   └── registry.meta.json
│   │   │   │   ├── bytecode_analysis.data.json
│   │   │   │   ├── bytecode_analysis.meta.json
│   │   │   │   ├── bytecode_transformation.data.json
│   │   │   │   ├── bytecode_transformation.meta.json
│   │   │   │   ├── cache_size.data.json
│   │   │   │   ├── cache_size.meta.json
│   │   │   │   ├── callback.data.json
│   │   │   │   ├── callback.meta.json
│   │   │   │   ├── code_context.data.json
│   │   │   │   ├── code_context.meta.json
│   │   │   │   ├── codegen.data.json
│   │   │   │   ├── codegen.meta.json
│   │   │   │   ├── compiled_autograd.data.json
│   │   │   │   ├── compiled_autograd.meta.json
│   │   │   │   ├── comptime.data.json
│   │   │   │   ├── comptime.meta.json
│   │   │   │   ├── config.data.json
│   │   │   │   ├── config.meta.json
│   │   │   │   ├── convert_frame.data.json
│   │   │   │   ├── convert_frame.meta.json
│   │   │   │   ├── create_parameter_op.data.json
│   │   │   │   ├── create_parameter_op.meta.json
│   │   │   │   ├── current_scope_id.data.json
│   │   │   │   ├── current_scope_id.meta.json
│   │   │   │   ├── debug_utils.data.json
│   │   │   │   ├── debug_utils.meta.json
│   │   │   │   ├── decorators.data.json
│   │   │   │   ├── decorators.meta.json
│   │   │   │   ├── device_interface.data.json
│   │   │   │   ├── device_interface.meta.json
│   │   │   │   ├── distributed.data.json
│   │   │   │   ├── distributed.meta.json
│   │   │   │   ├── eval_frame.data.json
│   │   │   │   ├── eval_frame.meta.json
│   │   │   │   ├── exc.data.json
│   │   │   │   ├── exc.meta.json
│   │   │   │   ├── external_utils.data.json
│   │   │   │   ├── external_utils.meta.json
│   │   │   │   ├── funcname_cache.data.json
│   │   │   │   ├── funcname_cache.meta.json
│   │   │   │   ├── graph_break_hints.data.json
│   │   │   │   ├── graph_break_hints.meta.json
│   │   │   │   ├── graph_deduplication.data.json
│   │   │   │   ├── graph_deduplication.meta.json
│   │   │   │   ├── graph_region_tracker.data.json
│   │   │   │   ├── graph_region_tracker.meta.json
│   │   │   │   ├── graph_utils.data.json
│   │   │   │   ├── graph_utils.meta.json
│   │   │   │   ├── guards.data.json
│   │   │   │   ├── guards.meta.json
│   │   │   │   ├── hooks.data.json
│   │   │   │   ├── hooks.meta.json
│   │   │   │   ├── logging.data.json
│   │   │   │   ├── logging.meta.json
│   │   │   │   ├── metrics_context.data.json
│   │   │   │   ├── metrics_context.meta.json
│   │   │   │   ├── mutation_guard.data.json
│   │   │   │   ├── mutation_guard.meta.json
│   │   │   │   ├── output_graph.data.json
│   │   │   │   ├── output_graph.meta.json
│   │   │   │   ├── package.data.json
│   │   │   │   ├── package.meta.json
│   │   │   │   ├── pgo.data.json
│   │   │   │   ├── pgo.meta.json
│   │   │   │   ├── polyfills
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── builtins.data.json
│   │   │   │   │   ├── builtins.meta.json
│   │   │   │   │   ├── functools.data.json
│   │   │   │   │   ├── functools.meta.json
│   │   │   │   │   ├── itertools.data.json
│   │   │   │   │   ├── itertools.meta.json
│   │   │   │   │   ├── loader.data.json
│   │   │   │   │   ├── loader.meta.json
│   │   │   │   │   ├── operator.data.json
│   │   │   │   │   ├── operator.meta.json
│   │   │   │   │   ├── os.data.json
│   │   │   │   │   ├── os.meta.json
│   │   │   │   │   ├── pytree.data.json
│   │   │   │   │   ├── pytree.meta.json
│   │   │   │   │   ├── sys.data.json
│   │   │   │   │   └── sys.meta.json
│   │   │   │   ├── precompile_context.data.json
│   │   │   │   ├── precompile_context.meta.json
│   │   │   │   ├── replay_record.data.json
│   │   │   │   ├── replay_record.meta.json
│   │   │   │   ├── repro
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── after_aot.data.json
│   │   │   │   │   ├── after_aot.meta.json
│   │   │   │   │   ├── after_dynamo.data.json
│   │   │   │   │   └── after_dynamo.meta.json
│   │   │   │   ├── resume_execution.data.json
│   │   │   │   ├── resume_execution.meta.json
│   │   │   │   ├── side_effects.data.json
│   │   │   │   ├── side_effects.meta.json
│   │   │   │   ├── source.data.json
│   │   │   │   ├── source.meta.json
│   │   │   │   ├── symbolic_convert.data.json
│   │   │   │   ├── symbolic_convert.meta.json
│   │   │   │   ├── tensor_version_op.data.json
│   │   │   │   ├── tensor_version_op.meta.json
│   │   │   │   ├── testing.data.json
│   │   │   │   ├── testing.meta.json
│   │   │   │   ├── trace_rules.data.json
│   │   │   │   ├── trace_rules.meta.json
│   │   │   │   ├── types.data.json
│   │   │   │   ├── types.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   ├── utils.meta.json
│   │   │   │   └── variables
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── base.data.json
│   │   │   │       ├── base.meta.json
│   │   │   │       ├── builder.data.json
│   │   │   │       ├── builder.meta.json
│   │   │   │       ├── builtin.data.json
│   │   │   │       ├── builtin.meta.json
│   │   │   │       ├── constant.data.json
│   │   │   │       ├── constant.meta.json
│   │   │   │       ├── ctx_manager.data.json
│   │   │   │       ├── ctx_manager.meta.json
│   │   │   │       ├── dicts.data.json
│   │   │   │       ├── dicts.meta.json
│   │   │   │       ├── distributed.data.json
│   │   │   │       ├── distributed.meta.json
│   │   │   │       ├── functions.data.json
│   │   │   │       ├── functions.meta.json
│   │   │   │       ├── higher_order_ops.data.json
│   │   │   │       ├── higher_order_ops.meta.json
│   │   │   │       ├── iter.data.json
│   │   │   │       ├── iter.meta.json
│   │   │   │       ├── lazy.data.json
│   │   │   │       ├── lazy.meta.json
│   │   │   │       ├── lists.data.json
│   │   │   │       ├── lists.meta.json
│   │   │   │       ├── misc.data.json
│   │   │   │       ├── misc.meta.json
│   │   │   │       ├── nn_module.data.json
│   │   │   │       ├── nn_module.meta.json
│   │   │   │       ├── optimizer.data.json
│   │   │   │       ├── optimizer.meta.json
│   │   │   │       ├── script_object.data.json
│   │   │   │       ├── script_object.meta.json
│   │   │   │       ├── sdpa.data.json
│   │   │   │       ├── sdpa.meta.json
│   │   │   │       ├── tensor.data.json
│   │   │   │       ├── tensor.meta.json
│   │   │   │       ├── torch.data.json
│   │   │   │       ├── torch.meta.json
│   │   │   │       ├── torch_function.data.json
│   │   │   │       ├── torch_function.meta.json
│   │   │   │       ├── user_defined.data.json
│   │   │   │       └── user_defined.meta.json
│   │   │   ├── _environment.data.json
│   │   │   ├── _environment.meta.json
│   │   │   ├── _export
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── db
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── logging.data.json
│   │   │   │   │   └── logging.meta.json
│   │   │   │   ├── error.data.json
│   │   │   │   ├── error.meta.json
│   │   │   │   ├── non_strict_utils.data.json
│   │   │   │   ├── non_strict_utils.meta.json
│   │   │   │   ├── pass_base.data.json
│   │   │   │   ├── pass_base.meta.json
│   │   │   │   ├── pass_infra
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── node_metadata.data.json
│   │   │   │   │   ├── node_metadata.meta.json
│   │   │   │   │   ├── proxy_value.data.json
│   │   │   │   │   └── proxy_value.meta.json
│   │   │   │   ├── passes
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _node_metadata_hook.data.json
│   │   │   │   │   ├── _node_metadata_hook.meta.json
│   │   │   │   │   ├── collect_tracepoints_pass.data.json
│   │   │   │   │   ├── collect_tracepoints_pass.meta.json
│   │   │   │   │   ├── insert_custom_op_guards.data.json
│   │   │   │   │   ├── insert_custom_op_guards.meta.json
│   │   │   │   │   ├── lift_constants_pass.data.json
│   │   │   │   │   ├── lift_constants_pass.meta.json
│   │   │   │   │   ├── replace_view_ops_with_view_copy_ops_pass.data.json
│   │   │   │   │   └── replace_view_ops_with_view_copy_ops_pass.meta.json
│   │   │   │   ├── serde
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── schema.data.json
│   │   │   │   │   ├── schema.meta.json
│   │   │   │   │   ├── serialize.data.json
│   │   │   │   │   ├── serialize.meta.json
│   │   │   │   │   ├── union.data.json
│   │   │   │   │   └── union.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   ├── utils.meta.json
│   │   │   │   ├── verifier.data.json
│   │   │   │   ├── verifier.meta.json
│   │   │   │   ├── wrappers.data.json
│   │   │   │   └── wrappers.meta.json
│   │   │   ├── _functorch
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _activation_checkpointing
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── ac_logging_utils.data.json
│   │   │   │   │   ├── ac_logging_utils.meta.json
│   │   │   │   │   ├── graph_info_provider.data.json
│   │   │   │   │   ├── graph_info_provider.meta.json
│   │   │   │   │   ├── knapsack.data.json
│   │   │   │   │   ├── knapsack.meta.json
│   │   │   │   │   ├── knapsack_evaluator.data.json
│   │   │   │   │   └── knapsack_evaluator.meta.json
│   │   │   │   ├── _aot_autograd
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── autograd_cache.data.json
│   │   │   │   │   ├── autograd_cache.meta.json
│   │   │   │   │   ├── collect_metadata_analysis.data.json
│   │   │   │   │   ├── collect_metadata_analysis.meta.json
│   │   │   │   │   ├── dispatch_and_compile_graph.data.json
│   │   │   │   │   ├── dispatch_and_compile_graph.meta.json
│   │   │   │   │   ├── functional_utils.data.json
│   │   │   │   │   ├── functional_utils.meta.json
│   │   │   │   │   ├── input_output_analysis.data.json
│   │   │   │   │   ├── input_output_analysis.meta.json
│   │   │   │   │   ├── jit_compile_runtime_wrappers.data.json
│   │   │   │   │   ├── jit_compile_runtime_wrappers.meta.json
│   │   │   │   │   ├── logging_utils.data.json
│   │   │   │   │   ├── logging_utils.meta.json
│   │   │   │   │   ├── runtime_wrappers.data.json
│   │   │   │   │   ├── runtime_wrappers.meta.json
│   │   │   │   │   ├── schemas.data.json
│   │   │   │   │   ├── schemas.meta.json
│   │   │   │   │   ├── subclass_parametrization.data.json
│   │   │   │   │   ├── subclass_parametrization.meta.json
│   │   │   │   │   ├── subclass_utils.data.json
│   │   │   │   │   ├── subclass_utils.meta.json
│   │   │   │   │   ├── traced_function_transforms.data.json
│   │   │   │   │   ├── traced_function_transforms.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   ├── aot_autograd.data.json
│   │   │   │   ├── aot_autograd.meta.json
│   │   │   │   ├── apis.data.json
│   │   │   │   ├── apis.meta.json
│   │   │   │   ├── autograd_function.data.json
│   │   │   │   ├── autograd_function.meta.json
│   │   │   │   ├── batch_norm_replacement.data.json
│   │   │   │   ├── batch_norm_replacement.meta.json
│   │   │   │   ├── compile_utils.data.json
│   │   │   │   ├── compile_utils.meta.json
│   │   │   │   ├── compilers.data.json
│   │   │   │   ├── compilers.meta.json
│   │   │   │   ├── config.data.json
│   │   │   │   ├── config.meta.json
│   │   │   │   ├── eager_transforms.data.json
│   │   │   │   ├── eager_transforms.meta.json
│   │   │   │   ├── functional_call.data.json
│   │   │   │   ├── functional_call.meta.json
│   │   │   │   ├── partitioners.data.json
│   │   │   │   ├── partitioners.meta.json
│   │   │   │   ├── pyfunctorch.data.json
│   │   │   │   ├── pyfunctorch.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   ├── utils.meta.json
│   │   │   │   ├── vmap.data.json
│   │   │   │   └── vmap.meta.json
│   │   │   ├── _guards.data.json
│   │   │   ├── _guards.meta.json
│   │   │   ├── _higher_order_ops
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _invoke_quant.data.json
│   │   │   │   ├── _invoke_quant.meta.json
│   │   │   │   ├── aoti_call_delegate.data.json
│   │   │   │   ├── aoti_call_delegate.meta.json
│   │   │   │   ├── associative_scan.data.json
│   │   │   │   ├── associative_scan.meta.json
│   │   │   │   ├── auto_functionalize.data.json
│   │   │   │   ├── auto_functionalize.meta.json
│   │   │   │   ├── base_hop.data.json
│   │   │   │   ├── base_hop.meta.json
│   │   │   │   ├── cond.data.json
│   │   │   │   ├── cond.meta.json
│   │   │   │   ├── effects.data.json
│   │   │   │   ├── effects.meta.json
│   │   │   │   ├── executorch_call_delegate.data.json
│   │   │   │   ├── executorch_call_delegate.meta.json
│   │   │   │   ├── flat_apply.data.json
│   │   │   │   ├── flat_apply.meta.json
│   │   │   │   ├── flex_attention.data.json
│   │   │   │   ├── flex_attention.meta.json
│   │   │   │   ├── foreach_map.data.json
│   │   │   │   ├── foreach_map.meta.json
│   │   │   │   ├── hints_wrap.data.json
│   │   │   │   ├── hints_wrap.meta.json
│   │   │   │   ├── invoke_subgraph.data.json
│   │   │   │   ├── invoke_subgraph.meta.json
│   │   │   │   ├── map.data.json
│   │   │   │   ├── map.meta.json
│   │   │   │   ├── out_dtype.data.json
│   │   │   │   ├── out_dtype.meta.json
│   │   │   │   ├── run_const_graph.data.json
│   │   │   │   ├── run_const_graph.meta.json
│   │   │   │   ├── scan.data.json
│   │   │   │   ├── scan.meta.json
│   │   │   │   ├── schema.data.json
│   │   │   │   ├── schema.meta.json
│   │   │   │   ├── strict_mode.data.json
│   │   │   │   ├── strict_mode.meta.json
│   │   │   │   ├── torchbind.data.json
│   │   │   │   ├── torchbind.meta.json
│   │   │   │   ├── triton_kernel_wrap.data.json
│   │   │   │   ├── triton_kernel_wrap.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   ├── utils.meta.json
│   │   │   │   ├── while_loop.data.json
│   │   │   │   ├── while_loop.meta.json
│   │   │   │   ├── wrap.data.json
│   │   │   │   └── wrap.meta.json
│   │   │   ├── _inductor
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── analyze_preserves_zero_mask.data.json
│   │   │   │   ├── analyze_preserves_zero_mask.meta.json
│   │   │   │   ├── async_compile.data.json
│   │   │   │   ├── async_compile.meta.json
│   │   │   │   ├── autoheuristic
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── autoheuristic.data.json
│   │   │   │   │   ├── autoheuristic.meta.json
│   │   │   │   │   ├── autoheuristic_utils.data.json
│   │   │   │   │   ├── autoheuristic_utils.meta.json
│   │   │   │   │   ├── learned_heuristic_controller.data.json
│   │   │   │   │   ├── learned_heuristic_controller.meta.json
│   │   │   │   │   ├── learnedheuristic_interface.data.json
│   │   │   │   │   └── learnedheuristic_interface.meta.json
│   │   │   │   ├── autotune_process.data.json
│   │   │   │   ├── autotune_process.meta.json
│   │   │   │   ├── bounds.data.json
│   │   │   │   ├── bounds.meta.json
│   │   │   │   ├── choices.data.json
│   │   │   │   ├── choices.meta.json
│   │   │   │   ├── codecache.data.json
│   │   │   │   ├── codecache.meta.json
│   │   │   │   ├── codegen
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── aoti_hipify_utils.data.json
│   │   │   │   │   ├── aoti_hipify_utils.meta.json
│   │   │   │   │   ├── block_analysis.data.json
│   │   │   │   │   ├── block_analysis.meta.json
│   │   │   │   │   ├── common.data.json
│   │   │   │   │   ├── common.meta.json
│   │   │   │   │   ├── cpp.data.json
│   │   │   │   │   ├── cpp.meta.json
│   │   │   │   │   ├── cpp_gemm_template.data.json
│   │   │   │   │   ├── cpp_gemm_template.meta.json
│   │   │   │   │   ├── cpp_grouped_gemm_template.data.json
│   │   │   │   │   ├── cpp_grouped_gemm_template.meta.json
│   │   │   │   │   ├── cpp_micro_gemm.data.json
│   │   │   │   │   ├── cpp_micro_gemm.meta.json
│   │   │   │   │   ├── cpp_template.data.json
│   │   │   │   │   ├── cpp_template.meta.json
│   │   │   │   │   ├── cpp_template_kernel.data.json
│   │   │   │   │   ├── cpp_template_kernel.meta.json
│   │   │   │   │   ├── cpp_utils.data.json
│   │   │   │   │   ├── cpp_utils.meta.json
│   │   │   │   │   ├── cpp_wrapper_cpu.data.json
│   │   │   │   │   ├── cpp_wrapper_cpu.meta.json
│   │   │   │   │   ├── cuda
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── cuda_cpp_scheduling.data.json
│   │   │   │   │   │   ├── cuda_cpp_scheduling.meta.json
│   │   │   │   │   │   ├── cuda_env.data.json
│   │   │   │   │   │   ├── cuda_env.meta.json
│   │   │   │   │   │   ├── cuda_kernel.data.json
│   │   │   │   │   │   ├── cuda_kernel.meta.json
│   │   │   │   │   │   ├── cuda_template.data.json
│   │   │   │   │   │   ├── cuda_template.meta.json
│   │   │   │   │   │   ├── cutlass_cache.data.json
│   │   │   │   │   │   ├── cutlass_cache.meta.json
│   │   │   │   │   │   ├── cutlass_lib_extensions
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── evt_extensions.data.json
│   │   │   │   │   │   │   ├── evt_extensions.meta.json
│   │   │   │   │   │   │   ├── gemm_operation_extensions.data.json
│   │   │   │   │   │   │   └── gemm_operation_extensions.meta.json
│   │   │   │   │   │   ├── cutlass_presets.data.json
│   │   │   │   │   │   ├── cutlass_presets.meta.json
│   │   │   │   │   │   ├── cutlass_python_evt.data.json
│   │   │   │   │   │   ├── cutlass_python_evt.meta.json
│   │   │   │   │   │   ├── cutlass_utils.data.json
│   │   │   │   │   │   ├── cutlass_utils.meta.json
│   │   │   │   │   │   ├── gemm_template.data.json
│   │   │   │   │   │   ├── gemm_template.meta.json
│   │   │   │   │   │   ├── serialization.data.json
│   │   │   │   │   │   └── serialization.meta.json
│   │   │   │   │   ├── cuda_combined_scheduling.data.json
│   │   │   │   │   ├── cuda_combined_scheduling.meta.json
│   │   │   │   │   ├── debug_utils.data.json
│   │   │   │   │   ├── debug_utils.meta.json
│   │   │   │   │   ├── memory_planning.data.json
│   │   │   │   │   ├── memory_planning.meta.json
│   │   │   │   │   ├── multi_kernel.data.json
│   │   │   │   │   ├── multi_kernel.meta.json
│   │   │   │   │   ├── rocm
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── ck_template.data.json
│   │   │   │   │   │   ├── ck_template.meta.json
│   │   │   │   │   │   ├── ck_tile_template.data.json
│   │   │   │   │   │   ├── ck_tile_template.meta.json
│   │   │   │   │   │   ├── ck_tile_universal_gemm_template.data.json
│   │   │   │   │   │   ├── ck_tile_universal_gemm_template.meta.json
│   │   │   │   │   │   ├── ck_universal_gemm_template.data.json
│   │   │   │   │   │   ├── ck_universal_gemm_template.meta.json
│   │   │   │   │   │   ├── compile_command.data.json
│   │   │   │   │   │   ├── compile_command.meta.json
│   │   │   │   │   │   ├── rocm_benchmark_request.data.json
│   │   │   │   │   │   ├── rocm_benchmark_request.meta.json
│   │   │   │   │   │   ├── rocm_cpp_scheduling.data.json
│   │   │   │   │   │   ├── rocm_cpp_scheduling.meta.json
│   │   │   │   │   │   ├── rocm_kernel.data.json
│   │   │   │   │   │   ├── rocm_kernel.meta.json
│   │   │   │   │   │   ├── rocm_template.data.json
│   │   │   │   │   │   ├── rocm_template.meta.json
│   │   │   │   │   │   ├── rocm_template_buffer.data.json
│   │   │   │   │   │   ├── rocm_template_buffer.meta.json
│   │   │   │   │   │   ├── rocm_utils.data.json
│   │   │   │   │   │   └── rocm_utils.meta.json
│   │   │   │   │   ├── simd.data.json
│   │   │   │   │   ├── simd.meta.json
│   │   │   │   │   ├── simd_kernel_features.data.json
│   │   │   │   │   ├── simd_kernel_features.meta.json
│   │   │   │   │   ├── subgraph.data.json
│   │   │   │   │   ├── subgraph.meta.json
│   │   │   │   │   ├── triton.data.json
│   │   │   │   │   ├── triton.meta.json
│   │   │   │   │   ├── triton_combo_kernel.data.json
│   │   │   │   │   ├── triton_combo_kernel.meta.json
│   │   │   │   │   ├── triton_split_scan.data.json
│   │   │   │   │   ├── triton_split_scan.meta.json
│   │   │   │   │   ├── triton_utils.data.json
│   │   │   │   │   ├── triton_utils.meta.json
│   │   │   │   │   ├── wrapper.data.json
│   │   │   │   │   ├── wrapper.meta.json
│   │   │   │   │   ├── wrapper_fxir.data.json
│   │   │   │   │   └── wrapper_fxir.meta.json
│   │   │   │   ├── comm_analysis.data.json
│   │   │   │   ├── comm_analysis.meta.json
│   │   │   │   ├── comm_lowering.data.json
│   │   │   │   ├── comm_lowering.meta.json
│   │   │   │   ├── comms.data.json
│   │   │   │   ├── comms.meta.json
│   │   │   │   ├── compile_fx.data.json
│   │   │   │   ├── compile_fx.meta.json
│   │   │   │   ├── compile_worker
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── subproc_pool.data.json
│   │   │   │   │   ├── subproc_pool.meta.json
│   │   │   │   │   ├── tracked_process_pool.data.json
│   │   │   │   │   ├── tracked_process_pool.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   ├── compiler_bisector.data.json
│   │   │   │   ├── compiler_bisector.meta.json
│   │   │   │   ├── config.data.json
│   │   │   │   ├── config.meta.json
│   │   │   │   ├── constant_folding.data.json
│   │   │   │   ├── constant_folding.meta.json
│   │   │   │   ├── cpp_builder.data.json
│   │   │   │   ├── cpp_builder.meta.json
│   │   │   │   ├── cpu_vec_isa.data.json
│   │   │   │   ├── cpu_vec_isa.meta.json
│   │   │   │   ├── cudagraph_trees.data.json
│   │   │   │   ├── cudagraph_trees.meta.json
│   │   │   │   ├── cudagraph_utils.data.json
│   │   │   │   ├── cudagraph_utils.meta.json
│   │   │   │   ├── custom_graph_pass.data.json
│   │   │   │   ├── custom_graph_pass.meta.json
│   │   │   │   ├── debug.data.json
│   │   │   │   ├── debug.meta.json
│   │   │   │   ├── decomposition.data.json
│   │   │   │   ├── decomposition.meta.json
│   │   │   │   ├── dependencies.data.json
│   │   │   │   ├── dependencies.meta.json
│   │   │   │   ├── dtype_propagation.data.json
│   │   │   │   ├── dtype_propagation.meta.json
│   │   │   │   ├── exc.data.json
│   │   │   │   ├── exc.meta.json
│   │   │   │   ├── extern_node_serializer.data.json
│   │   │   │   ├── extern_node_serializer.meta.json
│   │   │   │   ├── freezing_utils.data.json
│   │   │   │   ├── freezing_utils.meta.json
│   │   │   │   ├── fx_passes
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── b2b_gemm.data.json
│   │   │   │   │   ├── b2b_gemm.meta.json
│   │   │   │   │   ├── ddp_fusion.data.json
│   │   │   │   │   ├── ddp_fusion.meta.json
│   │   │   │   │   ├── decompose_mem_bound_mm.data.json
│   │   │   │   │   ├── decompose_mem_bound_mm.meta.json
│   │   │   │   │   ├── dedupe_symint_uses.data.json
│   │   │   │   │   ├── dedupe_symint_uses.meta.json
│   │   │   │   │   ├── group_batch_fusion.data.json
│   │   │   │   │   ├── group_batch_fusion.meta.json
│   │   │   │   │   ├── joint_graph.data.json
│   │   │   │   │   ├── joint_graph.meta.json
│   │   │   │   │   ├── micro_pipeline_tp.data.json
│   │   │   │   │   ├── micro_pipeline_tp.meta.json
│   │   │   │   │   ├── misc_patterns.data.json
│   │   │   │   │   ├── misc_patterns.meta.json
│   │   │   │   │   ├── post_grad.data.json
│   │   │   │   │   ├── post_grad.meta.json
│   │   │   │   │   ├── pre_grad.data.json
│   │   │   │   │   ├── pre_grad.meta.json
│   │   │   │   │   ├── reinplace.data.json
│   │   │   │   │   ├── reinplace.meta.json
│   │   │   │   │   ├── replace_random.data.json
│   │   │   │   │   ├── replace_random.meta.json
│   │   │   │   │   ├── split_cat.data.json
│   │   │   │   │   └── split_cat.meta.json
│   │   │   │   ├── fx_utils.data.json
│   │   │   │   ├── fx_utils.meta.json
│   │   │   │   ├── graph.data.json
│   │   │   │   ├── graph.meta.json
│   │   │   │   ├── index_propagation.data.json
│   │   │   │   ├── index_propagation.meta.json
│   │   │   │   ├── inductor_prims.data.json
│   │   │   │   ├── inductor_prims.meta.json
│   │   │   │   ├── ir.data.json
│   │   │   │   ├── ir.meta.json
│   │   │   │   ├── jagged_lowerings.data.json
│   │   │   │   ├── jagged_lowerings.meta.json
│   │   │   │   ├── kernel
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── mm.data.json
│   │   │   │   │   ├── mm.meta.json
│   │   │   │   │   ├── mm_common.data.json
│   │   │   │   │   ├── mm_common.meta.json
│   │   │   │   │   ├── mm_plus_mm.data.json
│   │   │   │   │   └── mm_plus_mm.meta.json
│   │   │   │   ├── loop_body.data.json
│   │   │   │   ├── loop_body.meta.json
│   │   │   │   ├── lowering.data.json
│   │   │   │   ├── lowering.meta.json
│   │   │   │   ├── memory.data.json
│   │   │   │   ├── memory.meta.json
│   │   │   │   ├── metrics.data.json
│   │   │   │   ├── metrics.meta.json
│   │   │   │   ├── mkldnn_ir.data.json
│   │   │   │   ├── mkldnn_ir.meta.json
│   │   │   │   ├── mkldnn_lowerings.data.json
│   │   │   │   ├── mkldnn_lowerings.meta.json
│   │   │   │   ├── ops_handler.data.json
│   │   │   │   ├── ops_handler.meta.json
│   │   │   │   ├── optimize_indexing.data.json
│   │   │   │   ├── optimize_indexing.meta.json
│   │   │   │   ├── output_code.data.json
│   │   │   │   ├── output_code.meta.json
│   │   │   │   ├── package
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── package.data.json
│   │   │   │   │   └── package.meta.json
│   │   │   │   ├── pattern_matcher.data.json
│   │   │   │   ├── pattern_matcher.meta.json
│   │   │   │   ├── quantized_lowerings.data.json
│   │   │   │   ├── quantized_lowerings.meta.json
│   │   │   │   ├── remote_cache.data.json
│   │   │   │   ├── remote_cache.meta.json
│   │   │   │   ├── runtime
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── autotune_cache.data.json
│   │   │   │   │   ├── autotune_cache.meta.json
│   │   │   │   │   ├── benchmarking.data.json
│   │   │   │   │   ├── benchmarking.meta.json
│   │   │   │   │   ├── cache_dir_utils.data.json
│   │   │   │   │   ├── cache_dir_utils.meta.json
│   │   │   │   │   ├── compile_tasks.data.json
│   │   │   │   │   ├── compile_tasks.meta.json
│   │   │   │   │   ├── coordinate_descent_tuner.data.json
│   │   │   │   │   ├── coordinate_descent_tuner.meta.json
│   │   │   │   │   ├── hints.data.json
│   │   │   │   │   ├── hints.meta.json
│   │   │   │   │   ├── runtime_utils.data.json
│   │   │   │   │   ├── runtime_utils.meta.json
│   │   │   │   │   ├── static_cuda_launcher.data.json
│   │   │   │   │   ├── static_cuda_launcher.meta.json
│   │   │   │   │   ├── triton_compat.data.json
│   │   │   │   │   ├── triton_compat.meta.json
│   │   │   │   │   ├── triton_helpers.data.json
│   │   │   │   │   ├── triton_helpers.meta.json
│   │   │   │   │   ├── triton_heuristics.data.json
│   │   │   │   │   └── triton_heuristics.meta.json
│   │   │   │   ├── scheduler.data.json
│   │   │   │   ├── scheduler.meta.json
│   │   │   │   ├── select_algorithm.data.json
│   │   │   │   ├── select_algorithm.meta.json
│   │   │   │   ├── sizevars.data.json
│   │   │   │   ├── sizevars.meta.json
│   │   │   │   ├── standalone_compile.data.json
│   │   │   │   ├── standalone_compile.meta.json
│   │   │   │   ├── template_heuristics.data.json
│   │   │   │   ├── template_heuristics.meta.json
│   │   │   │   ├── test_operators.data.json
│   │   │   │   ├── test_operators.meta.json
│   │   │   │   ├── tiling_utils.data.json
│   │   │   │   ├── tiling_utils.meta.json
│   │   │   │   ├── triton_bundler.data.json
│   │   │   │   ├── triton_bundler.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   ├── utils.meta.json
│   │   │   │   ├── virtualized.data.json
│   │   │   │   ├── virtualized.meta.json
│   │   │   │   ├── wrapper_benchmark.data.json
│   │   │   │   └── wrapper_benchmark.meta.json
│   │   │   ├── _jit_internal.data.json
│   │   │   ├── _jit_internal.meta.json
│   │   │   ├── _library
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── autograd.data.json
│   │   │   │   ├── autograd.meta.json
│   │   │   │   ├── custom_ops.data.json
│   │   │   │   ├── custom_ops.meta.json
│   │   │   │   ├── fake_class_registry.data.json
│   │   │   │   ├── fake_class_registry.meta.json
│   │   │   │   ├── fake_impl.data.json
│   │   │   │   ├── fake_impl.meta.json
│   │   │   │   ├── fake_profile.data.json
│   │   │   │   ├── fake_profile.meta.json
│   │   │   │   ├── infer_schema.data.json
│   │   │   │   ├── infer_schema.meta.json
│   │   │   │   ├── simple_registry.data.json
│   │   │   │   ├── simple_registry.meta.json
│   │   │   │   ├── triton.data.json
│   │   │   │   ├── triton.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── _linalg_utils.data.json
│   │   │   ├── _linalg_utils.meta.json
│   │   │   ├── _lobpcg.data.json
│   │   │   ├── _lobpcg.meta.json
│   │   │   ├── _logging
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _internal.data.json
│   │   │   │   ├── _internal.meta.json
│   │   │   │   ├── _registrations.data.json
│   │   │   │   ├── _registrations.meta.json
│   │   │   │   ├── structured.data.json
│   │   │   │   └── structured.meta.json
│   │   │   ├── _lowrank.data.json
│   │   │   ├── _lowrank.meta.json
│   │   │   ├── _meta_registrations.data.json
│   │   │   ├── _meta_registrations.meta.json
│   │   │   ├── _namedtensor_internals.data.json
│   │   │   ├── _namedtensor_internals.meta.json
│   │   │   ├── _numpy
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _binary_ufuncs_impl.data.json
│   │   │   │   ├── _binary_ufuncs_impl.meta.json
│   │   │   │   ├── _casting_dicts.data.json
│   │   │   │   ├── _casting_dicts.meta.json
│   │   │   │   ├── _dtypes.data.json
│   │   │   │   ├── _dtypes.meta.json
│   │   │   │   ├── _dtypes_impl.data.json
│   │   │   │   ├── _dtypes_impl.meta.json
│   │   │   │   ├── _funcs.data.json
│   │   │   │   ├── _funcs.meta.json
│   │   │   │   ├── _funcs_impl.data.json
│   │   │   │   ├── _funcs_impl.meta.json
│   │   │   │   ├── _getlimits.data.json
│   │   │   │   ├── _getlimits.meta.json
│   │   │   │   ├── _ndarray.data.json
│   │   │   │   ├── _ndarray.meta.json
│   │   │   │   ├── _normalizations.data.json
│   │   │   │   ├── _normalizations.meta.json
│   │   │   │   ├── _reductions_impl.data.json
│   │   │   │   ├── _reductions_impl.meta.json
│   │   │   │   ├── _ufuncs.data.json
│   │   │   │   ├── _ufuncs.meta.json
│   │   │   │   ├── _unary_ufuncs_impl.data.json
│   │   │   │   ├── _unary_ufuncs_impl.meta.json
│   │   │   │   ├── _util.data.json
│   │   │   │   ├── _util.meta.json
│   │   │   │   ├── fft.data.json
│   │   │   │   ├── fft.meta.json
│   │   │   │   ├── linalg.data.json
│   │   │   │   ├── linalg.meta.json
│   │   │   │   ├── random.data.json
│   │   │   │   └── random.meta.json
│   │   │   ├── _ops.data.json
│   │   │   ├── _ops.meta.json
│   │   │   ├── _prims
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── context.data.json
│   │   │   │   ├── context.meta.json
│   │   │   │   ├── debug_prims.data.json
│   │   │   │   ├── debug_prims.meta.json
│   │   │   │   ├── executor.data.json
│   │   │   │   ├── executor.meta.json
│   │   │   │   ├── rng_prims.data.json
│   │   │   │   └── rng_prims.meta.json
│   │   │   ├── _prims_common
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── wrappers.data.json
│   │   │   │   └── wrappers.meta.json
│   │   │   ├── _refs
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _conversions.data.json
│   │   │   │   ├── _conversions.meta.json
│   │   │   │   ├── fft.data.json
│   │   │   │   ├── fft.meta.json
│   │   │   │   ├── linalg
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── nn
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   └── functional
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       └── __init__.meta.json
│   │   │   │   └── special
│   │   │   │       ├── __init__.data.json
│   │   │   │       └── __init__.meta.json
│   │   │   ├── _size_docs.data.json
│   │   │   ├── _size_docs.meta.json
│   │   │   ├── _sources.data.json
│   │   │   ├── _sources.meta.json
│   │   │   ├── _storage_docs.data.json
│   │   │   ├── _storage_docs.meta.json
│   │   │   ├── _strobelight
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── cli_function_profiler.data.json
│   │   │   │   ├── cli_function_profiler.meta.json
│   │   │   │   ├── compile_time_profiler.data.json
│   │   │   │   └── compile_time_profiler.meta.json
│   │   │   ├── _subclasses
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _fake_tensor_utils.data.json
│   │   │   │   ├── _fake_tensor_utils.meta.json
│   │   │   │   ├── fake_impls.data.json
│   │   │   │   ├── fake_impls.meta.json
│   │   │   │   ├── fake_tensor.data.json
│   │   │   │   ├── fake_tensor.meta.json
│   │   │   │   ├── fake_utils.data.json
│   │   │   │   ├── fake_utils.meta.json
│   │   │   │   ├── functional_tensor.data.json
│   │   │   │   ├── functional_tensor.meta.json
│   │   │   │   ├── meta_utils.data.json
│   │   │   │   └── meta_utils.meta.json
│   │   │   ├── _tensor.data.json
│   │   │   ├── _tensor.meta.json
│   │   │   ├── _tensor_docs.data.json
│   │   │   ├── _tensor_docs.meta.json
│   │   │   ├── _tensor_str.data.json
│   │   │   ├── _tensor_str.meta.json
│   │   │   ├── _thread_safe_fork.data.json
│   │   │   ├── _thread_safe_fork.meta.json
│   │   │   ├── _torch_docs.data.json
│   │   │   ├── _torch_docs.meta.json
│   │   │   ├── _utils.data.json
│   │   │   ├── _utils.meta.json
│   │   │   ├── _utils_internal.data.json
│   │   │   ├── _utils_internal.meta.json
│   │   │   ├── _vendor
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   └── packaging
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── _structures.data.json
│   │   │   │       ├── _structures.meta.json
│   │   │   │       ├── version.data.json
│   │   │   │       └── version.meta.json
│   │   │   ├── _vmap_internals.data.json
│   │   │   ├── _vmap_internals.meta.json
│   │   │   ├── _weights_only_unpickler.data.json
│   │   │   ├── _weights_only_unpickler.meta.json
│   │   │   ├── accelerator
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _utils.data.json
│   │   │   │   └── _utils.meta.json
│   │   │   ├── amp
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── autocast_mode.data.json
│   │   │   │   ├── autocast_mode.meta.json
│   │   │   │   ├── grad_scaler.data.json
│   │   │   │   └── grad_scaler.meta.json
│   │   │   ├── ao
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── nn
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── intrinsic
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── modules
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── fused.data.json
│   │   │   │   │   │   │   └── fused.meta.json
│   │   │   │   │   │   ├── qat
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   └── modules
│   │   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │   │       ├── conv_fused.data.json
│   │   │   │   │   │   │       ├── conv_fused.meta.json
│   │   │   │   │   │   │       ├── linear_fused.data.json
│   │   │   │   │   │   │       ├── linear_fused.meta.json
│   │   │   │   │   │   │       ├── linear_relu.data.json
│   │   │   │   │   │   │       └── linear_relu.meta.json
│   │   │   │   │   │   └── quantized
│   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │       ├── dynamic
│   │   │   │   │   │       │   ├── __init__.data.json
│   │   │   │   │   │       │   ├── __init__.meta.json
│   │   │   │   │   │       │   └── modules
│   │   │   │   │   │       │       ├── __init__.data.json
│   │   │   │   │   │       │       ├── __init__.meta.json
│   │   │   │   │   │       │       ├── linear_relu.data.json
│   │   │   │   │   │       │       └── linear_relu.meta.json
│   │   │   │   │   │       └── modules
│   │   │   │   │   │           ├── __init__.data.json
│   │   │   │   │   │           ├── __init__.meta.json
│   │   │   │   │   │           ├── bn_relu.data.json
│   │   │   │   │   │           ├── bn_relu.meta.json
│   │   │   │   │   │           ├── conv_add.data.json
│   │   │   │   │   │           ├── conv_add.meta.json
│   │   │   │   │   │           ├── conv_relu.data.json
│   │   │   │   │   │           ├── conv_relu.meta.json
│   │   │   │   │   │           ├── linear_relu.data.json
│   │   │   │   │   │           └── linear_relu.meta.json
│   │   │   │   │   ├── qat
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── dynamic
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   └── modules
│   │   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │   │       ├── linear.data.json
│   │   │   │   │   │   │       └── linear.meta.json
│   │   │   │   │   │   └── modules
│   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │       ├── conv.data.json
│   │   │   │   │   │       ├── conv.meta.json
│   │   │   │   │   │       ├── embedding_ops.data.json
│   │   │   │   │   │       ├── embedding_ops.meta.json
│   │   │   │   │   │       ├── linear.data.json
│   │   │   │   │   │       └── linear.meta.json
│   │   │   │   │   ├── quantizable
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   └── modules
│   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │       ├── activation.data.json
│   │   │   │   │   │       ├── activation.meta.json
│   │   │   │   │   │       ├── rnn.data.json
│   │   │   │   │   │       └── rnn.meta.json
│   │   │   │   │   ├── quantized
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── dynamic
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   └── modules
│   │   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │   │       ├── conv.data.json
│   │   │   │   │   │   │       ├── conv.meta.json
│   │   │   │   │   │   │       ├── linear.data.json
│   │   │   │   │   │   │       ├── linear.meta.json
│   │   │   │   │   │   │       ├── rnn.data.json
│   │   │   │   │   │   │       └── rnn.meta.json
│   │   │   │   │   │   ├── functional.data.json
│   │   │   │   │   │   ├── functional.meta.json
│   │   │   │   │   │   ├── modules
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── activation.data.json
│   │   │   │   │   │   │   ├── activation.meta.json
│   │   │   │   │   │   │   ├── batchnorm.data.json
│   │   │   │   │   │   │   ├── batchnorm.meta.json
│   │   │   │   │   │   │   ├── conv.data.json
│   │   │   │   │   │   │   ├── conv.meta.json
│   │   │   │   │   │   │   ├── dropout.data.json
│   │   │   │   │   │   │   ├── dropout.meta.json
│   │   │   │   │   │   │   ├── embedding_ops.data.json
│   │   │   │   │   │   │   ├── embedding_ops.meta.json
│   │   │   │   │   │   │   ├── functional_modules.data.json
│   │   │   │   │   │   │   ├── functional_modules.meta.json
│   │   │   │   │   │   │   ├── linear.data.json
│   │   │   │   │   │   │   ├── linear.meta.json
│   │   │   │   │   │   │   ├── normalization.data.json
│   │   │   │   │   │   │   ├── normalization.meta.json
│   │   │   │   │   │   │   ├── rnn.data.json
│   │   │   │   │   │   │   ├── rnn.meta.json
│   │   │   │   │   │   │   ├── utils.data.json
│   │   │   │   │   │   │   └── utils.meta.json
│   │   │   │   │   │   └── reference
│   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │       └── modules
│   │   │   │   │   │           ├── __init__.data.json
│   │   │   │   │   │           ├── __init__.meta.json
│   │   │   │   │   │           ├── conv.data.json
│   │   │   │   │   │           ├── conv.meta.json
│   │   │   │   │   │           ├── linear.data.json
│   │   │   │   │   │           ├── linear.meta.json
│   │   │   │   │   │           ├── rnn.data.json
│   │   │   │   │   │           ├── rnn.meta.json
│   │   │   │   │   │           ├── sparse.data.json
│   │   │   │   │   │           ├── sparse.meta.json
│   │   │   │   │   │           ├── utils.data.json
│   │   │   │   │   │           └── utils.meta.json
│   │   │   │   │   └── sparse
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       └── quantized
│   │   │   │   │           ├── __init__.data.json
│   │   │   │   │           ├── __init__.meta.json
│   │   │   │   │           ├── dynamic
│   │   │   │   │           │   ├── __init__.data.json
│   │   │   │   │           │   ├── __init__.meta.json
│   │   │   │   │           │   ├── linear.data.json
│   │   │   │   │           │   └── linear.meta.json
│   │   │   │   │           ├── linear.data.json
│   │   │   │   │           ├── linear.meta.json
│   │   │   │   │           ├── utils.data.json
│   │   │   │   │           └── utils.meta.json
│   │   │   │   ├── ns
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   └── fx
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── ns_types.data.json
│   │   │   │   │       ├── ns_types.meta.json
│   │   │   │   │       ├── utils.data.json
│   │   │   │   │       └── utils.meta.json
│   │   │   │   ├── pruning
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _mappings.data.json
│   │   │   │   │   ├── _mappings.meta.json
│   │   │   │   │   ├── scheduler
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── base_scheduler.data.json
│   │   │   │   │   │   ├── base_scheduler.meta.json
│   │   │   │   │   │   ├── cubic_scheduler.data.json
│   │   │   │   │   │   ├── cubic_scheduler.meta.json
│   │   │   │   │   │   ├── lambda_scheduler.data.json
│   │   │   │   │   │   └── lambda_scheduler.meta.json
│   │   │   │   │   └── sparsifier
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── base_sparsifier.data.json
│   │   │   │   │       ├── base_sparsifier.meta.json
│   │   │   │   │       ├── nearly_diagonal_sparsifier.data.json
│   │   │   │   │       ├── nearly_diagonal_sparsifier.meta.json
│   │   │   │   │       ├── utils.data.json
│   │   │   │   │       ├── utils.meta.json
│   │   │   │   │       ├── weight_norm_sparsifier.data.json
│   │   │   │   │       └── weight_norm_sparsifier.meta.json
│   │   │   │   └── quantization
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── backend_config
│   │   │   │       │   ├── __init__.data.json
│   │   │   │       │   ├── __init__.meta.json
│   │   │   │       │   ├── _common_operator_config_utils.data.json
│   │   │   │       │   ├── _common_operator_config_utils.meta.json
│   │   │   │       │   ├── backend_config.data.json
│   │   │   │       │   ├── backend_config.meta.json
│   │   │   │       │   ├── executorch.data.json
│   │   │   │       │   ├── executorch.meta.json
│   │   │   │       │   ├── fbgemm.data.json
│   │   │   │       │   ├── fbgemm.meta.json
│   │   │   │       │   ├── native.data.json
│   │   │   │       │   ├── native.meta.json
│   │   │   │       │   ├── onednn.data.json
│   │   │   │       │   ├── onednn.meta.json
│   │   │   │       │   ├── qnnpack.data.json
│   │   │   │       │   ├── qnnpack.meta.json
│   │   │   │       │   ├── tensorrt.data.json
│   │   │   │       │   ├── tensorrt.meta.json
│   │   │   │       │   ├── utils.data.json
│   │   │   │       │   └── utils.meta.json
│   │   │   │       ├── fake_quantize.data.json
│   │   │   │       ├── fake_quantize.meta.json
│   │   │   │       ├── fuse_modules.data.json
│   │   │   │       ├── fuse_modules.meta.json
│   │   │   │       ├── fuser_method_mappings.data.json
│   │   │   │       ├── fuser_method_mappings.meta.json
│   │   │   │       ├── fx
│   │   │   │       │   ├── __init__.data.json
│   │   │   │       │   ├── __init__.meta.json
│   │   │   │       │   ├── _decomposed.data.json
│   │   │   │       │   ├── _decomposed.meta.json
│   │   │   │       │   ├── _equalize.data.json
│   │   │   │       │   ├── _equalize.meta.json
│   │   │   │       │   ├── _lower_to_native_backend.data.json
│   │   │   │       │   ├── _lower_to_native_backend.meta.json
│   │   │   │       │   ├── convert.data.json
│   │   │   │       │   ├── convert.meta.json
│   │   │   │       │   ├── custom_config.data.json
│   │   │   │       │   ├── custom_config.meta.json
│   │   │   │       │   ├── fuse.data.json
│   │   │   │       │   ├── fuse.meta.json
│   │   │   │       │   ├── fuse_handler.data.json
│   │   │   │       │   ├── fuse_handler.meta.json
│   │   │   │       │   ├── graph_module.data.json
│   │   │   │       │   ├── graph_module.meta.json
│   │   │   │       │   ├── lower_to_fbgemm.data.json
│   │   │   │       │   ├── lower_to_fbgemm.meta.json
│   │   │   │       │   ├── match_utils.data.json
│   │   │   │       │   ├── match_utils.meta.json
│   │   │   │       │   ├── pattern_utils.data.json
│   │   │   │       │   ├── pattern_utils.meta.json
│   │   │   │       │   ├── prepare.data.json
│   │   │   │       │   ├── prepare.meta.json
│   │   │   │       │   ├── qconfig_mapping_utils.data.json
│   │   │   │       │   ├── qconfig_mapping_utils.meta.json
│   │   │   │       │   ├── quantize_handler.data.json
│   │   │   │       │   ├── quantize_handler.meta.json
│   │   │   │       │   ├── utils.data.json
│   │   │   │       │   └── utils.meta.json
│   │   │   │       ├── observer.data.json
│   │   │   │       ├── observer.meta.json
│   │   │   │       ├── pt2e
│   │   │   │       │   ├── __init__.data.json
│   │   │   │       │   ├── __init__.meta.json
│   │   │   │       │   ├── _numeric_debugger.data.json
│   │   │   │       │   ├── _numeric_debugger.meta.json
│   │   │   │       │   ├── export_utils.data.json
│   │   │   │       │   ├── export_utils.meta.json
│   │   │   │       │   ├── graph_utils.data.json
│   │   │   │       │   └── graph_utils.meta.json
│   │   │   │       ├── qconfig.data.json
│   │   │   │       ├── qconfig.meta.json
│   │   │   │       ├── qconfig_mapping.data.json
│   │   │   │       ├── qconfig_mapping.meta.json
│   │   │   │       ├── quant_type.data.json
│   │   │   │       ├── quant_type.meta.json
│   │   │   │       ├── quantization_mappings.data.json
│   │   │   │       ├── quantization_mappings.meta.json
│   │   │   │       ├── quantize.data.json
│   │   │   │       ├── quantize.meta.json
│   │   │   │       ├── quantize_jit.data.json
│   │   │   │       ├── quantize_jit.meta.json
│   │   │   │       ├── quantizer
│   │   │   │       │   ├── __init__.data.json
│   │   │   │       │   ├── __init__.meta.json
│   │   │   │       │   ├── quantizer.data.json
│   │   │   │       │   └── quantizer.meta.json
│   │   │   │       ├── stubs.data.json
│   │   │   │       ├── stubs.meta.json
│   │   │   │       ├── utils.data.json
│   │   │   │       └── utils.meta.json
│   │   │   ├── autograd
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _functions
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tensor.data.json
│   │   │   │   │   └── tensor.meta.json
│   │   │   │   ├── anomaly_mode.data.json
│   │   │   │   ├── anomaly_mode.meta.json
│   │   │   │   ├── forward_ad.data.json
│   │   │   │   ├── forward_ad.meta.json
│   │   │   │   ├── function.data.json
│   │   │   │   ├── function.meta.json
│   │   │   │   ├── functional.data.json
│   │   │   │   ├── functional.meta.json
│   │   │   │   ├── grad_mode.data.json
│   │   │   │   ├── grad_mode.meta.json
│   │   │   │   ├── gradcheck.data.json
│   │   │   │   ├── gradcheck.meta.json
│   │   │   │   ├── graph.data.json
│   │   │   │   ├── graph.meta.json
│   │   │   │   ├── profiler.data.json
│   │   │   │   ├── profiler.meta.json
│   │   │   │   ├── profiler_legacy.data.json
│   │   │   │   ├── profiler_legacy.meta.json
│   │   │   │   ├── profiler_util.data.json
│   │   │   │   ├── profiler_util.meta.json
│   │   │   │   ├── variable.data.json
│   │   │   │   └── variable.meta.json
│   │   │   ├── backends
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── cpu
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── cuda
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── cudnn
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── rnn.data.json
│   │   │   │   │   └── rnn.meta.json
│   │   │   │   ├── cusparselt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── kleidiai
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── mha
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── mkl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── mkldnn
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── mps
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── nnpack
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── openmp
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   └── quantized
│   │   │   │       ├── __init__.data.json
│   │   │   │       └── __init__.meta.json
│   │   │   ├── compiler
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _cache.data.json
│   │   │   │   ├── _cache.meta.json
│   │   │   │   ├── config.data.json
│   │   │   │   └── config.meta.json
│   │   │   ├── cpu
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   └── amp
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── autocast_mode.data.json
│   │   │   │       ├── autocast_mode.meta.json
│   │   │   │       ├── grad_scaler.data.json
│   │   │   │       └── grad_scaler.meta.json
│   │   │   ├── cuda
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _gpu_trace.data.json
│   │   │   │   ├── _gpu_trace.meta.json
│   │   │   │   ├── _memory_viz.data.json
│   │   │   │   ├── _memory_viz.meta.json
│   │   │   │   ├── _pin_memory_utils.data.json
│   │   │   │   ├── _pin_memory_utils.meta.json
│   │   │   │   ├── _sanitizer.data.json
│   │   │   │   ├── _sanitizer.meta.json
│   │   │   │   ├── _utils.data.json
│   │   │   │   ├── _utils.meta.json
│   │   │   │   ├── amp
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── autocast_mode.data.json
│   │   │   │   │   ├── autocast_mode.meta.json
│   │   │   │   │   ├── common.data.json
│   │   │   │   │   ├── common.meta.json
│   │   │   │   │   ├── grad_scaler.data.json
│   │   │   │   │   └── grad_scaler.meta.json
│   │   │   │   ├── gds.data.json
│   │   │   │   ├── gds.meta.json
│   │   │   │   ├── graphs.data.json
│   │   │   │   ├── graphs.meta.json
│   │   │   │   ├── jiterator.data.json
│   │   │   │   ├── jiterator.meta.json
│   │   │   │   ├── memory.data.json
│   │   │   │   ├── memory.meta.json
│   │   │   │   ├── nccl.data.json
│   │   │   │   ├── nccl.meta.json
│   │   │   │   ├── nvtx.data.json
│   │   │   │   ├── nvtx.meta.json
│   │   │   │   ├── profiler.data.json
│   │   │   │   ├── profiler.meta.json
│   │   │   │   ├── random.data.json
│   │   │   │   ├── random.meta.json
│   │   │   │   ├── sparse.data.json
│   │   │   │   ├── sparse.meta.json
│   │   │   │   ├── streams.data.json
│   │   │   │   ├── streams.meta.json
│   │   │   │   ├── tunable.data.json
│   │   │   │   └── tunable.meta.json
│   │   │   ├── distributed
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _composable
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── checkpoint_activation.data.json
│   │   │   │   │   ├── checkpoint_activation.meta.json
│   │   │   │   │   ├── contract.data.json
│   │   │   │   │   ├── contract.meta.json
│   │   │   │   │   ├── replicate.data.json
│   │   │   │   │   └── replicate.meta.json
│   │   │   │   ├── _composable_state.data.json
│   │   │   │   ├── _composable_state.meta.json
│   │   │   │   ├── _functional_collectives.data.json
│   │   │   │   ├── _functional_collectives.meta.json
│   │   │   │   ├── _functional_collectives_impl.data.json
│   │   │   │   ├── _functional_collectives_impl.meta.json
│   │   │   │   ├── _shard
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _utils.data.json
│   │   │   │   │   ├── _utils.meta.json
│   │   │   │   │   ├── api.data.json
│   │   │   │   │   ├── api.meta.json
│   │   │   │   │   ├── common_op_utils.data.json
│   │   │   │   │   ├── common_op_utils.meta.json
│   │   │   │   │   ├── metadata.data.json
│   │   │   │   │   ├── metadata.meta.json
│   │   │   │   │   ├── op_registry_utils.data.json
│   │   │   │   │   ├── op_registry_utils.meta.json
│   │   │   │   │   ├── sharded_tensor
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── _ops
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── _common.data.json
│   │   │   │   │   │   │   ├── _common.meta.json
│   │   │   │   │   │   │   ├── binary_cmp.data.json
│   │   │   │   │   │   │   ├── binary_cmp.meta.json
│   │   │   │   │   │   │   ├── init.data.json
│   │   │   │   │   │   │   ├── init.meta.json
│   │   │   │   │   │   │   ├── misc_ops.data.json
│   │   │   │   │   │   │   ├── misc_ops.meta.json
│   │   │   │   │   │   │   ├── tensor_ops.data.json
│   │   │   │   │   │   │   └── tensor_ops.meta.json
│   │   │   │   │   │   ├── api.data.json
│   │   │   │   │   │   ├── api.meta.json
│   │   │   │   │   │   ├── metadata.data.json
│   │   │   │   │   │   ├── metadata.meta.json
│   │   │   │   │   │   ├── reshard.data.json
│   │   │   │   │   │   ├── reshard.meta.json
│   │   │   │   │   │   ├── shard.data.json
│   │   │   │   │   │   ├── shard.meta.json
│   │   │   │   │   │   ├── utils.data.json
│   │   │   │   │   │   └── utils.meta.json
│   │   │   │   │   ├── sharder.data.json
│   │   │   │   │   ├── sharder.meta.json
│   │   │   │   │   ├── sharding_plan
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── api.data.json
│   │   │   │   │   │   └── api.meta.json
│   │   │   │   │   └── sharding_spec
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── _internals.data.json
│   │   │   │   │       ├── _internals.meta.json
│   │   │   │   │       ├── api.data.json
│   │   │   │   │       ├── api.meta.json
│   │   │   │   │       ├── chunk_sharding_spec.data.json
│   │   │   │   │       ├── chunk_sharding_spec.meta.json
│   │   │   │   │       └── chunk_sharding_spec_ops
│   │   │   │   │           ├── __init__.data.json
│   │   │   │   │           ├── __init__.meta.json
│   │   │   │   │           ├── _common.data.json
│   │   │   │   │           ├── _common.meta.json
│   │   │   │   │           ├── embedding.data.json
│   │   │   │   │           ├── embedding.meta.json
│   │   │   │   │           ├── embedding_bag.data.json
│   │   │   │   │           └── embedding_bag.meta.json
│   │   │   │   ├── _state_dict_utils.data.json
│   │   │   │   ├── _state_dict_utils.meta.json
│   │   │   │   ├── algorithms
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _checkpoint
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── checkpoint_wrapper.data.json
│   │   │   │   │   │   └── checkpoint_wrapper.meta.json
│   │   │   │   │   ├── _comm_hooks
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── default_hooks.data.json
│   │   │   │   │   │   └── default_hooks.meta.json
│   │   │   │   │   ├── _optimizer_overlap
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── optimizer_overlap.data.json
│   │   │   │   │   │   └── optimizer_overlap.meta.json
│   │   │   │   │   ├── ddp_comm_hooks
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── debugging_hooks.data.json
│   │   │   │   │   │   ├── debugging_hooks.meta.json
│   │   │   │   │   │   ├── default_hooks.data.json
│   │   │   │   │   │   ├── default_hooks.meta.json
│   │   │   │   │   │   ├── mixed_precision_hooks.data.json
│   │   │   │   │   │   ├── mixed_precision_hooks.meta.json
│   │   │   │   │   │   ├── optimizer_overlap_hooks.data.json
│   │   │   │   │   │   ├── optimizer_overlap_hooks.meta.json
│   │   │   │   │   │   ├── powerSGD_hook.data.json
│   │   │   │   │   │   ├── powerSGD_hook.meta.json
│   │   │   │   │   │   ├── quantization_hooks.data.json
│   │   │   │   │   │   └── quantization_hooks.meta.json
│   │   │   │   │   ├── join.data.json
│   │   │   │   │   ├── join.meta.json
│   │   │   │   │   └── model_averaging
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── averagers.data.json
│   │   │   │   │       ├── averagers.meta.json
│   │   │   │   │       ├── utils.data.json
│   │   │   │   │       └── utils.meta.json
│   │   │   │   ├── autograd
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── c10d_logger.data.json
│   │   │   │   ├── c10d_logger.meta.json
│   │   │   │   ├── checkpoint
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _async_executor.data.json
│   │   │   │   │   ├── _async_executor.meta.json
│   │   │   │   │   ├── _async_process_executor.data.json
│   │   │   │   │   ├── _async_process_executor.meta.json
│   │   │   │   │   ├── _async_thread_executor.data.json
│   │   │   │   │   ├── _async_thread_executor.meta.json
│   │   │   │   │   ├── _dedup_save_plans.data.json
│   │   │   │   │   ├── _dedup_save_plans.meta.json
│   │   │   │   │   ├── _extension.data.json
│   │   │   │   │   ├── _extension.meta.json
│   │   │   │   │   ├── _fsspec_filesystem.data.json
│   │   │   │   │   ├── _fsspec_filesystem.meta.json
│   │   │   │   │   ├── _hf_utils.data.json
│   │   │   │   │   ├── _hf_utils.meta.json
│   │   │   │   │   ├── _nested_dict.data.json
│   │   │   │   │   ├── _nested_dict.meta.json
│   │   │   │   │   ├── _sharded_tensor_utils.data.json
│   │   │   │   │   ├── _sharded_tensor_utils.meta.json
│   │   │   │   │   ├── _storage_utils.data.json
│   │   │   │   │   ├── _storage_utils.meta.json
│   │   │   │   │   ├── _traverse.data.json
│   │   │   │   │   ├── _traverse.meta.json
│   │   │   │   │   ├── _version.data.json
│   │   │   │   │   ├── _version.meta.json
│   │   │   │   │   ├── api.data.json
│   │   │   │   │   ├── api.meta.json
│   │   │   │   │   ├── default_planner.data.json
│   │   │   │   │   ├── default_planner.meta.json
│   │   │   │   │   ├── filesystem.data.json
│   │   │   │   │   ├── filesystem.meta.json
│   │   │   │   │   ├── hf_storage.data.json
│   │   │   │   │   ├── hf_storage.meta.json
│   │   │   │   │   ├── logger.data.json
│   │   │   │   │   ├── logger.meta.json
│   │   │   │   │   ├── logging_handlers.data.json
│   │   │   │   │   ├── logging_handlers.meta.json
│   │   │   │   │   ├── metadata.data.json
│   │   │   │   │   ├── metadata.meta.json
│   │   │   │   │   ├── optimizer.data.json
│   │   │   │   │   ├── optimizer.meta.json
│   │   │   │   │   ├── planner.data.json
│   │   │   │   │   ├── planner.meta.json
│   │   │   │   │   ├── planner_helpers.data.json
│   │   │   │   │   ├── planner_helpers.meta.json
│   │   │   │   │   ├── resharding.data.json
│   │   │   │   │   ├── resharding.meta.json
│   │   │   │   │   ├── staging.data.json
│   │   │   │   │   ├── staging.meta.json
│   │   │   │   │   ├── state_dict_loader.data.json
│   │   │   │   │   ├── state_dict_loader.meta.json
│   │   │   │   │   ├── state_dict_saver.data.json
│   │   │   │   │   ├── state_dict_saver.meta.json
│   │   │   │   │   ├── stateful.data.json
│   │   │   │   │   ├── stateful.meta.json
│   │   │   │   │   ├── storage.data.json
│   │   │   │   │   ├── storage.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   ├── constants.data.json
│   │   │   │   ├── constants.meta.json
│   │   │   │   ├── device_mesh.data.json
│   │   │   │   ├── device_mesh.meta.json
│   │   │   │   ├── distributed_c10d.data.json
│   │   │   │   ├── distributed_c10d.meta.json
│   │   │   │   ├── elastic
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── agent
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   └── server
│   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │       ├── api.data.json
│   │   │   │   │   │       ├── api.meta.json
│   │   │   │   │   │       ├── health_check_server.data.json
│   │   │   │   │   │       ├── health_check_server.meta.json
│   │   │   │   │   │       ├── local_elastic_agent.data.json
│   │   │   │   │   │       └── local_elastic_agent.meta.json
│   │   │   │   │   ├── events
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── api.data.json
│   │   │   │   │   │   ├── api.meta.json
│   │   │   │   │   │   ├── handlers.data.json
│   │   │   │   │   │   └── handlers.meta.json
│   │   │   │   │   ├── metrics
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── api.data.json
│   │   │   │   │   │   └── api.meta.json
│   │   │   │   │   ├── multiprocessing
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── api.data.json
│   │   │   │   │   │   ├── api.meta.json
│   │   │   │   │   │   ├── errors
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── error_handler.data.json
│   │   │   │   │   │   │   ├── error_handler.meta.json
│   │   │   │   │   │   │   ├── handlers.data.json
│   │   │   │   │   │   │   └── handlers.meta.json
│   │   │   │   │   │   ├── redirects.data.json
│   │   │   │   │   │   ├── redirects.meta.json
│   │   │   │   │   │   ├── subprocess_handler
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── handlers.data.json
│   │   │   │   │   │   │   ├── handlers.meta.json
│   │   │   │   │   │   │   ├── subprocess_handler.data.json
│   │   │   │   │   │   │   └── subprocess_handler.meta.json
│   │   │   │   │   │   ├── tail_log.data.json
│   │   │   │   │   │   └── tail_log.meta.json
│   │   │   │   │   ├── rendezvous
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── api.data.json
│   │   │   │   │   │   ├── api.meta.json
│   │   │   │   │   │   ├── dynamic_rendezvous.data.json
│   │   │   │   │   │   ├── dynamic_rendezvous.meta.json
│   │   │   │   │   │   ├── registry.data.json
│   │   │   │   │   │   ├── registry.meta.json
│   │   │   │   │   │   ├── utils.data.json
│   │   │   │   │   │   └── utils.meta.json
│   │   │   │   │   ├── timer
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── api.data.json
│   │   │   │   │   │   ├── api.meta.json
│   │   │   │   │   │   ├── debug_info_logging.data.json
│   │   │   │   │   │   ├── debug_info_logging.meta.json
│   │   │   │   │   │   ├── file_based_local_timer.data.json
│   │   │   │   │   │   ├── file_based_local_timer.meta.json
│   │   │   │   │   │   ├── local_timer.data.json
│   │   │   │   │   │   └── local_timer.meta.json
│   │   │   │   │   └── utils
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── api.data.json
│   │   │   │   │       ├── api.meta.json
│   │   │   │   │       ├── distributed.data.json
│   │   │   │   │       ├── distributed.meta.json
│   │   │   │   │       ├── log_level.data.json
│   │   │   │   │       ├── log_level.meta.json
│   │   │   │   │       ├── logging.data.json
│   │   │   │   │       ├── logging.meta.json
│   │   │   │   │       ├── store.data.json
│   │   │   │   │       └── store.meta.json
│   │   │   │   ├── fsdp
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _common_utils.data.json
│   │   │   │   │   ├── _common_utils.meta.json
│   │   │   │   │   ├── _debug_utils.data.json
│   │   │   │   │   ├── _debug_utils.meta.json
│   │   │   │   │   ├── _dynamo_utils.data.json
│   │   │   │   │   ├── _dynamo_utils.meta.json
│   │   │   │   │   ├── _exec_order_utils.data.json
│   │   │   │   │   ├── _exec_order_utils.meta.json
│   │   │   │   │   ├── _flat_param.data.json
│   │   │   │   │   ├── _flat_param.meta.json
│   │   │   │   │   ├── _fsdp_extensions.data.json
│   │   │   │   │   ├── _fsdp_extensions.meta.json
│   │   │   │   │   ├── _fully_shard
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── _fsdp_api.data.json
│   │   │   │   │   │   ├── _fsdp_api.meta.json
│   │   │   │   │   │   ├── _fsdp_collectives.data.json
│   │   │   │   │   │   ├── _fsdp_collectives.meta.json
│   │   │   │   │   │   ├── _fsdp_common.data.json
│   │   │   │   │   │   ├── _fsdp_common.meta.json
│   │   │   │   │   │   ├── _fsdp_init.data.json
│   │   │   │   │   │   ├── _fsdp_init.meta.json
│   │   │   │   │   │   ├── _fsdp_param.data.json
│   │   │   │   │   │   ├── _fsdp_param.meta.json
│   │   │   │   │   │   ├── _fsdp_param_group.data.json
│   │   │   │   │   │   ├── _fsdp_param_group.meta.json
│   │   │   │   │   │   ├── _fsdp_state.data.json
│   │   │   │   │   │   ├── _fsdp_state.meta.json
│   │   │   │   │   │   ├── _fully_shard.data.json
│   │   │   │   │   │   └── _fully_shard.meta.json
│   │   │   │   │   ├── _init_utils.data.json
│   │   │   │   │   ├── _init_utils.meta.json
│   │   │   │   │   ├── _limiter_utils.data.json
│   │   │   │   │   ├── _limiter_utils.meta.json
│   │   │   │   │   ├── _optim_utils.data.json
│   │   │   │   │   ├── _optim_utils.meta.json
│   │   │   │   │   ├── _runtime_utils.data.json
│   │   │   │   │   ├── _runtime_utils.meta.json
│   │   │   │   │   ├── _shard_utils.data.json
│   │   │   │   │   ├── _shard_utils.meta.json
│   │   │   │   │   ├── _state_dict_utils.data.json
│   │   │   │   │   ├── _state_dict_utils.meta.json
│   │   │   │   │   ├── _traversal_utils.data.json
│   │   │   │   │   ├── _traversal_utils.meta.json
│   │   │   │   │   ├── _unshard_param_utils.data.json
│   │   │   │   │   ├── _unshard_param_utils.meta.json
│   │   │   │   │   ├── _wrap_utils.data.json
│   │   │   │   │   ├── _wrap_utils.meta.json
│   │   │   │   │   ├── api.data.json
│   │   │   │   │   ├── api.meta.json
│   │   │   │   │   ├── fully_sharded_data_parallel.data.json
│   │   │   │   │   ├── fully_sharded_data_parallel.meta.json
│   │   │   │   │   ├── wrap.data.json
│   │   │   │   │   └── wrap.meta.json
│   │   │   │   ├── logging_handlers.data.json
│   │   │   │   ├── logging_handlers.meta.json
│   │   │   │   ├── nn
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── api
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── remote_module.data.json
│   │   │   │   │   │   └── remote_module.meta.json
│   │   │   │   │   ├── functional.data.json
│   │   │   │   │   ├── functional.meta.json
│   │   │   │   │   └── jit
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── instantiator.data.json
│   │   │   │   │       ├── instantiator.meta.json
│   │   │   │   │       └── templates
│   │   │   │   │           ├── __init__.data.json
│   │   │   │   │           ├── __init__.meta.json
│   │   │   │   │           ├── remote_module_template.data.json
│   │   │   │   │           └── remote_module_template.meta.json
│   │   │   │   ├── optim
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _deprecation_warning.data.json
│   │   │   │   │   ├── _deprecation_warning.meta.json
│   │   │   │   │   ├── apply_optimizer_in_backward.data.json
│   │   │   │   │   ├── apply_optimizer_in_backward.meta.json
│   │   │   │   │   ├── functional_adadelta.data.json
│   │   │   │   │   ├── functional_adadelta.meta.json
│   │   │   │   │   ├── functional_adagrad.data.json
│   │   │   │   │   ├── functional_adagrad.meta.json
│   │   │   │   │   ├── functional_adam.data.json
│   │   │   │   │   ├── functional_adam.meta.json
│   │   │   │   │   ├── functional_adamax.data.json
│   │   │   │   │   ├── functional_adamax.meta.json
│   │   │   │   │   ├── functional_adamw.data.json
│   │   │   │   │   ├── functional_adamw.meta.json
│   │   │   │   │   ├── functional_rmsprop.data.json
│   │   │   │   │   ├── functional_rmsprop.meta.json
│   │   │   │   │   ├── functional_rprop.data.json
│   │   │   │   │   ├── functional_rprop.meta.json
│   │   │   │   │   ├── functional_sgd.data.json
│   │   │   │   │   ├── functional_sgd.meta.json
│   │   │   │   │   ├── named_optimizer.data.json
│   │   │   │   │   ├── named_optimizer.meta.json
│   │   │   │   │   ├── optimizer.data.json
│   │   │   │   │   ├── optimizer.meta.json
│   │   │   │   │   ├── post_localSGD_optimizer.data.json
│   │   │   │   │   ├── post_localSGD_optimizer.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   ├── utils.meta.json
│   │   │   │   │   ├── zero_redundancy_optimizer.data.json
│   │   │   │   │   └── zero_redundancy_optimizer.meta.json
│   │   │   │   ├── remote_device.data.json
│   │   │   │   ├── remote_device.meta.json
│   │   │   │   ├── rendezvous.data.json
│   │   │   │   ├── rendezvous.meta.json
│   │   │   │   ├── rpc
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _utils.data.json
│   │   │   │   │   ├── _utils.meta.json
│   │   │   │   │   ├── api.data.json
│   │   │   │   │   ├── api.meta.json
│   │   │   │   │   ├── backend_registry.data.json
│   │   │   │   │   ├── backend_registry.meta.json
│   │   │   │   │   ├── constants.data.json
│   │   │   │   │   ├── constants.meta.json
│   │   │   │   │   ├── functions.data.json
│   │   │   │   │   ├── functions.meta.json
│   │   │   │   │   ├── internal.data.json
│   │   │   │   │   ├── internal.meta.json
│   │   │   │   │   ├── options.data.json
│   │   │   │   │   ├── options.meta.json
│   │   │   │   │   ├── server_process_global_profiler.data.json
│   │   │   │   │   └── server_process_global_profiler.meta.json
│   │   │   │   ├── tensor
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _api.data.json
│   │   │   │   │   ├── _api.meta.json
│   │   │   │   │   ├── _collective_utils.data.json
│   │   │   │   │   ├── _collective_utils.meta.json
│   │   │   │   │   ├── _dispatch.data.json
│   │   │   │   │   ├── _dispatch.meta.json
│   │   │   │   │   ├── _dtensor_spec.data.json
│   │   │   │   │   ├── _dtensor_spec.meta.json
│   │   │   │   │   ├── _op_schema.data.json
│   │   │   │   │   ├── _op_schema.meta.json
│   │   │   │   │   ├── _ops
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── _common_rules.data.json
│   │   │   │   │   │   ├── _common_rules.meta.json
│   │   │   │   │   │   ├── _conv_ops.data.json
│   │   │   │   │   │   ├── _conv_ops.meta.json
│   │   │   │   │   │   ├── _einsum_strategy.data.json
│   │   │   │   │   │   ├── _einsum_strategy.meta.json
│   │   │   │   │   │   ├── _embedding_ops.data.json
│   │   │   │   │   │   ├── _embedding_ops.meta.json
│   │   │   │   │   │   ├── _math_ops.data.json
│   │   │   │   │   │   ├── _math_ops.meta.json
│   │   │   │   │   │   ├── _matrix_ops.data.json
│   │   │   │   │   │   ├── _matrix_ops.meta.json
│   │   │   │   │   │   ├── _pointwise_ops.data.json
│   │   │   │   │   │   ├── _pointwise_ops.meta.json
│   │   │   │   │   │   ├── _random_ops.data.json
│   │   │   │   │   │   ├── _random_ops.meta.json
│   │   │   │   │   │   ├── _tensor_ops.data.json
│   │   │   │   │   │   ├── _tensor_ops.meta.json
│   │   │   │   │   │   ├── _view_ops.data.json
│   │   │   │   │   │   ├── _view_ops.meta.json
│   │   │   │   │   │   ├── utils.data.json
│   │   │   │   │   │   └── utils.meta.json
│   │   │   │   │   ├── _random.data.json
│   │   │   │   │   ├── _random.meta.json
│   │   │   │   │   ├── _redistribute.data.json
│   │   │   │   │   ├── _redistribute.meta.json
│   │   │   │   │   ├── _sharding_prop.data.json
│   │   │   │   │   ├── _sharding_prop.meta.json
│   │   │   │   │   ├── _tp_conv.data.json
│   │   │   │   │   ├── _tp_conv.meta.json
│   │   │   │   │   ├── _utils.data.json
│   │   │   │   │   ├── _utils.meta.json
│   │   │   │   │   ├── device_mesh.data.json
│   │   │   │   │   ├── device_mesh.meta.json
│   │   │   │   │   ├── parallel
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── _data_parallel_utils.data.json
│   │   │   │   │   │   ├── _data_parallel_utils.meta.json
│   │   │   │   │   │   ├── _utils.data.json
│   │   │   │   │   │   ├── _utils.meta.json
│   │   │   │   │   │   ├── api.data.json
│   │   │   │   │   │   ├── api.meta.json
│   │   │   │   │   │   ├── ddp.data.json
│   │   │   │   │   │   ├── ddp.meta.json
│   │   │   │   │   │   ├── fsdp.data.json
│   │   │   │   │   │   ├── fsdp.meta.json
│   │   │   │   │   │   ├── loss.data.json
│   │   │   │   │   │   ├── loss.meta.json
│   │   │   │   │   │   ├── style.data.json
│   │   │   │   │   │   └── style.meta.json
│   │   │   │   │   ├── placement_types.data.json
│   │   │   │   │   └── placement_types.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── distributions
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── bernoulli.data.json
│   │   │   │   ├── bernoulli.meta.json
│   │   │   │   ├── beta.data.json
│   │   │   │   ├── beta.meta.json
│   │   │   │   ├── binomial.data.json
│   │   │   │   ├── binomial.meta.json
│   │   │   │   ├── categorical.data.json
│   │   │   │   ├── categorical.meta.json
│   │   │   │   ├── cauchy.data.json
│   │   │   │   ├── cauchy.meta.json
│   │   │   │   ├── chi2.data.json
│   │   │   │   ├── chi2.meta.json
│   │   │   │   ├── constraint_registry.data.json
│   │   │   │   ├── constraint_registry.meta.json
│   │   │   │   ├── constraints.data.json
│   │   │   │   ├── constraints.meta.json
│   │   │   │   ├── continuous_bernoulli.data.json
│   │   │   │   ├── continuous_bernoulli.meta.json
│   │   │   │   ├── dirichlet.data.json
│   │   │   │   ├── dirichlet.meta.json
│   │   │   │   ├── distribution.data.json
│   │   │   │   ├── distribution.meta.json
│   │   │   │   ├── exp_family.data.json
│   │   │   │   ├── exp_family.meta.json
│   │   │   │   ├── exponential.data.json
│   │   │   │   ├── exponential.meta.json
│   │   │   │   ├── fishersnedecor.data.json
│   │   │   │   ├── fishersnedecor.meta.json
│   │   │   │   ├── gamma.data.json
│   │   │   │   ├── gamma.meta.json
│   │   │   │   ├── generalized_pareto.data.json
│   │   │   │   ├── generalized_pareto.meta.json
│   │   │   │   ├── geometric.data.json
│   │   │   │   ├── geometric.meta.json
│   │   │   │   ├── gumbel.data.json
│   │   │   │   ├── gumbel.meta.json
│   │   │   │   ├── half_cauchy.data.json
│   │   │   │   ├── half_cauchy.meta.json
│   │   │   │   ├── half_normal.data.json
│   │   │   │   ├── half_normal.meta.json
│   │   │   │   ├── independent.data.json
│   │   │   │   ├── independent.meta.json
│   │   │   │   ├── inverse_gamma.data.json
│   │   │   │   ├── inverse_gamma.meta.json
│   │   │   │   ├── kl.data.json
│   │   │   │   ├── kl.meta.json
│   │   │   │   ├── kumaraswamy.data.json
│   │   │   │   ├── kumaraswamy.meta.json
│   │   │   │   ├── laplace.data.json
│   │   │   │   ├── laplace.meta.json
│   │   │   │   ├── lkj_cholesky.data.json
│   │   │   │   ├── lkj_cholesky.meta.json
│   │   │   │   ├── log_normal.data.json
│   │   │   │   ├── log_normal.meta.json
│   │   │   │   ├── logistic_normal.data.json
│   │   │   │   ├── logistic_normal.meta.json
│   │   │   │   ├── lowrank_multivariate_normal.data.json
│   │   │   │   ├── lowrank_multivariate_normal.meta.json
│   │   │   │   ├── mixture_same_family.data.json
│   │   │   │   ├── mixture_same_family.meta.json
│   │   │   │   ├── multinomial.data.json
│   │   │   │   ├── multinomial.meta.json
│   │   │   │   ├── multivariate_normal.data.json
│   │   │   │   ├── multivariate_normal.meta.json
│   │   │   │   ├── negative_binomial.data.json
│   │   │   │   ├── negative_binomial.meta.json
│   │   │   │   ├── normal.data.json
│   │   │   │   ├── normal.meta.json
│   │   │   │   ├── one_hot_categorical.data.json
│   │   │   │   ├── one_hot_categorical.meta.json
│   │   │   │   ├── pareto.data.json
│   │   │   │   ├── pareto.meta.json
│   │   │   │   ├── poisson.data.json
│   │   │   │   ├── poisson.meta.json
│   │   │   │   ├── relaxed_bernoulli.data.json
│   │   │   │   ├── relaxed_bernoulli.meta.json
│   │   │   │   ├── relaxed_categorical.data.json
│   │   │   │   ├── relaxed_categorical.meta.json
│   │   │   │   ├── studentT.data.json
│   │   │   │   ├── studentT.meta.json
│   │   │   │   ├── transformed_distribution.data.json
│   │   │   │   ├── transformed_distribution.meta.json
│   │   │   │   ├── transforms.data.json
│   │   │   │   ├── transforms.meta.json
│   │   │   │   ├── uniform.data.json
│   │   │   │   ├── uniform.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   ├── utils.meta.json
│   │   │   │   ├── von_mises.data.json
│   │   │   │   ├── von_mises.meta.json
│   │   │   │   ├── weibull.data.json
│   │   │   │   ├── weibull.meta.json
│   │   │   │   ├── wishart.data.json
│   │   │   │   └── wishart.meta.json
│   │   │   ├── export
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _draft_export.data.json
│   │   │   │   ├── _draft_export.meta.json
│   │   │   │   ├── _remove_effect_tokens_pass.data.json
│   │   │   │   ├── _remove_effect_tokens_pass.meta.json
│   │   │   │   ├── _safeguard.data.json
│   │   │   │   ├── _safeguard.meta.json
│   │   │   │   ├── _trace.data.json
│   │   │   │   ├── _trace.meta.json
│   │   │   │   ├── _tree_utils.data.json
│   │   │   │   ├── _tree_utils.meta.json
│   │   │   │   ├── _unlift.data.json
│   │   │   │   ├── _unlift.meta.json
│   │   │   │   ├── _wrapper_utils.data.json
│   │   │   │   ├── _wrapper_utils.meta.json
│   │   │   │   ├── custom_ops.data.json
│   │   │   │   ├── custom_ops.meta.json
│   │   │   │   ├── decomp_utils.data.json
│   │   │   │   ├── decomp_utils.meta.json
│   │   │   │   ├── dynamic_shapes.data.json
│   │   │   │   ├── dynamic_shapes.meta.json
│   │   │   │   ├── exported_program.data.json
│   │   │   │   ├── exported_program.meta.json
│   │   │   │   ├── graph_signature.data.json
│   │   │   │   ├── graph_signature.meta.json
│   │   │   │   ├── pt2_archive
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _package.data.json
│   │   │   │   │   ├── _package.meta.json
│   │   │   │   │   ├── _package_weights.data.json
│   │   │   │   │   ├── _package_weights.meta.json
│   │   │   │   │   ├── constants.data.json
│   │   │   │   │   └── constants.meta.json
│   │   │   │   ├── unflatten.data.json
│   │   │   │   └── unflatten.meta.json
│   │   │   ├── fft
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── func
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── functional.data.json
│   │   │   ├── functional.meta.json
│   │   │   ├── futures
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── fx
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _compatibility.data.json
│   │   │   │   ├── _compatibility.meta.json
│   │   │   │   ├── _lazy_graph_module.data.json
│   │   │   │   ├── _lazy_graph_module.meta.json
│   │   │   │   ├── _pytree.data.json
│   │   │   │   ├── _pytree.meta.json
│   │   │   │   ├── _symbolic_trace.data.json
│   │   │   │   ├── _symbolic_trace.meta.json
│   │   │   │   ├── _utils.data.json
│   │   │   │   ├── _utils.meta.json
│   │   │   │   ├── config.data.json
│   │   │   │   ├── config.meta.json
│   │   │   │   ├── experimental
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _backward_state.data.json
│   │   │   │   │   ├── _backward_state.meta.json
│   │   │   │   │   ├── _config.data.json
│   │   │   │   │   ├── _config.meta.json
│   │   │   │   │   ├── _constant_symnode.data.json
│   │   │   │   │   ├── _constant_symnode.meta.json
│   │   │   │   │   ├── _dynamism.data.json
│   │   │   │   │   ├── _dynamism.meta.json
│   │   │   │   │   ├── const_fold.data.json
│   │   │   │   │   ├── const_fold.meta.json
│   │   │   │   │   ├── optimization.data.json
│   │   │   │   │   ├── optimization.meta.json
│   │   │   │   │   ├── proxy_tensor.data.json
│   │   │   │   │   ├── proxy_tensor.meta.json
│   │   │   │   │   ├── recording.data.json
│   │   │   │   │   ├── recording.meta.json
│   │   │   │   │   ├── sym_node.data.json
│   │   │   │   │   ├── sym_node.meta.json
│   │   │   │   │   ├── symbolic_shapes.data.json
│   │   │   │   │   ├── symbolic_shapes.meta.json
│   │   │   │   │   ├── validator.data.json
│   │   │   │   │   └── validator.meta.json
│   │   │   │   ├── graph.data.json
│   │   │   │   ├── graph.meta.json
│   │   │   │   ├── graph_module.data.json
│   │   │   │   ├── graph_module.meta.json
│   │   │   │   ├── immutable_collections.data.json
│   │   │   │   ├── immutable_collections.meta.json
│   │   │   │   ├── interpreter.data.json
│   │   │   │   ├── interpreter.meta.json
│   │   │   │   ├── node.data.json
│   │   │   │   ├── node.meta.json
│   │   │   │   ├── operator_schemas.data.json
│   │   │   │   ├── operator_schemas.meta.json
│   │   │   │   ├── passes
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _tensorify_python_scalars.data.json
│   │   │   │   │   ├── _tensorify_python_scalars.meta.json
│   │   │   │   │   ├── fake_tensor_prop.data.json
│   │   │   │   │   ├── fake_tensor_prop.meta.json
│   │   │   │   │   ├── graph_drawer.data.json
│   │   │   │   │   ├── graph_drawer.meta.json
│   │   │   │   │   ├── graph_manipulation.data.json
│   │   │   │   │   ├── graph_manipulation.meta.json
│   │   │   │   │   ├── graph_transform_observer.data.json
│   │   │   │   │   ├── graph_transform_observer.meta.json
│   │   │   │   │   ├── infra
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── partitioner.data.json
│   │   │   │   │   │   ├── partitioner.meta.json
│   │   │   │   │   │   ├── pass_base.data.json
│   │   │   │   │   │   ├── pass_base.meta.json
│   │   │   │   │   │   ├── pass_manager.data.json
│   │   │   │   │   │   └── pass_manager.meta.json
│   │   │   │   │   ├── net_min_base.data.json
│   │   │   │   │   ├── net_min_base.meta.json
│   │   │   │   │   ├── operator_support.data.json
│   │   │   │   │   ├── operator_support.meta.json
│   │   │   │   │   ├── param_fetch.data.json
│   │   │   │   │   ├── param_fetch.meta.json
│   │   │   │   │   ├── reinplace.data.json
│   │   │   │   │   ├── reinplace.meta.json
│   │   │   │   │   ├── runtime_assert.data.json
│   │   │   │   │   ├── runtime_assert.meta.json
│   │   │   │   │   ├── shape_prop.data.json
│   │   │   │   │   ├── shape_prop.meta.json
│   │   │   │   │   ├── split_module.data.json
│   │   │   │   │   ├── split_module.meta.json
│   │   │   │   │   ├── split_utils.data.json
│   │   │   │   │   ├── split_utils.meta.json
│   │   │   │   │   ├── splitter_base.data.json
│   │   │   │   │   ├── splitter_base.meta.json
│   │   │   │   │   ├── tools_common.data.json
│   │   │   │   │   ├── tools_common.meta.json
│   │   │   │   │   └── utils
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── common.data.json
│   │   │   │   │       ├── common.meta.json
│   │   │   │   │       ├── fuser_utils.data.json
│   │   │   │   │       ├── fuser_utils.meta.json
│   │   │   │   │       ├── matcher_utils.data.json
│   │   │   │   │       ├── matcher_utils.meta.json
│   │   │   │   │       ├── matcher_with_name_node_map_utils.data.json
│   │   │   │   │       ├── matcher_with_name_node_map_utils.meta.json
│   │   │   │   │       ├── source_matcher_utils.data.json
│   │   │   │   │       └── source_matcher_utils.meta.json
│   │   │   │   ├── proxy.data.json
│   │   │   │   ├── proxy.meta.json
│   │   │   │   ├── subgraph_rewriter.data.json
│   │   │   │   ├── subgraph_rewriter.meta.json
│   │   │   │   ├── traceback.data.json
│   │   │   │   └── traceback.meta.json
│   │   │   ├── hub.data.json
│   │   │   ├── hub.meta.json
│   │   │   ├── jit
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _async.data.json
│   │   │   │   ├── _async.meta.json
│   │   │   │   ├── _await.data.json
│   │   │   │   ├── _await.meta.json
│   │   │   │   ├── _builtins.data.json
│   │   │   │   ├── _builtins.meta.json
│   │   │   │   ├── _check.data.json
│   │   │   │   ├── _check.meta.json
│   │   │   │   ├── _dataclass_impls.data.json
│   │   │   │   ├── _dataclass_impls.meta.json
│   │   │   │   ├── _decomposition_utils.data.json
│   │   │   │   ├── _decomposition_utils.meta.json
│   │   │   │   ├── _freeze.data.json
│   │   │   │   ├── _freeze.meta.json
│   │   │   │   ├── _fuser.data.json
│   │   │   │   ├── _fuser.meta.json
│   │   │   │   ├── _ir_utils.data.json
│   │   │   │   ├── _ir_utils.meta.json
│   │   │   │   ├── _monkeytype_config.data.json
│   │   │   │   ├── _monkeytype_config.meta.json
│   │   │   │   ├── _recursive.data.json
│   │   │   │   ├── _recursive.meta.json
│   │   │   │   ├── _script.data.json
│   │   │   │   ├── _script.meta.json
│   │   │   │   ├── _serialization.data.json
│   │   │   │   ├── _serialization.meta.json
│   │   │   │   ├── _state.data.json
│   │   │   │   ├── _state.meta.json
│   │   │   │   ├── _trace.data.json
│   │   │   │   ├── _trace.meta.json
│   │   │   │   ├── annotations.data.json
│   │   │   │   ├── annotations.meta.json
│   │   │   │   ├── frontend.data.json
│   │   │   │   └── frontend.meta.json
│   │   │   ├── library.data.json
│   │   │   ├── library.meta.json
│   │   │   ├── linalg
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── masked
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _docs.data.json
│   │   │   │   ├── _docs.meta.json
│   │   │   │   ├── _ops.data.json
│   │   │   │   ├── _ops.meta.json
│   │   │   │   └── maskedtensor
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── _ops_refs.data.json
│   │   │   │       ├── _ops_refs.meta.json
│   │   │   │       ├── binary.data.json
│   │   │   │       ├── binary.meta.json
│   │   │   │       ├── core.data.json
│   │   │   │       ├── core.meta.json
│   │   │   │       ├── creation.data.json
│   │   │   │       ├── creation.meta.json
│   │   │   │       ├── passthrough.data.json
│   │   │   │       ├── passthrough.meta.json
│   │   │   │       ├── reductions.data.json
│   │   │   │       ├── reductions.meta.json
│   │   │   │       ├── unary.data.json
│   │   │   │       └── unary.meta.json
│   │   │   ├── monitor
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── mps
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── event.data.json
│   │   │   │   ├── event.meta.json
│   │   │   │   ├── profiler.data.json
│   │   │   │   └── profiler.meta.json
│   │   │   ├── mtia
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _utils.data.json
│   │   │   │   ├── _utils.meta.json
│   │   │   │   ├── memory.data.json
│   │   │   │   └── memory.meta.json
│   │   │   ├── multiprocessing
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _atfork.data.json
│   │   │   │   ├── _atfork.meta.json
│   │   │   │   ├── reductions.data.json
│   │   │   │   ├── reductions.meta.json
│   │   │   │   ├── spawn.data.json
│   │   │   │   └── spawn.meta.json
│   │   │   ├── nested
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   └── _internal
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── nested_int.data.json
│   │   │   │       ├── nested_int.meta.json
│   │   │   │       ├── nested_tensor.data.json
│   │   │   │       ├── nested_tensor.meta.json
│   │   │   │       ├── ops.data.json
│   │   │   │       ├── ops.meta.json
│   │   │   │       ├── sdpa.data.json
│   │   │   │       └── sdpa.meta.json
│   │   │   ├── nn
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _reduction.data.json
│   │   │   │   ├── _reduction.meta.json
│   │   │   │   ├── attention
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _utils.data.json
│   │   │   │   │   ├── _utils.meta.json
│   │   │   │   │   ├── flex_attention.data.json
│   │   │   │   │   └── flex_attention.meta.json
│   │   │   │   ├── common_types.data.json
│   │   │   │   ├── common_types.meta.json
│   │   │   │   ├── functional.data.json
│   │   │   │   ├── functional.meta.json
│   │   │   │   ├── init.data.json
│   │   │   │   ├── init.meta.json
│   │   │   │   ├── intrinsic
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── modules
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── fused.data.json
│   │   │   │   │   │   └── fused.meta.json
│   │   │   │   │   ├── qat
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   └── modules
│   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │       ├── conv_fused.data.json
│   │   │   │   │   │       ├── conv_fused.meta.json
│   │   │   │   │   │       ├── linear_fused.data.json
│   │   │   │   │   │       ├── linear_fused.meta.json
│   │   │   │   │   │       ├── linear_relu.data.json
│   │   │   │   │   │       └── linear_relu.meta.json
│   │   │   │   │   └── quantized
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── dynamic
│   │   │   │   │       │   ├── __init__.data.json
│   │   │   │   │       │   ├── __init__.meta.json
│   │   │   │   │       │   └── modules
│   │   │   │   │       │       ├── __init__.data.json
│   │   │   │   │       │       ├── __init__.meta.json
│   │   │   │   │       │       ├── linear_relu.data.json
│   │   │   │   │       │       └── linear_relu.meta.json
│   │   │   │   │       └── modules
│   │   │   │   │           ├── __init__.data.json
│   │   │   │   │           ├── __init__.meta.json
│   │   │   │   │           ├── bn_relu.data.json
│   │   │   │   │           ├── bn_relu.meta.json
│   │   │   │   │           ├── conv_relu.data.json
│   │   │   │   │           ├── conv_relu.meta.json
│   │   │   │   │           ├── linear_relu.data.json
│   │   │   │   │           └── linear_relu.meta.json
│   │   │   │   ├── modules
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _functions.data.json
│   │   │   │   │   ├── _functions.meta.json
│   │   │   │   │   ├── activation.data.json
│   │   │   │   │   ├── activation.meta.json
│   │   │   │   │   ├── adaptive.data.json
│   │   │   │   │   ├── adaptive.meta.json
│   │   │   │   │   ├── batchnorm.data.json
│   │   │   │   │   ├── batchnorm.meta.json
│   │   │   │   │   ├── channelshuffle.data.json
│   │   │   │   │   ├── channelshuffle.meta.json
│   │   │   │   │   ├── container.data.json
│   │   │   │   │   ├── container.meta.json
│   │   │   │   │   ├── conv.data.json
│   │   │   │   │   ├── conv.meta.json
│   │   │   │   │   ├── distance.data.json
│   │   │   │   │   ├── distance.meta.json
│   │   │   │   │   ├── dropout.data.json
│   │   │   │   │   ├── dropout.meta.json
│   │   │   │   │   ├── flatten.data.json
│   │   │   │   │   ├── flatten.meta.json
│   │   │   │   │   ├── fold.data.json
│   │   │   │   │   ├── fold.meta.json
│   │   │   │   │   ├── instancenorm.data.json
│   │   │   │   │   ├── instancenorm.meta.json
│   │   │   │   │   ├── lazy.data.json
│   │   │   │   │   ├── lazy.meta.json
│   │   │   │   │   ├── linear.data.json
│   │   │   │   │   ├── linear.meta.json
│   │   │   │   │   ├── loss.data.json
│   │   │   │   │   ├── loss.meta.json
│   │   │   │   │   ├── module.data.json
│   │   │   │   │   ├── module.meta.json
│   │   │   │   │   ├── normalization.data.json
│   │   │   │   │   ├── normalization.meta.json
│   │   │   │   │   ├── padding.data.json
│   │   │   │   │   ├── padding.meta.json
│   │   │   │   │   ├── pixelshuffle.data.json
│   │   │   │   │   ├── pixelshuffle.meta.json
│   │   │   │   │   ├── pooling.data.json
│   │   │   │   │   ├── pooling.meta.json
│   │   │   │   │   ├── rnn.data.json
│   │   │   │   │   ├── rnn.meta.json
│   │   │   │   │   ├── sparse.data.json
│   │   │   │   │   ├── sparse.meta.json
│   │   │   │   │   ├── transformer.data.json
│   │   │   │   │   ├── transformer.meta.json
│   │   │   │   │   ├── upsampling.data.json
│   │   │   │   │   ├── upsampling.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   ├── parallel
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _functions.data.json
│   │   │   │   │   ├── _functions.meta.json
│   │   │   │   │   ├── comm.data.json
│   │   │   │   │   ├── comm.meta.json
│   │   │   │   │   ├── data_parallel.data.json
│   │   │   │   │   ├── data_parallel.meta.json
│   │   │   │   │   ├── distributed.data.json
│   │   │   │   │   ├── distributed.meta.json
│   │   │   │   │   ├── parallel_apply.data.json
│   │   │   │   │   ├── parallel_apply.meta.json
│   │   │   │   │   ├── replicate.data.json
│   │   │   │   │   ├── replicate.meta.json
│   │   │   │   │   ├── scatter_gather.data.json
│   │   │   │   │   └── scatter_gather.meta.json
│   │   │   │   ├── parameter.data.json
│   │   │   │   ├── parameter.meta.json
│   │   │   │   ├── qat
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── dynamic
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   └── modules
│   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │       ├── linear.data.json
│   │   │   │   │   │       └── linear.meta.json
│   │   │   │   │   └── modules
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── conv.data.json
│   │   │   │   │       ├── conv.meta.json
│   │   │   │   │       ├── embedding_ops.data.json
│   │   │   │   │       ├── embedding_ops.meta.json
│   │   │   │   │       ├── linear.data.json
│   │   │   │   │       └── linear.meta.json
│   │   │   │   ├── quantizable
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   └── modules
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       └── __init__.meta.json
│   │   │   │   ├── quantized
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── dynamic
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   └── __init__.meta.json
│   │   │   │   │   ├── functional.data.json
│   │   │   │   │   ├── functional.meta.json
│   │   │   │   │   └── modules
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       └── __init__.meta.json
│   │   │   │   └── utils
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── _expanded_weights
│   │   │   │       │   ├── __init__.data.json
│   │   │   │       │   ├── __init__.meta.json
│   │   │   │       │   ├── conv_expanded_weights.data.json
│   │   │   │       │   ├── conv_expanded_weights.meta.json
│   │   │   │       │   ├── conv_utils.data.json
│   │   │   │       │   ├── conv_utils.meta.json
│   │   │   │       │   ├── embedding_expanded_weights.data.json
│   │   │   │       │   ├── embedding_expanded_weights.meta.json
│   │   │   │       │   ├── expanded_weights_impl.data.json
│   │   │   │       │   ├── expanded_weights_impl.meta.json
│   │   │   │       │   ├── expanded_weights_utils.data.json
│   │   │   │       │   ├── expanded_weights_utils.meta.json
│   │   │   │       │   ├── group_norm_expanded_weights.data.json
│   │   │   │       │   ├── group_norm_expanded_weights.meta.json
│   │   │   │       │   ├── instance_norm_expanded_weights.data.json
│   │   │   │       │   ├── instance_norm_expanded_weights.meta.json
│   │   │   │       │   ├── layer_norm_expanded_weights.data.json
│   │   │   │       │   ├── layer_norm_expanded_weights.meta.json
│   │   │   │       │   ├── linear_expanded_weights.data.json
│   │   │   │       │   └── linear_expanded_weights.meta.json
│   │   │   │       ├── _named_member_accessor.data.json
│   │   │   │       ├── _named_member_accessor.meta.json
│   │   │   │       ├── clip_grad.data.json
│   │   │   │       ├── clip_grad.meta.json
│   │   │   │       ├── convert_parameters.data.json
│   │   │   │       ├── convert_parameters.meta.json
│   │   │   │       ├── fusion.data.json
│   │   │   │       ├── fusion.meta.json
│   │   │   │       ├── init.data.json
│   │   │   │       ├── init.meta.json
│   │   │   │       ├── memory_format.data.json
│   │   │   │       ├── memory_format.meta.json
│   │   │   │       ├── parametrizations.data.json
│   │   │   │       ├── parametrizations.meta.json
│   │   │   │       ├── parametrize.data.json
│   │   │   │       ├── parametrize.meta.json
│   │   │   │       ├── rnn.data.json
│   │   │   │       ├── rnn.meta.json
│   │   │   │       ├── spectral_norm.data.json
│   │   │   │       ├── spectral_norm.meta.json
│   │   │   │       ├── stateless.data.json
│   │   │   │       ├── stateless.meta.json
│   │   │   │       ├── weight_norm.data.json
│   │   │   │       └── weight_norm.meta.json
│   │   │   ├── onnx
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _constants.data.json
│   │   │   │   ├── _constants.meta.json
│   │   │   │   ├── _globals.data.json
│   │   │   │   ├── _globals.meta.json
│   │   │   │   ├── _internal
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _exporter_legacy.data.json
│   │   │   │   │   ├── _exporter_legacy.meta.json
│   │   │   │   │   ├── _lazy_import.data.json
│   │   │   │   │   ├── _lazy_import.meta.json
│   │   │   │   │   ├── exporter
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── _analysis.data.json
│   │   │   │   │   │   ├── _analysis.meta.json
│   │   │   │   │   │   ├── _building.data.json
│   │   │   │   │   │   ├── _building.meta.json
│   │   │   │   │   │   ├── _capture_strategies.data.json
│   │   │   │   │   │   ├── _capture_strategies.meta.json
│   │   │   │   │   │   ├── _constants.data.json
│   │   │   │   │   │   ├── _constants.meta.json
│   │   │   │   │   │   ├── _core.data.json
│   │   │   │   │   │   ├── _core.meta.json
│   │   │   │   │   │   ├── _decomp.data.json
│   │   │   │   │   │   ├── _decomp.meta.json
│   │   │   │   │   │   ├── _dispatching.data.json
│   │   │   │   │   │   ├── _dispatching.meta.json
│   │   │   │   │   │   ├── _dynamic_shapes.data.json
│   │   │   │   │   │   ├── _dynamic_shapes.meta.json
│   │   │   │   │   │   ├── _errors.data.json
│   │   │   │   │   │   ├── _errors.meta.json
│   │   │   │   │   │   ├── _flags.data.json
│   │   │   │   │   │   ├── _flags.meta.json
│   │   │   │   │   │   ├── _fx_passes.data.json
│   │   │   │   │   │   ├── _fx_passes.meta.json
│   │   │   │   │   │   ├── _ir_passes.data.json
│   │   │   │   │   │   ├── _ir_passes.meta.json
│   │   │   │   │   │   ├── _onnx_program.data.json
│   │   │   │   │   │   ├── _onnx_program.meta.json
│   │   │   │   │   │   ├── _registration.data.json
│   │   │   │   │   │   ├── _registration.meta.json
│   │   │   │   │   │   ├── _reporting.data.json
│   │   │   │   │   │   ├── _reporting.meta.json
│   │   │   │   │   │   ├── _schemas.data.json
│   │   │   │   │   │   ├── _schemas.meta.json
│   │   │   │   │   │   ├── _tensors.data.json
│   │   │   │   │   │   ├── _tensors.meta.json
│   │   │   │   │   │   ├── _torchlib
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── _torchlib_registry.data.json
│   │   │   │   │   │   │   └── _torchlib_registry.meta.json
│   │   │   │   │   │   ├── _type_casting.data.json
│   │   │   │   │   │   ├── _type_casting.meta.json
│   │   │   │   │   │   ├── _verification.data.json
│   │   │   │   │   │   └── _verification.meta.json
│   │   │   │   │   ├── fx
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── _pass.data.json
│   │   │   │   │   │   ├── _pass.meta.json
│   │   │   │   │   │   ├── decomposition_table.data.json
│   │   │   │   │   │   ├── decomposition_table.meta.json
│   │   │   │   │   │   ├── dynamo_graph_extractor.data.json
│   │   │   │   │   │   ├── dynamo_graph_extractor.meta.json
│   │   │   │   │   │   ├── fx_onnx_interpreter.data.json
│   │   │   │   │   │   ├── fx_onnx_interpreter.meta.json
│   │   │   │   │   │   ├── onnxfunction_dispatcher.data.json
│   │   │   │   │   │   ├── onnxfunction_dispatcher.meta.json
│   │   │   │   │   │   ├── passes
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── _utils.data.json
│   │   │   │   │   │   │   ├── _utils.meta.json
│   │   │   │   │   │   │   ├── decomp.data.json
│   │   │   │   │   │   │   ├── decomp.meta.json
│   │   │   │   │   │   │   ├── functionalization.data.json
│   │   │   │   │   │   │   ├── functionalization.meta.json
│   │   │   │   │   │   │   ├── modularization.data.json
│   │   │   │   │   │   │   ├── modularization.meta.json
│   │   │   │   │   │   │   ├── readability.data.json
│   │   │   │   │   │   │   ├── readability.meta.json
│   │   │   │   │   │   │   ├── type_promotion.data.json
│   │   │   │   │   │   │   ├── type_promotion.meta.json
│   │   │   │   │   │   │   ├── virtualization.data.json
│   │   │   │   │   │   │   └── virtualization.meta.json
│   │   │   │   │   │   ├── patcher.data.json
│   │   │   │   │   │   ├── patcher.meta.json
│   │   │   │   │   │   ├── registration.data.json
│   │   │   │   │   │   ├── registration.meta.json
│   │   │   │   │   │   ├── serialization.data.json
│   │   │   │   │   │   ├── serialization.meta.json
│   │   │   │   │   │   ├── type_utils.data.json
│   │   │   │   │   │   └── type_utils.meta.json
│   │   │   │   │   ├── io_adapter.data.json
│   │   │   │   │   ├── io_adapter.meta.json
│   │   │   │   │   ├── jit_utils.data.json
│   │   │   │   │   ├── jit_utils.meta.json
│   │   │   │   │   ├── onnx_proto_utils.data.json
│   │   │   │   │   ├── onnx_proto_utils.meta.json
│   │   │   │   │   ├── onnxruntime.data.json
│   │   │   │   │   ├── onnxruntime.meta.json
│   │   │   │   │   ├── registration.data.json
│   │   │   │   │   └── registration.meta.json
│   │   │   │   ├── _type_utils.data.json
│   │   │   │   ├── _type_utils.meta.json
│   │   │   │   ├── errors.data.json
│   │   │   │   ├── errors.meta.json
│   │   │   │   ├── ops
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _dtype_mappings.data.json
│   │   │   │   │   ├── _dtype_mappings.meta.json
│   │   │   │   │   ├── _impl.data.json
│   │   │   │   │   ├── _impl.meta.json
│   │   │   │   │   ├── _symbolic_impl.data.json
│   │   │   │   │   └── _symbolic_impl.meta.json
│   │   │   │   ├── symbolic_caffe2.data.json
│   │   │   │   ├── symbolic_caffe2.meta.json
│   │   │   │   ├── symbolic_helper.data.json
│   │   │   │   ├── symbolic_helper.meta.json
│   │   │   │   ├── symbolic_opset10.data.json
│   │   │   │   ├── symbolic_opset10.meta.json
│   │   │   │   ├── symbolic_opset11.data.json
│   │   │   │   ├── symbolic_opset11.meta.json
│   │   │   │   ├── symbolic_opset12.data.json
│   │   │   │   ├── symbolic_opset12.meta.json
│   │   │   │   ├── symbolic_opset13.data.json
│   │   │   │   ├── symbolic_opset13.meta.json
│   │   │   │   ├── symbolic_opset14.data.json
│   │   │   │   ├── symbolic_opset14.meta.json
│   │   │   │   ├── symbolic_opset15.data.json
│   │   │   │   ├── symbolic_opset15.meta.json
│   │   │   │   ├── symbolic_opset16.data.json
│   │   │   │   ├── symbolic_opset16.meta.json
│   │   │   │   ├── symbolic_opset17.data.json
│   │   │   │   ├── symbolic_opset17.meta.json
│   │   │   │   ├── symbolic_opset18.data.json
│   │   │   │   ├── symbolic_opset18.meta.json
│   │   │   │   ├── symbolic_opset19.data.json
│   │   │   │   ├── symbolic_opset19.meta.json
│   │   │   │   ├── symbolic_opset20.data.json
│   │   │   │   ├── symbolic_opset20.meta.json
│   │   │   │   ├── symbolic_opset7.data.json
│   │   │   │   ├── symbolic_opset7.meta.json
│   │   │   │   ├── symbolic_opset8.data.json
│   │   │   │   ├── symbolic_opset8.meta.json
│   │   │   │   ├── symbolic_opset9.data.json
│   │   │   │   ├── symbolic_opset9.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── optim
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _adafactor.data.json
│   │   │   │   ├── _adafactor.meta.json
│   │   │   │   ├── _functional.data.json
│   │   │   │   ├── _functional.meta.json
│   │   │   │   ├── adadelta.data.json
│   │   │   │   ├── adadelta.meta.json
│   │   │   │   ├── adagrad.data.json
│   │   │   │   ├── adagrad.meta.json
│   │   │   │   ├── adam.data.json
│   │   │   │   ├── adam.meta.json
│   │   │   │   ├── adamax.data.json
│   │   │   │   ├── adamax.meta.json
│   │   │   │   ├── adamw.data.json
│   │   │   │   ├── adamw.meta.json
│   │   │   │   ├── asgd.data.json
│   │   │   │   ├── asgd.meta.json
│   │   │   │   ├── lbfgs.data.json
│   │   │   │   ├── lbfgs.meta.json
│   │   │   │   ├── lr_scheduler.data.json
│   │   │   │   ├── lr_scheduler.meta.json
│   │   │   │   ├── nadam.data.json
│   │   │   │   ├── nadam.meta.json
│   │   │   │   ├── optimizer.data.json
│   │   │   │   ├── optimizer.meta.json
│   │   │   │   ├── radam.data.json
│   │   │   │   ├── radam.meta.json
│   │   │   │   ├── rmsprop.data.json
│   │   │   │   ├── rmsprop.meta.json
│   │   │   │   ├── rprop.data.json
│   │   │   │   ├── rprop.meta.json
│   │   │   │   ├── sgd.data.json
│   │   │   │   ├── sgd.meta.json
│   │   │   │   ├── sparse_adam.data.json
│   │   │   │   ├── sparse_adam.meta.json
│   │   │   │   ├── swa_utils.data.json
│   │   │   │   └── swa_utils.meta.json
│   │   │   ├── overrides.data.json
│   │   │   ├── overrides.meta.json
│   │   │   ├── package
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _digraph.data.json
│   │   │   │   ├── _digraph.meta.json
│   │   │   │   ├── _directory_reader.data.json
│   │   │   │   ├── _directory_reader.meta.json
│   │   │   │   ├── _importlib.data.json
│   │   │   │   ├── _importlib.meta.json
│   │   │   │   ├── _mangling.data.json
│   │   │   │   ├── _mangling.meta.json
│   │   │   │   ├── _package_pickler.data.json
│   │   │   │   ├── _package_pickler.meta.json
│   │   │   │   ├── _package_unpickler.data.json
│   │   │   │   ├── _package_unpickler.meta.json
│   │   │   │   ├── _stdlib.data.json
│   │   │   │   ├── _stdlib.meta.json
│   │   │   │   ├── analyze
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── find_first_use_of_broken_modules.data.json
│   │   │   │   │   ├── find_first_use_of_broken_modules.meta.json
│   │   │   │   │   ├── is_from_package.data.json
│   │   │   │   │   ├── is_from_package.meta.json
│   │   │   │   │   ├── trace_dependencies.data.json
│   │   │   │   │   └── trace_dependencies.meta.json
│   │   │   │   ├── file_structure_representation.data.json
│   │   │   │   ├── file_structure_representation.meta.json
│   │   │   │   ├── find_file_dependencies.data.json
│   │   │   │   ├── find_file_dependencies.meta.json
│   │   │   │   ├── glob_group.data.json
│   │   │   │   ├── glob_group.meta.json
│   │   │   │   ├── importer.data.json
│   │   │   │   ├── importer.meta.json
│   │   │   │   ├── package_exporter.data.json
│   │   │   │   ├── package_exporter.meta.json
│   │   │   │   ├── package_importer.data.json
│   │   │   │   └── package_importer.meta.json
│   │   │   ├── profiler
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _memory_profiler.data.json
│   │   │   │   ├── _memory_profiler.meta.json
│   │   │   │   ├── _utils.data.json
│   │   │   │   ├── _utils.meta.json
│   │   │   │   ├── itt.data.json
│   │   │   │   ├── itt.meta.json
│   │   │   │   ├── profiler.data.json
│   │   │   │   └── profiler.meta.json
│   │   │   ├── quantization
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── fake_quantize.data.json
│   │   │   │   ├── fake_quantize.meta.json
│   │   │   │   ├── fuse_modules.data.json
│   │   │   │   ├── fuse_modules.meta.json
│   │   │   │   ├── fuser_method_mappings.data.json
│   │   │   │   ├── fuser_method_mappings.meta.json
│   │   │   │   ├── observer.data.json
│   │   │   │   ├── observer.meta.json
│   │   │   │   ├── qconfig.data.json
│   │   │   │   ├── qconfig.meta.json
│   │   │   │   ├── quant_type.data.json
│   │   │   │   ├── quant_type.meta.json
│   │   │   │   ├── quantization_mappings.data.json
│   │   │   │   ├── quantization_mappings.meta.json
│   │   │   │   ├── quantize.data.json
│   │   │   │   ├── quantize.meta.json
│   │   │   │   ├── quantize_jit.data.json
│   │   │   │   ├── quantize_jit.meta.json
│   │   │   │   ├── stubs.data.json
│   │   │   │   └── stubs.meta.json
│   │   │   ├── quasirandom.data.json
│   │   │   ├── quasirandom.meta.json
│   │   │   ├── random.data.json
│   │   │   ├── random.meta.json
│   │   │   ├── return_types.data.json
│   │   │   ├── return_types.meta.json
│   │   │   ├── serialization.data.json
│   │   │   ├── serialization.meta.json
│   │   │   ├── signal
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   └── windows
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── windows.data.json
│   │   │   │       └── windows.meta.json
│   │   │   ├── sparse
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _semi_structured_conversions.data.json
│   │   │   │   ├── _semi_structured_conversions.meta.json
│   │   │   │   ├── _semi_structured_ops.data.json
│   │   │   │   ├── _semi_structured_ops.meta.json
│   │   │   │   ├── semi_structured.data.json
│   │   │   │   └── semi_structured.meta.json
│   │   │   ├── special
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── storage.data.json
│   │   │   ├── storage.meta.json
│   │   │   ├── testing
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _comparison.data.json
│   │   │   │   ├── _comparison.meta.json
│   │   │   │   ├── _creation.data.json
│   │   │   │   ├── _creation.meta.json
│   │   │   │   ├── _internal
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── distributed
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── fake_pg.data.json
│   │   │   │   │   │   └── fake_pg.meta.json
│   │   │   │   │   ├── logging_tensor.data.json
│   │   │   │   │   └── logging_tensor.meta.json
│   │   │   │   ├── _utils.data.json
│   │   │   │   └── _utils.meta.json
│   │   │   ├── torch_version.data.json
│   │   │   ├── torch_version.meta.json
│   │   │   ├── types.data.json
│   │   │   ├── types.meta.json
│   │   │   ├── utils
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _appending_byte_serializer.data.json
│   │   │   │   ├── _appending_byte_serializer.meta.json
│   │   │   │   ├── _backport_slots.data.json
│   │   │   │   ├── _backport_slots.meta.json
│   │   │   │   ├── _config_module.data.json
│   │   │   │   ├── _config_module.meta.json
│   │   │   │   ├── _config_typing.data.json
│   │   │   │   ├── _config_typing.meta.json
│   │   │   │   ├── _content_store.data.json
│   │   │   │   ├── _content_store.meta.json
│   │   │   │   ├── _contextlib.data.json
│   │   │   │   ├── _contextlib.meta.json
│   │   │   │   ├── _cpp_extension_versioner.data.json
│   │   │   │   ├── _cpp_extension_versioner.meta.json
│   │   │   │   ├── _cxx_pytree.data.json
│   │   │   │   ├── _cxx_pytree.meta.json
│   │   │   │   ├── _device.data.json
│   │   │   │   ├── _device.meta.json
│   │   │   │   ├── _dtype_abbrs.data.json
│   │   │   │   ├── _dtype_abbrs.meta.json
│   │   │   │   ├── _exposed_in.data.json
│   │   │   │   ├── _exposed_in.meta.json
│   │   │   │   ├── _filelock.data.json
│   │   │   │   ├── _filelock.meta.json
│   │   │   │   ├── _foreach_utils.data.json
│   │   │   │   ├── _foreach_utils.meta.json
│   │   │   │   ├── _functools.data.json
│   │   │   │   ├── _functools.meta.json
│   │   │   │   ├── _import_utils.data.json
│   │   │   │   ├── _import_utils.meta.json
│   │   │   │   ├── _mode_utils.data.json
│   │   │   │   ├── _mode_utils.meta.json
│   │   │   │   ├── _ordered_set.data.json
│   │   │   │   ├── _ordered_set.meta.json
│   │   │   │   ├── _python_dispatch.data.json
│   │   │   │   ├── _python_dispatch.meta.json
│   │   │   │   ├── _pytree.data.json
│   │   │   │   ├── _pytree.meta.json
│   │   │   │   ├── _stats.data.json
│   │   │   │   ├── _stats.meta.json
│   │   │   │   ├── _sympy
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── functions.data.json
│   │   │   │   │   ├── functions.meta.json
│   │   │   │   │   ├── interp.data.json
│   │   │   │   │   ├── interp.meta.json
│   │   │   │   │   ├── numbers.data.json
│   │   │   │   │   ├── numbers.meta.json
│   │   │   │   │   ├── printers.data.json
│   │   │   │   │   ├── printers.meta.json
│   │   │   │   │   ├── reference.data.json
│   │   │   │   │   ├── reference.meta.json
│   │   │   │   │   ├── singleton_int.data.json
│   │   │   │   │   ├── singleton_int.meta.json
│   │   │   │   │   ├── solve.data.json
│   │   │   │   │   ├── solve.meta.json
│   │   │   │   │   ├── symbol.data.json
│   │   │   │   │   ├── symbol.meta.json
│   │   │   │   │   ├── value_ranges.data.json
│   │   │   │   │   └── value_ranges.meta.json
│   │   │   │   ├── _thunk.data.json
│   │   │   │   ├── _thunk.meta.json
│   │   │   │   ├── _traceback.data.json
│   │   │   │   ├── _traceback.meta.json
│   │   │   │   ├── _triton.data.json
│   │   │   │   ├── _triton.meta.json
│   │   │   │   ├── _typing_utils.data.json
│   │   │   │   ├── _typing_utils.meta.json
│   │   │   │   ├── backcompat
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── backend_registration.data.json
│   │   │   │   ├── backend_registration.meta.json
│   │   │   │   ├── checkpoint.data.json
│   │   │   │   ├── checkpoint.meta.json
│   │   │   │   ├── collect_env.data.json
│   │   │   │   ├── collect_env.meta.json
│   │   │   │   ├── cpp_backtrace.data.json
│   │   │   │   ├── cpp_backtrace.meta.json
│   │   │   │   ├── cpp_extension.data.json
│   │   │   │   ├── cpp_extension.meta.json
│   │   │   │   ├── data
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _utils
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── collate.data.json
│   │   │   │   │   │   ├── collate.meta.json
│   │   │   │   │   │   ├── fetch.data.json
│   │   │   │   │   │   ├── fetch.meta.json
│   │   │   │   │   │   ├── pin_memory.data.json
│   │   │   │   │   │   ├── pin_memory.meta.json
│   │   │   │   │   │   ├── signal_handling.data.json
│   │   │   │   │   │   ├── signal_handling.meta.json
│   │   │   │   │   │   ├── worker.data.json
│   │   │   │   │   │   └── worker.meta.json
│   │   │   │   │   ├── dataloader.data.json
│   │   │   │   │   ├── dataloader.meta.json
│   │   │   │   │   ├── datapipes
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── _decorator.data.json
│   │   │   │   │   │   ├── _decorator.meta.json
│   │   │   │   │   │   ├── _hook_iterator.data.json
│   │   │   │   │   │   ├── _hook_iterator.meta.json
│   │   │   │   │   │   ├── _typing.data.json
│   │   │   │   │   │   ├── _typing.meta.json
│   │   │   │   │   │   ├── dataframe
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── dataframe_wrapper.data.json
│   │   │   │   │   │   │   ├── dataframe_wrapper.meta.json
│   │   │   │   │   │   │   ├── dataframes.data.json
│   │   │   │   │   │   │   ├── dataframes.meta.json
│   │   │   │   │   │   │   ├── datapipes.data.json
│   │   │   │   │   │   │   ├── datapipes.meta.json
│   │   │   │   │   │   │   ├── structures.data.json
│   │   │   │   │   │   │   └── structures.meta.json
│   │   │   │   │   │   ├── datapipe.data.json
│   │   │   │   │   │   ├── datapipe.meta.json
│   │   │   │   │   │   ├── iter
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── callable.data.json
│   │   │   │   │   │   │   ├── callable.meta.json
│   │   │   │   │   │   │   ├── combinatorics.data.json
│   │   │   │   │   │   │   ├── combinatorics.meta.json
│   │   │   │   │   │   │   ├── combining.data.json
│   │   │   │   │   │   │   ├── combining.meta.json
│   │   │   │   │   │   │   ├── filelister.data.json
│   │   │   │   │   │   │   ├── filelister.meta.json
│   │   │   │   │   │   │   ├── fileopener.data.json
│   │   │   │   │   │   │   ├── fileopener.meta.json
│   │   │   │   │   │   │   ├── grouping.data.json
│   │   │   │   │   │   │   ├── grouping.meta.json
│   │   │   │   │   │   │   ├── routeddecoder.data.json
│   │   │   │   │   │   │   ├── routeddecoder.meta.json
│   │   │   │   │   │   │   ├── selecting.data.json
│   │   │   │   │   │   │   ├── selecting.meta.json
│   │   │   │   │   │   │   ├── sharding.data.json
│   │   │   │   │   │   │   ├── sharding.meta.json
│   │   │   │   │   │   │   ├── streamreader.data.json
│   │   │   │   │   │   │   ├── streamreader.meta.json
│   │   │   │   │   │   │   ├── utils.data.json
│   │   │   │   │   │   │   └── utils.meta.json
│   │   │   │   │   │   ├── map
│   │   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   │   ├── callable.data.json
│   │   │   │   │   │   │   ├── callable.meta.json
│   │   │   │   │   │   │   ├── combinatorics.data.json
│   │   │   │   │   │   │   ├── combinatorics.meta.json
│   │   │   │   │   │   │   ├── combining.data.json
│   │   │   │   │   │   │   ├── combining.meta.json
│   │   │   │   │   │   │   ├── grouping.data.json
│   │   │   │   │   │   │   ├── grouping.meta.json
│   │   │   │   │   │   │   ├── utils.data.json
│   │   │   │   │   │   │   └── utils.meta.json
│   │   │   │   │   │   └── utils
│   │   │   │   │   │       ├── __init__.data.json
│   │   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │   │       ├── common.data.json
│   │   │   │   │   │       ├── common.meta.json
│   │   │   │   │   │       ├── decoder.data.json
│   │   │   │   │   │       └── decoder.meta.json
│   │   │   │   │   ├── dataset.data.json
│   │   │   │   │   ├── dataset.meta.json
│   │   │   │   │   ├── distributed.data.json
│   │   │   │   │   ├── distributed.meta.json
│   │   │   │   │   ├── graph.data.json
│   │   │   │   │   ├── graph.meta.json
│   │   │   │   │   ├── graph_settings.data.json
│   │   │   │   │   ├── graph_settings.meta.json
│   │   │   │   │   ├── sampler.data.json
│   │   │   │   │   └── sampler.meta.json
│   │   │   │   ├── deterministic.data.json
│   │   │   │   ├── deterministic.meta.json
│   │   │   │   ├── dlpack.data.json
│   │   │   │   ├── dlpack.meta.json
│   │   │   │   ├── file_baton.data.json
│   │   │   │   ├── file_baton.meta.json
│   │   │   │   ├── flop_counter.data.json
│   │   │   │   ├── flop_counter.meta.json
│   │   │   │   ├── hipify
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── constants.data.json
│   │   │   │   │   ├── constants.meta.json
│   │   │   │   │   ├── cuda_to_hip_mappings.data.json
│   │   │   │   │   ├── cuda_to_hip_mappings.meta.json
│   │   │   │   │   ├── hipify_python.data.json
│   │   │   │   │   ├── hipify_python.meta.json
│   │   │   │   │   ├── version.data.json
│   │   │   │   │   └── version.meta.json
│   │   │   │   ├── hooks.data.json
│   │   │   │   ├── hooks.meta.json
│   │   │   │   ├── mkldnn.data.json
│   │   │   │   ├── mkldnn.meta.json
│   │   │   │   ├── module_tracker.data.json
│   │   │   │   ├── module_tracker.meta.json
│   │   │   │   ├── serialization
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── config.data.json
│   │   │   │   │   └── config.meta.json
│   │   │   │   ├── tensorboard
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── _convert_np.data.json
│   │   │   │   │   ├── _convert_np.meta.json
│   │   │   │   │   ├── _embedding.data.json
│   │   │   │   │   ├── _embedding.meta.json
│   │   │   │   │   ├── _onnx_graph.data.json
│   │   │   │   │   ├── _onnx_graph.meta.json
│   │   │   │   │   ├── _proto_graph.data.json
│   │   │   │   │   ├── _proto_graph.meta.json
│   │   │   │   │   ├── _pytorch_graph.data.json
│   │   │   │   │   ├── _pytorch_graph.meta.json
│   │   │   │   │   ├── _utils.data.json
│   │   │   │   │   ├── _utils.meta.json
│   │   │   │   │   ├── summary.data.json
│   │   │   │   │   ├── summary.meta.json
│   │   │   │   │   ├── writer.data.json
│   │   │   │   │   └── writer.meta.json
│   │   │   │   ├── throughput_benchmark.data.json
│   │   │   │   ├── throughput_benchmark.meta.json
│   │   │   │   ├── weak.data.json
│   │   │   │   └── weak.meta.json
│   │   │   ├── version.data.json
│   │   │   ├── version.meta.json
│   │   │   └── xpu
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── _utils.data.json
│   │   │       ├── _utils.meta.json
│   │   │       ├── memory.data.json
│   │   │       ├── memory.meta.json
│   │   │       ├── random.data.json
│   │   │       ├── random.meta.json
│   │   │       ├── streams.data.json
│   │   │       └── streams.meta.json
│   │   ├── traceback.data.json
│   │   ├── traceback.meta.json
│   │   ├── transformer_test.data.json
│   │   ├── transformer_test.meta.json
│   │   ├── transformers
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── activations.data.json
│   │   │   ├── activations.meta.json
│   │   │   ├── activations_tf.data.json
│   │   │   ├── activations_tf.meta.json
│   │   │   ├── audio_utils.data.json
│   │   │   ├── audio_utils.meta.json
│   │   │   ├── cache_utils.data.json
│   │   │   ├── cache_utils.meta.json
│   │   │   ├── configuration_utils.data.json
│   │   │   ├── configuration_utils.meta.json
│   │   │   ├── convert_slow_tokenizer.data.json
│   │   │   ├── convert_slow_tokenizer.meta.json
│   │   │   ├── data
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── data_collator.data.json
│   │   │   │   ├── data_collator.meta.json
│   │   │   │   ├── datasets
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── glue.data.json
│   │   │   │   │   ├── glue.meta.json
│   │   │   │   │   ├── language_modeling.data.json
│   │   │   │   │   ├── language_modeling.meta.json
│   │   │   │   │   ├── squad.data.json
│   │   │   │   │   └── squad.meta.json
│   │   │   │   ├── metrics
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   └── processors
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── glue.data.json
│   │   │   │       ├── glue.meta.json
│   │   │   │       ├── squad.data.json
│   │   │   │       ├── squad.meta.json
│   │   │   │       ├── utils.data.json
│   │   │   │       ├── utils.meta.json
│   │   │   │       ├── xnli.data.json
│   │   │   │       └── xnli.meta.json
│   │   │   ├── debug_utils.data.json
│   │   │   ├── debug_utils.meta.json
│   │   │   ├── dependency_versions_check.data.json
│   │   │   ├── dependency_versions_check.meta.json
│   │   │   ├── dependency_versions_table.data.json
│   │   │   ├── dependency_versions_table.meta.json
│   │   │   ├── distributed
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── configuration_utils.data.json
│   │   │   │   └── configuration_utils.meta.json
│   │   │   ├── dynamic_module_utils.data.json
│   │   │   ├── dynamic_module_utils.meta.json
│   │   │   ├── feature_extraction_sequence_utils.data.json
│   │   │   ├── feature_extraction_sequence_utils.meta.json
│   │   │   ├── feature_extraction_utils.data.json
│   │   │   ├── feature_extraction_utils.meta.json
│   │   │   ├── file_utils.data.json
│   │   │   ├── file_utils.meta.json
│   │   │   ├── generation
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── beam_constraints.data.json
│   │   │   │   ├── beam_constraints.meta.json
│   │   │   │   ├── beam_search.data.json
│   │   │   │   ├── beam_search.meta.json
│   │   │   │   ├── candidate_generator.data.json
│   │   │   │   ├── candidate_generator.meta.json
│   │   │   │   ├── configuration_utils.data.json
│   │   │   │   ├── configuration_utils.meta.json
│   │   │   │   ├── continuous_batching.data.json
│   │   │   │   ├── continuous_batching.meta.json
│   │   │   │   ├── flax_logits_process.data.json
│   │   │   │   ├── flax_logits_process.meta.json
│   │   │   │   ├── flax_utils.data.json
│   │   │   │   ├── flax_utils.meta.json
│   │   │   │   ├── logits_process.data.json
│   │   │   │   ├── logits_process.meta.json
│   │   │   │   ├── stopping_criteria.data.json
│   │   │   │   ├── stopping_criteria.meta.json
│   │   │   │   ├── streamers.data.json
│   │   │   │   ├── streamers.meta.json
│   │   │   │   ├── tf_logits_process.data.json
│   │   │   │   ├── tf_logits_process.meta.json
│   │   │   │   ├── tf_utils.data.json
│   │   │   │   ├── tf_utils.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   ├── utils.meta.json
│   │   │   │   ├── watermarking.data.json
│   │   │   │   └── watermarking.meta.json
│   │   │   ├── hf_argparser.data.json
│   │   │   ├── hf_argparser.meta.json
│   │   │   ├── hyperparameter_search.data.json
│   │   │   ├── hyperparameter_search.meta.json
│   │   │   ├── image_processing_base.data.json
│   │   │   ├── image_processing_base.meta.json
│   │   │   ├── image_processing_utils.data.json
│   │   │   ├── image_processing_utils.meta.json
│   │   │   ├── image_processing_utils_fast.data.json
│   │   │   ├── image_processing_utils_fast.meta.json
│   │   │   ├── image_transforms.data.json
│   │   │   ├── image_transforms.meta.json
│   │   │   ├── image_utils.data.json
│   │   │   ├── image_utils.meta.json
│   │   │   ├── integrations
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── accelerate.data.json
│   │   │   │   ├── accelerate.meta.json
│   │   │   │   ├── aqlm.data.json
│   │   │   │   ├── aqlm.meta.json
│   │   │   │   ├── awq.data.json
│   │   │   │   ├── awq.meta.json
│   │   │   │   ├── bitnet.data.json
│   │   │   │   ├── bitnet.meta.json
│   │   │   │   ├── bitsandbytes.data.json
│   │   │   │   ├── bitsandbytes.meta.json
│   │   │   │   ├── deepspeed.data.json
│   │   │   │   ├── deepspeed.meta.json
│   │   │   │   ├── eager_paged.data.json
│   │   │   │   ├── eager_paged.meta.json
│   │   │   │   ├── eetq.data.json
│   │   │   │   ├── eetq.meta.json
│   │   │   │   ├── executorch.data.json
│   │   │   │   ├── executorch.meta.json
│   │   │   │   ├── fbgemm_fp8.data.json
│   │   │   │   ├── fbgemm_fp8.meta.json
│   │   │   │   ├── finegrained_fp8.data.json
│   │   │   │   ├── finegrained_fp8.meta.json
│   │   │   │   ├── flash_attention.data.json
│   │   │   │   ├── flash_attention.meta.json
│   │   │   │   ├── flash_paged.data.json
│   │   │   │   ├── flash_paged.meta.json
│   │   │   │   ├── flex_attention.data.json
│   │   │   │   ├── flex_attention.meta.json
│   │   │   │   ├── fp_quant.data.json
│   │   │   │   ├── fp_quant.meta.json
│   │   │   │   ├── fsdp.data.json
│   │   │   │   ├── fsdp.meta.json
│   │   │   │   ├── ggml.data.json
│   │   │   │   ├── ggml.meta.json
│   │   │   │   ├── higgs.data.json
│   │   │   │   ├── higgs.meta.json
│   │   │   │   ├── hqq.data.json
│   │   │   │   ├── hqq.meta.json
│   │   │   │   ├── hub_kernels.data.json
│   │   │   │   ├── hub_kernels.meta.json
│   │   │   │   ├── integration_utils.data.json
│   │   │   │   ├── integration_utils.meta.json
│   │   │   │   ├── peft.data.json
│   │   │   │   ├── peft.meta.json
│   │   │   │   ├── quanto.data.json
│   │   │   │   ├── quanto.meta.json
│   │   │   │   ├── sdpa_attention.data.json
│   │   │   │   ├── sdpa_attention.meta.json
│   │   │   │   ├── sdpa_paged.data.json
│   │   │   │   ├── sdpa_paged.meta.json
│   │   │   │   ├── spqr.data.json
│   │   │   │   ├── spqr.meta.json
│   │   │   │   ├── tensor_parallel.data.json
│   │   │   │   ├── tensor_parallel.meta.json
│   │   │   │   ├── tpu.data.json
│   │   │   │   ├── tpu.meta.json
│   │   │   │   ├── vptq.data.json
│   │   │   │   └── vptq.meta.json
│   │   │   ├── keras_callbacks.data.json
│   │   │   ├── keras_callbacks.meta.json
│   │   │   ├── kernels
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   └── falcon_mamba
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── selective_scan_with_ln_interface.data.json
│   │   │   │       └── selective_scan_with_ln_interface.meta.json
│   │   │   ├── loss
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── loss_d_fine.data.json
│   │   │   │   ├── loss_d_fine.meta.json
│   │   │   │   ├── loss_deformable_detr.data.json
│   │   │   │   ├── loss_deformable_detr.meta.json
│   │   │   │   ├── loss_for_object_detection.data.json
│   │   │   │   ├── loss_for_object_detection.meta.json
│   │   │   │   ├── loss_grounding_dino.data.json
│   │   │   │   ├── loss_grounding_dino.meta.json
│   │   │   │   ├── loss_rt_detr.data.json
│   │   │   │   ├── loss_rt_detr.meta.json
│   │   │   │   ├── loss_utils.data.json
│   │   │   │   └── loss_utils.meta.json
│   │   │   ├── masking_utils.data.json
│   │   │   ├── masking_utils.meta.json
│   │   │   ├── model_debugging_utils.data.json
│   │   │   ├── model_debugging_utils.meta.json
│   │   │   ├── modelcard.data.json
│   │   │   ├── modelcard.meta.json
│   │   │   ├── modeling_attn_mask_utils.data.json
│   │   │   ├── modeling_attn_mask_utils.meta.json
│   │   │   ├── modeling_flash_attention_utils.data.json
│   │   │   ├── modeling_flash_attention_utils.meta.json
│   │   │   ├── modeling_flax_outputs.data.json
│   │   │   ├── modeling_flax_outputs.meta.json
│   │   │   ├── modeling_flax_pytorch_utils.data.json
│   │   │   ├── modeling_flax_pytorch_utils.meta.json
│   │   │   ├── modeling_flax_utils.data.json
│   │   │   ├── modeling_flax_utils.meta.json
│   │   │   ├── modeling_gguf_pytorch_utils.data.json
│   │   │   ├── modeling_gguf_pytorch_utils.meta.json
│   │   │   ├── modeling_layers.data.json
│   │   │   ├── modeling_layers.meta.json
│   │   │   ├── modeling_outputs.data.json
│   │   │   ├── modeling_outputs.meta.json
│   │   │   ├── modeling_rope_utils.data.json
│   │   │   ├── modeling_rope_utils.meta.json
│   │   │   ├── modeling_tf_outputs.data.json
│   │   │   ├── modeling_tf_outputs.meta.json
│   │   │   ├── modeling_tf_pytorch_utils.data.json
│   │   │   ├── modeling_tf_pytorch_utils.meta.json
│   │   │   ├── modeling_tf_utils.data.json
│   │   │   ├── modeling_tf_utils.meta.json
│   │   │   ├── modeling_utils.data.json
│   │   │   ├── modeling_utils.meta.json
│   │   │   ├── models
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── aimv2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_aimv2.data.json
│   │   │   │   │   ├── configuration_aimv2.meta.json
│   │   │   │   │   ├── modeling_aimv2.data.json
│   │   │   │   │   └── modeling_aimv2.meta.json
│   │   │   │   ├── albert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_albert.data.json
│   │   │   │   │   ├── configuration_albert.meta.json
│   │   │   │   │   ├── modeling_albert.data.json
│   │   │   │   │   ├── modeling_albert.meta.json
│   │   │   │   │   ├── modeling_flax_albert.data.json
│   │   │   │   │   ├── modeling_flax_albert.meta.json
│   │   │   │   │   ├── modeling_tf_albert.data.json
│   │   │   │   │   ├── modeling_tf_albert.meta.json
│   │   │   │   │   ├── tokenization_albert.data.json
│   │   │   │   │   ├── tokenization_albert.meta.json
│   │   │   │   │   ├── tokenization_albert_fast.data.json
│   │   │   │   │   └── tokenization_albert_fast.meta.json
│   │   │   │   ├── align
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_align.data.json
│   │   │   │   │   ├── configuration_align.meta.json
│   │   │   │   │   ├── modeling_align.data.json
│   │   │   │   │   ├── modeling_align.meta.json
│   │   │   │   │   ├── processing_align.data.json
│   │   │   │   │   └── processing_align.meta.json
│   │   │   │   ├── altclip
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_altclip.data.json
│   │   │   │   │   ├── configuration_altclip.meta.json
│   │   │   │   │   ├── modeling_altclip.data.json
│   │   │   │   │   ├── modeling_altclip.meta.json
│   │   │   │   │   ├── processing_altclip.data.json
│   │   │   │   │   └── processing_altclip.meta.json
│   │   │   │   ├── arcee
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_arcee.data.json
│   │   │   │   │   ├── configuration_arcee.meta.json
│   │   │   │   │   ├── modeling_arcee.data.json
│   │   │   │   │   └── modeling_arcee.meta.json
│   │   │   │   ├── aria
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_aria.data.json
│   │   │   │   │   ├── configuration_aria.meta.json
│   │   │   │   │   ├── image_processing_aria.data.json
│   │   │   │   │   ├── image_processing_aria.meta.json
│   │   │   │   │   ├── modeling_aria.data.json
│   │   │   │   │   ├── modeling_aria.meta.json
│   │   │   │   │   ├── processing_aria.data.json
│   │   │   │   │   └── processing_aria.meta.json
│   │   │   │   ├── audio_spectrogram_transformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_audio_spectrogram_transformer.data.json
│   │   │   │   │   ├── configuration_audio_spectrogram_transformer.meta.json
│   │   │   │   │   ├── feature_extraction_audio_spectrogram_transformer.data.json
│   │   │   │   │   ├── feature_extraction_audio_spectrogram_transformer.meta.json
│   │   │   │   │   ├── modeling_audio_spectrogram_transformer.data.json
│   │   │   │   │   └── modeling_audio_spectrogram_transformer.meta.json
│   │   │   │   ├── auto
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── auto_factory.data.json
│   │   │   │   │   ├── auto_factory.meta.json
│   │   │   │   │   ├── configuration_auto.data.json
│   │   │   │   │   ├── configuration_auto.meta.json
│   │   │   │   │   ├── feature_extraction_auto.data.json
│   │   │   │   │   ├── feature_extraction_auto.meta.json
│   │   │   │   │   ├── image_processing_auto.data.json
│   │   │   │   │   ├── image_processing_auto.meta.json
│   │   │   │   │   ├── modeling_auto.data.json
│   │   │   │   │   ├── modeling_auto.meta.json
│   │   │   │   │   ├── modeling_flax_auto.data.json
│   │   │   │   │   ├── modeling_flax_auto.meta.json
│   │   │   │   │   ├── modeling_tf_auto.data.json
│   │   │   │   │   ├── modeling_tf_auto.meta.json
│   │   │   │   │   ├── processing_auto.data.json
│   │   │   │   │   ├── processing_auto.meta.json
│   │   │   │   │   ├── tokenization_auto.data.json
│   │   │   │   │   ├── tokenization_auto.meta.json
│   │   │   │   │   ├── video_processing_auto.data.json
│   │   │   │   │   └── video_processing_auto.meta.json
│   │   │   │   ├── autoformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_autoformer.data.json
│   │   │   │   │   ├── configuration_autoformer.meta.json
│   │   │   │   │   ├── modeling_autoformer.data.json
│   │   │   │   │   └── modeling_autoformer.meta.json
│   │   │   │   ├── aya_vision
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_aya_vision.data.json
│   │   │   │   │   ├── configuration_aya_vision.meta.json
│   │   │   │   │   ├── modeling_aya_vision.data.json
│   │   │   │   │   ├── modeling_aya_vision.meta.json
│   │   │   │   │   ├── processing_aya_vision.data.json
│   │   │   │   │   └── processing_aya_vision.meta.json
│   │   │   │   ├── bamba
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bamba.data.json
│   │   │   │   │   ├── configuration_bamba.meta.json
│   │   │   │   │   ├── modeling_bamba.data.json
│   │   │   │   │   └── modeling_bamba.meta.json
│   │   │   │   ├── bark
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bark.data.json
│   │   │   │   │   ├── configuration_bark.meta.json
│   │   │   │   │   ├── generation_configuration_bark.data.json
│   │   │   │   │   ├── generation_configuration_bark.meta.json
│   │   │   │   │   ├── modeling_bark.data.json
│   │   │   │   │   ├── modeling_bark.meta.json
│   │   │   │   │   ├── processing_bark.data.json
│   │   │   │   │   └── processing_bark.meta.json
│   │   │   │   ├── bart
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bart.data.json
│   │   │   │   │   ├── configuration_bart.meta.json
│   │   │   │   │   ├── modeling_bart.data.json
│   │   │   │   │   ├── modeling_bart.meta.json
│   │   │   │   │   ├── modeling_flax_bart.data.json
│   │   │   │   │   ├── modeling_flax_bart.meta.json
│   │   │   │   │   ├── modeling_tf_bart.data.json
│   │   │   │   │   ├── modeling_tf_bart.meta.json
│   │   │   │   │   ├── tokenization_bart.data.json
│   │   │   │   │   ├── tokenization_bart.meta.json
│   │   │   │   │   ├── tokenization_bart_fast.data.json
│   │   │   │   │   └── tokenization_bart_fast.meta.json
│   │   │   │   ├── barthez
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_barthez.data.json
│   │   │   │   │   ├── tokenization_barthez.meta.json
│   │   │   │   │   ├── tokenization_barthez_fast.data.json
│   │   │   │   │   └── tokenization_barthez_fast.meta.json
│   │   │   │   ├── bartpho
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_bartpho.data.json
│   │   │   │   │   └── tokenization_bartpho.meta.json
│   │   │   │   ├── beit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_beit.data.json
│   │   │   │   │   ├── configuration_beit.meta.json
│   │   │   │   │   ├── feature_extraction_beit.data.json
│   │   │   │   │   ├── feature_extraction_beit.meta.json
│   │   │   │   │   ├── image_processing_beit.data.json
│   │   │   │   │   ├── image_processing_beit.meta.json
│   │   │   │   │   ├── image_processing_beit_fast.data.json
│   │   │   │   │   ├── image_processing_beit_fast.meta.json
│   │   │   │   │   ├── modeling_beit.data.json
│   │   │   │   │   ├── modeling_beit.meta.json
│   │   │   │   │   ├── modeling_flax_beit.data.json
│   │   │   │   │   └── modeling_flax_beit.meta.json
│   │   │   │   ├── bert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bert.data.json
│   │   │   │   │   ├── configuration_bert.meta.json
│   │   │   │   │   ├── modeling_bert.data.json
│   │   │   │   │   ├── modeling_bert.meta.json
│   │   │   │   │   ├── modeling_flax_bert.data.json
│   │   │   │   │   ├── modeling_flax_bert.meta.json
│   │   │   │   │   ├── modeling_tf_bert.data.json
│   │   │   │   │   ├── modeling_tf_bert.meta.json
│   │   │   │   │   ├── tokenization_bert.data.json
│   │   │   │   │   ├── tokenization_bert.meta.json
│   │   │   │   │   ├── tokenization_bert_fast.data.json
│   │   │   │   │   ├── tokenization_bert_fast.meta.json
│   │   │   │   │   ├── tokenization_bert_tf.data.json
│   │   │   │   │   └── tokenization_bert_tf.meta.json
│   │   │   │   ├── bert_generation
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bert_generation.data.json
│   │   │   │   │   ├── configuration_bert_generation.meta.json
│   │   │   │   │   ├── modeling_bert_generation.data.json
│   │   │   │   │   ├── modeling_bert_generation.meta.json
│   │   │   │   │   ├── tokenization_bert_generation.data.json
│   │   │   │   │   └── tokenization_bert_generation.meta.json
│   │   │   │   ├── bert_japanese
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_bert_japanese.data.json
│   │   │   │   │   └── tokenization_bert_japanese.meta.json
│   │   │   │   ├── bertweet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_bertweet.data.json
│   │   │   │   │   └── tokenization_bertweet.meta.json
│   │   │   │   ├── big_bird
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_big_bird.data.json
│   │   │   │   │   ├── configuration_big_bird.meta.json
│   │   │   │   │   ├── modeling_big_bird.data.json
│   │   │   │   │   ├── modeling_big_bird.meta.json
│   │   │   │   │   ├── modeling_flax_big_bird.data.json
│   │   │   │   │   ├── modeling_flax_big_bird.meta.json
│   │   │   │   │   ├── tokenization_big_bird.data.json
│   │   │   │   │   ├── tokenization_big_bird.meta.json
│   │   │   │   │   ├── tokenization_big_bird_fast.data.json
│   │   │   │   │   └── tokenization_big_bird_fast.meta.json
│   │   │   │   ├── bigbird_pegasus
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bigbird_pegasus.data.json
│   │   │   │   │   ├── configuration_bigbird_pegasus.meta.json
│   │   │   │   │   ├── modeling_bigbird_pegasus.data.json
│   │   │   │   │   └── modeling_bigbird_pegasus.meta.json
│   │   │   │   ├── biogpt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_biogpt.data.json
│   │   │   │   │   ├── configuration_biogpt.meta.json
│   │   │   │   │   ├── modeling_biogpt.data.json
│   │   │   │   │   ├── modeling_biogpt.meta.json
│   │   │   │   │   ├── tokenization_biogpt.data.json
│   │   │   │   │   └── tokenization_biogpt.meta.json
│   │   │   │   ├── bit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bit.data.json
│   │   │   │   │   ├── configuration_bit.meta.json
│   │   │   │   │   ├── image_processing_bit.data.json
│   │   │   │   │   ├── image_processing_bit.meta.json
│   │   │   │   │   ├── image_processing_bit_fast.data.json
│   │   │   │   │   ├── image_processing_bit_fast.meta.json
│   │   │   │   │   ├── modeling_bit.data.json
│   │   │   │   │   └── modeling_bit.meta.json
│   │   │   │   ├── bitnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bitnet.data.json
│   │   │   │   │   ├── configuration_bitnet.meta.json
│   │   │   │   │   ├── modeling_bitnet.data.json
│   │   │   │   │   └── modeling_bitnet.meta.json
│   │   │   │   ├── blenderbot
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_blenderbot.data.json
│   │   │   │   │   ├── configuration_blenderbot.meta.json
│   │   │   │   │   ├── modeling_blenderbot.data.json
│   │   │   │   │   ├── modeling_blenderbot.meta.json
│   │   │   │   │   ├── modeling_flax_blenderbot.data.json
│   │   │   │   │   ├── modeling_flax_blenderbot.meta.json
│   │   │   │   │   ├── modeling_tf_blenderbot.data.json
│   │   │   │   │   ├── modeling_tf_blenderbot.meta.json
│   │   │   │   │   ├── tokenization_blenderbot.data.json
│   │   │   │   │   ├── tokenization_blenderbot.meta.json
│   │   │   │   │   ├── tokenization_blenderbot_fast.data.json
│   │   │   │   │   └── tokenization_blenderbot_fast.meta.json
│   │   │   │   ├── blenderbot_small
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_blenderbot_small.data.json
│   │   │   │   │   ├── configuration_blenderbot_small.meta.json
│   │   │   │   │   ├── modeling_blenderbot_small.data.json
│   │   │   │   │   ├── modeling_blenderbot_small.meta.json
│   │   │   │   │   ├── modeling_flax_blenderbot_small.data.json
│   │   │   │   │   ├── modeling_flax_blenderbot_small.meta.json
│   │   │   │   │   ├── modeling_tf_blenderbot_small.data.json
│   │   │   │   │   ├── modeling_tf_blenderbot_small.meta.json
│   │   │   │   │   ├── tokenization_blenderbot_small.data.json
│   │   │   │   │   ├── tokenization_blenderbot_small.meta.json
│   │   │   │   │   ├── tokenization_blenderbot_small_fast.data.json
│   │   │   │   │   └── tokenization_blenderbot_small_fast.meta.json
│   │   │   │   ├── blip
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_blip.data.json
│   │   │   │   │   ├── configuration_blip.meta.json
│   │   │   │   │   ├── image_processing_blip.data.json
│   │   │   │   │   ├── image_processing_blip.meta.json
│   │   │   │   │   ├── image_processing_blip_fast.data.json
│   │   │   │   │   ├── image_processing_blip_fast.meta.json
│   │   │   │   │   ├── modeling_blip.data.json
│   │   │   │   │   ├── modeling_blip.meta.json
│   │   │   │   │   ├── modeling_blip_text.data.json
│   │   │   │   │   ├── modeling_blip_text.meta.json
│   │   │   │   │   ├── modeling_tf_blip.data.json
│   │   │   │   │   ├── modeling_tf_blip.meta.json
│   │   │   │   │   ├── modeling_tf_blip_text.data.json
│   │   │   │   │   ├── modeling_tf_blip_text.meta.json
│   │   │   │   │   ├── processing_blip.data.json
│   │   │   │   │   └── processing_blip.meta.json
│   │   │   │   ├── blip_2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_blip_2.data.json
│   │   │   │   │   ├── configuration_blip_2.meta.json
│   │   │   │   │   ├── modeling_blip_2.data.json
│   │   │   │   │   ├── modeling_blip_2.meta.json
│   │   │   │   │   ├── processing_blip_2.data.json
│   │   │   │   │   └── processing_blip_2.meta.json
│   │   │   │   ├── bloom
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bloom.data.json
│   │   │   │   │   ├── configuration_bloom.meta.json
│   │   │   │   │   ├── modeling_bloom.data.json
│   │   │   │   │   ├── modeling_bloom.meta.json
│   │   │   │   │   ├── modeling_flax_bloom.data.json
│   │   │   │   │   ├── modeling_flax_bloom.meta.json
│   │   │   │   │   ├── tokenization_bloom_fast.data.json
│   │   │   │   │   └── tokenization_bloom_fast.meta.json
│   │   │   │   ├── bridgetower
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bridgetower.data.json
│   │   │   │   │   ├── configuration_bridgetower.meta.json
│   │   │   │   │   ├── image_processing_bridgetower.data.json
│   │   │   │   │   ├── image_processing_bridgetower.meta.json
│   │   │   │   │   ├── image_processing_bridgetower_fast.data.json
│   │   │   │   │   ├── image_processing_bridgetower_fast.meta.json
│   │   │   │   │   ├── modeling_bridgetower.data.json
│   │   │   │   │   ├── modeling_bridgetower.meta.json
│   │   │   │   │   ├── processing_bridgetower.data.json
│   │   │   │   │   └── processing_bridgetower.meta.json
│   │   │   │   ├── bros
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_bros.data.json
│   │   │   │   │   ├── configuration_bros.meta.json
│   │   │   │   │   ├── modeling_bros.data.json
│   │   │   │   │   ├── modeling_bros.meta.json
│   │   │   │   │   ├── processing_bros.data.json
│   │   │   │   │   └── processing_bros.meta.json
│   │   │   │   ├── byt5
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_byt5.data.json
│   │   │   │   │   └── tokenization_byt5.meta.json
│   │   │   │   ├── camembert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_camembert.data.json
│   │   │   │   │   ├── configuration_camembert.meta.json
│   │   │   │   │   ├── modeling_camembert.data.json
│   │   │   │   │   ├── modeling_camembert.meta.json
│   │   │   │   │   ├── modeling_tf_camembert.data.json
│   │   │   │   │   ├── modeling_tf_camembert.meta.json
│   │   │   │   │   ├── tokenization_camembert.data.json
│   │   │   │   │   ├── tokenization_camembert.meta.json
│   │   │   │   │   ├── tokenization_camembert_fast.data.json
│   │   │   │   │   └── tokenization_camembert_fast.meta.json
│   │   │   │   ├── canine
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_canine.data.json
│   │   │   │   │   ├── configuration_canine.meta.json
│   │   │   │   │   ├── modeling_canine.data.json
│   │   │   │   │   ├── modeling_canine.meta.json
│   │   │   │   │   ├── tokenization_canine.data.json
│   │   │   │   │   └── tokenization_canine.meta.json
│   │   │   │   ├── chameleon
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_chameleon.data.json
│   │   │   │   │   ├── configuration_chameleon.meta.json
│   │   │   │   │   ├── image_processing_chameleon.data.json
│   │   │   │   │   ├── image_processing_chameleon.meta.json
│   │   │   │   │   ├── image_processing_chameleon_fast.data.json
│   │   │   │   │   ├── image_processing_chameleon_fast.meta.json
│   │   │   │   │   ├── modeling_chameleon.data.json
│   │   │   │   │   ├── modeling_chameleon.meta.json
│   │   │   │   │   ├── processing_chameleon.data.json
│   │   │   │   │   └── processing_chameleon.meta.json
│   │   │   │   ├── chinese_clip
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_chinese_clip.data.json
│   │   │   │   │   ├── configuration_chinese_clip.meta.json
│   │   │   │   │   ├── feature_extraction_chinese_clip.data.json
│   │   │   │   │   ├── feature_extraction_chinese_clip.meta.json
│   │   │   │   │   ├── image_processing_chinese_clip.data.json
│   │   │   │   │   ├── image_processing_chinese_clip.meta.json
│   │   │   │   │   ├── image_processing_chinese_clip_fast.data.json
│   │   │   │   │   ├── image_processing_chinese_clip_fast.meta.json
│   │   │   │   │   ├── modeling_chinese_clip.data.json
│   │   │   │   │   ├── modeling_chinese_clip.meta.json
│   │   │   │   │   ├── processing_chinese_clip.data.json
│   │   │   │   │   └── processing_chinese_clip.meta.json
│   │   │   │   ├── clap
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_clap.data.json
│   │   │   │   │   ├── configuration_clap.meta.json
│   │   │   │   │   ├── feature_extraction_clap.data.json
│   │   │   │   │   ├── feature_extraction_clap.meta.json
│   │   │   │   │   ├── modeling_clap.data.json
│   │   │   │   │   ├── modeling_clap.meta.json
│   │   │   │   │   ├── processing_clap.data.json
│   │   │   │   │   └── processing_clap.meta.json
│   │   │   │   ├── clip
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_clip.data.json
│   │   │   │   │   ├── configuration_clip.meta.json
│   │   │   │   │   ├── feature_extraction_clip.data.json
│   │   │   │   │   ├── feature_extraction_clip.meta.json
│   │   │   │   │   ├── image_processing_clip.data.json
│   │   │   │   │   ├── image_processing_clip.meta.json
│   │   │   │   │   ├── image_processing_clip_fast.data.json
│   │   │   │   │   ├── image_processing_clip_fast.meta.json
│   │   │   │   │   ├── modeling_clip.data.json
│   │   │   │   │   ├── modeling_clip.meta.json
│   │   │   │   │   ├── modeling_flax_clip.data.json
│   │   │   │   │   ├── modeling_flax_clip.meta.json
│   │   │   │   │   ├── modeling_tf_clip.data.json
│   │   │   │   │   ├── modeling_tf_clip.meta.json
│   │   │   │   │   ├── processing_clip.data.json
│   │   │   │   │   ├── processing_clip.meta.json
│   │   │   │   │   ├── tokenization_clip.data.json
│   │   │   │   │   ├── tokenization_clip.meta.json
│   │   │   │   │   ├── tokenization_clip_fast.data.json
│   │   │   │   │   └── tokenization_clip_fast.meta.json
│   │   │   │   ├── clipseg
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_clipseg.data.json
│   │   │   │   │   ├── configuration_clipseg.meta.json
│   │   │   │   │   ├── modeling_clipseg.data.json
│   │   │   │   │   ├── modeling_clipseg.meta.json
│   │   │   │   │   ├── processing_clipseg.data.json
│   │   │   │   │   └── processing_clipseg.meta.json
│   │   │   │   ├── clvp
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_clvp.data.json
│   │   │   │   │   ├── configuration_clvp.meta.json
│   │   │   │   │   ├── feature_extraction_clvp.data.json
│   │   │   │   │   ├── feature_extraction_clvp.meta.json
│   │   │   │   │   ├── modeling_clvp.data.json
│   │   │   │   │   ├── modeling_clvp.meta.json
│   │   │   │   │   ├── number_normalizer.data.json
│   │   │   │   │   ├── number_normalizer.meta.json
│   │   │   │   │   ├── processing_clvp.data.json
│   │   │   │   │   ├── processing_clvp.meta.json
│   │   │   │   │   ├── tokenization_clvp.data.json
│   │   │   │   │   └── tokenization_clvp.meta.json
│   │   │   │   ├── code_llama
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_code_llama.data.json
│   │   │   │   │   ├── tokenization_code_llama.meta.json
│   │   │   │   │   ├── tokenization_code_llama_fast.data.json
│   │   │   │   │   └── tokenization_code_llama_fast.meta.json
│   │   │   │   ├── codegen
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_codegen.data.json
│   │   │   │   │   ├── configuration_codegen.meta.json
│   │   │   │   │   ├── modeling_codegen.data.json
│   │   │   │   │   ├── modeling_codegen.meta.json
│   │   │   │   │   ├── tokenization_codegen.data.json
│   │   │   │   │   ├── tokenization_codegen.meta.json
│   │   │   │   │   ├── tokenization_codegen_fast.data.json
│   │   │   │   │   └── tokenization_codegen_fast.meta.json
│   │   │   │   ├── cohere
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_cohere.data.json
│   │   │   │   │   ├── configuration_cohere.meta.json
│   │   │   │   │   ├── modeling_cohere.data.json
│   │   │   │   │   ├── modeling_cohere.meta.json
│   │   │   │   │   ├── tokenization_cohere_fast.data.json
│   │   │   │   │   └── tokenization_cohere_fast.meta.json
│   │   │   │   ├── cohere2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_cohere2.data.json
│   │   │   │   │   ├── configuration_cohere2.meta.json
│   │   │   │   │   ├── modeling_cohere2.data.json
│   │   │   │   │   └── modeling_cohere2.meta.json
│   │   │   │   ├── colpali
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_colpali.data.json
│   │   │   │   │   ├── configuration_colpali.meta.json
│   │   │   │   │   ├── modeling_colpali.data.json
│   │   │   │   │   ├── modeling_colpali.meta.json
│   │   │   │   │   ├── processing_colpali.data.json
│   │   │   │   │   └── processing_colpali.meta.json
│   │   │   │   ├── colqwen2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_colqwen2.data.json
│   │   │   │   │   ├── configuration_colqwen2.meta.json
│   │   │   │   │   ├── modeling_colqwen2.data.json
│   │   │   │   │   ├── modeling_colqwen2.meta.json
│   │   │   │   │   ├── processing_colqwen2.data.json
│   │   │   │   │   └── processing_colqwen2.meta.json
│   │   │   │   ├── conditional_detr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_conditional_detr.data.json
│   │   │   │   │   ├── configuration_conditional_detr.meta.json
│   │   │   │   │   ├── feature_extraction_conditional_detr.data.json
│   │   │   │   │   ├── feature_extraction_conditional_detr.meta.json
│   │   │   │   │   ├── image_processing_conditional_detr.data.json
│   │   │   │   │   ├── image_processing_conditional_detr.meta.json
│   │   │   │   │   ├── image_processing_conditional_detr_fast.data.json
│   │   │   │   │   ├── image_processing_conditional_detr_fast.meta.json
│   │   │   │   │   ├── modeling_conditional_detr.data.json
│   │   │   │   │   └── modeling_conditional_detr.meta.json
│   │   │   │   ├── convbert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_convbert.data.json
│   │   │   │   │   ├── configuration_convbert.meta.json
│   │   │   │   │   ├── modeling_convbert.data.json
│   │   │   │   │   ├── modeling_convbert.meta.json
│   │   │   │   │   ├── modeling_tf_convbert.data.json
│   │   │   │   │   ├── modeling_tf_convbert.meta.json
│   │   │   │   │   ├── tokenization_convbert.data.json
│   │   │   │   │   ├── tokenization_convbert.meta.json
│   │   │   │   │   ├── tokenization_convbert_fast.data.json
│   │   │   │   │   └── tokenization_convbert_fast.meta.json
│   │   │   │   ├── convnext
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_convnext.data.json
│   │   │   │   │   ├── configuration_convnext.meta.json
│   │   │   │   │   ├── feature_extraction_convnext.data.json
│   │   │   │   │   ├── feature_extraction_convnext.meta.json
│   │   │   │   │   ├── image_processing_convnext.data.json
│   │   │   │   │   ├── image_processing_convnext.meta.json
│   │   │   │   │   ├── image_processing_convnext_fast.data.json
│   │   │   │   │   ├── image_processing_convnext_fast.meta.json
│   │   │   │   │   ├── modeling_convnext.data.json
│   │   │   │   │   ├── modeling_convnext.meta.json
│   │   │   │   │   ├── modeling_tf_convnext.data.json
│   │   │   │   │   └── modeling_tf_convnext.meta.json
│   │   │   │   ├── convnextv2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_convnextv2.data.json
│   │   │   │   │   ├── configuration_convnextv2.meta.json
│   │   │   │   │   ├── modeling_convnextv2.data.json
│   │   │   │   │   ├── modeling_convnextv2.meta.json
│   │   │   │   │   ├── modeling_tf_convnextv2.data.json
│   │   │   │   │   └── modeling_tf_convnextv2.meta.json
│   │   │   │   ├── cpm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_cpm.data.json
│   │   │   │   │   ├── tokenization_cpm.meta.json
│   │   │   │   │   ├── tokenization_cpm_fast.data.json
│   │   │   │   │   └── tokenization_cpm_fast.meta.json
│   │   │   │   ├── cpmant
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_cpmant.data.json
│   │   │   │   │   ├── configuration_cpmant.meta.json
│   │   │   │   │   ├── modeling_cpmant.data.json
│   │   │   │   │   ├── modeling_cpmant.meta.json
│   │   │   │   │   ├── tokenization_cpmant.data.json
│   │   │   │   │   └── tokenization_cpmant.meta.json
│   │   │   │   ├── csm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_csm.data.json
│   │   │   │   │   ├── configuration_csm.meta.json
│   │   │   │   │   ├── generation_csm.data.json
│   │   │   │   │   ├── generation_csm.meta.json
│   │   │   │   │   ├── modeling_csm.data.json
│   │   │   │   │   ├── modeling_csm.meta.json
│   │   │   │   │   ├── processing_csm.data.json
│   │   │   │   │   └── processing_csm.meta.json
│   │   │   │   ├── ctrl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_ctrl.data.json
│   │   │   │   │   ├── configuration_ctrl.meta.json
│   │   │   │   │   ├── modeling_ctrl.data.json
│   │   │   │   │   ├── modeling_ctrl.meta.json
│   │   │   │   │   ├── modeling_tf_ctrl.data.json
│   │   │   │   │   ├── modeling_tf_ctrl.meta.json
│   │   │   │   │   ├── tokenization_ctrl.data.json
│   │   │   │   │   └── tokenization_ctrl.meta.json
│   │   │   │   ├── cvt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_cvt.data.json
│   │   │   │   │   ├── configuration_cvt.meta.json
│   │   │   │   │   ├── modeling_cvt.data.json
│   │   │   │   │   ├── modeling_cvt.meta.json
│   │   │   │   │   ├── modeling_tf_cvt.data.json
│   │   │   │   │   └── modeling_tf_cvt.meta.json
│   │   │   │   ├── d_fine
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_d_fine.data.json
│   │   │   │   │   ├── configuration_d_fine.meta.json
│   │   │   │   │   ├── modeling_d_fine.data.json
│   │   │   │   │   └── modeling_d_fine.meta.json
│   │   │   │   ├── dab_detr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dab_detr.data.json
│   │   │   │   │   ├── configuration_dab_detr.meta.json
│   │   │   │   │   ├── modeling_dab_detr.data.json
│   │   │   │   │   └── modeling_dab_detr.meta.json
│   │   │   │   ├── dac
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dac.data.json
│   │   │   │   │   ├── configuration_dac.meta.json
│   │   │   │   │   ├── feature_extraction_dac.data.json
│   │   │   │   │   ├── feature_extraction_dac.meta.json
│   │   │   │   │   ├── modeling_dac.data.json
│   │   │   │   │   └── modeling_dac.meta.json
│   │   │   │   ├── data2vec
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_data2vec_audio.data.json
│   │   │   │   │   ├── configuration_data2vec_audio.meta.json
│   │   │   │   │   ├── configuration_data2vec_text.data.json
│   │   │   │   │   ├── configuration_data2vec_text.meta.json
│   │   │   │   │   ├── configuration_data2vec_vision.data.json
│   │   │   │   │   ├── configuration_data2vec_vision.meta.json
│   │   │   │   │   ├── modeling_data2vec_audio.data.json
│   │   │   │   │   ├── modeling_data2vec_audio.meta.json
│   │   │   │   │   ├── modeling_data2vec_text.data.json
│   │   │   │   │   ├── modeling_data2vec_text.meta.json
│   │   │   │   │   ├── modeling_data2vec_vision.data.json
│   │   │   │   │   ├── modeling_data2vec_vision.meta.json
│   │   │   │   │   ├── modeling_tf_data2vec_vision.data.json
│   │   │   │   │   └── modeling_tf_data2vec_vision.meta.json
│   │   │   │   ├── dbrx
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dbrx.data.json
│   │   │   │   │   ├── configuration_dbrx.meta.json
│   │   │   │   │   ├── modeling_dbrx.data.json
│   │   │   │   │   └── modeling_dbrx.meta.json
│   │   │   │   ├── deberta
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_deberta.data.json
│   │   │   │   │   ├── configuration_deberta.meta.json
│   │   │   │   │   ├── modeling_deberta.data.json
│   │   │   │   │   ├── modeling_deberta.meta.json
│   │   │   │   │   ├── modeling_tf_deberta.data.json
│   │   │   │   │   ├── modeling_tf_deberta.meta.json
│   │   │   │   │   ├── tokenization_deberta.data.json
│   │   │   │   │   ├── tokenization_deberta.meta.json
│   │   │   │   │   ├── tokenization_deberta_fast.data.json
│   │   │   │   │   └── tokenization_deberta_fast.meta.json
│   │   │   │   ├── deberta_v2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_deberta_v2.data.json
│   │   │   │   │   ├── configuration_deberta_v2.meta.json
│   │   │   │   │   ├── modeling_deberta_v2.data.json
│   │   │   │   │   ├── modeling_deberta_v2.meta.json
│   │   │   │   │   ├── modeling_tf_deberta_v2.data.json
│   │   │   │   │   ├── modeling_tf_deberta_v2.meta.json
│   │   │   │   │   ├── tokenization_deberta_v2.data.json
│   │   │   │   │   ├── tokenization_deberta_v2.meta.json
│   │   │   │   │   ├── tokenization_deberta_v2_fast.data.json
│   │   │   │   │   └── tokenization_deberta_v2_fast.meta.json
│   │   │   │   ├── decision_transformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_decision_transformer.data.json
│   │   │   │   │   ├── configuration_decision_transformer.meta.json
│   │   │   │   │   ├── modeling_decision_transformer.data.json
│   │   │   │   │   └── modeling_decision_transformer.meta.json
│   │   │   │   ├── deepseek_v2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_deepseek_v2.data.json
│   │   │   │   │   ├── configuration_deepseek_v2.meta.json
│   │   │   │   │   ├── modeling_deepseek_v2.data.json
│   │   │   │   │   └── modeling_deepseek_v2.meta.json
│   │   │   │   ├── deepseek_v3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_deepseek_v3.data.json
│   │   │   │   │   ├── configuration_deepseek_v3.meta.json
│   │   │   │   │   ├── modeling_deepseek_v3.data.json
│   │   │   │   │   └── modeling_deepseek_v3.meta.json
│   │   │   │   ├── deepseek_vl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_deepseek_vl.data.json
│   │   │   │   │   ├── configuration_deepseek_vl.meta.json
│   │   │   │   │   ├── image_processing_deepseek_vl.data.json
│   │   │   │   │   ├── image_processing_deepseek_vl.meta.json
│   │   │   │   │   ├── modeling_deepseek_vl.data.json
│   │   │   │   │   ├── modeling_deepseek_vl.meta.json
│   │   │   │   │   ├── processing_deepseek_vl.data.json
│   │   │   │   │   └── processing_deepseek_vl.meta.json
│   │   │   │   ├── deepseek_vl_hybrid
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_deepseek_vl_hybrid.data.json
│   │   │   │   │   ├── configuration_deepseek_vl_hybrid.meta.json
│   │   │   │   │   ├── image_processing_deepseek_vl_hybrid.data.json
│   │   │   │   │   ├── image_processing_deepseek_vl_hybrid.meta.json
│   │   │   │   │   ├── modeling_deepseek_vl_hybrid.data.json
│   │   │   │   │   ├── modeling_deepseek_vl_hybrid.meta.json
│   │   │   │   │   ├── processing_deepseek_vl_hybrid.data.json
│   │   │   │   │   └── processing_deepseek_vl_hybrid.meta.json
│   │   │   │   ├── deformable_detr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_deformable_detr.data.json
│   │   │   │   │   ├── configuration_deformable_detr.meta.json
│   │   │   │   │   ├── feature_extraction_deformable_detr.data.json
│   │   │   │   │   ├── feature_extraction_deformable_detr.meta.json
│   │   │   │   │   ├── image_processing_deformable_detr.data.json
│   │   │   │   │   ├── image_processing_deformable_detr.meta.json
│   │   │   │   │   ├── image_processing_deformable_detr_fast.data.json
│   │   │   │   │   ├── image_processing_deformable_detr_fast.meta.json
│   │   │   │   │   ├── modeling_deformable_detr.data.json
│   │   │   │   │   └── modeling_deformable_detr.meta.json
│   │   │   │   ├── deit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_deit.data.json
│   │   │   │   │   ├── configuration_deit.meta.json
│   │   │   │   │   ├── feature_extraction_deit.data.json
│   │   │   │   │   ├── feature_extraction_deit.meta.json
│   │   │   │   │   ├── image_processing_deit.data.json
│   │   │   │   │   ├── image_processing_deit.meta.json
│   │   │   │   │   ├── image_processing_deit_fast.data.json
│   │   │   │   │   ├── image_processing_deit_fast.meta.json
│   │   │   │   │   ├── modeling_deit.data.json
│   │   │   │   │   ├── modeling_deit.meta.json
│   │   │   │   │   ├── modeling_tf_deit.data.json
│   │   │   │   │   └── modeling_tf_deit.meta.json
│   │   │   │   ├── deprecated
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── bort
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   └── __init__.meta.json
│   │   │   │   │   ├── deta
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_deta.data.json
│   │   │   │   │   │   ├── configuration_deta.meta.json
│   │   │   │   │   │   ├── image_processing_deta.data.json
│   │   │   │   │   │   ├── image_processing_deta.meta.json
│   │   │   │   │   │   ├── modeling_deta.data.json
│   │   │   │   │   │   └── modeling_deta.meta.json
│   │   │   │   │   ├── efficientformer
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_efficientformer.data.json
│   │   │   │   │   │   ├── configuration_efficientformer.meta.json
│   │   │   │   │   │   ├── image_processing_efficientformer.data.json
│   │   │   │   │   │   ├── image_processing_efficientformer.meta.json
│   │   │   │   │   │   ├── modeling_efficientformer.data.json
│   │   │   │   │   │   ├── modeling_efficientformer.meta.json
│   │   │   │   │   │   ├── modeling_tf_efficientformer.data.json
│   │   │   │   │   │   └── modeling_tf_efficientformer.meta.json
│   │   │   │   │   ├── ernie_m
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_ernie_m.data.json
│   │   │   │   │   │   ├── configuration_ernie_m.meta.json
│   │   │   │   │   │   ├── modeling_ernie_m.data.json
│   │   │   │   │   │   ├── modeling_ernie_m.meta.json
│   │   │   │   │   │   ├── tokenization_ernie_m.data.json
│   │   │   │   │   │   └── tokenization_ernie_m.meta.json
│   │   │   │   │   ├── gptsan_japanese
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_gptsan_japanese.data.json
│   │   │   │   │   │   ├── configuration_gptsan_japanese.meta.json
│   │   │   │   │   │   ├── modeling_gptsan_japanese.data.json
│   │   │   │   │   │   ├── modeling_gptsan_japanese.meta.json
│   │   │   │   │   │   ├── tokenization_gptsan_japanese.data.json
│   │   │   │   │   │   └── tokenization_gptsan_japanese.meta.json
│   │   │   │   │   ├── graphormer
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_graphormer.data.json
│   │   │   │   │   │   ├── configuration_graphormer.meta.json
│   │   │   │   │   │   ├── modeling_graphormer.data.json
│   │   │   │   │   │   └── modeling_graphormer.meta.json
│   │   │   │   │   ├── jukebox
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_jukebox.data.json
│   │   │   │   │   │   ├── configuration_jukebox.meta.json
│   │   │   │   │   │   ├── modeling_jukebox.data.json
│   │   │   │   │   │   ├── modeling_jukebox.meta.json
│   │   │   │   │   │   ├── tokenization_jukebox.data.json
│   │   │   │   │   │   └── tokenization_jukebox.meta.json
│   │   │   │   │   ├── mctct
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_mctct.data.json
│   │   │   │   │   │   ├── configuration_mctct.meta.json
│   │   │   │   │   │   ├── feature_extraction_mctct.data.json
│   │   │   │   │   │   ├── feature_extraction_mctct.meta.json
│   │   │   │   │   │   ├── modeling_mctct.data.json
│   │   │   │   │   │   ├── modeling_mctct.meta.json
│   │   │   │   │   │   ├── processing_mctct.data.json
│   │   │   │   │   │   └── processing_mctct.meta.json
│   │   │   │   │   ├── mega
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_mega.data.json
│   │   │   │   │   │   ├── configuration_mega.meta.json
│   │   │   │   │   │   ├── modeling_mega.data.json
│   │   │   │   │   │   └── modeling_mega.meta.json
│   │   │   │   │   ├── mmbt
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_mmbt.data.json
│   │   │   │   │   │   ├── configuration_mmbt.meta.json
│   │   │   │   │   │   ├── modeling_mmbt.data.json
│   │   │   │   │   │   └── modeling_mmbt.meta.json
│   │   │   │   │   ├── nat
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_nat.data.json
│   │   │   │   │   │   ├── configuration_nat.meta.json
│   │   │   │   │   │   ├── modeling_nat.data.json
│   │   │   │   │   │   └── modeling_nat.meta.json
│   │   │   │   │   ├── nezha
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_nezha.data.json
│   │   │   │   │   │   ├── configuration_nezha.meta.json
│   │   │   │   │   │   ├── modeling_nezha.data.json
│   │   │   │   │   │   └── modeling_nezha.meta.json
│   │   │   │   │   ├── open_llama
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_open_llama.data.json
│   │   │   │   │   │   ├── configuration_open_llama.meta.json
│   │   │   │   │   │   ├── modeling_open_llama.data.json
│   │   │   │   │   │   └── modeling_open_llama.meta.json
│   │   │   │   │   ├── qdqbert
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_qdqbert.data.json
│   │   │   │   │   │   ├── configuration_qdqbert.meta.json
│   │   │   │   │   │   ├── modeling_qdqbert.data.json
│   │   │   │   │   │   └── modeling_qdqbert.meta.json
│   │   │   │   │   ├── realm
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_realm.data.json
│   │   │   │   │   │   ├── configuration_realm.meta.json
│   │   │   │   │   │   ├── modeling_realm.data.json
│   │   │   │   │   │   ├── modeling_realm.meta.json
│   │   │   │   │   │   ├── retrieval_realm.data.json
│   │   │   │   │   │   ├── retrieval_realm.meta.json
│   │   │   │   │   │   ├── tokenization_realm.data.json
│   │   │   │   │   │   ├── tokenization_realm.meta.json
│   │   │   │   │   │   ├── tokenization_realm_fast.data.json
│   │   │   │   │   │   └── tokenization_realm_fast.meta.json
│   │   │   │   │   ├── retribert
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_retribert.data.json
│   │   │   │   │   │   ├── configuration_retribert.meta.json
│   │   │   │   │   │   ├── modeling_retribert.data.json
│   │   │   │   │   │   ├── modeling_retribert.meta.json
│   │   │   │   │   │   ├── tokenization_retribert.data.json
│   │   │   │   │   │   ├── tokenization_retribert.meta.json
│   │   │   │   │   │   ├── tokenization_retribert_fast.data.json
│   │   │   │   │   │   └── tokenization_retribert_fast.meta.json
│   │   │   │   │   ├── speech_to_text_2
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_speech_to_text_2.data.json
│   │   │   │   │   │   ├── configuration_speech_to_text_2.meta.json
│   │   │   │   │   │   ├── modeling_speech_to_text_2.data.json
│   │   │   │   │   │   ├── modeling_speech_to_text_2.meta.json
│   │   │   │   │   │   ├── processing_speech_to_text_2.data.json
│   │   │   │   │   │   ├── processing_speech_to_text_2.meta.json
│   │   │   │   │   │   ├── tokenization_speech_to_text_2.data.json
│   │   │   │   │   │   └── tokenization_speech_to_text_2.meta.json
│   │   │   │   │   ├── tapex
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── tokenization_tapex.data.json
│   │   │   │   │   │   └── tokenization_tapex.meta.json
│   │   │   │   │   ├── trajectory_transformer
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_trajectory_transformer.data.json
│   │   │   │   │   │   ├── configuration_trajectory_transformer.meta.json
│   │   │   │   │   │   ├── modeling_trajectory_transformer.data.json
│   │   │   │   │   │   └── modeling_trajectory_transformer.meta.json
│   │   │   │   │   ├── transfo_xl
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_transfo_xl.data.json
│   │   │   │   │   │   ├── configuration_transfo_xl.meta.json
│   │   │   │   │   │   ├── modeling_tf_transfo_xl.data.json
│   │   │   │   │   │   ├── modeling_tf_transfo_xl.meta.json
│   │   │   │   │   │   ├── modeling_tf_transfo_xl_utilities.data.json
│   │   │   │   │   │   ├── modeling_tf_transfo_xl_utilities.meta.json
│   │   │   │   │   │   ├── modeling_transfo_xl.data.json
│   │   │   │   │   │   ├── modeling_transfo_xl.meta.json
│   │   │   │   │   │   ├── modeling_transfo_xl_utilities.data.json
│   │   │   │   │   │   ├── modeling_transfo_xl_utilities.meta.json
│   │   │   │   │   │   ├── tokenization_transfo_xl.data.json
│   │   │   │   │   │   └── tokenization_transfo_xl.meta.json
│   │   │   │   │   ├── tvlt
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_tvlt.data.json
│   │   │   │   │   │   ├── configuration_tvlt.meta.json
│   │   │   │   │   │   ├── feature_extraction_tvlt.data.json
│   │   │   │   │   │   ├── feature_extraction_tvlt.meta.json
│   │   │   │   │   │   ├── image_processing_tvlt.data.json
│   │   │   │   │   │   ├── image_processing_tvlt.meta.json
│   │   │   │   │   │   ├── modeling_tvlt.data.json
│   │   │   │   │   │   ├── modeling_tvlt.meta.json
│   │   │   │   │   │   ├── processing_tvlt.data.json
│   │   │   │   │   │   └── processing_tvlt.meta.json
│   │   │   │   │   ├── van
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_van.data.json
│   │   │   │   │   │   ├── configuration_van.meta.json
│   │   │   │   │   │   ├── modeling_van.data.json
│   │   │   │   │   │   └── modeling_van.meta.json
│   │   │   │   │   ├── vit_hybrid
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── configuration_vit_hybrid.data.json
│   │   │   │   │   │   ├── configuration_vit_hybrid.meta.json
│   │   │   │   │   │   ├── image_processing_vit_hybrid.data.json
│   │   │   │   │   │   ├── image_processing_vit_hybrid.meta.json
│   │   │   │   │   │   ├── modeling_vit_hybrid.data.json
│   │   │   │   │   │   └── modeling_vit_hybrid.meta.json
│   │   │   │   │   └── xlm_prophetnet
│   │   │   │   │       ├── __init__.data.json
│   │   │   │   │       ├── __init__.meta.json
│   │   │   │   │       ├── configuration_xlm_prophetnet.data.json
│   │   │   │   │       ├── configuration_xlm_prophetnet.meta.json
│   │   │   │   │       ├── modeling_xlm_prophetnet.data.json
│   │   │   │   │       ├── modeling_xlm_prophetnet.meta.json
│   │   │   │   │       ├── tokenization_xlm_prophetnet.data.json
│   │   │   │   │       └── tokenization_xlm_prophetnet.meta.json
│   │   │   │   ├── depth_anything
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_depth_anything.data.json
│   │   │   │   │   ├── configuration_depth_anything.meta.json
│   │   │   │   │   ├── modeling_depth_anything.data.json
│   │   │   │   │   └── modeling_depth_anything.meta.json
│   │   │   │   ├── depth_pro
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_depth_pro.data.json
│   │   │   │   │   ├── configuration_depth_pro.meta.json
│   │   │   │   │   ├── image_processing_depth_pro.data.json
│   │   │   │   │   ├── image_processing_depth_pro.meta.json
│   │   │   │   │   ├── image_processing_depth_pro_fast.data.json
│   │   │   │   │   ├── image_processing_depth_pro_fast.meta.json
│   │   │   │   │   ├── modeling_depth_pro.data.json
│   │   │   │   │   └── modeling_depth_pro.meta.json
│   │   │   │   ├── detr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_detr.data.json
│   │   │   │   │   ├── configuration_detr.meta.json
│   │   │   │   │   ├── feature_extraction_detr.data.json
│   │   │   │   │   ├── feature_extraction_detr.meta.json
│   │   │   │   │   ├── image_processing_detr.data.json
│   │   │   │   │   ├── image_processing_detr.meta.json
│   │   │   │   │   ├── image_processing_detr_fast.data.json
│   │   │   │   │   ├── image_processing_detr_fast.meta.json
│   │   │   │   │   ├── modeling_detr.data.json
│   │   │   │   │   └── modeling_detr.meta.json
│   │   │   │   ├── dia
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dia.data.json
│   │   │   │   │   ├── configuration_dia.meta.json
│   │   │   │   │   ├── feature_extraction_dia.data.json
│   │   │   │   │   ├── feature_extraction_dia.meta.json
│   │   │   │   │   ├── generation_dia.data.json
│   │   │   │   │   ├── generation_dia.meta.json
│   │   │   │   │   ├── modeling_dia.data.json
│   │   │   │   │   ├── modeling_dia.meta.json
│   │   │   │   │   ├── processing_dia.data.json
│   │   │   │   │   ├── processing_dia.meta.json
│   │   │   │   │   ├── tokenization_dia.data.json
│   │   │   │   │   └── tokenization_dia.meta.json
│   │   │   │   ├── dialogpt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── diffllama
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_diffllama.data.json
│   │   │   │   │   ├── configuration_diffllama.meta.json
│   │   │   │   │   ├── modeling_diffllama.data.json
│   │   │   │   │   └── modeling_diffllama.meta.json
│   │   │   │   ├── dinat
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dinat.data.json
│   │   │   │   │   ├── configuration_dinat.meta.json
│   │   │   │   │   ├── modeling_dinat.data.json
│   │   │   │   │   └── modeling_dinat.meta.json
│   │   │   │   ├── dinov2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dinov2.data.json
│   │   │   │   │   ├── configuration_dinov2.meta.json
│   │   │   │   │   ├── modeling_dinov2.data.json
│   │   │   │   │   ├── modeling_dinov2.meta.json
│   │   │   │   │   ├── modeling_flax_dinov2.data.json
│   │   │   │   │   └── modeling_flax_dinov2.meta.json
│   │   │   │   ├── dinov2_with_registers
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dinov2_with_registers.data.json
│   │   │   │   │   ├── configuration_dinov2_with_registers.meta.json
│   │   │   │   │   ├── modeling_dinov2_with_registers.data.json
│   │   │   │   │   └── modeling_dinov2_with_registers.meta.json
│   │   │   │   ├── distilbert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_distilbert.data.json
│   │   │   │   │   ├── configuration_distilbert.meta.json
│   │   │   │   │   ├── modeling_distilbert.data.json
│   │   │   │   │   ├── modeling_distilbert.meta.json
│   │   │   │   │   ├── modeling_flax_distilbert.data.json
│   │   │   │   │   ├── modeling_flax_distilbert.meta.json
│   │   │   │   │   ├── modeling_tf_distilbert.data.json
│   │   │   │   │   ├── modeling_tf_distilbert.meta.json
│   │   │   │   │   ├── tokenization_distilbert.data.json
│   │   │   │   │   ├── tokenization_distilbert.meta.json
│   │   │   │   │   ├── tokenization_distilbert_fast.data.json
│   │   │   │   │   └── tokenization_distilbert_fast.meta.json
│   │   │   │   ├── dit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── donut
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_donut_swin.data.json
│   │   │   │   │   ├── configuration_donut_swin.meta.json
│   │   │   │   │   ├── feature_extraction_donut.data.json
│   │   │   │   │   ├── feature_extraction_donut.meta.json
│   │   │   │   │   ├── image_processing_donut.data.json
│   │   │   │   │   ├── image_processing_donut.meta.json
│   │   │   │   │   ├── image_processing_donut_fast.data.json
│   │   │   │   │   ├── image_processing_donut_fast.meta.json
│   │   │   │   │   ├── modeling_donut_swin.data.json
│   │   │   │   │   ├── modeling_donut_swin.meta.json
│   │   │   │   │   ├── processing_donut.data.json
│   │   │   │   │   └── processing_donut.meta.json
│   │   │   │   ├── dots1
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dots1.data.json
│   │   │   │   │   ├── configuration_dots1.meta.json
│   │   │   │   │   ├── modeling_dots1.data.json
│   │   │   │   │   └── modeling_dots1.meta.json
│   │   │   │   ├── dpr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dpr.data.json
│   │   │   │   │   ├── configuration_dpr.meta.json
│   │   │   │   │   ├── modeling_dpr.data.json
│   │   │   │   │   ├── modeling_dpr.meta.json
│   │   │   │   │   ├── modeling_tf_dpr.data.json
│   │   │   │   │   ├── modeling_tf_dpr.meta.json
│   │   │   │   │   ├── tokenization_dpr.data.json
│   │   │   │   │   ├── tokenization_dpr.meta.json
│   │   │   │   │   ├── tokenization_dpr_fast.data.json
│   │   │   │   │   └── tokenization_dpr_fast.meta.json
│   │   │   │   ├── dpt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_dpt.data.json
│   │   │   │   │   ├── configuration_dpt.meta.json
│   │   │   │   │   ├── feature_extraction_dpt.data.json
│   │   │   │   │   ├── feature_extraction_dpt.meta.json
│   │   │   │   │   ├── image_processing_dpt.data.json
│   │   │   │   │   ├── image_processing_dpt.meta.json
│   │   │   │   │   ├── image_processing_dpt_fast.data.json
│   │   │   │   │   ├── image_processing_dpt_fast.meta.json
│   │   │   │   │   ├── modeling_dpt.data.json
│   │   │   │   │   └── modeling_dpt.meta.json
│   │   │   │   ├── efficientloftr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_efficientloftr.data.json
│   │   │   │   │   ├── configuration_efficientloftr.meta.json
│   │   │   │   │   ├── image_processing_efficientloftr.data.json
│   │   │   │   │   ├── image_processing_efficientloftr.meta.json
│   │   │   │   │   ├── modeling_efficientloftr.data.json
│   │   │   │   │   └── modeling_efficientloftr.meta.json
│   │   │   │   ├── efficientnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_efficientnet.data.json
│   │   │   │   │   ├── configuration_efficientnet.meta.json
│   │   │   │   │   ├── image_processing_efficientnet.data.json
│   │   │   │   │   ├── image_processing_efficientnet.meta.json
│   │   │   │   │   ├── image_processing_efficientnet_fast.data.json
│   │   │   │   │   ├── image_processing_efficientnet_fast.meta.json
│   │   │   │   │   ├── modeling_efficientnet.data.json
│   │   │   │   │   └── modeling_efficientnet.meta.json
│   │   │   │   ├── electra
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_electra.data.json
│   │   │   │   │   ├── configuration_electra.meta.json
│   │   │   │   │   ├── modeling_electra.data.json
│   │   │   │   │   ├── modeling_electra.meta.json
│   │   │   │   │   ├── modeling_flax_electra.data.json
│   │   │   │   │   ├── modeling_flax_electra.meta.json
│   │   │   │   │   ├── modeling_tf_electra.data.json
│   │   │   │   │   ├── modeling_tf_electra.meta.json
│   │   │   │   │   ├── tokenization_electra.data.json
│   │   │   │   │   ├── tokenization_electra.meta.json
│   │   │   │   │   ├── tokenization_electra_fast.data.json
│   │   │   │   │   └── tokenization_electra_fast.meta.json
│   │   │   │   ├── emu3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_emu3.data.json
│   │   │   │   │   ├── configuration_emu3.meta.json
│   │   │   │   │   ├── image_processing_emu3.data.json
│   │   │   │   │   ├── image_processing_emu3.meta.json
│   │   │   │   │   ├── modeling_emu3.data.json
│   │   │   │   │   ├── modeling_emu3.meta.json
│   │   │   │   │   ├── processing_emu3.data.json
│   │   │   │   │   └── processing_emu3.meta.json
│   │   │   │   ├── encodec
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_encodec.data.json
│   │   │   │   │   ├── configuration_encodec.meta.json
│   │   │   │   │   ├── feature_extraction_encodec.data.json
│   │   │   │   │   ├── feature_extraction_encodec.meta.json
│   │   │   │   │   ├── modeling_encodec.data.json
│   │   │   │   │   └── modeling_encodec.meta.json
│   │   │   │   ├── encoder_decoder
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_encoder_decoder.data.json
│   │   │   │   │   ├── configuration_encoder_decoder.meta.json
│   │   │   │   │   ├── modeling_encoder_decoder.data.json
│   │   │   │   │   ├── modeling_encoder_decoder.meta.json
│   │   │   │   │   ├── modeling_flax_encoder_decoder.data.json
│   │   │   │   │   ├── modeling_flax_encoder_decoder.meta.json
│   │   │   │   │   ├── modeling_tf_encoder_decoder.data.json
│   │   │   │   │   └── modeling_tf_encoder_decoder.meta.json
│   │   │   │   ├── ernie
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_ernie.data.json
│   │   │   │   │   ├── configuration_ernie.meta.json
│   │   │   │   │   ├── modeling_ernie.data.json
│   │   │   │   │   └── modeling_ernie.meta.json
│   │   │   │   ├── esm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_esm.data.json
│   │   │   │   │   ├── configuration_esm.meta.json
│   │   │   │   │   ├── modeling_esm.data.json
│   │   │   │   │   ├── modeling_esm.meta.json
│   │   │   │   │   ├── modeling_esmfold.data.json
│   │   │   │   │   ├── modeling_esmfold.meta.json
│   │   │   │   │   ├── modeling_tf_esm.data.json
│   │   │   │   │   ├── modeling_tf_esm.meta.json
│   │   │   │   │   ├── openfold_utils
│   │   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   │   ├── chunk_utils.data.json
│   │   │   │   │   │   ├── chunk_utils.meta.json
│   │   │   │   │   │   ├── data_transforms.data.json
│   │   │   │   │   │   ├── data_transforms.meta.json
│   │   │   │   │   │   ├── feats.data.json
│   │   │   │   │   │   ├── feats.meta.json
│   │   │   │   │   │   ├── loss.data.json
│   │   │   │   │   │   ├── loss.meta.json
│   │   │   │   │   │   ├── protein.data.json
│   │   │   │   │   │   ├── protein.meta.json
│   │   │   │   │   │   ├── residue_constants.data.json
│   │   │   │   │   │   ├── residue_constants.meta.json
│   │   │   │   │   │   ├── rigid_utils.data.json
│   │   │   │   │   │   ├── rigid_utils.meta.json
│   │   │   │   │   │   ├── tensor_utils.data.json
│   │   │   │   │   │   └── tensor_utils.meta.json
│   │   │   │   │   ├── tokenization_esm.data.json
│   │   │   │   │   └── tokenization_esm.meta.json
│   │   │   │   ├── evolla
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_evolla.data.json
│   │   │   │   │   ├── configuration_evolla.meta.json
│   │   │   │   │   ├── modeling_evolla.data.json
│   │   │   │   │   ├── modeling_evolla.meta.json
│   │   │   │   │   ├── processing_evolla.data.json
│   │   │   │   │   └── processing_evolla.meta.json
│   │   │   │   ├── exaone4
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_exaone4.data.json
│   │   │   │   │   ├── configuration_exaone4.meta.json
│   │   │   │   │   ├── modeling_exaone4.data.json
│   │   │   │   │   └── modeling_exaone4.meta.json
│   │   │   │   ├── falcon
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_falcon.data.json
│   │   │   │   │   ├── configuration_falcon.meta.json
│   │   │   │   │   ├── modeling_falcon.data.json
│   │   │   │   │   └── modeling_falcon.meta.json
│   │   │   │   ├── falcon_h1
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_falcon_h1.data.json
│   │   │   │   │   ├── configuration_falcon_h1.meta.json
│   │   │   │   │   ├── modeling_falcon_h1.data.json
│   │   │   │   │   └── modeling_falcon_h1.meta.json
│   │   │   │   ├── falcon_mamba
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_falcon_mamba.data.json
│   │   │   │   │   ├── configuration_falcon_mamba.meta.json
│   │   │   │   │   ├── modeling_falcon_mamba.data.json
│   │   │   │   │   └── modeling_falcon_mamba.meta.json
│   │   │   │   ├── fastspeech2_conformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_fastspeech2_conformer.data.json
│   │   │   │   │   ├── configuration_fastspeech2_conformer.meta.json
│   │   │   │   │   ├── modeling_fastspeech2_conformer.data.json
│   │   │   │   │   ├── modeling_fastspeech2_conformer.meta.json
│   │   │   │   │   ├── tokenization_fastspeech2_conformer.data.json
│   │   │   │   │   └── tokenization_fastspeech2_conformer.meta.json
│   │   │   │   ├── flaubert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_flaubert.data.json
│   │   │   │   │   ├── configuration_flaubert.meta.json
│   │   │   │   │   ├── modeling_flaubert.data.json
│   │   │   │   │   ├── modeling_flaubert.meta.json
│   │   │   │   │   ├── modeling_tf_flaubert.data.json
│   │   │   │   │   ├── modeling_tf_flaubert.meta.json
│   │   │   │   │   ├── tokenization_flaubert.data.json
│   │   │   │   │   └── tokenization_flaubert.meta.json
│   │   │   │   ├── flava
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_flava.data.json
│   │   │   │   │   ├── configuration_flava.meta.json
│   │   │   │   │   ├── feature_extraction_flava.data.json
│   │   │   │   │   ├── feature_extraction_flava.meta.json
│   │   │   │   │   ├── image_processing_flava.data.json
│   │   │   │   │   ├── image_processing_flava.meta.json
│   │   │   │   │   ├── image_processing_flava_fast.data.json
│   │   │   │   │   ├── image_processing_flava_fast.meta.json
│   │   │   │   │   ├── modeling_flava.data.json
│   │   │   │   │   ├── modeling_flava.meta.json
│   │   │   │   │   ├── processing_flava.data.json
│   │   │   │   │   └── processing_flava.meta.json
│   │   │   │   ├── fnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_fnet.data.json
│   │   │   │   │   ├── configuration_fnet.meta.json
│   │   │   │   │   ├── modeling_fnet.data.json
│   │   │   │   │   ├── modeling_fnet.meta.json
│   │   │   │   │   ├── tokenization_fnet.data.json
│   │   │   │   │   ├── tokenization_fnet.meta.json
│   │   │   │   │   ├── tokenization_fnet_fast.data.json
│   │   │   │   │   └── tokenization_fnet_fast.meta.json
│   │   │   │   ├── focalnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_focalnet.data.json
│   │   │   │   │   ├── configuration_focalnet.meta.json
│   │   │   │   │   ├── modeling_focalnet.data.json
│   │   │   │   │   └── modeling_focalnet.meta.json
│   │   │   │   ├── fsmt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_fsmt.data.json
│   │   │   │   │   ├── configuration_fsmt.meta.json
│   │   │   │   │   ├── modeling_fsmt.data.json
│   │   │   │   │   ├── modeling_fsmt.meta.json
│   │   │   │   │   ├── tokenization_fsmt.data.json
│   │   │   │   │   └── tokenization_fsmt.meta.json
│   │   │   │   ├── funnel
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_funnel.data.json
│   │   │   │   │   ├── configuration_funnel.meta.json
│   │   │   │   │   ├── modeling_funnel.data.json
│   │   │   │   │   ├── modeling_funnel.meta.json
│   │   │   │   │   ├── modeling_tf_funnel.data.json
│   │   │   │   │   ├── modeling_tf_funnel.meta.json
│   │   │   │   │   ├── tokenization_funnel.data.json
│   │   │   │   │   ├── tokenization_funnel.meta.json
│   │   │   │   │   ├── tokenization_funnel_fast.data.json
│   │   │   │   │   └── tokenization_funnel_fast.meta.json
│   │   │   │   ├── fuyu
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_fuyu.data.json
│   │   │   │   │   ├── configuration_fuyu.meta.json
│   │   │   │   │   ├── image_processing_fuyu.data.json
│   │   │   │   │   ├── image_processing_fuyu.meta.json
│   │   │   │   │   ├── modeling_fuyu.data.json
│   │   │   │   │   ├── modeling_fuyu.meta.json
│   │   │   │   │   ├── processing_fuyu.data.json
│   │   │   │   │   └── processing_fuyu.meta.json
│   │   │   │   ├── gemma
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gemma.data.json
│   │   │   │   │   ├── configuration_gemma.meta.json
│   │   │   │   │   ├── modeling_flax_gemma.data.json
│   │   │   │   │   ├── modeling_flax_gemma.meta.json
│   │   │   │   │   ├── modeling_gemma.data.json
│   │   │   │   │   ├── modeling_gemma.meta.json
│   │   │   │   │   ├── tokenization_gemma.data.json
│   │   │   │   │   ├── tokenization_gemma.meta.json
│   │   │   │   │   ├── tokenization_gemma_fast.data.json
│   │   │   │   │   └── tokenization_gemma_fast.meta.json
│   │   │   │   ├── gemma2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gemma2.data.json
│   │   │   │   │   ├── configuration_gemma2.meta.json
│   │   │   │   │   ├── modeling_gemma2.data.json
│   │   │   │   │   └── modeling_gemma2.meta.json
│   │   │   │   ├── gemma3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gemma3.data.json
│   │   │   │   │   ├── configuration_gemma3.meta.json
│   │   │   │   │   ├── image_processing_gemma3.data.json
│   │   │   │   │   ├── image_processing_gemma3.meta.json
│   │   │   │   │   ├── image_processing_gemma3_fast.data.json
│   │   │   │   │   ├── image_processing_gemma3_fast.meta.json
│   │   │   │   │   ├── modeling_gemma3.data.json
│   │   │   │   │   ├── modeling_gemma3.meta.json
│   │   │   │   │   ├── processing_gemma3.data.json
│   │   │   │   │   └── processing_gemma3.meta.json
│   │   │   │   ├── git
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_git.data.json
│   │   │   │   │   ├── configuration_git.meta.json
│   │   │   │   │   ├── modeling_git.data.json
│   │   │   │   │   ├── modeling_git.meta.json
│   │   │   │   │   ├── processing_git.data.json
│   │   │   │   │   └── processing_git.meta.json
│   │   │   │   ├── glm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_glm.data.json
│   │   │   │   │   ├── configuration_glm.meta.json
│   │   │   │   │   ├── modeling_glm.data.json
│   │   │   │   │   └── modeling_glm.meta.json
│   │   │   │   ├── glm4
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_glm4.data.json
│   │   │   │   │   ├── configuration_glm4.meta.json
│   │   │   │   │   ├── modeling_glm4.data.json
│   │   │   │   │   └── modeling_glm4.meta.json
│   │   │   │   ├── glpn
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_glpn.data.json
│   │   │   │   │   ├── configuration_glpn.meta.json
│   │   │   │   │   ├── feature_extraction_glpn.data.json
│   │   │   │   │   ├── feature_extraction_glpn.meta.json
│   │   │   │   │   ├── image_processing_glpn.data.json
│   │   │   │   │   ├── image_processing_glpn.meta.json
│   │   │   │   │   ├── modeling_glpn.data.json
│   │   │   │   │   └── modeling_glpn.meta.json
│   │   │   │   ├── got_ocr2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_got_ocr2.data.json
│   │   │   │   │   ├── configuration_got_ocr2.meta.json
│   │   │   │   │   ├── image_processing_got_ocr2.data.json
│   │   │   │   │   ├── image_processing_got_ocr2.meta.json
│   │   │   │   │   ├── image_processing_got_ocr2_fast.data.json
│   │   │   │   │   ├── image_processing_got_ocr2_fast.meta.json
│   │   │   │   │   ├── modeling_got_ocr2.data.json
│   │   │   │   │   ├── modeling_got_ocr2.meta.json
│   │   │   │   │   ├── processing_got_ocr2.data.json
│   │   │   │   │   └── processing_got_ocr2.meta.json
│   │   │   │   ├── gpt2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gpt2.data.json
│   │   │   │   │   ├── configuration_gpt2.meta.json
│   │   │   │   │   ├── modeling_flax_gpt2.data.json
│   │   │   │   │   ├── modeling_flax_gpt2.meta.json
│   │   │   │   │   ├── modeling_gpt2.data.json
│   │   │   │   │   ├── modeling_gpt2.meta.json
│   │   │   │   │   ├── modeling_tf_gpt2.data.json
│   │   │   │   │   ├── modeling_tf_gpt2.meta.json
│   │   │   │   │   ├── tokenization_gpt2.data.json
│   │   │   │   │   ├── tokenization_gpt2.meta.json
│   │   │   │   │   ├── tokenization_gpt2_fast.data.json
│   │   │   │   │   ├── tokenization_gpt2_fast.meta.json
│   │   │   │   │   ├── tokenization_gpt2_tf.data.json
│   │   │   │   │   └── tokenization_gpt2_tf.meta.json
│   │   │   │   ├── gpt_bigcode
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gpt_bigcode.data.json
│   │   │   │   │   ├── configuration_gpt_bigcode.meta.json
│   │   │   │   │   ├── modeling_gpt_bigcode.data.json
│   │   │   │   │   └── modeling_gpt_bigcode.meta.json
│   │   │   │   ├── gpt_neo
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gpt_neo.data.json
│   │   │   │   │   ├── configuration_gpt_neo.meta.json
│   │   │   │   │   ├── modeling_flax_gpt_neo.data.json
│   │   │   │   │   ├── modeling_flax_gpt_neo.meta.json
│   │   │   │   │   ├── modeling_gpt_neo.data.json
│   │   │   │   │   └── modeling_gpt_neo.meta.json
│   │   │   │   ├── gpt_neox
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gpt_neox.data.json
│   │   │   │   │   ├── configuration_gpt_neox.meta.json
│   │   │   │   │   ├── modeling_gpt_neox.data.json
│   │   │   │   │   ├── modeling_gpt_neox.meta.json
│   │   │   │   │   ├── tokenization_gpt_neox_fast.data.json
│   │   │   │   │   └── tokenization_gpt_neox_fast.meta.json
│   │   │   │   ├── gpt_neox_japanese
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gpt_neox_japanese.data.json
│   │   │   │   │   ├── configuration_gpt_neox_japanese.meta.json
│   │   │   │   │   ├── modeling_gpt_neox_japanese.data.json
│   │   │   │   │   ├── modeling_gpt_neox_japanese.meta.json
│   │   │   │   │   ├── tokenization_gpt_neox_japanese.data.json
│   │   │   │   │   └── tokenization_gpt_neox_japanese.meta.json
│   │   │   │   ├── gpt_sw3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_gpt_sw3.data.json
│   │   │   │   │   └── tokenization_gpt_sw3.meta.json
│   │   │   │   ├── gptj
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_gptj.data.json
│   │   │   │   │   ├── configuration_gptj.meta.json
│   │   │   │   │   ├── modeling_flax_gptj.data.json
│   │   │   │   │   ├── modeling_flax_gptj.meta.json
│   │   │   │   │   ├── modeling_gptj.data.json
│   │   │   │   │   ├── modeling_gptj.meta.json
│   │   │   │   │   ├── modeling_tf_gptj.data.json
│   │   │   │   │   └── modeling_tf_gptj.meta.json
│   │   │   │   ├── granite
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_granite.data.json
│   │   │   │   │   ├── configuration_granite.meta.json
│   │   │   │   │   ├── modeling_granite.data.json
│   │   │   │   │   └── modeling_granite.meta.json
│   │   │   │   ├── granite_speech
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_granite_speech.data.json
│   │   │   │   │   ├── configuration_granite_speech.meta.json
│   │   │   │   │   ├── feature_extraction_granite_speech.data.json
│   │   │   │   │   ├── feature_extraction_granite_speech.meta.json
│   │   │   │   │   ├── modeling_granite_speech.data.json
│   │   │   │   │   ├── modeling_granite_speech.meta.json
│   │   │   │   │   ├── processing_granite_speech.data.json
│   │   │   │   │   └── processing_granite_speech.meta.json
│   │   │   │   ├── granitemoe
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_granitemoe.data.json
│   │   │   │   │   ├── configuration_granitemoe.meta.json
│   │   │   │   │   ├── modeling_granitemoe.data.json
│   │   │   │   │   └── modeling_granitemoe.meta.json
│   │   │   │   ├── granitemoehybrid
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_granitemoehybrid.data.json
│   │   │   │   │   ├── configuration_granitemoehybrid.meta.json
│   │   │   │   │   ├── modeling_granitemoehybrid.data.json
│   │   │   │   │   └── modeling_granitemoehybrid.meta.json
│   │   │   │   ├── granitemoeshared
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_granitemoeshared.data.json
│   │   │   │   │   ├── configuration_granitemoeshared.meta.json
│   │   │   │   │   ├── modeling_granitemoeshared.data.json
│   │   │   │   │   └── modeling_granitemoeshared.meta.json
│   │   │   │   ├── grounding_dino
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_grounding_dino.data.json
│   │   │   │   │   ├── configuration_grounding_dino.meta.json
│   │   │   │   │   ├── image_processing_grounding_dino.data.json
│   │   │   │   │   ├── image_processing_grounding_dino.meta.json
│   │   │   │   │   ├── image_processing_grounding_dino_fast.data.json
│   │   │   │   │   ├── image_processing_grounding_dino_fast.meta.json
│   │   │   │   │   ├── modeling_grounding_dino.data.json
│   │   │   │   │   ├── modeling_grounding_dino.meta.json
│   │   │   │   │   ├── processing_grounding_dino.data.json
│   │   │   │   │   └── processing_grounding_dino.meta.json
│   │   │   │   ├── groupvit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_groupvit.data.json
│   │   │   │   │   ├── configuration_groupvit.meta.json
│   │   │   │   │   ├── modeling_groupvit.data.json
│   │   │   │   │   ├── modeling_groupvit.meta.json
│   │   │   │   │   ├── modeling_tf_groupvit.data.json
│   │   │   │   │   └── modeling_tf_groupvit.meta.json
│   │   │   │   ├── helium
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_helium.data.json
│   │   │   │   │   ├── configuration_helium.meta.json
│   │   │   │   │   ├── modeling_helium.data.json
│   │   │   │   │   └── modeling_helium.meta.json
│   │   │   │   ├── herbert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_herbert.data.json
│   │   │   │   │   ├── tokenization_herbert.meta.json
│   │   │   │   │   ├── tokenization_herbert_fast.data.json
│   │   │   │   │   └── tokenization_herbert_fast.meta.json
│   │   │   │   ├── hgnet_v2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_hgnet_v2.data.json
│   │   │   │   │   ├── configuration_hgnet_v2.meta.json
│   │   │   │   │   ├── modeling_hgnet_v2.data.json
│   │   │   │   │   └── modeling_hgnet_v2.meta.json
│   │   │   │   ├── hiera
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_hiera.data.json
│   │   │   │   │   ├── configuration_hiera.meta.json
│   │   │   │   │   ├── modeling_hiera.data.json
│   │   │   │   │   └── modeling_hiera.meta.json
│   │   │   │   ├── hubert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_hubert.data.json
│   │   │   │   │   ├── configuration_hubert.meta.json
│   │   │   │   │   ├── modeling_hubert.data.json
│   │   │   │   │   ├── modeling_hubert.meta.json
│   │   │   │   │   ├── modeling_tf_hubert.data.json
│   │   │   │   │   └── modeling_tf_hubert.meta.json
│   │   │   │   ├── ibert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_ibert.data.json
│   │   │   │   │   ├── configuration_ibert.meta.json
│   │   │   │   │   ├── modeling_ibert.data.json
│   │   │   │   │   ├── modeling_ibert.meta.json
│   │   │   │   │   ├── quant_modules.data.json
│   │   │   │   │   └── quant_modules.meta.json
│   │   │   │   ├── idefics
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_idefics.data.json
│   │   │   │   │   ├── configuration_idefics.meta.json
│   │   │   │   │   ├── image_processing_idefics.data.json
│   │   │   │   │   ├── image_processing_idefics.meta.json
│   │   │   │   │   ├── modeling_idefics.data.json
│   │   │   │   │   ├── modeling_idefics.meta.json
│   │   │   │   │   ├── modeling_tf_idefics.data.json
│   │   │   │   │   ├── modeling_tf_idefics.meta.json
│   │   │   │   │   ├── perceiver.data.json
│   │   │   │   │   ├── perceiver.meta.json
│   │   │   │   │   ├── perceiver_tf.data.json
│   │   │   │   │   ├── perceiver_tf.meta.json
│   │   │   │   │   ├── processing_idefics.data.json
│   │   │   │   │   ├── processing_idefics.meta.json
│   │   │   │   │   ├── vision.data.json
│   │   │   │   │   ├── vision.meta.json
│   │   │   │   │   ├── vision_tf.data.json
│   │   │   │   │   └── vision_tf.meta.json
│   │   │   │   ├── idefics2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_idefics2.data.json
│   │   │   │   │   ├── configuration_idefics2.meta.json
│   │   │   │   │   ├── image_processing_idefics2.data.json
│   │   │   │   │   ├── image_processing_idefics2.meta.json
│   │   │   │   │   ├── image_processing_idefics2_fast.data.json
│   │   │   │   │   ├── image_processing_idefics2_fast.meta.json
│   │   │   │   │   ├── modeling_idefics2.data.json
│   │   │   │   │   ├── modeling_idefics2.meta.json
│   │   │   │   │   ├── processing_idefics2.data.json
│   │   │   │   │   └── processing_idefics2.meta.json
│   │   │   │   ├── idefics3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_idefics3.data.json
│   │   │   │   │   ├── configuration_idefics3.meta.json
│   │   │   │   │   ├── image_processing_idefics3.data.json
│   │   │   │   │   ├── image_processing_idefics3.meta.json
│   │   │   │   │   ├── image_processing_idefics3_fast.data.json
│   │   │   │   │   ├── image_processing_idefics3_fast.meta.json
│   │   │   │   │   ├── modeling_idefics3.data.json
│   │   │   │   │   ├── modeling_idefics3.meta.json
│   │   │   │   │   ├── processing_idefics3.data.json
│   │   │   │   │   └── processing_idefics3.meta.json
│   │   │   │   ├── ijepa
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_ijepa.data.json
│   │   │   │   │   ├── configuration_ijepa.meta.json
│   │   │   │   │   ├── modeling_ijepa.data.json
│   │   │   │   │   └── modeling_ijepa.meta.json
│   │   │   │   ├── imagegpt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_imagegpt.data.json
│   │   │   │   │   ├── configuration_imagegpt.meta.json
│   │   │   │   │   ├── feature_extraction_imagegpt.data.json
│   │   │   │   │   ├── feature_extraction_imagegpt.meta.json
│   │   │   │   │   ├── image_processing_imagegpt.data.json
│   │   │   │   │   ├── image_processing_imagegpt.meta.json
│   │   │   │   │   ├── modeling_imagegpt.data.json
│   │   │   │   │   └── modeling_imagegpt.meta.json
│   │   │   │   ├── informer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_informer.data.json
│   │   │   │   │   ├── configuration_informer.meta.json
│   │   │   │   │   ├── modeling_informer.data.json
│   │   │   │   │   └── modeling_informer.meta.json
│   │   │   │   ├── instructblip
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_instructblip.data.json
│   │   │   │   │   ├── configuration_instructblip.meta.json
│   │   │   │   │   ├── modeling_instructblip.data.json
│   │   │   │   │   ├── modeling_instructblip.meta.json
│   │   │   │   │   ├── processing_instructblip.data.json
│   │   │   │   │   └── processing_instructblip.meta.json
│   │   │   │   ├── instructblipvideo
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_instructblipvideo.data.json
│   │   │   │   │   ├── configuration_instructblipvideo.meta.json
│   │   │   │   │   ├── image_processing_instructblipvideo.data.json
│   │   │   │   │   ├── image_processing_instructblipvideo.meta.json
│   │   │   │   │   ├── modeling_instructblipvideo.data.json
│   │   │   │   │   ├── modeling_instructblipvideo.meta.json
│   │   │   │   │   ├── processing_instructblipvideo.data.json
│   │   │   │   │   ├── processing_instructblipvideo.meta.json
│   │   │   │   │   ├── video_processing_instructblipvideo.data.json
│   │   │   │   │   └── video_processing_instructblipvideo.meta.json
│   │   │   │   ├── internvl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_internvl.data.json
│   │   │   │   │   ├── configuration_internvl.meta.json
│   │   │   │   │   ├── modeling_internvl.data.json
│   │   │   │   │   ├── modeling_internvl.meta.json
│   │   │   │   │   ├── processing_internvl.data.json
│   │   │   │   │   ├── processing_internvl.meta.json
│   │   │   │   │   ├── video_processing_internvl.data.json
│   │   │   │   │   └── video_processing_internvl.meta.json
│   │   │   │   ├── jamba
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_jamba.data.json
│   │   │   │   │   ├── configuration_jamba.meta.json
│   │   │   │   │   ├── modeling_jamba.data.json
│   │   │   │   │   └── modeling_jamba.meta.json
│   │   │   │   ├── janus
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_janus.data.json
│   │   │   │   │   ├── configuration_janus.meta.json
│   │   │   │   │   ├── image_processing_janus.data.json
│   │   │   │   │   ├── image_processing_janus.meta.json
│   │   │   │   │   ├── modeling_janus.data.json
│   │   │   │   │   ├── modeling_janus.meta.json
│   │   │   │   │   ├── processing_janus.data.json
│   │   │   │   │   └── processing_janus.meta.json
│   │   │   │   ├── jetmoe
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_jetmoe.data.json
│   │   │   │   │   ├── configuration_jetmoe.meta.json
│   │   │   │   │   ├── modeling_jetmoe.data.json
│   │   │   │   │   └── modeling_jetmoe.meta.json
│   │   │   │   ├── kosmos2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_kosmos2.data.json
│   │   │   │   │   ├── configuration_kosmos2.meta.json
│   │   │   │   │   ├── modeling_kosmos2.data.json
│   │   │   │   │   ├── modeling_kosmos2.meta.json
│   │   │   │   │   ├── processing_kosmos2.data.json
│   │   │   │   │   └── processing_kosmos2.meta.json
│   │   │   │   ├── kyutai_speech_to_text
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_kyutai_speech_to_text.data.json
│   │   │   │   │   ├── configuration_kyutai_speech_to_text.meta.json
│   │   │   │   │   ├── feature_extraction_kyutai_speech_to_text.data.json
│   │   │   │   │   ├── feature_extraction_kyutai_speech_to_text.meta.json
│   │   │   │   │   ├── modeling_kyutai_speech_to_text.data.json
│   │   │   │   │   ├── modeling_kyutai_speech_to_text.meta.json
│   │   │   │   │   ├── processing_kyutai_speech_to_text.data.json
│   │   │   │   │   └── processing_kyutai_speech_to_text.meta.json
│   │   │   │   ├── layoutlm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_layoutlm.data.json
│   │   │   │   │   ├── configuration_layoutlm.meta.json
│   │   │   │   │   ├── modeling_layoutlm.data.json
│   │   │   │   │   ├── modeling_layoutlm.meta.json
│   │   │   │   │   ├── modeling_tf_layoutlm.data.json
│   │   │   │   │   ├── modeling_tf_layoutlm.meta.json
│   │   │   │   │   ├── tokenization_layoutlm.data.json
│   │   │   │   │   ├── tokenization_layoutlm.meta.json
│   │   │   │   │   ├── tokenization_layoutlm_fast.data.json
│   │   │   │   │   └── tokenization_layoutlm_fast.meta.json
│   │   │   │   ├── layoutlmv2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_layoutlmv2.data.json
│   │   │   │   │   ├── configuration_layoutlmv2.meta.json
│   │   │   │   │   ├── feature_extraction_layoutlmv2.data.json
│   │   │   │   │   ├── feature_extraction_layoutlmv2.meta.json
│   │   │   │   │   ├── image_processing_layoutlmv2.data.json
│   │   │   │   │   ├── image_processing_layoutlmv2.meta.json
│   │   │   │   │   ├── image_processing_layoutlmv2_fast.data.json
│   │   │   │   │   ├── image_processing_layoutlmv2_fast.meta.json
│   │   │   │   │   ├── modeling_layoutlmv2.data.json
│   │   │   │   │   ├── modeling_layoutlmv2.meta.json
│   │   │   │   │   ├── processing_layoutlmv2.data.json
│   │   │   │   │   ├── processing_layoutlmv2.meta.json
│   │   │   │   │   ├── tokenization_layoutlmv2.data.json
│   │   │   │   │   ├── tokenization_layoutlmv2.meta.json
│   │   │   │   │   ├── tokenization_layoutlmv2_fast.data.json
│   │   │   │   │   └── tokenization_layoutlmv2_fast.meta.json
│   │   │   │   ├── layoutlmv3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_layoutlmv3.data.json
│   │   │   │   │   ├── configuration_layoutlmv3.meta.json
│   │   │   │   │   ├── feature_extraction_layoutlmv3.data.json
│   │   │   │   │   ├── feature_extraction_layoutlmv3.meta.json
│   │   │   │   │   ├── image_processing_layoutlmv3.data.json
│   │   │   │   │   ├── image_processing_layoutlmv3.meta.json
│   │   │   │   │   ├── image_processing_layoutlmv3_fast.data.json
│   │   │   │   │   ├── image_processing_layoutlmv3_fast.meta.json
│   │   │   │   │   ├── modeling_layoutlmv3.data.json
│   │   │   │   │   ├── modeling_layoutlmv3.meta.json
│   │   │   │   │   ├── modeling_tf_layoutlmv3.data.json
│   │   │   │   │   ├── modeling_tf_layoutlmv3.meta.json
│   │   │   │   │   ├── processing_layoutlmv3.data.json
│   │   │   │   │   ├── processing_layoutlmv3.meta.json
│   │   │   │   │   ├── tokenization_layoutlmv3.data.json
│   │   │   │   │   ├── tokenization_layoutlmv3.meta.json
│   │   │   │   │   ├── tokenization_layoutlmv3_fast.data.json
│   │   │   │   │   └── tokenization_layoutlmv3_fast.meta.json
│   │   │   │   ├── layoutxlm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── processing_layoutxlm.data.json
│   │   │   │   │   ├── processing_layoutxlm.meta.json
│   │   │   │   │   ├── tokenization_layoutxlm.data.json
│   │   │   │   │   ├── tokenization_layoutxlm.meta.json
│   │   │   │   │   ├── tokenization_layoutxlm_fast.data.json
│   │   │   │   │   └── tokenization_layoutxlm_fast.meta.json
│   │   │   │   ├── led
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_led.data.json
│   │   │   │   │   ├── configuration_led.meta.json
│   │   │   │   │   ├── modeling_led.data.json
│   │   │   │   │   ├── modeling_led.meta.json
│   │   │   │   │   ├── modeling_tf_led.data.json
│   │   │   │   │   ├── modeling_tf_led.meta.json
│   │   │   │   │   ├── tokenization_led.data.json
│   │   │   │   │   ├── tokenization_led.meta.json
│   │   │   │   │   ├── tokenization_led_fast.data.json
│   │   │   │   │   └── tokenization_led_fast.meta.json
│   │   │   │   ├── levit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_levit.data.json
│   │   │   │   │   ├── configuration_levit.meta.json
│   │   │   │   │   ├── feature_extraction_levit.data.json
│   │   │   │   │   ├── feature_extraction_levit.meta.json
│   │   │   │   │   ├── image_processing_levit.data.json
│   │   │   │   │   ├── image_processing_levit.meta.json
│   │   │   │   │   ├── image_processing_levit_fast.data.json
│   │   │   │   │   ├── image_processing_levit_fast.meta.json
│   │   │   │   │   ├── modeling_levit.data.json
│   │   │   │   │   └── modeling_levit.meta.json
│   │   │   │   ├── lfm2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_lfm2.data.json
│   │   │   │   │   ├── configuration_lfm2.meta.json
│   │   │   │   │   ├── modeling_lfm2.data.json
│   │   │   │   │   └── modeling_lfm2.meta.json
│   │   │   │   ├── lightglue
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_lightglue.data.json
│   │   │   │   │   ├── configuration_lightglue.meta.json
│   │   │   │   │   ├── image_processing_lightglue.data.json
│   │   │   │   │   ├── image_processing_lightglue.meta.json
│   │   │   │   │   ├── modeling_lightglue.data.json
│   │   │   │   │   └── modeling_lightglue.meta.json
│   │   │   │   ├── lilt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_lilt.data.json
│   │   │   │   │   ├── configuration_lilt.meta.json
│   │   │   │   │   ├── modeling_lilt.data.json
│   │   │   │   │   └── modeling_lilt.meta.json
│   │   │   │   ├── llama
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_llama.data.json
│   │   │   │   │   ├── configuration_llama.meta.json
│   │   │   │   │   ├── modeling_flax_llama.data.json
│   │   │   │   │   ├── modeling_flax_llama.meta.json
│   │   │   │   │   ├── modeling_llama.data.json
│   │   │   │   │   ├── modeling_llama.meta.json
│   │   │   │   │   ├── tokenization_llama.data.json
│   │   │   │   │   ├── tokenization_llama.meta.json
│   │   │   │   │   ├── tokenization_llama_fast.data.json
│   │   │   │   │   └── tokenization_llama_fast.meta.json
│   │   │   │   ├── llama4
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_llama4.data.json
│   │   │   │   │   ├── configuration_llama4.meta.json
│   │   │   │   │   ├── image_processing_llama4_fast.data.json
│   │   │   │   │   ├── image_processing_llama4_fast.meta.json
│   │   │   │   │   ├── modeling_llama4.data.json
│   │   │   │   │   ├── modeling_llama4.meta.json
│   │   │   │   │   ├── processing_llama4.data.json
│   │   │   │   │   └── processing_llama4.meta.json
│   │   │   │   ├── llava
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_llava.data.json
│   │   │   │   │   ├── configuration_llava.meta.json
│   │   │   │   │   ├── image_processing_llava_fast.data.json
│   │   │   │   │   ├── image_processing_llava_fast.meta.json
│   │   │   │   │   ├── modeling_llava.data.json
│   │   │   │   │   ├── modeling_llava.meta.json
│   │   │   │   │   ├── processing_llava.data.json
│   │   │   │   │   └── processing_llava.meta.json
│   │   │   │   ├── llava_next
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_llava_next.data.json
│   │   │   │   │   ├── configuration_llava_next.meta.json
│   │   │   │   │   ├── image_processing_llava_next.data.json
│   │   │   │   │   ├── image_processing_llava_next.meta.json
│   │   │   │   │   ├── image_processing_llava_next_fast.data.json
│   │   │   │   │   ├── image_processing_llava_next_fast.meta.json
│   │   │   │   │   ├── modeling_llava_next.data.json
│   │   │   │   │   ├── modeling_llava_next.meta.json
│   │   │   │   │   ├── processing_llava_next.data.json
│   │   │   │   │   └── processing_llava_next.meta.json
│   │   │   │   ├── llava_next_video
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_llava_next_video.data.json
│   │   │   │   │   ├── configuration_llava_next_video.meta.json
│   │   │   │   │   ├── image_processing_llava_next_video.data.json
│   │   │   │   │   ├── image_processing_llava_next_video.meta.json
│   │   │   │   │   ├── modeling_llava_next_video.data.json
│   │   │   │   │   ├── modeling_llava_next_video.meta.json
│   │   │   │   │   ├── processing_llava_next_video.data.json
│   │   │   │   │   └── processing_llava_next_video.meta.json
│   │   │   │   ├── llava_onevision
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_llava_onevision.data.json
│   │   │   │   │   ├── configuration_llava_onevision.meta.json
│   │   │   │   │   ├── image_processing_llava_onevision.data.json
│   │   │   │   │   ├── image_processing_llava_onevision.meta.json
│   │   │   │   │   ├── image_processing_llava_onevision_fast.data.json
│   │   │   │   │   ├── image_processing_llava_onevision_fast.meta.json
│   │   │   │   │   ├── modeling_llava_onevision.data.json
│   │   │   │   │   ├── modeling_llava_onevision.meta.json
│   │   │   │   │   ├── processing_llava_onevision.data.json
│   │   │   │   │   ├── processing_llava_onevision.meta.json
│   │   │   │   │   ├── video_processing_llava_onevision.data.json
│   │   │   │   │   └── video_processing_llava_onevision.meta.json
│   │   │   │   ├── longformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_longformer.data.json
│   │   │   │   │   ├── configuration_longformer.meta.json
│   │   │   │   │   ├── modeling_longformer.data.json
│   │   │   │   │   ├── modeling_longformer.meta.json
│   │   │   │   │   ├── modeling_tf_longformer.data.json
│   │   │   │   │   ├── modeling_tf_longformer.meta.json
│   │   │   │   │   ├── tokenization_longformer.data.json
│   │   │   │   │   ├── tokenization_longformer.meta.json
│   │   │   │   │   ├── tokenization_longformer_fast.data.json
│   │   │   │   │   └── tokenization_longformer_fast.meta.json
│   │   │   │   ├── longt5
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_longt5.data.json
│   │   │   │   │   ├── configuration_longt5.meta.json
│   │   │   │   │   ├── modeling_flax_longt5.data.json
│   │   │   │   │   ├── modeling_flax_longt5.meta.json
│   │   │   │   │   ├── modeling_longt5.data.json
│   │   │   │   │   └── modeling_longt5.meta.json
│   │   │   │   ├── luke
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_luke.data.json
│   │   │   │   │   ├── configuration_luke.meta.json
│   │   │   │   │   ├── modeling_luke.data.json
│   │   │   │   │   ├── modeling_luke.meta.json
│   │   │   │   │   ├── tokenization_luke.data.json
│   │   │   │   │   └── tokenization_luke.meta.json
│   │   │   │   ├── lxmert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_lxmert.data.json
│   │   │   │   │   ├── configuration_lxmert.meta.json
│   │   │   │   │   ├── modeling_lxmert.data.json
│   │   │   │   │   ├── modeling_lxmert.meta.json
│   │   │   │   │   ├── modeling_tf_lxmert.data.json
│   │   │   │   │   ├── modeling_tf_lxmert.meta.json
│   │   │   │   │   ├── tokenization_lxmert.data.json
│   │   │   │   │   ├── tokenization_lxmert.meta.json
│   │   │   │   │   ├── tokenization_lxmert_fast.data.json
│   │   │   │   │   └── tokenization_lxmert_fast.meta.json
│   │   │   │   ├── m2m_100
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_m2m_100.data.json
│   │   │   │   │   ├── configuration_m2m_100.meta.json
│   │   │   │   │   ├── modeling_m2m_100.data.json
│   │   │   │   │   ├── modeling_m2m_100.meta.json
│   │   │   │   │   ├── tokenization_m2m_100.data.json
│   │   │   │   │   └── tokenization_m2m_100.meta.json
│   │   │   │   ├── mamba
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mamba.data.json
│   │   │   │   │   ├── configuration_mamba.meta.json
│   │   │   │   │   ├── modeling_mamba.data.json
│   │   │   │   │   └── modeling_mamba.meta.json
│   │   │   │   ├── mamba2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mamba2.data.json
│   │   │   │   │   ├── configuration_mamba2.meta.json
│   │   │   │   │   ├── modeling_mamba2.data.json
│   │   │   │   │   └── modeling_mamba2.meta.json
│   │   │   │   ├── marian
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_marian.data.json
│   │   │   │   │   ├── configuration_marian.meta.json
│   │   │   │   │   ├── modeling_flax_marian.data.json
│   │   │   │   │   ├── modeling_flax_marian.meta.json
│   │   │   │   │   ├── modeling_marian.data.json
│   │   │   │   │   ├── modeling_marian.meta.json
│   │   │   │   │   ├── modeling_tf_marian.data.json
│   │   │   │   │   ├── modeling_tf_marian.meta.json
│   │   │   │   │   ├── tokenization_marian.data.json
│   │   │   │   │   └── tokenization_marian.meta.json
│   │   │   │   ├── markuplm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_markuplm.data.json
│   │   │   │   │   ├── configuration_markuplm.meta.json
│   │   │   │   │   ├── feature_extraction_markuplm.data.json
│   │   │   │   │   ├── feature_extraction_markuplm.meta.json
│   │   │   │   │   ├── modeling_markuplm.data.json
│   │   │   │   │   ├── modeling_markuplm.meta.json
│   │   │   │   │   ├── processing_markuplm.data.json
│   │   │   │   │   ├── processing_markuplm.meta.json
│   │   │   │   │   ├── tokenization_markuplm.data.json
│   │   │   │   │   ├── tokenization_markuplm.meta.json
│   │   │   │   │   ├── tokenization_markuplm_fast.data.json
│   │   │   │   │   └── tokenization_markuplm_fast.meta.json
│   │   │   │   ├── mask2former
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mask2former.data.json
│   │   │   │   │   ├── configuration_mask2former.meta.json
│   │   │   │   │   ├── image_processing_mask2former.data.json
│   │   │   │   │   ├── image_processing_mask2former.meta.json
│   │   │   │   │   ├── image_processing_mask2former_fast.data.json
│   │   │   │   │   ├── image_processing_mask2former_fast.meta.json
│   │   │   │   │   ├── modeling_mask2former.data.json
│   │   │   │   │   └── modeling_mask2former.meta.json
│   │   │   │   ├── maskformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_maskformer.data.json
│   │   │   │   │   ├── configuration_maskformer.meta.json
│   │   │   │   │   ├── configuration_maskformer_swin.data.json
│   │   │   │   │   ├── configuration_maskformer_swin.meta.json
│   │   │   │   │   ├── feature_extraction_maskformer.data.json
│   │   │   │   │   ├── feature_extraction_maskformer.meta.json
│   │   │   │   │   ├── image_processing_maskformer.data.json
│   │   │   │   │   ├── image_processing_maskformer.meta.json
│   │   │   │   │   ├── image_processing_maskformer_fast.data.json
│   │   │   │   │   ├── image_processing_maskformer_fast.meta.json
│   │   │   │   │   ├── modeling_maskformer.data.json
│   │   │   │   │   ├── modeling_maskformer.meta.json
│   │   │   │   │   ├── modeling_maskformer_swin.data.json
│   │   │   │   │   └── modeling_maskformer_swin.meta.json
│   │   │   │   ├── mbart
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mbart.data.json
│   │   │   │   │   ├── configuration_mbart.meta.json
│   │   │   │   │   ├── modeling_flax_mbart.data.json
│   │   │   │   │   ├── modeling_flax_mbart.meta.json
│   │   │   │   │   ├── modeling_mbart.data.json
│   │   │   │   │   ├── modeling_mbart.meta.json
│   │   │   │   │   ├── modeling_tf_mbart.data.json
│   │   │   │   │   ├── modeling_tf_mbart.meta.json
│   │   │   │   │   ├── tokenization_mbart.data.json
│   │   │   │   │   ├── tokenization_mbart.meta.json
│   │   │   │   │   ├── tokenization_mbart_fast.data.json
│   │   │   │   │   └── tokenization_mbart_fast.meta.json
│   │   │   │   ├── mbart50
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_mbart50.data.json
│   │   │   │   │   ├── tokenization_mbart50.meta.json
│   │   │   │   │   ├── tokenization_mbart50_fast.data.json
│   │   │   │   │   └── tokenization_mbart50_fast.meta.json
│   │   │   │   ├── megatron_bert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_megatron_bert.data.json
│   │   │   │   │   ├── configuration_megatron_bert.meta.json
│   │   │   │   │   ├── modeling_megatron_bert.data.json
│   │   │   │   │   └── modeling_megatron_bert.meta.json
│   │   │   │   ├── megatron_gpt2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── mgp_str
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mgp_str.data.json
│   │   │   │   │   ├── configuration_mgp_str.meta.json
│   │   │   │   │   ├── modeling_mgp_str.data.json
│   │   │   │   │   ├── modeling_mgp_str.meta.json
│   │   │   │   │   ├── processing_mgp_str.data.json
│   │   │   │   │   ├── processing_mgp_str.meta.json
│   │   │   │   │   ├── tokenization_mgp_str.data.json
│   │   │   │   │   └── tokenization_mgp_str.meta.json
│   │   │   │   ├── mimi
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mimi.data.json
│   │   │   │   │   ├── configuration_mimi.meta.json
│   │   │   │   │   ├── modeling_mimi.data.json
│   │   │   │   │   └── modeling_mimi.meta.json
│   │   │   │   ├── minimax
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_minimax.data.json
│   │   │   │   │   ├── configuration_minimax.meta.json
│   │   │   │   │   ├── modeling_minimax.data.json
│   │   │   │   │   └── modeling_minimax.meta.json
│   │   │   │   ├── mistral
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mistral.data.json
│   │   │   │   │   ├── configuration_mistral.meta.json
│   │   │   │   │   ├── modeling_flax_mistral.data.json
│   │   │   │   │   ├── modeling_flax_mistral.meta.json
│   │   │   │   │   ├── modeling_mistral.data.json
│   │   │   │   │   ├── modeling_mistral.meta.json
│   │   │   │   │   ├── modeling_tf_mistral.data.json
│   │   │   │   │   └── modeling_tf_mistral.meta.json
│   │   │   │   ├── mistral3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mistral3.data.json
│   │   │   │   │   ├── configuration_mistral3.meta.json
│   │   │   │   │   ├── modeling_mistral3.data.json
│   │   │   │   │   └── modeling_mistral3.meta.json
│   │   │   │   ├── mixtral
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mixtral.data.json
│   │   │   │   │   ├── configuration_mixtral.meta.json
│   │   │   │   │   ├── modeling_mixtral.data.json
│   │   │   │   │   └── modeling_mixtral.meta.json
│   │   │   │   ├── mlcd
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mlcd.data.json
│   │   │   │   │   ├── configuration_mlcd.meta.json
│   │   │   │   │   ├── modeling_mlcd.data.json
│   │   │   │   │   └── modeling_mlcd.meta.json
│   │   │   │   ├── mllama
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mllama.data.json
│   │   │   │   │   ├── configuration_mllama.meta.json
│   │   │   │   │   ├── image_processing_mllama.data.json
│   │   │   │   │   ├── image_processing_mllama.meta.json
│   │   │   │   │   ├── modeling_mllama.data.json
│   │   │   │   │   ├── modeling_mllama.meta.json
│   │   │   │   │   ├── processing_mllama.data.json
│   │   │   │   │   └── processing_mllama.meta.json
│   │   │   │   ├── mluke
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_mluke.data.json
│   │   │   │   │   └── tokenization_mluke.meta.json
│   │   │   │   ├── mobilebert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mobilebert.data.json
│   │   │   │   │   ├── configuration_mobilebert.meta.json
│   │   │   │   │   ├── modeling_mobilebert.data.json
│   │   │   │   │   ├── modeling_mobilebert.meta.json
│   │   │   │   │   ├── modeling_tf_mobilebert.data.json
│   │   │   │   │   ├── modeling_tf_mobilebert.meta.json
│   │   │   │   │   ├── tokenization_mobilebert.data.json
│   │   │   │   │   ├── tokenization_mobilebert.meta.json
│   │   │   │   │   ├── tokenization_mobilebert_fast.data.json
│   │   │   │   │   └── tokenization_mobilebert_fast.meta.json
│   │   │   │   ├── mobilenet_v1
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mobilenet_v1.data.json
│   │   │   │   │   ├── configuration_mobilenet_v1.meta.json
│   │   │   │   │   ├── feature_extraction_mobilenet_v1.data.json
│   │   │   │   │   ├── feature_extraction_mobilenet_v1.meta.json
│   │   │   │   │   ├── image_processing_mobilenet_v1.data.json
│   │   │   │   │   ├── image_processing_mobilenet_v1.meta.json
│   │   │   │   │   ├── image_processing_mobilenet_v1_fast.data.json
│   │   │   │   │   ├── image_processing_mobilenet_v1_fast.meta.json
│   │   │   │   │   ├── modeling_mobilenet_v1.data.json
│   │   │   │   │   └── modeling_mobilenet_v1.meta.json
│   │   │   │   ├── mobilenet_v2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mobilenet_v2.data.json
│   │   │   │   │   ├── configuration_mobilenet_v2.meta.json
│   │   │   │   │   ├── feature_extraction_mobilenet_v2.data.json
│   │   │   │   │   ├── feature_extraction_mobilenet_v2.meta.json
│   │   │   │   │   ├── image_processing_mobilenet_v2.data.json
│   │   │   │   │   ├── image_processing_mobilenet_v2.meta.json
│   │   │   │   │   ├── image_processing_mobilenet_v2_fast.data.json
│   │   │   │   │   ├── image_processing_mobilenet_v2_fast.meta.json
│   │   │   │   │   ├── modeling_mobilenet_v2.data.json
│   │   │   │   │   └── modeling_mobilenet_v2.meta.json
│   │   │   │   ├── mobilevit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mobilevit.data.json
│   │   │   │   │   ├── configuration_mobilevit.meta.json
│   │   │   │   │   ├── feature_extraction_mobilevit.data.json
│   │   │   │   │   ├── feature_extraction_mobilevit.meta.json
│   │   │   │   │   ├── image_processing_mobilevit.data.json
│   │   │   │   │   ├── image_processing_mobilevit.meta.json
│   │   │   │   │   ├── image_processing_mobilevit_fast.data.json
│   │   │   │   │   ├── image_processing_mobilevit_fast.meta.json
│   │   │   │   │   ├── modeling_mobilevit.data.json
│   │   │   │   │   ├── modeling_mobilevit.meta.json
│   │   │   │   │   ├── modeling_tf_mobilevit.data.json
│   │   │   │   │   └── modeling_tf_mobilevit.meta.json
│   │   │   │   ├── mobilevitv2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mobilevitv2.data.json
│   │   │   │   │   ├── configuration_mobilevitv2.meta.json
│   │   │   │   │   ├── modeling_mobilevitv2.data.json
│   │   │   │   │   └── modeling_mobilevitv2.meta.json
│   │   │   │   ├── modernbert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_modernbert.data.json
│   │   │   │   │   ├── configuration_modernbert.meta.json
│   │   │   │   │   ├── modeling_modernbert.data.json
│   │   │   │   │   └── modeling_modernbert.meta.json
│   │   │   │   ├── modernbert_decoder
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_modernbert_decoder.data.json
│   │   │   │   │   ├── configuration_modernbert_decoder.meta.json
│   │   │   │   │   ├── modeling_modernbert_decoder.data.json
│   │   │   │   │   └── modeling_modernbert_decoder.meta.json
│   │   │   │   ├── moonshine
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_moonshine.data.json
│   │   │   │   │   ├── configuration_moonshine.meta.json
│   │   │   │   │   ├── modeling_moonshine.data.json
│   │   │   │   │   └── modeling_moonshine.meta.json
│   │   │   │   ├── moshi
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_moshi.data.json
│   │   │   │   │   ├── configuration_moshi.meta.json
│   │   │   │   │   ├── modeling_moshi.data.json
│   │   │   │   │   └── modeling_moshi.meta.json
│   │   │   │   ├── mpnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mpnet.data.json
│   │   │   │   │   ├── configuration_mpnet.meta.json
│   │   │   │   │   ├── modeling_mpnet.data.json
│   │   │   │   │   ├── modeling_mpnet.meta.json
│   │   │   │   │   ├── modeling_tf_mpnet.data.json
│   │   │   │   │   ├── modeling_tf_mpnet.meta.json
│   │   │   │   │   ├── tokenization_mpnet.data.json
│   │   │   │   │   ├── tokenization_mpnet.meta.json
│   │   │   │   │   ├── tokenization_mpnet_fast.data.json
│   │   │   │   │   └── tokenization_mpnet_fast.meta.json
│   │   │   │   ├── mpt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mpt.data.json
│   │   │   │   │   ├── configuration_mpt.meta.json
│   │   │   │   │   ├── modeling_mpt.data.json
│   │   │   │   │   └── modeling_mpt.meta.json
│   │   │   │   ├── mra
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mra.data.json
│   │   │   │   │   ├── configuration_mra.meta.json
│   │   │   │   │   ├── modeling_mra.data.json
│   │   │   │   │   └── modeling_mra.meta.json
│   │   │   │   ├── mt5
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mt5.data.json
│   │   │   │   │   ├── configuration_mt5.meta.json
│   │   │   │   │   ├── modeling_flax_mt5.data.json
│   │   │   │   │   ├── modeling_flax_mt5.meta.json
│   │   │   │   │   ├── modeling_mt5.data.json
│   │   │   │   │   ├── modeling_mt5.meta.json
│   │   │   │   │   ├── modeling_tf_mt5.data.json
│   │   │   │   │   ├── modeling_tf_mt5.meta.json
│   │   │   │   │   ├── tokenization_mt5.data.json
│   │   │   │   │   └── tokenization_mt5.meta.json
│   │   │   │   ├── musicgen
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_musicgen.data.json
│   │   │   │   │   ├── configuration_musicgen.meta.json
│   │   │   │   │   ├── modeling_musicgen.data.json
│   │   │   │   │   ├── modeling_musicgen.meta.json
│   │   │   │   │   ├── processing_musicgen.data.json
│   │   │   │   │   └── processing_musicgen.meta.json
│   │   │   │   ├── musicgen_melody
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_musicgen_melody.data.json
│   │   │   │   │   ├── configuration_musicgen_melody.meta.json
│   │   │   │   │   ├── modeling_musicgen_melody.data.json
│   │   │   │   │   └── modeling_musicgen_melody.meta.json
│   │   │   │   ├── mvp
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_mvp.data.json
│   │   │   │   │   ├── configuration_mvp.meta.json
│   │   │   │   │   ├── modeling_mvp.data.json
│   │   │   │   │   ├── modeling_mvp.meta.json
│   │   │   │   │   ├── tokenization_mvp.data.json
│   │   │   │   │   ├── tokenization_mvp.meta.json
│   │   │   │   │   ├── tokenization_mvp_fast.data.json
│   │   │   │   │   └── tokenization_mvp_fast.meta.json
│   │   │   │   ├── myt5
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_myt5.data.json
│   │   │   │   │   └── tokenization_myt5.meta.json
│   │   │   │   ├── nemotron
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_nemotron.data.json
│   │   │   │   │   ├── configuration_nemotron.meta.json
│   │   │   │   │   ├── modeling_nemotron.data.json
│   │   │   │   │   └── modeling_nemotron.meta.json
│   │   │   │   ├── nllb
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_nllb.data.json
│   │   │   │   │   ├── tokenization_nllb.meta.json
│   │   │   │   │   ├── tokenization_nllb_fast.data.json
│   │   │   │   │   └── tokenization_nllb_fast.meta.json
│   │   │   │   ├── nllb_moe
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_nllb_moe.data.json
│   │   │   │   │   ├── configuration_nllb_moe.meta.json
│   │   │   │   │   ├── modeling_nllb_moe.data.json
│   │   │   │   │   └── modeling_nllb_moe.meta.json
│   │   │   │   ├── nougat
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── image_processing_nougat.data.json
│   │   │   │   │   ├── image_processing_nougat.meta.json
│   │   │   │   │   ├── image_processing_nougat_fast.data.json
│   │   │   │   │   ├── image_processing_nougat_fast.meta.json
│   │   │   │   │   ├── processing_nougat.data.json
│   │   │   │   │   ├── processing_nougat.meta.json
│   │   │   │   │   ├── tokenization_nougat_fast.data.json
│   │   │   │   │   └── tokenization_nougat_fast.meta.json
│   │   │   │   ├── nystromformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_nystromformer.data.json
│   │   │   │   │   ├── configuration_nystromformer.meta.json
│   │   │   │   │   ├── modeling_nystromformer.data.json
│   │   │   │   │   └── modeling_nystromformer.meta.json
│   │   │   │   ├── olmo
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_olmo.data.json
│   │   │   │   │   ├── configuration_olmo.meta.json
│   │   │   │   │   ├── modeling_olmo.data.json
│   │   │   │   │   └── modeling_olmo.meta.json
│   │   │   │   ├── olmo2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_olmo2.data.json
│   │   │   │   │   ├── configuration_olmo2.meta.json
│   │   │   │   │   ├── modeling_olmo2.data.json
│   │   │   │   │   └── modeling_olmo2.meta.json
│   │   │   │   ├── olmoe
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_olmoe.data.json
│   │   │   │   │   ├── configuration_olmoe.meta.json
│   │   │   │   │   ├── modeling_olmoe.data.json
│   │   │   │   │   └── modeling_olmoe.meta.json
│   │   │   │   ├── omdet_turbo
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_omdet_turbo.data.json
│   │   │   │   │   ├── configuration_omdet_turbo.meta.json
│   │   │   │   │   ├── modeling_omdet_turbo.data.json
│   │   │   │   │   ├── modeling_omdet_turbo.meta.json
│   │   │   │   │   ├── processing_omdet_turbo.data.json
│   │   │   │   │   └── processing_omdet_turbo.meta.json
│   │   │   │   ├── oneformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_oneformer.data.json
│   │   │   │   │   ├── configuration_oneformer.meta.json
│   │   │   │   │   ├── image_processing_oneformer.data.json
│   │   │   │   │   ├── image_processing_oneformer.meta.json
│   │   │   │   │   ├── image_processing_oneformer_fast.data.json
│   │   │   │   │   ├── image_processing_oneformer_fast.meta.json
│   │   │   │   │   ├── modeling_oneformer.data.json
│   │   │   │   │   ├── modeling_oneformer.meta.json
│   │   │   │   │   ├── processing_oneformer.data.json
│   │   │   │   │   └── processing_oneformer.meta.json
│   │   │   │   ├── openai
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_openai.data.json
│   │   │   │   │   ├── configuration_openai.meta.json
│   │   │   │   │   ├── modeling_openai.data.json
│   │   │   │   │   ├── modeling_openai.meta.json
│   │   │   │   │   ├── modeling_tf_openai.data.json
│   │   │   │   │   ├── modeling_tf_openai.meta.json
│   │   │   │   │   ├── tokenization_openai.data.json
│   │   │   │   │   ├── tokenization_openai.meta.json
│   │   │   │   │   ├── tokenization_openai_fast.data.json
│   │   │   │   │   └── tokenization_openai_fast.meta.json
│   │   │   │   ├── opt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_opt.data.json
│   │   │   │   │   ├── configuration_opt.meta.json
│   │   │   │   │   ├── modeling_flax_opt.data.json
│   │   │   │   │   ├── modeling_flax_opt.meta.json
│   │   │   │   │   ├── modeling_opt.data.json
│   │   │   │   │   ├── modeling_opt.meta.json
│   │   │   │   │   ├── modeling_tf_opt.data.json
│   │   │   │   │   └── modeling_tf_opt.meta.json
│   │   │   │   ├── owlv2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_owlv2.data.json
│   │   │   │   │   ├── configuration_owlv2.meta.json
│   │   │   │   │   ├── image_processing_owlv2.data.json
│   │   │   │   │   ├── image_processing_owlv2.meta.json
│   │   │   │   │   ├── image_processing_owlv2_fast.data.json
│   │   │   │   │   ├── image_processing_owlv2_fast.meta.json
│   │   │   │   │   ├── modeling_owlv2.data.json
│   │   │   │   │   ├── modeling_owlv2.meta.json
│   │   │   │   │   ├── processing_owlv2.data.json
│   │   │   │   │   └── processing_owlv2.meta.json
│   │   │   │   ├── owlvit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_owlvit.data.json
│   │   │   │   │   ├── configuration_owlvit.meta.json
│   │   │   │   │   ├── feature_extraction_owlvit.data.json
│   │   │   │   │   ├── feature_extraction_owlvit.meta.json
│   │   │   │   │   ├── image_processing_owlvit.data.json
│   │   │   │   │   ├── image_processing_owlvit.meta.json
│   │   │   │   │   ├── image_processing_owlvit_fast.data.json
│   │   │   │   │   ├── image_processing_owlvit_fast.meta.json
│   │   │   │   │   ├── modeling_owlvit.data.json
│   │   │   │   │   ├── modeling_owlvit.meta.json
│   │   │   │   │   ├── processing_owlvit.data.json
│   │   │   │   │   └── processing_owlvit.meta.json
│   │   │   │   ├── paligemma
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_paligemma.data.json
│   │   │   │   │   ├── configuration_paligemma.meta.json
│   │   │   │   │   ├── modeling_paligemma.data.json
│   │   │   │   │   ├── modeling_paligemma.meta.json
│   │   │   │   │   ├── processing_paligemma.data.json
│   │   │   │   │   └── processing_paligemma.meta.json
│   │   │   │   ├── patchtsmixer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_patchtsmixer.data.json
│   │   │   │   │   ├── configuration_patchtsmixer.meta.json
│   │   │   │   │   ├── modeling_patchtsmixer.data.json
│   │   │   │   │   └── modeling_patchtsmixer.meta.json
│   │   │   │   ├── patchtst
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_patchtst.data.json
│   │   │   │   │   ├── configuration_patchtst.meta.json
│   │   │   │   │   ├── modeling_patchtst.data.json
│   │   │   │   │   └── modeling_patchtst.meta.json
│   │   │   │   ├── pegasus
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_pegasus.data.json
│   │   │   │   │   ├── configuration_pegasus.meta.json
│   │   │   │   │   ├── modeling_flax_pegasus.data.json
│   │   │   │   │   ├── modeling_flax_pegasus.meta.json
│   │   │   │   │   ├── modeling_pegasus.data.json
│   │   │   │   │   ├── modeling_pegasus.meta.json
│   │   │   │   │   ├── modeling_tf_pegasus.data.json
│   │   │   │   │   ├── modeling_tf_pegasus.meta.json
│   │   │   │   │   ├── tokenization_pegasus.data.json
│   │   │   │   │   ├── tokenization_pegasus.meta.json
│   │   │   │   │   ├── tokenization_pegasus_fast.data.json
│   │   │   │   │   └── tokenization_pegasus_fast.meta.json
│   │   │   │   ├── pegasus_x
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_pegasus_x.data.json
│   │   │   │   │   ├── configuration_pegasus_x.meta.json
│   │   │   │   │   ├── modeling_pegasus_x.data.json
│   │   │   │   │   └── modeling_pegasus_x.meta.json
│   │   │   │   ├── perceiver
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_perceiver.data.json
│   │   │   │   │   ├── configuration_perceiver.meta.json
│   │   │   │   │   ├── feature_extraction_perceiver.data.json
│   │   │   │   │   ├── feature_extraction_perceiver.meta.json
│   │   │   │   │   ├── image_processing_perceiver.data.json
│   │   │   │   │   ├── image_processing_perceiver.meta.json
│   │   │   │   │   ├── image_processing_perceiver_fast.data.json
│   │   │   │   │   ├── image_processing_perceiver_fast.meta.json
│   │   │   │   │   ├── modeling_perceiver.data.json
│   │   │   │   │   ├── modeling_perceiver.meta.json
│   │   │   │   │   ├── tokenization_perceiver.data.json
│   │   │   │   │   └── tokenization_perceiver.meta.json
│   │   │   │   ├── perception_lm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_perception_lm.data.json
│   │   │   │   │   ├── configuration_perception_lm.meta.json
│   │   │   │   │   ├── image_processing_perception_lm_fast.data.json
│   │   │   │   │   ├── image_processing_perception_lm_fast.meta.json
│   │   │   │   │   ├── modeling_perception_lm.data.json
│   │   │   │   │   ├── modeling_perception_lm.meta.json
│   │   │   │   │   ├── processing_perception_lm.data.json
│   │   │   │   │   └── processing_perception_lm.meta.json
│   │   │   │   ├── persimmon
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_persimmon.data.json
│   │   │   │   │   ├── configuration_persimmon.meta.json
│   │   │   │   │   ├── modeling_persimmon.data.json
│   │   │   │   │   └── modeling_persimmon.meta.json
│   │   │   │   ├── phi
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_phi.data.json
│   │   │   │   │   ├── configuration_phi.meta.json
│   │   │   │   │   ├── modeling_phi.data.json
│   │   │   │   │   └── modeling_phi.meta.json
│   │   │   │   ├── phi3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_phi3.data.json
│   │   │   │   │   ├── configuration_phi3.meta.json
│   │   │   │   │   ├── modeling_phi3.data.json
│   │   │   │   │   └── modeling_phi3.meta.json
│   │   │   │   ├── phi4_multimodal
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_phi4_multimodal.data.json
│   │   │   │   │   ├── configuration_phi4_multimodal.meta.json
│   │   │   │   │   ├── feature_extraction_phi4_multimodal.data.json
│   │   │   │   │   ├── feature_extraction_phi4_multimodal.meta.json
│   │   │   │   │   ├── image_processing_phi4_multimodal_fast.data.json
│   │   │   │   │   ├── image_processing_phi4_multimodal_fast.meta.json
│   │   │   │   │   ├── modeling_phi4_multimodal.data.json
│   │   │   │   │   ├── modeling_phi4_multimodal.meta.json
│   │   │   │   │   ├── processing_phi4_multimodal.data.json
│   │   │   │   │   └── processing_phi4_multimodal.meta.json
│   │   │   │   ├── phimoe
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_phimoe.data.json
│   │   │   │   │   ├── configuration_phimoe.meta.json
│   │   │   │   │   ├── modeling_phimoe.data.json
│   │   │   │   │   └── modeling_phimoe.meta.json
│   │   │   │   ├── phobert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_phobert.data.json
│   │   │   │   │   └── tokenization_phobert.meta.json
│   │   │   │   ├── pix2struct
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_pix2struct.data.json
│   │   │   │   │   ├── configuration_pix2struct.meta.json
│   │   │   │   │   ├── image_processing_pix2struct.data.json
│   │   │   │   │   ├── image_processing_pix2struct.meta.json
│   │   │   │   │   ├── modeling_pix2struct.data.json
│   │   │   │   │   ├── modeling_pix2struct.meta.json
│   │   │   │   │   ├── processing_pix2struct.data.json
│   │   │   │   │   └── processing_pix2struct.meta.json
│   │   │   │   ├── pixtral
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_pixtral.data.json
│   │   │   │   │   ├── configuration_pixtral.meta.json
│   │   │   │   │   ├── image_processing_pixtral.data.json
│   │   │   │   │   ├── image_processing_pixtral.meta.json
│   │   │   │   │   ├── image_processing_pixtral_fast.data.json
│   │   │   │   │   ├── image_processing_pixtral_fast.meta.json
│   │   │   │   │   ├── modeling_pixtral.data.json
│   │   │   │   │   ├── modeling_pixtral.meta.json
│   │   │   │   │   ├── processing_pixtral.data.json
│   │   │   │   │   └── processing_pixtral.meta.json
│   │   │   │   ├── plbart
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_plbart.data.json
│   │   │   │   │   ├── configuration_plbart.meta.json
│   │   │   │   │   ├── modeling_plbart.data.json
│   │   │   │   │   ├── modeling_plbart.meta.json
│   │   │   │   │   ├── tokenization_plbart.data.json
│   │   │   │   │   └── tokenization_plbart.meta.json
│   │   │   │   ├── poolformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_poolformer.data.json
│   │   │   │   │   ├── configuration_poolformer.meta.json
│   │   │   │   │   ├── feature_extraction_poolformer.data.json
│   │   │   │   │   ├── feature_extraction_poolformer.meta.json
│   │   │   │   │   ├── image_processing_poolformer.data.json
│   │   │   │   │   ├── image_processing_poolformer.meta.json
│   │   │   │   │   ├── image_processing_poolformer_fast.data.json
│   │   │   │   │   ├── image_processing_poolformer_fast.meta.json
│   │   │   │   │   ├── modeling_poolformer.data.json
│   │   │   │   │   └── modeling_poolformer.meta.json
│   │   │   │   ├── pop2piano
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_pop2piano.data.json
│   │   │   │   │   ├── configuration_pop2piano.meta.json
│   │   │   │   │   ├── modeling_pop2piano.data.json
│   │   │   │   │   └── modeling_pop2piano.meta.json
│   │   │   │   ├── prompt_depth_anything
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_prompt_depth_anything.data.json
│   │   │   │   │   ├── configuration_prompt_depth_anything.meta.json
│   │   │   │   │   ├── image_processing_prompt_depth_anything.data.json
│   │   │   │   │   ├── image_processing_prompt_depth_anything.meta.json
│   │   │   │   │   ├── modeling_prompt_depth_anything.data.json
│   │   │   │   │   └── modeling_prompt_depth_anything.meta.json
│   │   │   │   ├── prophetnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_prophetnet.data.json
│   │   │   │   │   ├── configuration_prophetnet.meta.json
│   │   │   │   │   ├── modeling_prophetnet.data.json
│   │   │   │   │   ├── modeling_prophetnet.meta.json
│   │   │   │   │   ├── tokenization_prophetnet.data.json
│   │   │   │   │   └── tokenization_prophetnet.meta.json
│   │   │   │   ├── pvt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_pvt.data.json
│   │   │   │   │   ├── configuration_pvt.meta.json
│   │   │   │   │   ├── image_processing_pvt.data.json
│   │   │   │   │   ├── image_processing_pvt.meta.json
│   │   │   │   │   ├── image_processing_pvt_fast.data.json
│   │   │   │   │   ├── image_processing_pvt_fast.meta.json
│   │   │   │   │   ├── modeling_pvt.data.json
│   │   │   │   │   └── modeling_pvt.meta.json
│   │   │   │   ├── pvt_v2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_pvt_v2.data.json
│   │   │   │   │   ├── configuration_pvt_v2.meta.json
│   │   │   │   │   ├── modeling_pvt_v2.data.json
│   │   │   │   │   └── modeling_pvt_v2.meta.json
│   │   │   │   ├── qwen2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_qwen2.data.json
│   │   │   │   │   ├── configuration_qwen2.meta.json
│   │   │   │   │   ├── modeling_qwen2.data.json
│   │   │   │   │   ├── modeling_qwen2.meta.json
│   │   │   │   │   ├── tokenization_qwen2.data.json
│   │   │   │   │   ├── tokenization_qwen2.meta.json
│   │   │   │   │   ├── tokenization_qwen2_fast.data.json
│   │   │   │   │   └── tokenization_qwen2_fast.meta.json
│   │   │   │   ├── qwen2_5_vl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_qwen2_5_vl.data.json
│   │   │   │   │   ├── configuration_qwen2_5_vl.meta.json
│   │   │   │   │   ├── modeling_qwen2_5_vl.data.json
│   │   │   │   │   ├── modeling_qwen2_5_vl.meta.json
│   │   │   │   │   ├── processing_qwen2_5_vl.data.json
│   │   │   │   │   └── processing_qwen2_5_vl.meta.json
│   │   │   │   ├── qwen2_audio
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_qwen2_audio.data.json
│   │   │   │   │   ├── configuration_qwen2_audio.meta.json
│   │   │   │   │   ├── modeling_qwen2_audio.data.json
│   │   │   │   │   ├── modeling_qwen2_audio.meta.json
│   │   │   │   │   ├── processing_qwen2_audio.data.json
│   │   │   │   │   └── processing_qwen2_audio.meta.json
│   │   │   │   ├── qwen2_moe
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_qwen2_moe.data.json
│   │   │   │   │   ├── configuration_qwen2_moe.meta.json
│   │   │   │   │   ├── modeling_qwen2_moe.data.json
│   │   │   │   │   └── modeling_qwen2_moe.meta.json
│   │   │   │   ├── qwen2_vl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_qwen2_vl.data.json
│   │   │   │   │   ├── configuration_qwen2_vl.meta.json
│   │   │   │   │   ├── image_processing_qwen2_vl.data.json
│   │   │   │   │   ├── image_processing_qwen2_vl.meta.json
│   │   │   │   │   ├── image_processing_qwen2_vl_fast.data.json
│   │   │   │   │   ├── image_processing_qwen2_vl_fast.meta.json
│   │   │   │   │   ├── modeling_qwen2_vl.data.json
│   │   │   │   │   ├── modeling_qwen2_vl.meta.json
│   │   │   │   │   ├── processing_qwen2_vl.data.json
│   │   │   │   │   └── processing_qwen2_vl.meta.json
│   │   │   │   ├── qwen3
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_qwen3.data.json
│   │   │   │   │   ├── configuration_qwen3.meta.json
│   │   │   │   │   ├── modeling_qwen3.data.json
│   │   │   │   │   └── modeling_qwen3.meta.json
│   │   │   │   ├── qwen3_moe
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_qwen3_moe.data.json
│   │   │   │   │   ├── configuration_qwen3_moe.meta.json
│   │   │   │   │   ├── modeling_qwen3_moe.data.json
│   │   │   │   │   └── modeling_qwen3_moe.meta.json
│   │   │   │   ├── rag
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_rag.data.json
│   │   │   │   │   ├── configuration_rag.meta.json
│   │   │   │   │   ├── modeling_rag.data.json
│   │   │   │   │   ├── modeling_rag.meta.json
│   │   │   │   │   ├── modeling_tf_rag.data.json
│   │   │   │   │   ├── modeling_tf_rag.meta.json
│   │   │   │   │   ├── retrieval_rag.data.json
│   │   │   │   │   ├── retrieval_rag.meta.json
│   │   │   │   │   ├── tokenization_rag.data.json
│   │   │   │   │   └── tokenization_rag.meta.json
│   │   │   │   ├── recurrent_gemma
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_recurrent_gemma.data.json
│   │   │   │   │   ├── configuration_recurrent_gemma.meta.json
│   │   │   │   │   ├── modeling_recurrent_gemma.data.json
│   │   │   │   │   └── modeling_recurrent_gemma.meta.json
│   │   │   │   ├── reformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_reformer.data.json
│   │   │   │   │   ├── configuration_reformer.meta.json
│   │   │   │   │   ├── modeling_reformer.data.json
│   │   │   │   │   ├── modeling_reformer.meta.json
│   │   │   │   │   ├── tokenization_reformer.data.json
│   │   │   │   │   ├── tokenization_reformer.meta.json
│   │   │   │   │   ├── tokenization_reformer_fast.data.json
│   │   │   │   │   └── tokenization_reformer_fast.meta.json
│   │   │   │   ├── regnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_regnet.data.json
│   │   │   │   │   ├── configuration_regnet.meta.json
│   │   │   │   │   ├── modeling_flax_regnet.data.json
│   │   │   │   │   ├── modeling_flax_regnet.meta.json
│   │   │   │   │   ├── modeling_regnet.data.json
│   │   │   │   │   ├── modeling_regnet.meta.json
│   │   │   │   │   ├── modeling_tf_regnet.data.json
│   │   │   │   │   └── modeling_tf_regnet.meta.json
│   │   │   │   ├── rembert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_rembert.data.json
│   │   │   │   │   ├── configuration_rembert.meta.json
│   │   │   │   │   ├── modeling_rembert.data.json
│   │   │   │   │   ├── modeling_rembert.meta.json
│   │   │   │   │   ├── modeling_tf_rembert.data.json
│   │   │   │   │   ├── modeling_tf_rembert.meta.json
│   │   │   │   │   ├── tokenization_rembert.data.json
│   │   │   │   │   ├── tokenization_rembert.meta.json
│   │   │   │   │   ├── tokenization_rembert_fast.data.json
│   │   │   │   │   └── tokenization_rembert_fast.meta.json
│   │   │   │   ├── resnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_resnet.data.json
│   │   │   │   │   ├── configuration_resnet.meta.json
│   │   │   │   │   ├── modeling_flax_resnet.data.json
│   │   │   │   │   ├── modeling_flax_resnet.meta.json
│   │   │   │   │   ├── modeling_resnet.data.json
│   │   │   │   │   ├── modeling_resnet.meta.json
│   │   │   │   │   ├── modeling_tf_resnet.data.json
│   │   │   │   │   └── modeling_tf_resnet.meta.json
│   │   │   │   ├── roberta
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_roberta.data.json
│   │   │   │   │   ├── configuration_roberta.meta.json
│   │   │   │   │   ├── modeling_flax_roberta.data.json
│   │   │   │   │   ├── modeling_flax_roberta.meta.json
│   │   │   │   │   ├── modeling_roberta.data.json
│   │   │   │   │   ├── modeling_roberta.meta.json
│   │   │   │   │   ├── modeling_tf_roberta.data.json
│   │   │   │   │   ├── modeling_tf_roberta.meta.json
│   │   │   │   │   ├── tokenization_roberta.data.json
│   │   │   │   │   ├── tokenization_roberta.meta.json
│   │   │   │   │   ├── tokenization_roberta_fast.data.json
│   │   │   │   │   └── tokenization_roberta_fast.meta.json
│   │   │   │   ├── roberta_prelayernorm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_roberta_prelayernorm.data.json
│   │   │   │   │   ├── configuration_roberta_prelayernorm.meta.json
│   │   │   │   │   ├── modeling_flax_roberta_prelayernorm.data.json
│   │   │   │   │   ├── modeling_flax_roberta_prelayernorm.meta.json
│   │   │   │   │   ├── modeling_roberta_prelayernorm.data.json
│   │   │   │   │   ├── modeling_roberta_prelayernorm.meta.json
│   │   │   │   │   ├── modeling_tf_roberta_prelayernorm.data.json
│   │   │   │   │   └── modeling_tf_roberta_prelayernorm.meta.json
│   │   │   │   ├── roc_bert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_roc_bert.data.json
│   │   │   │   │   ├── configuration_roc_bert.meta.json
│   │   │   │   │   ├── modeling_roc_bert.data.json
│   │   │   │   │   ├── modeling_roc_bert.meta.json
│   │   │   │   │   ├── tokenization_roc_bert.data.json
│   │   │   │   │   └── tokenization_roc_bert.meta.json
│   │   │   │   ├── roformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_roformer.data.json
│   │   │   │   │   ├── configuration_roformer.meta.json
│   │   │   │   │   ├── modeling_flax_roformer.data.json
│   │   │   │   │   ├── modeling_flax_roformer.meta.json
│   │   │   │   │   ├── modeling_roformer.data.json
│   │   │   │   │   ├── modeling_roformer.meta.json
│   │   │   │   │   ├── modeling_tf_roformer.data.json
│   │   │   │   │   ├── modeling_tf_roformer.meta.json
│   │   │   │   │   ├── tokenization_roformer.data.json
│   │   │   │   │   ├── tokenization_roformer.meta.json
│   │   │   │   │   ├── tokenization_roformer_fast.data.json
│   │   │   │   │   ├── tokenization_roformer_fast.meta.json
│   │   │   │   │   ├── tokenization_utils.data.json
│   │   │   │   │   └── tokenization_utils.meta.json
│   │   │   │   ├── rt_detr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_rt_detr.data.json
│   │   │   │   │   ├── configuration_rt_detr.meta.json
│   │   │   │   │   ├── configuration_rt_detr_resnet.data.json
│   │   │   │   │   ├── configuration_rt_detr_resnet.meta.json
│   │   │   │   │   ├── image_processing_rt_detr.data.json
│   │   │   │   │   ├── image_processing_rt_detr.meta.json
│   │   │   │   │   ├── image_processing_rt_detr_fast.data.json
│   │   │   │   │   ├── image_processing_rt_detr_fast.meta.json
│   │   │   │   │   ├── modeling_rt_detr.data.json
│   │   │   │   │   ├── modeling_rt_detr.meta.json
│   │   │   │   │   ├── modeling_rt_detr_resnet.data.json
│   │   │   │   │   └── modeling_rt_detr_resnet.meta.json
│   │   │   │   ├── rt_detr_v2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_rt_detr_v2.data.json
│   │   │   │   │   ├── configuration_rt_detr_v2.meta.json
│   │   │   │   │   ├── modeling_rt_detr_v2.data.json
│   │   │   │   │   └── modeling_rt_detr_v2.meta.json
│   │   │   │   ├── rwkv
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_rwkv.data.json
│   │   │   │   │   ├── configuration_rwkv.meta.json
│   │   │   │   │   ├── modeling_rwkv.data.json
│   │   │   │   │   └── modeling_rwkv.meta.json
│   │   │   │   ├── sam
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_sam.data.json
│   │   │   │   │   ├── configuration_sam.meta.json
│   │   │   │   │   ├── image_processing_sam.data.json
│   │   │   │   │   ├── image_processing_sam.meta.json
│   │   │   │   │   ├── image_processing_sam_fast.data.json
│   │   │   │   │   ├── image_processing_sam_fast.meta.json
│   │   │   │   │   ├── modeling_sam.data.json
│   │   │   │   │   ├── modeling_sam.meta.json
│   │   │   │   │   ├── modeling_tf_sam.data.json
│   │   │   │   │   ├── modeling_tf_sam.meta.json
│   │   │   │   │   ├── processing_sam.data.json
│   │   │   │   │   └── processing_sam.meta.json
│   │   │   │   ├── sam_hq
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_sam_hq.data.json
│   │   │   │   │   ├── configuration_sam_hq.meta.json
│   │   │   │   │   ├── modeling_sam_hq.data.json
│   │   │   │   │   ├── modeling_sam_hq.meta.json
│   │   │   │   │   ├── processing_samhq.data.json
│   │   │   │   │   └── processing_samhq.meta.json
│   │   │   │   ├── seamless_m4t
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_seamless_m4t.data.json
│   │   │   │   │   ├── configuration_seamless_m4t.meta.json
│   │   │   │   │   ├── feature_extraction_seamless_m4t.data.json
│   │   │   │   │   ├── feature_extraction_seamless_m4t.meta.json
│   │   │   │   │   ├── modeling_seamless_m4t.data.json
│   │   │   │   │   ├── modeling_seamless_m4t.meta.json
│   │   │   │   │   ├── processing_seamless_m4t.data.json
│   │   │   │   │   ├── processing_seamless_m4t.meta.json
│   │   │   │   │   ├── tokenization_seamless_m4t.data.json
│   │   │   │   │   ├── tokenization_seamless_m4t.meta.json
│   │   │   │   │   ├── tokenization_seamless_m4t_fast.data.json
│   │   │   │   │   └── tokenization_seamless_m4t_fast.meta.json
│   │   │   │   ├── seamless_m4t_v2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_seamless_m4t_v2.data.json
│   │   │   │   │   ├── configuration_seamless_m4t_v2.meta.json
│   │   │   │   │   ├── modeling_seamless_m4t_v2.data.json
│   │   │   │   │   └── modeling_seamless_m4t_v2.meta.json
│   │   │   │   ├── segformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_segformer.data.json
│   │   │   │   │   ├── configuration_segformer.meta.json
│   │   │   │   │   ├── feature_extraction_segformer.data.json
│   │   │   │   │   ├── feature_extraction_segformer.meta.json
│   │   │   │   │   ├── image_processing_segformer.data.json
│   │   │   │   │   ├── image_processing_segformer.meta.json
│   │   │   │   │   ├── modeling_segformer.data.json
│   │   │   │   │   ├── modeling_segformer.meta.json
│   │   │   │   │   ├── modeling_tf_segformer.data.json
│   │   │   │   │   └── modeling_tf_segformer.meta.json
│   │   │   │   ├── seggpt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_seggpt.data.json
│   │   │   │   │   ├── configuration_seggpt.meta.json
│   │   │   │   │   ├── image_processing_seggpt.data.json
│   │   │   │   │   ├── image_processing_seggpt.meta.json
│   │   │   │   │   ├── modeling_seggpt.data.json
│   │   │   │   │   └── modeling_seggpt.meta.json
│   │   │   │   ├── sew
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_sew.data.json
│   │   │   │   │   ├── configuration_sew.meta.json
│   │   │   │   │   ├── modeling_sew.data.json
│   │   │   │   │   └── modeling_sew.meta.json
│   │   │   │   ├── sew_d
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_sew_d.data.json
│   │   │   │   │   ├── configuration_sew_d.meta.json
│   │   │   │   │   ├── modeling_sew_d.data.json
│   │   │   │   │   └── modeling_sew_d.meta.json
│   │   │   │   ├── shieldgemma2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_shieldgemma2.data.json
│   │   │   │   │   ├── configuration_shieldgemma2.meta.json
│   │   │   │   │   ├── modeling_shieldgemma2.data.json
│   │   │   │   │   ├── modeling_shieldgemma2.meta.json
│   │   │   │   │   ├── processing_shieldgemma2.data.json
│   │   │   │   │   └── processing_shieldgemma2.meta.json
│   │   │   │   ├── siglip
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_siglip.data.json
│   │   │   │   │   ├── configuration_siglip.meta.json
│   │   │   │   │   ├── image_processing_siglip.data.json
│   │   │   │   │   ├── image_processing_siglip.meta.json
│   │   │   │   │   ├── image_processing_siglip_fast.data.json
│   │   │   │   │   ├── image_processing_siglip_fast.meta.json
│   │   │   │   │   ├── modeling_siglip.data.json
│   │   │   │   │   ├── modeling_siglip.meta.json
│   │   │   │   │   ├── processing_siglip.data.json
│   │   │   │   │   ├── processing_siglip.meta.json
│   │   │   │   │   ├── tokenization_siglip.data.json
│   │   │   │   │   └── tokenization_siglip.meta.json
│   │   │   │   ├── siglip2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_siglip2.data.json
│   │   │   │   │   ├── configuration_siglip2.meta.json
│   │   │   │   │   ├── image_processing_siglip2.data.json
│   │   │   │   │   ├── image_processing_siglip2.meta.json
│   │   │   │   │   ├── image_processing_siglip2_fast.data.json
│   │   │   │   │   ├── image_processing_siglip2_fast.meta.json
│   │   │   │   │   ├── modeling_siglip2.data.json
│   │   │   │   │   ├── modeling_siglip2.meta.json
│   │   │   │   │   ├── processing_siglip2.data.json
│   │   │   │   │   └── processing_siglip2.meta.json
│   │   │   │   ├── smolvlm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_smolvlm.data.json
│   │   │   │   │   ├── configuration_smolvlm.meta.json
│   │   │   │   │   ├── image_processing_smolvlm.data.json
│   │   │   │   │   ├── image_processing_smolvlm.meta.json
│   │   │   │   │   ├── image_processing_smolvlm_fast.data.json
│   │   │   │   │   ├── image_processing_smolvlm_fast.meta.json
│   │   │   │   │   ├── modeling_smolvlm.data.json
│   │   │   │   │   ├── modeling_smolvlm.meta.json
│   │   │   │   │   ├── processing_smolvlm.data.json
│   │   │   │   │   ├── processing_smolvlm.meta.json
│   │   │   │   │   ├── video_processing_smolvlm.data.json
│   │   │   │   │   └── video_processing_smolvlm.meta.json
│   │   │   │   ├── speech_encoder_decoder
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_speech_encoder_decoder.data.json
│   │   │   │   │   ├── configuration_speech_encoder_decoder.meta.json
│   │   │   │   │   ├── modeling_flax_speech_encoder_decoder.data.json
│   │   │   │   │   ├── modeling_flax_speech_encoder_decoder.meta.json
│   │   │   │   │   ├── modeling_speech_encoder_decoder.data.json
│   │   │   │   │   └── modeling_speech_encoder_decoder.meta.json
│   │   │   │   ├── speech_to_text
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_speech_to_text.data.json
│   │   │   │   │   ├── configuration_speech_to_text.meta.json
│   │   │   │   │   ├── feature_extraction_speech_to_text.data.json
│   │   │   │   │   ├── feature_extraction_speech_to_text.meta.json
│   │   │   │   │   ├── modeling_speech_to_text.data.json
│   │   │   │   │   ├── modeling_speech_to_text.meta.json
│   │   │   │   │   ├── modeling_tf_speech_to_text.data.json
│   │   │   │   │   ├── modeling_tf_speech_to_text.meta.json
│   │   │   │   │   ├── processing_speech_to_text.data.json
│   │   │   │   │   ├── processing_speech_to_text.meta.json
│   │   │   │   │   ├── tokenization_speech_to_text.data.json
│   │   │   │   │   └── tokenization_speech_to_text.meta.json
│   │   │   │   ├── speecht5
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_speecht5.data.json
│   │   │   │   │   ├── configuration_speecht5.meta.json
│   │   │   │   │   ├── feature_extraction_speecht5.data.json
│   │   │   │   │   ├── feature_extraction_speecht5.meta.json
│   │   │   │   │   ├── modeling_speecht5.data.json
│   │   │   │   │   ├── modeling_speecht5.meta.json
│   │   │   │   │   ├── number_normalizer.data.json
│   │   │   │   │   ├── number_normalizer.meta.json
│   │   │   │   │   ├── processing_speecht5.data.json
│   │   │   │   │   ├── processing_speecht5.meta.json
│   │   │   │   │   ├── tokenization_speecht5.data.json
│   │   │   │   │   └── tokenization_speecht5.meta.json
│   │   │   │   ├── splinter
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_splinter.data.json
│   │   │   │   │   ├── configuration_splinter.meta.json
│   │   │   │   │   ├── modeling_splinter.data.json
│   │   │   │   │   ├── modeling_splinter.meta.json
│   │   │   │   │   ├── tokenization_splinter.data.json
│   │   │   │   │   ├── tokenization_splinter.meta.json
│   │   │   │   │   ├── tokenization_splinter_fast.data.json
│   │   │   │   │   └── tokenization_splinter_fast.meta.json
│   │   │   │   ├── squeezebert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_squeezebert.data.json
│   │   │   │   │   ├── configuration_squeezebert.meta.json
│   │   │   │   │   ├── modeling_squeezebert.data.json
│   │   │   │   │   ├── modeling_squeezebert.meta.json
│   │   │   │   │   ├── tokenization_squeezebert.data.json
│   │   │   │   │   ├── tokenization_squeezebert.meta.json
│   │   │   │   │   ├── tokenization_squeezebert_fast.data.json
│   │   │   │   │   └── tokenization_squeezebert_fast.meta.json
│   │   │   │   ├── stablelm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_stablelm.data.json
│   │   │   │   │   ├── configuration_stablelm.meta.json
│   │   │   │   │   ├── modeling_stablelm.data.json
│   │   │   │   │   └── modeling_stablelm.meta.json
│   │   │   │   ├── starcoder2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_starcoder2.data.json
│   │   │   │   │   ├── configuration_starcoder2.meta.json
│   │   │   │   │   ├── modeling_starcoder2.data.json
│   │   │   │   │   └── modeling_starcoder2.meta.json
│   │   │   │   ├── superglue
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_superglue.data.json
│   │   │   │   │   ├── configuration_superglue.meta.json
│   │   │   │   │   ├── image_processing_superglue.data.json
│   │   │   │   │   ├── image_processing_superglue.meta.json
│   │   │   │   │   ├── modeling_superglue.data.json
│   │   │   │   │   └── modeling_superglue.meta.json
│   │   │   │   ├── superpoint
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_superpoint.data.json
│   │   │   │   │   ├── configuration_superpoint.meta.json
│   │   │   │   │   ├── image_processing_superpoint.data.json
│   │   │   │   │   ├── image_processing_superpoint.meta.json
│   │   │   │   │   ├── modeling_superpoint.data.json
│   │   │   │   │   └── modeling_superpoint.meta.json
│   │   │   │   ├── swiftformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_swiftformer.data.json
│   │   │   │   │   ├── configuration_swiftformer.meta.json
│   │   │   │   │   ├── modeling_swiftformer.data.json
│   │   │   │   │   ├── modeling_swiftformer.meta.json
│   │   │   │   │   ├── modeling_tf_swiftformer.data.json
│   │   │   │   │   └── modeling_tf_swiftformer.meta.json
│   │   │   │   ├── swin
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_swin.data.json
│   │   │   │   │   ├── configuration_swin.meta.json
│   │   │   │   │   ├── modeling_swin.data.json
│   │   │   │   │   ├── modeling_swin.meta.json
│   │   │   │   │   ├── modeling_tf_swin.data.json
│   │   │   │   │   └── modeling_tf_swin.meta.json
│   │   │   │   ├── swin2sr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_swin2sr.data.json
│   │   │   │   │   ├── configuration_swin2sr.meta.json
│   │   │   │   │   ├── image_processing_swin2sr.data.json
│   │   │   │   │   ├── image_processing_swin2sr.meta.json
│   │   │   │   │   ├── image_processing_swin2sr_fast.data.json
│   │   │   │   │   ├── image_processing_swin2sr_fast.meta.json
│   │   │   │   │   ├── modeling_swin2sr.data.json
│   │   │   │   │   └── modeling_swin2sr.meta.json
│   │   │   │   ├── swinv2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_swinv2.data.json
│   │   │   │   │   ├── configuration_swinv2.meta.json
│   │   │   │   │   ├── modeling_swinv2.data.json
│   │   │   │   │   └── modeling_swinv2.meta.json
│   │   │   │   ├── switch_transformers
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_switch_transformers.data.json
│   │   │   │   │   ├── configuration_switch_transformers.meta.json
│   │   │   │   │   ├── modeling_switch_transformers.data.json
│   │   │   │   │   └── modeling_switch_transformers.meta.json
│   │   │   │   ├── t5
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_t5.data.json
│   │   │   │   │   ├── configuration_t5.meta.json
│   │   │   │   │   ├── modeling_flax_t5.data.json
│   │   │   │   │   ├── modeling_flax_t5.meta.json
│   │   │   │   │   ├── modeling_t5.data.json
│   │   │   │   │   ├── modeling_t5.meta.json
│   │   │   │   │   ├── modeling_tf_t5.data.json
│   │   │   │   │   ├── modeling_tf_t5.meta.json
│   │   │   │   │   ├── tokenization_t5.data.json
│   │   │   │   │   ├── tokenization_t5.meta.json
│   │   │   │   │   ├── tokenization_t5_fast.data.json
│   │   │   │   │   └── tokenization_t5_fast.meta.json
│   │   │   │   ├── t5gemma
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── table_transformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_table_transformer.data.json
│   │   │   │   │   ├── configuration_table_transformer.meta.json
│   │   │   │   │   ├── modeling_table_transformer.data.json
│   │   │   │   │   └── modeling_table_transformer.meta.json
│   │   │   │   ├── tapas
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_tapas.data.json
│   │   │   │   │   ├── configuration_tapas.meta.json
│   │   │   │   │   ├── modeling_tapas.data.json
│   │   │   │   │   ├── modeling_tapas.meta.json
│   │   │   │   │   ├── modeling_tf_tapas.data.json
│   │   │   │   │   ├── modeling_tf_tapas.meta.json
│   │   │   │   │   ├── tokenization_tapas.data.json
│   │   │   │   │   └── tokenization_tapas.meta.json
│   │   │   │   ├── textnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_textnet.data.json
│   │   │   │   │   ├── configuration_textnet.meta.json
│   │   │   │   │   ├── image_processing_textnet.data.json
│   │   │   │   │   ├── image_processing_textnet.meta.json
│   │   │   │   │   ├── modeling_textnet.data.json
│   │   │   │   │   └── modeling_textnet.meta.json
│   │   │   │   ├── time_series_transformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_time_series_transformer.data.json
│   │   │   │   │   ├── configuration_time_series_transformer.meta.json
│   │   │   │   │   ├── modeling_time_series_transformer.data.json
│   │   │   │   │   └── modeling_time_series_transformer.meta.json
│   │   │   │   ├── timesfm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_timesfm.data.json
│   │   │   │   │   ├── configuration_timesfm.meta.json
│   │   │   │   │   ├── modeling_timesfm.data.json
│   │   │   │   │   └── modeling_timesfm.meta.json
│   │   │   │   ├── timesformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_timesformer.data.json
│   │   │   │   │   ├── configuration_timesformer.meta.json
│   │   │   │   │   ├── modeling_timesformer.data.json
│   │   │   │   │   └── modeling_timesformer.meta.json
│   │   │   │   ├── timm_backbone
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_timm_backbone.data.json
│   │   │   │   │   ├── configuration_timm_backbone.meta.json
│   │   │   │   │   ├── modeling_timm_backbone.data.json
│   │   │   │   │   └── modeling_timm_backbone.meta.json
│   │   │   │   ├── timm_wrapper
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_timm_wrapper.data.json
│   │   │   │   │   ├── configuration_timm_wrapper.meta.json
│   │   │   │   │   ├── modeling_timm_wrapper.data.json
│   │   │   │   │   └── modeling_timm_wrapper.meta.json
│   │   │   │   ├── trocr
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_trocr.data.json
│   │   │   │   │   ├── configuration_trocr.meta.json
│   │   │   │   │   ├── modeling_trocr.data.json
│   │   │   │   │   ├── modeling_trocr.meta.json
│   │   │   │   │   ├── processing_trocr.data.json
│   │   │   │   │   └── processing_trocr.meta.json
│   │   │   │   ├── tvp
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_tvp.data.json
│   │   │   │   │   ├── configuration_tvp.meta.json
│   │   │   │   │   ├── image_processing_tvp.data.json
│   │   │   │   │   ├── image_processing_tvp.meta.json
│   │   │   │   │   ├── modeling_tvp.data.json
│   │   │   │   │   ├── modeling_tvp.meta.json
│   │   │   │   │   ├── processing_tvp.data.json
│   │   │   │   │   └── processing_tvp.meta.json
│   │   │   │   ├── udop
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_udop.data.json
│   │   │   │   │   ├── configuration_udop.meta.json
│   │   │   │   │   ├── modeling_udop.data.json
│   │   │   │   │   ├── modeling_udop.meta.json
│   │   │   │   │   ├── processing_udop.data.json
│   │   │   │   │   ├── processing_udop.meta.json
│   │   │   │   │   ├── tokenization_udop.data.json
│   │   │   │   │   ├── tokenization_udop.meta.json
│   │   │   │   │   ├── tokenization_udop_fast.data.json
│   │   │   │   │   └── tokenization_udop_fast.meta.json
│   │   │   │   ├── umt5
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_umt5.data.json
│   │   │   │   │   ├── configuration_umt5.meta.json
│   │   │   │   │   ├── modeling_umt5.data.json
│   │   │   │   │   └── modeling_umt5.meta.json
│   │   │   │   ├── unispeech
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_unispeech.data.json
│   │   │   │   │   ├── configuration_unispeech.meta.json
│   │   │   │   │   ├── modeling_unispeech.data.json
│   │   │   │   │   └── modeling_unispeech.meta.json
│   │   │   │   ├── unispeech_sat
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_unispeech_sat.data.json
│   │   │   │   │   ├── configuration_unispeech_sat.meta.json
│   │   │   │   │   ├── modeling_unispeech_sat.data.json
│   │   │   │   │   └── modeling_unispeech_sat.meta.json
│   │   │   │   ├── univnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_univnet.data.json
│   │   │   │   │   ├── configuration_univnet.meta.json
│   │   │   │   │   ├── feature_extraction_univnet.data.json
│   │   │   │   │   ├── feature_extraction_univnet.meta.json
│   │   │   │   │   ├── modeling_univnet.data.json
│   │   │   │   │   └── modeling_univnet.meta.json
│   │   │   │   ├── upernet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_upernet.data.json
│   │   │   │   │   ├── configuration_upernet.meta.json
│   │   │   │   │   ├── modeling_upernet.data.json
│   │   │   │   │   └── modeling_upernet.meta.json
│   │   │   │   ├── video_llava
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_video_llava.data.json
│   │   │   │   │   ├── configuration_video_llava.meta.json
│   │   │   │   │   ├── image_processing_video_llava.data.json
│   │   │   │   │   ├── image_processing_video_llava.meta.json
│   │   │   │   │   ├── modeling_video_llava.data.json
│   │   │   │   │   ├── modeling_video_llava.meta.json
│   │   │   │   │   ├── processing_video_llava.data.json
│   │   │   │   │   └── processing_video_llava.meta.json
│   │   │   │   ├── videomae
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_videomae.data.json
│   │   │   │   │   ├── configuration_videomae.meta.json
│   │   │   │   │   ├── feature_extraction_videomae.data.json
│   │   │   │   │   ├── feature_extraction_videomae.meta.json
│   │   │   │   │   ├── image_processing_videomae.data.json
│   │   │   │   │   ├── image_processing_videomae.meta.json
│   │   │   │   │   ├── modeling_videomae.data.json
│   │   │   │   │   └── modeling_videomae.meta.json
│   │   │   │   ├── vilt
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vilt.data.json
│   │   │   │   │   ├── configuration_vilt.meta.json
│   │   │   │   │   ├── feature_extraction_vilt.data.json
│   │   │   │   │   ├── feature_extraction_vilt.meta.json
│   │   │   │   │   ├── image_processing_vilt.data.json
│   │   │   │   │   ├── image_processing_vilt.meta.json
│   │   │   │   │   ├── image_processing_vilt_fast.data.json
│   │   │   │   │   ├── image_processing_vilt_fast.meta.json
│   │   │   │   │   ├── modeling_vilt.data.json
│   │   │   │   │   ├── modeling_vilt.meta.json
│   │   │   │   │   ├── processing_vilt.data.json
│   │   │   │   │   └── processing_vilt.meta.json
│   │   │   │   ├── vipllava
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vipllava.data.json
│   │   │   │   │   ├── configuration_vipllava.meta.json
│   │   │   │   │   ├── modeling_vipllava.data.json
│   │   │   │   │   └── modeling_vipllava.meta.json
│   │   │   │   ├── vision_encoder_decoder
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vision_encoder_decoder.data.json
│   │   │   │   │   ├── configuration_vision_encoder_decoder.meta.json
│   │   │   │   │   ├── modeling_flax_vision_encoder_decoder.data.json
│   │   │   │   │   ├── modeling_flax_vision_encoder_decoder.meta.json
│   │   │   │   │   ├── modeling_tf_vision_encoder_decoder.data.json
│   │   │   │   │   ├── modeling_tf_vision_encoder_decoder.meta.json
│   │   │   │   │   ├── modeling_vision_encoder_decoder.data.json
│   │   │   │   │   └── modeling_vision_encoder_decoder.meta.json
│   │   │   │   ├── vision_text_dual_encoder
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vision_text_dual_encoder.data.json
│   │   │   │   │   ├── configuration_vision_text_dual_encoder.meta.json
│   │   │   │   │   ├── modeling_flax_vision_text_dual_encoder.data.json
│   │   │   │   │   ├── modeling_flax_vision_text_dual_encoder.meta.json
│   │   │   │   │   ├── modeling_tf_vision_text_dual_encoder.data.json
│   │   │   │   │   ├── modeling_tf_vision_text_dual_encoder.meta.json
│   │   │   │   │   ├── modeling_vision_text_dual_encoder.data.json
│   │   │   │   │   ├── modeling_vision_text_dual_encoder.meta.json
│   │   │   │   │   ├── processing_vision_text_dual_encoder.data.json
│   │   │   │   │   └── processing_vision_text_dual_encoder.meta.json
│   │   │   │   ├── visual_bert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_visual_bert.data.json
│   │   │   │   │   ├── configuration_visual_bert.meta.json
│   │   │   │   │   ├── modeling_visual_bert.data.json
│   │   │   │   │   └── modeling_visual_bert.meta.json
│   │   │   │   ├── vit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vit.data.json
│   │   │   │   │   ├── configuration_vit.meta.json
│   │   │   │   │   ├── feature_extraction_vit.data.json
│   │   │   │   │   ├── feature_extraction_vit.meta.json
│   │   │   │   │   ├── image_processing_vit.data.json
│   │   │   │   │   ├── image_processing_vit.meta.json
│   │   │   │   │   ├── image_processing_vit_fast.data.json
│   │   │   │   │   ├── image_processing_vit_fast.meta.json
│   │   │   │   │   ├── modeling_flax_vit.data.json
│   │   │   │   │   ├── modeling_flax_vit.meta.json
│   │   │   │   │   ├── modeling_tf_vit.data.json
│   │   │   │   │   ├── modeling_tf_vit.meta.json
│   │   │   │   │   ├── modeling_vit.data.json
│   │   │   │   │   └── modeling_vit.meta.json
│   │   │   │   ├── vit_mae
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vit_mae.data.json
│   │   │   │   │   ├── configuration_vit_mae.meta.json
│   │   │   │   │   ├── modeling_tf_vit_mae.data.json
│   │   │   │   │   ├── modeling_tf_vit_mae.meta.json
│   │   │   │   │   ├── modeling_vit_mae.data.json
│   │   │   │   │   └── modeling_vit_mae.meta.json
│   │   │   │   ├── vit_msn
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vit_msn.data.json
│   │   │   │   │   ├── configuration_vit_msn.meta.json
│   │   │   │   │   ├── modeling_vit_msn.data.json
│   │   │   │   │   └── modeling_vit_msn.meta.json
│   │   │   │   ├── vitdet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vitdet.data.json
│   │   │   │   │   ├── configuration_vitdet.meta.json
│   │   │   │   │   ├── modeling_vitdet.data.json
│   │   │   │   │   └── modeling_vitdet.meta.json
│   │   │   │   ├── vitmatte
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vitmatte.data.json
│   │   │   │   │   ├── configuration_vitmatte.meta.json
│   │   │   │   │   ├── image_processing_vitmatte.data.json
│   │   │   │   │   ├── image_processing_vitmatte.meta.json
│   │   │   │   │   ├── image_processing_vitmatte_fast.data.json
│   │   │   │   │   ├── image_processing_vitmatte_fast.meta.json
│   │   │   │   │   ├── modeling_vitmatte.data.json
│   │   │   │   │   └── modeling_vitmatte.meta.json
│   │   │   │   ├── vitpose
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vitpose.data.json
│   │   │   │   │   ├── configuration_vitpose.meta.json
│   │   │   │   │   ├── image_processing_vitpose.data.json
│   │   │   │   │   ├── image_processing_vitpose.meta.json
│   │   │   │   │   ├── modeling_vitpose.data.json
│   │   │   │   │   └── modeling_vitpose.meta.json
│   │   │   │   ├── vitpose_backbone
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vitpose_backbone.data.json
│   │   │   │   │   ├── configuration_vitpose_backbone.meta.json
│   │   │   │   │   ├── modeling_vitpose_backbone.data.json
│   │   │   │   │   └── modeling_vitpose_backbone.meta.json
│   │   │   │   ├── vits
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vits.data.json
│   │   │   │   │   ├── configuration_vits.meta.json
│   │   │   │   │   ├── modeling_vits.data.json
│   │   │   │   │   ├── modeling_vits.meta.json
│   │   │   │   │   ├── tokenization_vits.data.json
│   │   │   │   │   └── tokenization_vits.meta.json
│   │   │   │   ├── vivit
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vivit.data.json
│   │   │   │   │   ├── configuration_vivit.meta.json
│   │   │   │   │   ├── image_processing_vivit.data.json
│   │   │   │   │   ├── image_processing_vivit.meta.json
│   │   │   │   │   ├── modeling_vivit.data.json
│   │   │   │   │   └── modeling_vivit.meta.json
│   │   │   │   ├── vjepa2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_vjepa2.data.json
│   │   │   │   │   ├── configuration_vjepa2.meta.json
│   │   │   │   │   ├── modeling_vjepa2.data.json
│   │   │   │   │   ├── modeling_vjepa2.meta.json
│   │   │   │   │   ├── video_processing_vjepa2.data.json
│   │   │   │   │   └── video_processing_vjepa2.meta.json
│   │   │   │   ├── voxtral
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_voxtral.data.json
│   │   │   │   │   ├── configuration_voxtral.meta.json
│   │   │   │   │   ├── modeling_voxtral.data.json
│   │   │   │   │   ├── modeling_voxtral.meta.json
│   │   │   │   │   ├── processing_voxtral.data.json
│   │   │   │   │   └── processing_voxtral.meta.json
│   │   │   │   ├── wav2vec2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_wav2vec2.data.json
│   │   │   │   │   ├── configuration_wav2vec2.meta.json
│   │   │   │   │   ├── feature_extraction_wav2vec2.data.json
│   │   │   │   │   ├── feature_extraction_wav2vec2.meta.json
│   │   │   │   │   ├── modeling_flax_wav2vec2.data.json
│   │   │   │   │   ├── modeling_flax_wav2vec2.meta.json
│   │   │   │   │   ├── modeling_tf_wav2vec2.data.json
│   │   │   │   │   ├── modeling_tf_wav2vec2.meta.json
│   │   │   │   │   ├── modeling_wav2vec2.data.json
│   │   │   │   │   ├── modeling_wav2vec2.meta.json
│   │   │   │   │   ├── processing_wav2vec2.data.json
│   │   │   │   │   ├── processing_wav2vec2.meta.json
│   │   │   │   │   ├── tokenization_wav2vec2.data.json
│   │   │   │   │   └── tokenization_wav2vec2.meta.json
│   │   │   │   ├── wav2vec2_bert
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_wav2vec2_bert.data.json
│   │   │   │   │   ├── configuration_wav2vec2_bert.meta.json
│   │   │   │   │   ├── modeling_wav2vec2_bert.data.json
│   │   │   │   │   ├── modeling_wav2vec2_bert.meta.json
│   │   │   │   │   ├── processing_wav2vec2_bert.data.json
│   │   │   │   │   └── processing_wav2vec2_bert.meta.json
│   │   │   │   ├── wav2vec2_conformer
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_wav2vec2_conformer.data.json
│   │   │   │   │   ├── configuration_wav2vec2_conformer.meta.json
│   │   │   │   │   ├── modeling_wav2vec2_conformer.data.json
│   │   │   │   │   └── modeling_wav2vec2_conformer.meta.json
│   │   │   │   ├── wav2vec2_phoneme
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── tokenization_wav2vec2_phoneme.data.json
│   │   │   │   │   └── tokenization_wav2vec2_phoneme.meta.json
│   │   │   │   ├── wav2vec2_with_lm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── processing_wav2vec2_with_lm.data.json
│   │   │   │   │   └── processing_wav2vec2_with_lm.meta.json
│   │   │   │   ├── wavlm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_wavlm.data.json
│   │   │   │   │   ├── configuration_wavlm.meta.json
│   │   │   │   │   ├── modeling_wavlm.data.json
│   │   │   │   │   └── modeling_wavlm.meta.json
│   │   │   │   ├── whisper
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_whisper.data.json
│   │   │   │   │   ├── configuration_whisper.meta.json
│   │   │   │   │   ├── english_normalizer.data.json
│   │   │   │   │   ├── english_normalizer.meta.json
│   │   │   │   │   ├── feature_extraction_whisper.data.json
│   │   │   │   │   ├── feature_extraction_whisper.meta.json
│   │   │   │   │   ├── generation_whisper.data.json
│   │   │   │   │   ├── generation_whisper.meta.json
│   │   │   │   │   ├── modeling_flax_whisper.data.json
│   │   │   │   │   ├── modeling_flax_whisper.meta.json
│   │   │   │   │   ├── modeling_tf_whisper.data.json
│   │   │   │   │   ├── modeling_tf_whisper.meta.json
│   │   │   │   │   ├── modeling_whisper.data.json
│   │   │   │   │   ├── modeling_whisper.meta.json
│   │   │   │   │   ├── processing_whisper.data.json
│   │   │   │   │   ├── processing_whisper.meta.json
│   │   │   │   │   ├── tokenization_whisper.data.json
│   │   │   │   │   ├── tokenization_whisper.meta.json
│   │   │   │   │   ├── tokenization_whisper_fast.data.json
│   │   │   │   │   └── tokenization_whisper_fast.meta.json
│   │   │   │   ├── x_clip
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_x_clip.data.json
│   │   │   │   │   ├── configuration_x_clip.meta.json
│   │   │   │   │   ├── modeling_x_clip.data.json
│   │   │   │   │   ├── modeling_x_clip.meta.json
│   │   │   │   │   ├── processing_x_clip.data.json
│   │   │   │   │   └── processing_x_clip.meta.json
│   │   │   │   ├── xglm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_xglm.data.json
│   │   │   │   │   ├── configuration_xglm.meta.json
│   │   │   │   │   ├── modeling_flax_xglm.data.json
│   │   │   │   │   ├── modeling_flax_xglm.meta.json
│   │   │   │   │   ├── modeling_tf_xglm.data.json
│   │   │   │   │   ├── modeling_tf_xglm.meta.json
│   │   │   │   │   ├── modeling_xglm.data.json
│   │   │   │   │   ├── modeling_xglm.meta.json
│   │   │   │   │   ├── tokenization_xglm.data.json
│   │   │   │   │   ├── tokenization_xglm.meta.json
│   │   │   │   │   ├── tokenization_xglm_fast.data.json
│   │   │   │   │   └── tokenization_xglm_fast.meta.json
│   │   │   │   ├── xlm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_xlm.data.json
│   │   │   │   │   ├── configuration_xlm.meta.json
│   │   │   │   │   ├── modeling_tf_xlm.data.json
│   │   │   │   │   ├── modeling_tf_xlm.meta.json
│   │   │   │   │   ├── modeling_xlm.data.json
│   │   │   │   │   ├── modeling_xlm.meta.json
│   │   │   │   │   ├── tokenization_xlm.data.json
│   │   │   │   │   └── tokenization_xlm.meta.json
│   │   │   │   ├── xlm_roberta
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_xlm_roberta.data.json
│   │   │   │   │   ├── configuration_xlm_roberta.meta.json
│   │   │   │   │   ├── modeling_flax_xlm_roberta.data.json
│   │   │   │   │   ├── modeling_flax_xlm_roberta.meta.json
│   │   │   │   │   ├── modeling_tf_xlm_roberta.data.json
│   │   │   │   │   ├── modeling_tf_xlm_roberta.meta.json
│   │   │   │   │   ├── modeling_xlm_roberta.data.json
│   │   │   │   │   ├── modeling_xlm_roberta.meta.json
│   │   │   │   │   ├── tokenization_xlm_roberta.data.json
│   │   │   │   │   ├── tokenization_xlm_roberta.meta.json
│   │   │   │   │   ├── tokenization_xlm_roberta_fast.data.json
│   │   │   │   │   └── tokenization_xlm_roberta_fast.meta.json
│   │   │   │   ├── xlm_roberta_xl
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_xlm_roberta_xl.data.json
│   │   │   │   │   ├── configuration_xlm_roberta_xl.meta.json
│   │   │   │   │   ├── modeling_xlm_roberta_xl.data.json
│   │   │   │   │   └── modeling_xlm_roberta_xl.meta.json
│   │   │   │   ├── xlnet
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_xlnet.data.json
│   │   │   │   │   ├── configuration_xlnet.meta.json
│   │   │   │   │   ├── modeling_tf_xlnet.data.json
│   │   │   │   │   ├── modeling_tf_xlnet.meta.json
│   │   │   │   │   ├── modeling_xlnet.data.json
│   │   │   │   │   ├── modeling_xlnet.meta.json
│   │   │   │   │   ├── tokenization_xlnet.data.json
│   │   │   │   │   ├── tokenization_xlnet.meta.json
│   │   │   │   │   ├── tokenization_xlnet_fast.data.json
│   │   │   │   │   └── tokenization_xlnet_fast.meta.json
│   │   │   │   ├── xlstm
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   └── __init__.meta.json
│   │   │   │   ├── xmod
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_xmod.data.json
│   │   │   │   │   ├── configuration_xmod.meta.json
│   │   │   │   │   ├── modeling_xmod.data.json
│   │   │   │   │   └── modeling_xmod.meta.json
│   │   │   │   ├── yolos
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_yolos.data.json
│   │   │   │   │   ├── configuration_yolos.meta.json
│   │   │   │   │   ├── feature_extraction_yolos.data.json
│   │   │   │   │   ├── feature_extraction_yolos.meta.json
│   │   │   │   │   ├── image_processing_yolos.data.json
│   │   │   │   │   ├── image_processing_yolos.meta.json
│   │   │   │   │   ├── image_processing_yolos_fast.data.json
│   │   │   │   │   ├── image_processing_yolos_fast.meta.json
│   │   │   │   │   ├── modeling_yolos.data.json
│   │   │   │   │   └── modeling_yolos.meta.json
│   │   │   │   ├── yoso
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_yoso.data.json
│   │   │   │   │   ├── configuration_yoso.meta.json
│   │   │   │   │   ├── modeling_yoso.data.json
│   │   │   │   │   └── modeling_yoso.meta.json
│   │   │   │   ├── zamba
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_zamba.data.json
│   │   │   │   │   ├── configuration_zamba.meta.json
│   │   │   │   │   ├── modeling_zamba.data.json
│   │   │   │   │   └── modeling_zamba.meta.json
│   │   │   │   ├── zamba2
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── configuration_zamba2.data.json
│   │   │   │   │   ├── configuration_zamba2.meta.json
│   │   │   │   │   ├── modeling_zamba2.data.json
│   │   │   │   │   └── modeling_zamba2.meta.json
│   │   │   │   └── zoedepth
│   │   │   │       ├── __init__.data.json
│   │   │   │       ├── __init__.meta.json
│   │   │   │       ├── configuration_zoedepth.data.json
│   │   │   │       ├── configuration_zoedepth.meta.json
│   │   │   │       ├── image_processing_zoedepth.data.json
│   │   │   │       ├── image_processing_zoedepth.meta.json
│   │   │   │       ├── image_processing_zoedepth_fast.data.json
│   │   │   │       ├── image_processing_zoedepth_fast.meta.json
│   │   │   │       ├── modeling_zoedepth.data.json
│   │   │   │       └── modeling_zoedepth.meta.json
│   │   │   ├── onnx
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── config.data.json
│   │   │   │   ├── config.meta.json
│   │   │   │   ├── convert.data.json
│   │   │   │   ├── convert.meta.json
│   │   │   │   ├── features.data.json
│   │   │   │   ├── features.meta.json
│   │   │   │   ├── utils.data.json
│   │   │   │   └── utils.meta.json
│   │   │   ├── optimization.data.json
│   │   │   ├── optimization.meta.json
│   │   │   ├── optimization_tf.data.json
│   │   │   ├── optimization_tf.meta.json
│   │   │   ├── pipelines
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── audio_classification.data.json
│   │   │   │   ├── audio_classification.meta.json
│   │   │   │   ├── audio_utils.data.json
│   │   │   │   ├── audio_utils.meta.json
│   │   │   │   ├── automatic_speech_recognition.data.json
│   │   │   │   ├── automatic_speech_recognition.meta.json
│   │   │   │   ├── base.data.json
│   │   │   │   ├── base.meta.json
│   │   │   │   ├── depth_estimation.data.json
│   │   │   │   ├── depth_estimation.meta.json
│   │   │   │   ├── document_question_answering.data.json
│   │   │   │   ├── document_question_answering.meta.json
│   │   │   │   ├── feature_extraction.data.json
│   │   │   │   ├── feature_extraction.meta.json
│   │   │   │   ├── fill_mask.data.json
│   │   │   │   ├── fill_mask.meta.json
│   │   │   │   ├── image_classification.data.json
│   │   │   │   ├── image_classification.meta.json
│   │   │   │   ├── image_feature_extraction.data.json
│   │   │   │   ├── image_feature_extraction.meta.json
│   │   │   │   ├── image_segmentation.data.json
│   │   │   │   ├── image_segmentation.meta.json
│   │   │   │   ├── image_text_to_text.data.json
│   │   │   │   ├── image_text_to_text.meta.json
│   │   │   │   ├── image_to_image.data.json
│   │   │   │   ├── image_to_image.meta.json
│   │   │   │   ├── image_to_text.data.json
│   │   │   │   ├── image_to_text.meta.json
│   │   │   │   ├── mask_generation.data.json
│   │   │   │   ├── mask_generation.meta.json
│   │   │   │   ├── object_detection.data.json
│   │   │   │   ├── object_detection.meta.json
│   │   │   │   ├── pt_utils.data.json
│   │   │   │   ├── pt_utils.meta.json
│   │   │   │   ├── question_answering.data.json
│   │   │   │   ├── question_answering.meta.json
│   │   │   │   ├── table_question_answering.data.json
│   │   │   │   ├── table_question_answering.meta.json
│   │   │   │   ├── text2text_generation.data.json
│   │   │   │   ├── text2text_generation.meta.json
│   │   │   │   ├── text_classification.data.json
│   │   │   │   ├── text_classification.meta.json
│   │   │   │   ├── text_generation.data.json
│   │   │   │   ├── text_generation.meta.json
│   │   │   │   ├── text_to_audio.data.json
│   │   │   │   ├── text_to_audio.meta.json
│   │   │   │   ├── token_classification.data.json
│   │   │   │   ├── token_classification.meta.json
│   │   │   │   ├── video_classification.data.json
│   │   │   │   ├── video_classification.meta.json
│   │   │   │   ├── visual_question_answering.data.json
│   │   │   │   ├── visual_question_answering.meta.json
│   │   │   │   ├── zero_shot_audio_classification.data.json
│   │   │   │   ├── zero_shot_audio_classification.meta.json
│   │   │   │   ├── zero_shot_classification.data.json
│   │   │   │   ├── zero_shot_classification.meta.json
│   │   │   │   ├── zero_shot_image_classification.data.json
│   │   │   │   ├── zero_shot_image_classification.meta.json
│   │   │   │   ├── zero_shot_object_detection.data.json
│   │   │   │   └── zero_shot_object_detection.meta.json
│   │   │   ├── processing_utils.data.json
│   │   │   ├── processing_utils.meta.json
│   │   │   ├── pytorch_utils.data.json
│   │   │   ├── pytorch_utils.meta.json
│   │   │   ├── quantizers
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── auto.data.json
│   │   │   │   ├── auto.meta.json
│   │   │   │   ├── base.data.json
│   │   │   │   ├── base.meta.json
│   │   │   │   ├── quantizer_aqlm.data.json
│   │   │   │   ├── quantizer_aqlm.meta.json
│   │   │   │   ├── quantizer_auto_round.data.json
│   │   │   │   ├── quantizer_auto_round.meta.json
│   │   │   │   ├── quantizer_awq.data.json
│   │   │   │   ├── quantizer_awq.meta.json
│   │   │   │   ├── quantizer_bitnet.data.json
│   │   │   │   ├── quantizer_bitnet.meta.json
│   │   │   │   ├── quantizer_bnb_4bit.data.json
│   │   │   │   ├── quantizer_bnb_4bit.meta.json
│   │   │   │   ├── quantizer_bnb_8bit.data.json
│   │   │   │   ├── quantizer_bnb_8bit.meta.json
│   │   │   │   ├── quantizer_compressed_tensors.data.json
│   │   │   │   ├── quantizer_compressed_tensors.meta.json
│   │   │   │   ├── quantizer_eetq.data.json
│   │   │   │   ├── quantizer_eetq.meta.json
│   │   │   │   ├── quantizer_fbgemm_fp8.data.json
│   │   │   │   ├── quantizer_fbgemm_fp8.meta.json
│   │   │   │   ├── quantizer_finegrained_fp8.data.json
│   │   │   │   ├── quantizer_finegrained_fp8.meta.json
│   │   │   │   ├── quantizer_fp_quant.data.json
│   │   │   │   ├── quantizer_fp_quant.meta.json
│   │   │   │   ├── quantizer_gptq.data.json
│   │   │   │   ├── quantizer_gptq.meta.json
│   │   │   │   ├── quantizer_higgs.data.json
│   │   │   │   ├── quantizer_higgs.meta.json
│   │   │   │   ├── quantizer_hqq.data.json
│   │   │   │   ├── quantizer_hqq.meta.json
│   │   │   │   ├── quantizer_quanto.data.json
│   │   │   │   ├── quantizer_quanto.meta.json
│   │   │   │   ├── quantizer_quark.data.json
│   │   │   │   ├── quantizer_quark.meta.json
│   │   │   │   ├── quantizer_spqr.data.json
│   │   │   │   ├── quantizer_spqr.meta.json
│   │   │   │   ├── quantizer_torchao.data.json
│   │   │   │   ├── quantizer_torchao.meta.json
│   │   │   │   ├── quantizer_vptq.data.json
│   │   │   │   ├── quantizer_vptq.meta.json
│   │   │   │   ├── quantizers_utils.data.json
│   │   │   │   └── quantizers_utils.meta.json
│   │   │   ├── safetensors_conversion.data.json
│   │   │   ├── safetensors_conversion.meta.json
│   │   │   ├── tf_utils.data.json
│   │   │   ├── tf_utils.meta.json
│   │   │   ├── time_series_utils.data.json
│   │   │   ├── time_series_utils.meta.json
│   │   │   ├── tokenization_utils.data.json
│   │   │   ├── tokenization_utils.meta.json
│   │   │   ├── tokenization_utils_base.data.json
│   │   │   ├── tokenization_utils_base.meta.json
│   │   │   ├── tokenization_utils_fast.data.json
│   │   │   ├── tokenization_utils_fast.meta.json
│   │   │   ├── trainer.data.json
│   │   │   ├── trainer.meta.json
│   │   │   ├── trainer_callback.data.json
│   │   │   ├── trainer_callback.meta.json
│   │   │   ├── trainer_pt_utils.data.json
│   │   │   ├── trainer_pt_utils.meta.json
│   │   │   ├── trainer_seq2seq.data.json
│   │   │   ├── trainer_seq2seq.meta.json
│   │   │   ├── trainer_utils.data.json
│   │   │   ├── trainer_utils.meta.json
│   │   │   ├── training_args.data.json
│   │   │   ├── training_args.meta.json
│   │   │   ├── training_args_seq2seq.data.json
│   │   │   ├── training_args_seq2seq.meta.json
│   │   │   ├── training_args_tf.data.json
│   │   │   ├── training_args_tf.meta.json
│   │   │   ├── utils
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── auto_docstring.data.json
│   │   │   │   ├── auto_docstring.meta.json
│   │   │   │   ├── backbone_utils.data.json
│   │   │   │   ├── backbone_utils.meta.json
│   │   │   │   ├── chat_template_utils.data.json
│   │   │   │   ├── chat_template_utils.meta.json
│   │   │   │   ├── constants.data.json
│   │   │   │   ├── constants.meta.json
│   │   │   │   ├── deprecation.data.json
│   │   │   │   ├── deprecation.meta.json
│   │   │   │   ├── doc.data.json
│   │   │   │   ├── doc.meta.json
│   │   │   │   ├── dummy_flax_objects.data.json
│   │   │   │   ├── dummy_flax_objects.meta.json
│   │   │   │   ├── dummy_mistral_common_objects.data.json
│   │   │   │   ├── dummy_mistral_common_objects.meta.json
│   │   │   │   ├── dummy_pt_objects.data.json
│   │   │   │   ├── dummy_pt_objects.meta.json
│   │   │   │   ├── dummy_sentencepiece_and_tokenizers_objects.data.json
│   │   │   │   ├── dummy_sentencepiece_and_tokenizers_objects.meta.json
│   │   │   │   ├── dummy_tf_objects.data.json
│   │   │   │   ├── dummy_tf_objects.meta.json
│   │   │   │   ├── dummy_tokenizers_objects.data.json
│   │   │   │   ├── dummy_tokenizers_objects.meta.json
│   │   │   │   ├── dummy_torchvision_objects.data.json
│   │   │   │   ├── dummy_torchvision_objects.meta.json
│   │   │   │   ├── dummy_vision_objects.data.json
│   │   │   │   ├── dummy_vision_objects.meta.json
│   │   │   │   ├── generic.data.json
│   │   │   │   ├── generic.meta.json
│   │   │   │   ├── hub.data.json
│   │   │   │   ├── hub.meta.json
│   │   │   │   ├── import_utils.data.json
│   │   │   │   ├── import_utils.meta.json
│   │   │   │   ├── logging.data.json
│   │   │   │   ├── logging.meta.json
│   │   │   │   ├── metrics.data.json
│   │   │   │   ├── metrics.meta.json
│   │   │   │   ├── model_parallel_utils.data.json
│   │   │   │   ├── model_parallel_utils.meta.json
│   │   │   │   ├── notebook.data.json
│   │   │   │   ├── notebook.meta.json
│   │   │   │   ├── peft_utils.data.json
│   │   │   │   ├── peft_utils.meta.json
│   │   │   │   ├── quantization_config.data.json
│   │   │   │   ├── quantization_config.meta.json
│   │   │   │   ├── versions.data.json
│   │   │   │   └── versions.meta.json
│   │   │   ├── video_processing_utils.data.json
│   │   │   ├── video_processing_utils.meta.json
│   │   │   ├── video_utils.data.json
│   │   │   └── video_utils.meta.json
│   │   ├── types.data.json
│   │   ├── types.meta.json
│   │   ├── typing.data.json
│   │   ├── typing.meta.json
│   │   ├── typing_extensions.data.json
│   │   ├── typing_extensions.meta.json
│   │   ├── typing_inspection
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── introspection.data.json
│   │   │   ├── introspection.meta.json
│   │   │   ├── typing_objects.data.json
│   │   │   └── typing_objects.meta.json
│   │   ├── ujson
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── unicodedata.data.json
│   │   ├── unicodedata.meta.json
│   │   ├── unittest
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _log.data.json
│   │   │   ├── _log.meta.json
│   │   │   ├── async_case.data.json
│   │   │   ├── async_case.meta.json
│   │   │   ├── case.data.json
│   │   │   ├── case.meta.json
│   │   │   ├── loader.data.json
│   │   │   ├── loader.meta.json
│   │   │   ├── main.data.json
│   │   │   ├── main.meta.json
│   │   │   ├── mock.data.json
│   │   │   ├── mock.meta.json
│   │   │   ├── result.data.json
│   │   │   ├── result.meta.json
│   │   │   ├── runner.data.json
│   │   │   ├── runner.meta.json
│   │   │   ├── signals.data.json
│   │   │   ├── signals.meta.json
│   │   │   ├── suite.data.json
│   │   │   └── suite.meta.json
│   │   ├── urllib
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── error.data.json
│   │   │   ├── error.meta.json
│   │   │   ├── parse.data.json
│   │   │   ├── parse.meta.json
│   │   │   ├── request.data.json
│   │   │   ├── request.meta.json
│   │   │   ├── response.data.json
│   │   │   └── response.meta.json
│   │   ├── urllib3
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _base_connection.data.json
│   │   │   ├── _base_connection.meta.json
│   │   │   ├── _collections.data.json
│   │   │   ├── _collections.meta.json
│   │   │   ├── _request_methods.data.json
│   │   │   ├── _request_methods.meta.json
│   │   │   ├── _version.data.json
│   │   │   ├── _version.meta.json
│   │   │   ├── connection.data.json
│   │   │   ├── connection.meta.json
│   │   │   ├── connectionpool.data.json
│   │   │   ├── connectionpool.meta.json
│   │   │   ├── contrib
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── socks.data.json
│   │   │   │   └── socks.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── fields.data.json
│   │   │   ├── fields.meta.json
│   │   │   ├── filepost.data.json
│   │   │   ├── filepost.meta.json
│   │   │   ├── http2
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── probe.data.json
│   │   │   │   └── probe.meta.json
│   │   │   ├── poolmanager.data.json
│   │   │   ├── poolmanager.meta.json
│   │   │   ├── response.data.json
│   │   │   ├── response.meta.json
│   │   │   └── util
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── connection.data.json
│   │   │       ├── connection.meta.json
│   │   │       ├── proxy.data.json
│   │   │       ├── proxy.meta.json
│   │   │       ├── request.data.json
│   │   │       ├── request.meta.json
│   │   │       ├── response.data.json
│   │   │       ├── response.meta.json
│   │   │       ├── retry.data.json
│   │   │       ├── retry.meta.json
│   │   │       ├── ssl_.data.json
│   │   │       ├── ssl_.meta.json
│   │   │       ├── ssl_match_hostname.data.json
│   │   │       ├── ssl_match_hostname.meta.json
│   │   │       ├── ssltransport.data.json
│   │   │       ├── ssltransport.meta.json
│   │   │       ├── timeout.data.json
│   │   │       ├── timeout.meta.json
│   │   │       ├── url.data.json
│   │   │       ├── url.meta.json
│   │   │       ├── util.data.json
│   │   │       ├── util.meta.json
│   │   │       ├── wait.data.json
│   │   │       └── wait.meta.json
│   │   ├── utils
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── monitoring.data.json
│   │   │   ├── monitoring.meta.json
│   │   │   ├── thought_logger.data.json
│   │   │   └── thought_logger.meta.json
│   │   ├── uuid.data.json
│   │   ├── uuid.meta.json
│   │   ├── uvloop
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _version.data.json
│   │   │   ├── _version.meta.json
│   │   │   ├── includes
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── loop.data.json
│   │   │   └── loop.meta.json
│   │   ├── visualizer_test.data.json
│   │   ├── visualizer_test.meta.json
│   │   ├── warnings.data.json
│   │   ├── warnings.meta.json
│   │   ├── weakref.data.json
│   │   ├── weakref.meta.json
│   │   ├── workspace
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── global_workspace.data.json
│   │   │   └── global_workspace.meta.json
│   │   ├── xml
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── etree
│   │   │   │   ├── ElementTree.data.json
│   │   │   │   ├── ElementTree.meta.json
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   └── parsers
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       └── expat
│   │   │           ├── __init__.data.json
│   │   │           └── __init__.meta.json
│   │   ├── yaml
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _yaml.data.json
│   │   │   ├── _yaml.meta.json
│   │   │   ├── composer.data.json
│   │   │   ├── composer.meta.json
│   │   │   ├── constructor.data.json
│   │   │   ├── constructor.meta.json
│   │   │   ├── cyaml.data.json
│   │   │   ├── cyaml.meta.json
│   │   │   ├── dumper.data.json
│   │   │   ├── dumper.meta.json
│   │   │   ├── emitter.data.json
│   │   │   ├── emitter.meta.json
│   │   │   ├── error.data.json
│   │   │   ├── error.meta.json
│   │   │   ├── events.data.json
│   │   │   ├── events.meta.json
│   │   │   ├── loader.data.json
│   │   │   ├── loader.meta.json
│   │   │   ├── nodes.data.json
│   │   │   ├── nodes.meta.json
│   │   │   ├── parser.data.json
│   │   │   ├── parser.meta.json
│   │   │   ├── reader.data.json
│   │   │   ├── reader.meta.json
│   │   │   ├── representer.data.json
│   │   │   ├── representer.meta.json
│   │   │   ├── resolver.data.json
│   │   │   ├── resolver.meta.json
│   │   │   ├── scanner.data.json
│   │   │   ├── scanner.meta.json
│   │   │   ├── serializer.data.json
│   │   │   ├── serializer.meta.json
│   │   │   ├── tokens.data.json
│   │   │   └── tokens.meta.json
│   │   ├── yarl
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _parse.data.json
│   │   │   ├── _parse.meta.json
│   │   │   ├── _path.data.json
│   │   │   ├── _path.meta.json
│   │   │   ├── _query.data.json
│   │   │   ├── _query.meta.json
│   │   │   ├── _quoters.data.json
│   │   │   ├── _quoters.meta.json
│   │   │   ├── _quoting.data.json
│   │   │   ├── _quoting.meta.json
│   │   │   ├── _quoting_py.data.json
│   │   │   ├── _quoting_py.meta.json
│   │   │   ├── _url.data.json
│   │   │   └── _url.meta.json
│   │   ├── zipfile
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── zipimport.data.json
│   │   ├── zipimport.meta.json
│   │   ├── zlib.data.json
│   │   ├── zlib.meta.json
│   │   ├── zoneinfo
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _common.data.json
│   │   │   ├── _common.meta.json
│   │   │   ├── _tzpath.data.json
│   │   │   └── _tzpath.meta.json
│   │   └── zstandard
│   │       ├── __init__.data.json
│   │       └── __init__.meta.json
│   └── CACHEDIR.TAG
├── README.md
├── __init__.py (45 bytes)
├── agents
│   ├── .DS_Store
│   ├── __init__.py (136 bytes)
│   ├── base_agent.py (4267 bytes)
│   ├── consultant_agent.py (4476 bytes)
│   ├── critic_agent.py (4667 bytes)
│   ├── emergence_agent.py (6109 bytes)
│   ├── generator_agent.py (10668 bytes)
│   ├── metacognition_agent.py (2874 bytes)
│   ├── planner_agent.py (11881 bytes)
│   ├── rag_agent.py (4035 bytes)
│   ├── reporter_agent.py (3937 bytes)
│   ├── reviewer_agent.py (2760 bytes)
│   ├── safety_director_agent.py (2967 bytes)
│   ├── tool_router_agent.py (6228 bytes)
│   ├── web_browser_agent.py (5413 bytes)
│   ├── wikipedia_agent.py (5514 bytes)
│   └── worker.py (3799 bytes)
├── config
│   ├── __init__.py (39 bytes)
│   └── models.yml
├── container
│   ├── __init__.py (42 bytes)
│   └── container.py (5738 bytes)
├── doc
│   ├── improved_ai_architecture 2.html
│   └── roadmap.md
├── domain
│   ├── boundary_enforcer.py (1542 bytes)
│   ├── evaluation.py (1058 bytes)
│   ├── model_manager.py (4553 bytes)
│   └── schemas.py (2674 bytes)
├── enhanced_project_structure.md
├── enhanced_python_analyzer.py (23016 bytes)
├── env.sample
├── hrm_test.py (3961 bytes)
├── jamba_test.py (3599 bytes)
├── liquids4_test.py (4510 bytes)
├── logs
│   └── worker.log
├── main.py (2667 bytes)
├── model_files
│   ├── .DS_Store
│   ├── AI21-Jamba-Mini-1.7.i1-IQ1_S.gguf
│   ├── L3.1-Dark-Reason-Dark-Plnt-Hrm-R1-Uncen-Hrr-Imtr-MAX-8B-D_AU-IQ3_XXS-imat.gguf
│   ├── L3.1-Dark-Reason-Dark-Plnt-Hrm-R1-Uncen-Hrr-Imtr-MAX-8B-D_AU-Q6_K-imat.gguf
│   ├── gemma-3-4b-it-q4_0.gguf
│   ├── gpt-oss-20b-MXFP4.gguf
│   └── readme.txt
├── orchestrator
│   ├── __init__.py (45 bytes)
│   ├── hiple_orchestrator.py (22927 bytes)
│   └── router.py (2584 bytes)
├── pyproject.toml
├── rag
│   ├── __init__.py (127 bytes)
│   ├── data_sources.py (1981 bytes)
│   └── retrievers.py (3007 bytes)
├── requirements.txt
├── services
│   ├── .DS_Store
│   ├── __init__.py (41 bytes)
│   ├── evolution_service.py (3211 bytes)
│   ├── model_loader.py (5311 bytes)
│   ├── performance_tracker_service.py (5741 bytes)
│   ├── plan_evaluation_service.py (2924 bytes)
│   ├── rag_manager_service.py (2131 bytes)
│   ├── tool_manager_service.py (4258 bytes)
│   ├── vectorization_service.py (2636 bytes)
│   ├── web_browser_service.py (2504 bytes)
│   ├── wikipedia_service.py (4395 bytes)
│   └── worker_manager.py (5376 bytes)
├── transformer_test.py (3617 bytes)
├── utils
│   ├── __init__.py (94 bytes)
│   ├── monitoring.py (745 bytes)
│   └── thought_logger.py (1899 bytes)
├── visualizer_test.py (3539 bytes)
└── workspace
    ├── __init__.py (42 bytes)
    └── global_workspace.py (2762 bytes)
```

## 2. Dependencies

### `requirements.txt`

```
# /hybrid_llm_system/requirements.txt
# プロジェクトに必要なライブラリ

# LangChain関連
langchain
langchain-community

# Llama.cppのPythonバインディング
# CPUのみの場合: pip install llama-cpp-python
# GPU(NVIDIA)を利用する場合: CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python
llama-cpp-python

# DIコンテナ
dependency-injector

# .envファイル読み込み
python-dotenv

# YAMLパーサー
PyYAML

# 拡散モデル用ライブラリ
diffusers
transformers
torch
accelerate

# システム監視用ライブラリ
psutil

# ベクトル化と意味検索用
sentence-transformers
faiss-cpu

# ベクトル類似度計算用
scikit-learn

# --- Web Browser Agent用ライブラリ ---
playwright
beautifulsoup4
googlesearch-python

# --- Wikipedia Agent用ライブラリ ---
wikipedia
```

### `pyproject.toml`

```
# /hybrid_llm_system/pyproject.toml
# mypyを含むプロジェクト全体の設定ファイル

[tool.mypy]
python_version = "3.10"

# --- "Source file found twice" エラーを解決するための設定 ---
# この設定は、mypyがパッケージの起点（ベース）をどのように認識するかを明確にし、
# インポートパスの曖昧さを解消します。
explicit_package_bases = true
namespace_packages = true
# -----------------------------------------------------------

# 推奨される標準的な設定
warn_return_any = true
warn_unused_configs = true

# 型定義ファイル（スタブ）が見つからないライブラリについての警告を無視します。
ignore_missing_imports = true
```

## 3. Internal Module Dependencies

### `agents.base_agent`
Dependencies:
- domain.schemas.ExpertModel
- services.model_loader.ModelLoaderService

### `agents.consultant_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel
- domain.schemas.SubTask

### `agents.critic_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel
- domain.schemas.Plan

### `agents.emergence_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel
- services.model_loader.ModelLoaderService

### `agents.generator_agent`
Dependencies:
- agents.base_agent.BaseAgent
- agents.consultant_agent.ConsultantAgent
- domain.schemas.ExpertModel
- domain.schemas.Milestone
- domain.schemas.SubTask
- services.model_loader.ModelLoaderService
- services.worker_manager.WorkerExecutionError
- services.worker_manager.WorkerManagerService

### `agents.metacognition_agent`
Dependencies:
- domain.schemas.Plan

### `agents.planner_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel
- domain.schemas.Milestone
- domain.schemas.Plan
- domain.schemas.SubTask
- services.tool_manager_service.ToolManagerService

### `agents.rag_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel

### `agents.reporter_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel
- domain.schemas.Plan

### `agents.reviewer_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel
- domain.schemas.SubTask

### `agents.safety_director_agent`
Dependencies:
- domain.schemas.Plan
- domain.schemas.SubTask
- workspace.global_workspace.GlobalWorkspace

### `agents.tool_router_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel

### `agents.web_browser_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel

### `agents.wikipedia_agent`
Dependencies:
- agents.base_agent.BaseAgent
- domain.schemas.ExpertModel
- services.model_loader.ModelLoaderService
- services.wikipedia_service.WikipediaService

### `container.container`
Dependencies:
- agents.consultant_agent.ConsultantAgent
- agents.critic_agent.CriticAgent
- agents.emergence_agent.EmergenceAgent
- agents.generator_agent.GeneratorAgent
- agents.metacognition_agent.MetacognitionAgent
- agents.planner_agent.PlannerAgent
- agents.rag_agent.RAGAgent
- agents.reporter_agent.ReporterAgent
- agents.reviewer_agent.ReviewerAgent
- agents.safety_director_agent.SafetyDirectorAgent
- agents.tool_router_agent.ToolRouterAgent
- agents.web_browser_agent.WebBrowserAgent
- agents.wikipedia_agent.WikipediaAgent
- domain.boundary_enforcer.BoundaryConditionEnforcer
- domain.model_manager.ModelManager
- orchestrator.hiple_orchestrator.HipleOrchestrator
- rag.retrievers.FaissRetriever
- services.evolution_service.EvolutionService
- services.model_loader.ModelLoaderService
- services.performance_tracker_service.PerformanceTrackerService
- services.plan_evaluation_service.PlanEvaluationService
- services.rag_manager_service.RAGManagerService
- services.tool_manager_service.ToolManagerService
- services.vectorization_service.VectorizationService
- services.web_browser_service.WebBrowserService
- services.wikipedia_service.WikipediaService
- services.worker_manager.WorkerManagerService
- utils.thought_logger.ThoughtLogger
- workspace.global_workspace.GlobalWorkspace

### `hrm_test`
Dependencies:
- utils.monitoring.print_memory_usage

### `jamba_test`
Dependencies:
- utils.monitoring.print_memory_usage

### `main`
Dependencies:
- container.container.Container
- orchestrator.hiple_orchestrator.HipleOrchestrator
- utils.monitoring.print_memory_usage

### `orchestrator.hiple_orchestrator`
Dependencies:
- agents.critic_agent.CriticAgent
- agents.emergence_agent.EmergenceAgent
- agents.generator_agent.GeneratorAgent
- agents.metacognition_agent.MetacognitionAgent
- agents.planner_agent.PlannerAgent
- agents.rag_agent.RAGAgent
- agents.reporter_agent.ReporterAgent
- agents.reviewer_agent.ReviewerAgent
- agents.safety_director_agent.SafetyDirectorAgent
- agents.tool_router_agent.ToolRouterAgent
- domain.model_manager.ModelManager
- domain.schemas.ExpertModel
- domain.schemas.Milestone
- domain.schemas.Plan
- domain.schemas.SubTask
- rag.data_sources.Document
- rag.data_sources.PlanDataSource
- rag.retrievers.BaseRetriever
- services.evolution_service.EvolutionService
- services.performance_tracker_service.PerformanceTrackerService
- services.plan_evaluation_service.PlanEvaluationService
- services.rag_manager_service.RAGManagerService
- services.tool_manager_service.ToolManagerService
- utils.thought_logger.ThoughtLogger
- workspace.global_workspace.GlobalWorkspace

### `rag.data_sources`
Dependencies:
- domain.schemas.Plan

### `rag.retrievers`
Dependencies:
- rag.data_sources.Document
- services.vectorization_service.VectorizationService

### `services.evolution_service`
Dependencies:
- domain.boundary_enforcer.BoundaryConditionEnforcer
- domain.schemas.ExpertModel
- services.performance_tracker_service.PerformanceTrackerService

### `services.model_loader`
Dependencies:
- domain.schemas.ExpertModel
- utils.monitoring.print_memory_usage

### `services.performance_tracker_service`
Dependencies:
- domain.evaluation.PerformanceMetrics
- domain.schemas.ExpertModel

### `services.plan_evaluation_service`
Dependencies:
- domain.schemas.SubTask
- services.vectorization_service.VectorizationService

### `services.rag_manager_service`
Dependencies:
- rag.data_sources.DataSource
- rag.data_sources.Document
- rag.retrievers.BaseRetriever
- services.vectorization_service.VectorizationService

### `services.tool_manager_service`
Dependencies:
- agents.web_browser_agent.WebBrowserAgent
- agents.wikipedia_agent.WikipediaAgent
- domain.schemas.ExpertModel
- services.web_browser_service.WebBrowserService

### `services.worker_manager`
Dependencies:
- domain.schemas.ExpertModel

## 4. DI Container and LangChain Analysis Overview

### `agents/base_agent.py` (DI Container Analysis)
**Injected Dependencies**: BaseAgent.__init__(model_loader)

### `agents/emergence_agent.py` (DI Container Analysis)
**Injected Dependencies**: EmergenceAgent.__init__(model_loader)

### `agents/generator_agent.py` (DI Container Analysis)
**Injected Dependencies**: GeneratorAgent.__init__(model_loader), GeneratorAgent.__init__(worker_manager), GeneratorAgent.__init__(consultant_agent)

### `agents/metacognition_agent.py` (DI Container Analysis)
**Injected Dependencies**: MetacognitionAgent.__init__(task_limit), MetacognitionAgent.__init__(dependency_depth_limit)

### `agents/safety_director_agent.py` (DI Container Analysis)
**Injected Dependencies**: SafetyDirectorAgent.__init__(max_replanning), SafetyDirectorAgent.__init__(max_feedback_loops), SafetyDirectorAgent.__init__(confidence_threshold)

### `agents/wikipedia_agent.py` (DI Container Analysis)
**Injected Dependencies**: WikipediaAgent.__init__(model_loader), WikipediaAgent.__init__(wikipedia_service)

### `domain/model_manager.py` (DI Container Analysis)
**Injected Dependencies**: ModelManager.__init__(config_path)

### `main.py` (DI Container Analysis)
**DI Container Instantiations**: Container

### `orchestrator/hiple_orchestrator.py` (DI Container Analysis)
**Injected Dependencies**: HipleOrchestrator.__init__(model_manager), HipleOrchestrator.__init__(tool_router_agent), HipleOrchestrator.__init__(planner_agent), HipleOrchestrator.__init__(generator_agent), HipleOrchestrator.__init__(reporter_agent), HipleOrchestrator.__init__(reviewer_agent), HipleOrchestrator.__init__(plan_evaluation_service), HipleOrchestrator.__init__(performance_tracker), HipleOrchestrator.__init__(rag_agent), HipleOrchestrator.__init__(rag_manager), HipleOrchestrator.__init__(faiss_retriever), HipleOrchestrator.__init__(critic_agent), HipleOrchestrator.__init__(tool_manager), HipleOrchestrator.__init__(global_workspace), HipleOrchestrator.__init__(thought_logger), HipleOrchestrator.__init__(safety_director_agent), HipleOrchestrator.__init__(metacognition_agent), HipleOrchestrator.__init__(evolution_service), HipleOrchestrator.__init__(emergence_agent)

### `rag/data_sources.py` (DI Container Analysis)
**Injected Dependencies**: PlanDataSource.__init__(plan)

### `rag/retrievers.py` (DI Container Analysis)
**Injected Dependencies**: FaissRetriever.__init__(vectorization_service)

### `services/evolution_service.py` (DI Container Analysis)
**Injected Dependencies**: EvolutionService.__init__(performance_tracker), EvolutionService.__init__(boundary_enforcer), EvolutionService.__init__(all_experts)

### `services/model_loader.py` (DI Container Analysis)
**Injected Dependencies**: ModelLoaderService.__init__(memory_threshold_gb)

### `services/plan_evaluation_service.py` (DI Container Analysis)
**Injected Dependencies**: PlanEvaluationService.__init__(vectorization_service)

### `services/rag_manager_service.py` (DI Container Analysis)
**Injected Dependencies**: RAGManagerService.__init__(vectorization_service)

### `services/tool_manager_service.py` (DI Container Analysis)
**Injected Dependencies**: ToolManagerService.__init__(wikipedia_agent), ToolManagerService.__init__(web_browser_agent), ToolManagerService.__init__(web_browser_service)

### `services/vectorization_service.py` (DI Container Analysis)
**Injected Dependencies**: VectorizationService.__init__(model_name)

### `services/web_browser_service.py` (DI Container Analysis)
**Injected Dependencies**: WebBrowserService.__init__(headless)

### `services/wikipedia_service.py` (DI Container Analysis)
**Injected Dependencies**: WikipediaService.__init__(lang)

No explicit LangChain components detected.

## 5. File Analysis Overview

### `__init__.py`

### `agents/__init__.py`

### `agents/base_agent.py`
**Classes**: BaseAgent
**Functions**: __init__, execute, _add_self_evaluation_prompt, _query_llm
**External imports**: abc.ABC, abc.abstractmethod, domain.schemas.ExpertModel, json, llama_cpp.Llama, llama_cpp.llama_types.ChatCompletionRequestMessage, re, services.model_loader.ModelLoaderService, typing.Any, typing.Dict, typing.List, typing.Optional, typing.cast

### `agents/consultant_agent.py`
**Classes**: ConsultantAgent
**Functions**: execute, _get_advice_from_expert, _summarize_advice, _find_expert
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, domain.schemas.SubTask, llama_cpp.llama_types.ChatCompletionRequestMessage, typing.Any, typing.Dict, typing.List

### `agents/critic_agent.py`
**Classes**: CriticAgent
**Functions**: execute, _find_critic_expert, _format_plan_for_review
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, domain.schemas.Plan, llama_cpp.llama_types.ChatCompletionRequestMessage, typing.Any, typing.Dict, typing.List

### `agents/emergence_agent.py`
**Classes**: EmergenceAgent
**Functions**: __init__, execute, _select_participants, _create_contribution_prompt, _create_synthesis_prompt, _find_expert
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, llama_cpp.llama_types.ChatCompletionRequestMessage, services.model_loader.ModelLoaderService, typing.Any, typing.Dict, typing.List, typing.Optional

### `agents/generator_agent.py`
**Classes**: GeneratorAgent
**Functions**: __init__, execute, _parse_self_evaluation_from_str, _build_messages_with_context, _generate_image
**External imports**: agents.base_agent.BaseAgent, agents.consultant_agent.ConsultantAgent, diffusers.DiffusionPipeline, domain.schemas.ExpertModel, domain.schemas.Milestone, domain.schemas.SubTask, json, llama_cpp.llama_types.ChatCompletionRequestMessage, os, re, services.model_loader.ModelLoaderService, services.worker_manager.WorkerExecutionError, services.worker_manager.WorkerManagerService, traceback, typing.Any, typing.Dict, typing.List, typing.Optional, typing.Union, typing.cast, uuid

### `agents/metacognition_agent.py`
**Classes**: MetacognitionAgent
**Functions**: __init__, analyze_cognitive_load, _calculate_max_dependency_depth, dfs
**External imports**: domain.schemas.Plan, typing.Any, typing.Dict, typing.List, typing.Tuple

### `agents/planner_agent.py`
**Classes**: PlannerAgent
**Functions**: execute, _find_planner_expert, _build_system_prompt, _build_user_prompt, _parse_plan_from_response, _create_fallback_plan, _format_expert_descriptions, _get_json_format_section, _get_rules_section
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, domain.schemas.Milestone, domain.schemas.Plan, domain.schemas.SubTask, json, llama_cpp.llama_types.ChatCompletionRequestMessage, re, services.tool_manager_service.ToolManagerService, typing.Any, typing.Dict, typing.List, typing.Optional

### `agents/rag_agent.py`
**Classes**: RAGAgent
**Functions**: execute, _find_expert
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, json, llama_cpp.llama_types.ChatCompletionRequestMessage, re, typing.Any, typing.Dict, typing.List

### `agents/reporter_agent.py`
**Classes**: ReporterAgent
**Functions**: execute, _find_reporter_expert, _build_context, _build_final_prompt
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, domain.schemas.Plan, llama_cpp.llama_types.ChatCompletionRequestMessage, typing.List

### `agents/reviewer_agent.py`
**Classes**: ReviewerAgent
**Functions**: execute
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, domain.schemas.SubTask, llama_cpp.llama_types.ChatCompletionRequestMessage, typing.Any, typing.Dict, typing.List

### `agents/safety_director_agent.py`
**Classes**: SafetyDirectorAgent
**Functions**: __init__, review_thought_process
**External imports**: domain.schemas.Plan, domain.schemas.SubTask, typing.Any, typing.Dict, typing.List, typing.Optional, workspace.global_workspace.GlobalWorkspace

### `agents/tool_router_agent.py`
**Classes**: ToolRouterAgent
**Functions**: execute, _find_expert
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, json, llama_cpp.llama_types.ChatCompletionRequestMessage, re, typing.Any, typing.Dict, typing.List, typing.Optional

### `agents/web_browser_agent.py`
**Classes**: WebBrowserAgent
**Functions**: execute, _summarize_with_llm, _find_expert
**External imports**: agents.base_agent.BaseAgent, bs4.BeautifulSoup, bs4.NavigableString, domain.schemas.ExpertModel, llama_cpp.llama_types.ChatCompletionRequestMessage, re, typing.List

### `agents/wikipedia_agent.py`
**Classes**: WikipediaAgent
**Functions**: __init__, execute, _extract_search_term, _find_expert
**External imports**: agents.base_agent.BaseAgent, domain.schemas.ExpertModel, llama_cpp.llama_types.ChatCompletionRequestMessage, services.model_loader.ModelLoaderService, services.wikipedia_service.WikipediaService, typing.Any, typing.Dict, typing.List, typing.Optional

### `agents/worker.py`
**Functions**: main
**External imports**: dotenv.load_dotenv, json, llama_cpp.Llama, logging, os, pathlib.Path, psutil, sys, traceback

### `config/__init__.py`

### `container/__init__.py`

### `container/container.py`
**Classes**: Container
**External imports**: agents.consultant_agent.ConsultantAgent, agents.critic_agent.CriticAgent, agents.emergence_agent.EmergenceAgent, agents.generator_agent.GeneratorAgent, agents.metacognition_agent.MetacognitionAgent, agents.planner_agent.PlannerAgent, agents.rag_agent.RAGAgent, agents.reporter_agent.ReporterAgent, agents.reviewer_agent.ReviewerAgent, agents.safety_director_agent.SafetyDirectorAgent, agents.tool_router_agent.ToolRouterAgent, agents.web_browser_agent.WebBrowserAgent, agents.wikipedia_agent.WikipediaAgent, dependency_injector.containers, dependency_injector.providers, domain.boundary_enforcer.BoundaryConditionEnforcer, domain.model_manager.ModelManager, orchestrator.hiple_orchestrator.HipleOrchestrator, rag.retrievers.FaissRetriever, services.evolution_service.EvolutionService, services.model_loader.ModelLoaderService, services.performance_tracker_service.PerformanceTrackerService, services.plan_evaluation_service.PlanEvaluationService, services.rag_manager_service.RAGManagerService, services.tool_manager_service.ToolManagerService, services.vectorization_service.VectorizationService, services.web_browser_service.WebBrowserService, services.wikipedia_service.WikipediaService, services.worker_manager.WorkerManagerService, utils.thought_logger.ThoughtLogger, workspace.global_workspace.GlobalWorkspace

### `domain/boundary_enforcer.py`
**Classes**: BoundaryConditionEnforcer
**Functions**: __init__, validate_evolution
**External imports**: typing.Any, typing.Dict, typing.List, typing.Tuple

### `domain/evaluation.py`
**Classes**: PerformanceMetrics
**Functions**: total_runs, success_rate, average_execution_time
**External imports**: dataclasses.dataclass, dataclasses.field

### `domain/model_manager.py`
**Classes**: ModelManager
**Functions**: __init__, _load_experts_from_config, get_expert, get_all_experts
**External imports**: dotenv.load_dotenv, os, schemas.ExpertModel, typing.Dict, typing.List, typing.Optional, yaml

### `domain/schemas.py`
**Classes**: ExpertModel, SubTask, Milestone, Plan
**External imports**: dataclasses.dataclass, dataclasses.field, diffusers.DiffusionPipeline, llama_cpp.Llama, numpy, typing.Any, typing.Dict, typing.List, typing.Optional, typing.TYPE_CHECKING, typing.Union

### `enhanced_python_analyzer.py`
**Classes**: CustomASTVisitor
**Functions**: get_project_tree, __init__, visit_Import, visit_ImportFrom, visit_FunctionDef, visit_AsyncFunctionDef, visit_ClassDef, visit_Assign, visit_Call, visit_Decorator, extract_module_details, analyze_module_dependencies, get_project_summary, aggregate_enhanced_project_structure
**External imports**: ast, collections.defaultdict, os, pathlib.Path, re, typing.Any, typing.Dict, typing.List, typing.Optional, typing.Set, typing.Tuple, typing.Union, typing.cast
**Constants**: PROJECT_DIRECTORY, OUTPUT_MARKDOWN_FILE, INCLUDE_ANALYSIS

### `hrm_test.py`
**Functions**: main
**External imports**: dotenv.load_dotenv, llama_cpp.Llama, llama_cpp.llama_types.ChatCompletionRequestMessage, os, psutil, sys, traceback, typing.Any, typing.Dict, typing.List, typing.Optional, utils.monitoring.print_memory_usage

### `jamba_test.py`
**Functions**: main
**External imports**: dotenv.load_dotenv, llama_cpp.Llama, llama_cpp.llama_types.ChatCompletionRequestMessage, os, psutil, sys, traceback, typing.Any, typing.Dict, typing.List, typing.Optional, utils.monitoring.print_memory_usage

### `liquids4_test.py`
**Functions**: main
**External imports**: dotenv.load_dotenv, llama_cpp.Llama, llama_cpp.llama_types.ChatCompletionRequestMessage, os, sys, typing.Any, typing.Dict, typing.List, typing.Optional

### `main.py`
**Functions**: main
**External imports**: container.container.Container, orchestrator.hiple_orchestrator.HipleOrchestrator, os, readline, sys, traceback, utils.monitoring.print_memory_usage

### `orchestrator/__init__.py`

### `orchestrator/hiple_orchestrator.py`
**Classes**: HipleOrchestrator
**Functions**: __init__, process_task, _process_simple_task, _process_complex_task, _execute_plan, _validate_plan_structure, _build_context_for_task, _build_minimal_context
**External imports**: agents.critic_agent.CriticAgent, agents.emergence_agent.EmergenceAgent, agents.generator_agent.GeneratorAgent, agents.metacognition_agent.MetacognitionAgent, agents.planner_agent.PlannerAgent, agents.rag_agent.RAGAgent, agents.reporter_agent.ReporterAgent, agents.reviewer_agent.ReviewerAgent, agents.safety_director_agent.SafetyDirectorAgent, agents.tool_router_agent.ToolRouterAgent, bs4.BeautifulSoup, domain.model_manager.ModelManager, domain.schemas.ExpertModel, domain.schemas.Milestone, domain.schemas.Plan, domain.schemas.SubTask, rag.data_sources.Document, rag.data_sources.PlanDataSource, rag.retrievers.BaseRetriever, services.evolution_service.EvolutionService, services.performance_tracker_service.PerformanceTrackerService, services.plan_evaluation_service.PlanEvaluationService, services.rag_manager_service.RAGManagerService, services.tool_manager_service.ToolManagerService, time, traceback, typing.Any, typing.Dict, typing.List, typing.Optional, typing.Tuple, typing.cast, utils.thought_logger.ThoughtLogger, workspace.global_workspace.GlobalWorkspace

### `orchestrator/router.py`
**Classes**: SimpleRouter
**Functions**: __init__, route
**External imports**: typing.Any, typing.Dict, typing.List

### `rag/__init__.py`

### `rag/data_sources.py`
**Classes**: Document, DataSource, PlanDataSource
**Functions**: load_documents, __init__, load_documents
**External imports**: abc.ABC, abc.abstractmethod, dataclasses.dataclass, dataclasses.field, domain.schemas.Plan, typing.Any, typing.Dict, typing.Iterator, typing.List

### `rag/retrievers.py`
**Classes**: BaseRetriever, FaissRetriever
**Functions**: build_index, retrieve, __init__, build_index, retrieve
**External imports**: abc.ABC, abc.abstractmethod, faiss, numpy, rag.data_sources.Document, services.vectorization_service.VectorizationService, typing.List, typing.Optional

### `services/__init__.py`

### `services/evolution_service.py`
**Classes**: EvolutionService
**Functions**: __init__, run_evolution_cycle
**External imports**: domain.boundary_enforcer.BoundaryConditionEnforcer, domain.schemas.ExpertModel, services.performance_tracker_service.PerformanceTrackerService, typing.Any, typing.Dict, typing.List, typing.Optional

### `services/model_loader.py`
**Classes**: ModelLoaderService
**Functions**: __init__, _check_memory, load_expert, unload_expert
**External imports**: diffusers.AutoencoderKL, diffusers.DiffusionPipeline, domain.schemas.ExpertModel, gc, llama_cpp.Llama, os, psutil, sys, torch, traceback, typing.Any, typing.Optional, typing.Union, utils.monitoring.print_memory_usage

### `services/performance_tracker_service.py`
**Classes**: PerformanceTrackerService
**Functions**: __init__, update_performance, _recalculate_score, get_best_expert, get_underperforming_experts, get_performance_summary
**External imports**: domain.evaluation.PerformanceMetrics, domain.schemas.ExpertModel, time, typing.Dict, typing.List, typing.Optional, typing.Tuple

### `services/plan_evaluation_service.py`
**Classes**: PlanEvaluationService
**Functions**: __init__, check_semantic_coherence
**External imports**: domain.schemas.SubTask, numpy, services.vectorization_service.VectorizationService, sklearn.metrics.pairwise.cosine_similarity, typing.List, typing.Tuple

### `services/rag_manager_service.py`
**Classes**: RAGManagerService
**Functions**: __init__, register_retriever, build_index_from_source, query
**External imports**: rag.data_sources.DataSource, rag.data_sources.Document, rag.retrievers.BaseRetriever, services.vectorization_service.VectorizationService, typing.Dict, typing.Iterator, typing.List

### `services/tool_manager_service.py`
**Classes**: ToolManagerService
**Functions**: __init__, get_tool_descriptions, execute_tool
**External imports**: agents.web_browser_agent.WebBrowserAgent, agents.wikipedia_agent.WikipediaAgent, domain.schemas.ExpertModel, googlesearch, services.web_browser_service.WebBrowserService, traceback, typing.Any, typing.Dict, typing.List, typing.cast

### `services/vectorization_service.py`
**Classes**: VectorizationService
**Functions**: __init__, encode, encode_batch
**External imports**: numpy, sentence_transformers.SentenceTransformer, typing.List

### `services/web_browser_service.py`
**Classes**: WebBrowserService
**Functions**: __init__, launch_browser, close_browser, get_page_content
**External imports**: playwright.sync_api.Browser, playwright.sync_api.Page, playwright.sync_api.Playwright, playwright.sync_api.sync_playwright, typing.Optional

### `services/wikipedia_service.py`
**Classes**: WikipediaService
**Functions**: __init__, search, get_summary, get_page_content
**External imports**: typing.List, typing.Optional, typing.cast, wikipedia

### `services/worker_manager.py`
**Classes**: WorkerExecutionError, WorkerManagerService
**Functions**: invoke_llm_worker, invoke_diffusion_worker
**External imports**: diffusers.AutoencoderKL, diffusers.DiffusionPipeline, domain.schemas.ExpertModel, json, llama_cpp.llama_types.ChatCompletionRequestMessage, subprocess, sys, torch, traceback, typing.Any, typing.Dict, typing.List, typing.cast

### `transformer_test.py`
**Functions**: main
**External imports**: dotenv.load_dotenv, llama_cpp.Llama, llama_cpp.llama_types.ChatCompletionRequestMessage, os, sys, typing.Any, typing.Dict, typing.List, typing.Optional

### `utils/__init__.py`

### `utils/monitoring.py`
**Functions**: print_memory_usage
**External imports**: os, psutil

### `utils/thought_logger.py`
**Classes**: ThoughtLogger
**Functions**: format_thoughts
**External imports**: typing.Any, typing.Dict, typing.List

### `visualizer_test.py`
**Functions**: main
**External imports**: diffusers.AutoencoderKL, diffusers.DiffusionPipeline, dotenv.load_dotenv, os, torch, traceback, typing.Optional

### `workspace/__init__.py`

### `workspace/global_workspace.py`
**Classes**: GlobalWorkspace
**Functions**: __init__, clear, set_initial_prompt, add_thought, get_last_thought, get_full_history_for_expert, update_expert_history, set_final_answer
**External imports**: copy, llama_cpp.llama_types.ChatCompletionRequestMessage, typing.Any, typing.Dict, typing.List, typing.Optional

## 6. Source Code

### `__init__.py`

```python
# /hybrid_llm_system/orchestrator/__init__.py
```

### `agents/__init__.py`

```python
# path: ./agents/__init__.py
# title: Agents Package Initializer
# description: This file makes the 'agents' directory a Python package.
```

### `agents/base_agent.py`

```python
# path: ./agents/base_agent.py
# title: Base Agent with Self-Evaluation Capability (Corrected)
# description: 全てのエージェントの基盤。LLMからの応答と自己評価（自信度・理由）をJSON形式で受け取る。

from abc import ABC, abstractmethod
import json
import re
from typing import List, Any, Optional, cast, Dict
from llama_cpp import Llama
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from services.model_loader import ModelLoaderService

class BaseAgent(ABC):
    """
    すべてのエージェントの基本となる抽象基底クラス。
    自己評価機能を組み込んでいる。
    """
    def __init__(self, model_loader: ModelLoaderService):
        self.model_loader = model_loader

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """エージェントの主処理を実行するメソッド"""
        pass

    def _add_self_evaluation_prompt(self, system_prompt: str) -> str:
        """システムプロンプトに自己評価を促す指示を追加する"""
        evaluation_prompt = """
# 自己評価
あなたの応答が完了したら、必ず以下のJSON形式で自己評価を追加してください。

```json
{
  "response": "（ここにあなたの主たる応答を記述）",
  "self_evaluation": {
    "confidence": "（あなたの応答に対する自信度を0.0から1.0の数値で評価）",
    "reasoning": "（その自信度に至った理由や、応答の限界、注意点を簡潔に説明）"
  }
}
```
"""
        return system_prompt + "\n" + evaluation_prompt

    def _query_llm(self, expert: ExpertModel, messages: List[ChatCompletionRequestMessage]) -> Dict[str, Any]:
        """LLMに問い合わせを実行し、応答と自己評価をパースして返す"""
        llm = cast(Llama, self.model_loader.load_expert(expert))
        
        if messages and messages[0]["role"] == "system":
            original_prompt = cast(str, messages[0]["content"])
            if "content" in messages[0] and isinstance(messages[0]["content"], str):
                 messages[0]["content"] = self._add_self_evaluation_prompt(messages[0]["content"])


        output: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=4096,
            temperature=0.2,
            stop=["<|im_end|>", "</s>", "<|endoftext|>"]
        )
        
        raw_response = ""
        if (
            "choices" in output and isinstance(output["choices"], list) and output["choices"] and
            "message" in output["choices"][0] and isinstance(output["choices"][0]["message"], dict) and
            "content" in output["choices"][0]["message"] and isinstance(output["choices"][0]["message"]["content"], str)
        ):
            raw_response = output["choices"][0]["message"]["content"].strip()
        
        if not raw_response:
            return {"response": "", "self_evaluation": {"confidence": 0.0, "reasoning": "No response from LLM."}}

        try:
            json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_response, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                start_index = raw_response.find('{')
                end_index = raw_response.rfind('}')
                if start_index != -1 and end_index != -1:
                    json_str = raw_response[start_index:end_index + 1]
                else:
                    return {"response": raw_response, "self_evaluation": {"confidence": 0.5, "reasoning": "Could not parse JSON structure."}}

            data = json.loads(json_str)
            
            response = data.get("response", raw_response)
            evaluation = data.get("self_evaluation", {"confidence": 0.5, "reasoning": "Evaluation data missing."})

            if not isinstance(evaluation.get("confidence"), (int, float)):
                evaluation["confidence"] = 0.5

            return {"response": response, "self_evaluation": evaluation}

        except (json.JSONDecodeError, KeyError):
            return {"response": raw_response, "self_evaluation": {"confidence": 0.5, "reasoning": "Failed to parse self-evaluation JSON."}}

```

### `agents/consultant_agent.py`

```python
# path: ./agents/consultant_agent.py
# title: Consultant Agent (Self-Evaluation Aware)
# description: 他のエキスパートに助言を求め、その内容を要約して返し、自己評価も行う。

from typing import List, Dict, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import SubTask, ExpertModel
from agents.base_agent import BaseAgent

class ConsultantAgent(BaseAgent):
    """
    他のエキスパートに助言を求め、その結果を統合するエージェント。
    """
    def execute(
        self,
        original_task: SubTask,
        primary_expert: ExpertModel,
        all_experts: List[ExpertModel]
    ) -> Dict[str, Any]:
        consulting_experts = [
            e for e in all_experts
            if e.name in original_task.consultation_experts and e.name != primary_expert.name
        ]

        if not consulting_experts:
            return {"response": "追加の助言はありません。", "self_evaluation": {"confidence": 1.0, "reasoning": "No consultants were assigned."}}

        print(f"🤝 {primary_expert.name} のために、{[e.name for e in consulting_experts]} へ助言を求めます...")

        advice_list: List[str] = []
        for expert in consulting_experts:
            advice_data = self._get_advice_from_expert(original_task, primary_expert, expert)
            advice = advice_data.get("response")
            if advice:
                advice_list.append(f"### {expert.name}からの助言:\n{advice}\n")

        if not advice_list:
            return {"response": "有益な助言は得られませんでした。", "self_evaluation": {"confidence": 1.0, "reasoning": "Consultants provided no useful advice."}}

        summarizer_expert = self._find_expert("HRM", all_experts)
        return self._summarize_advice(advice_list, summarizer_expert)

    def _get_advice_from_expert(self, original_task: SubTask, primary_expert: ExpertModel, consulting_expert: ExpertModel) -> Dict[str, Any]:
        system_prompt = f"""あなたは、他のAIエキスパートのタスク遂行を支援する、優秀なコンサルタントです。
あなたの専門分野は「{consulting_expert.description}」です。
これから、エキスパート「{primary_expert.name}」が担当するタスクが提示されます。
あなたの専門的な観点から、そのタスクをより良く達成するための具体的なアイデア、注意点、代替アプローチなどを助言してください。
回答は簡潔かつ要点を得たものにしてください。"""

        user_prompt = f"""以下のタスクについて、専門的な助言をお願いします。

# 担当エキスパート
- **名前:** {primary_expert.name}
- **役割:** {primary_expert.description}

# タスク内容
- **目的(SSV):** {original_task.ssv_description}
- **詳細:** {original_task.description}
"""
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return self._query_llm(consulting_expert, messages)

    def _summarize_advice(self, advice_list: List[str], summarizer_expert: ExpertModel) -> Dict[str, Any]:
        if not advice_list:
            return {"response": "", "self_evaluation": {"confidence": 1.0, "reasoning": "No advice to summarize."}}

        all_advice = "\n---\n".join(advice_list)
        system_prompt = "あなたは、複数の専門家からの助言を整理し、要点を抽出して、実行可能な一つのサマリーにまとめる編集者です。各助言の重要な部分を抽出し、簡潔にまとめてください。"
        user_prompt = f"以下の専門家からの助言を一つのサマリーにまとめてください:\n\n{all_advice}"

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        summary_data = self._query_llm(summarizer_expert, messages)
        print(f"📝 助言の要約が完了しました。")
        return summary_data

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")

```

### `agents/critic_agent.py`

```python
# path: ./agents/critic_agent.py
# title: Critic Agent (Self-Evaluation Aware)
# description: A specialized agent that reviews a generated plan and provides self-evaluated feedback.

from typing import List, Dict, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import Plan, ExpertModel
from agents.base_agent import BaseAgent

class CriticAgent(BaseAgent):
    """
    生成された計画全体をレビューし、戦略的な欠陥や非効率性を指摘する批評家エージェント。
    """
    def execute(self, plan: Plan, experts: List[ExpertModel]) -> str:
        """
        計画をレビューし、改善のためのフィードバック、または承認のメッセージを返す。
        """
        critic_expert = self._find_critic_expert(experts)
        plan_str = self._format_plan_for_review(plan)

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = """あなたは、AIプロジェクトマネージャーが作成した実行計画をレビューする、超優秀な戦略コンサルタントです。
あなたの役割は、計画の構造的な正しさだけでなく、その「戦略的な妥当性」を厳しく評価することです。

# 評価の観点
- **過不足**: 目標達成に不要なタスクはないか？逆に、欠けている重要なステップはないか？
- **効率性**: タスクの順序は最適か？もっと効率的な進め方はないか？
- **エキスパート選定**: 各タスクに割り当てられたエキスパートは本当に最適か？より適任なエキスパートはいないか？
- **リスク**: 計画に潜むリスクや、失敗する可能性の高い箇所はないか？

# あなたへの指示
提示された計画を上記の観点から評価してください。
- **計画が実行可能で妥当な場合**: まず「**承認します。**」という一文から始めてください。その後に、任意で改善点を箇条書きで提案しても構いません。
- **計画に致命的な欠陥があり実行不可能な場合**: まず「**却下します。**」という一文から始めてください。その後に、修正が必須である理由を具体的に指摘してください。

必ず「承認します。」か「却下します。」のどちらかのフレーズから応答を開始してください。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": plan_str}
        ]
        
        response_data = self._query_llm(critic_expert, messages)
        feedback = response_data.get("response", "批評家エージェントからの応答がありません。")
        print(f"🧐 批評家エージェントによる計画レビューが完了しました。")
        return feedback

    def _find_critic_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        fallback = next((e for e in experts if e.chat_format != "diffusion"), None)
        if fallback: return fallback
        raise ValueError("利用可能な批評家エキスパートが見つかりません。")

    def _format_plan_for_review(self, plan: Plan) -> str:
        lines = [f"# レビュー対象の計画: {plan.overall_goal}\n"]

        for milestone in sorted(plan.milestones, key=lambda m: m.milestone_id):
            lines.append(f"\n## マイルストーン {milestone.milestone_id}: {milestone.title}")
            lines.append(f"   - 説明: {milestone.description}")
            
            tasks_in_milestone = sorted(
                [t for t in plan.tasks if t.milestone_id == milestone.milestone_id],
                key=lambda t: t.task_id
            )
            
            for task in tasks_in_milestone:
                lines.append(f"###    - タスク {task.task_id}: {task.description}")
                lines.append(f"       - 担当: {task.expert_name}")
                if task.dependencies:
                    lines.append(f"       - 依存関係: {task.dependencies}")
                if task.reviewer_expert:
                    lines.append(f"       - レビュアー: {task.reviewer_expert}")
        
        return "\n".join(lines)

```

### `agents/emergence_agent.py`

```python
# path: ./agents/emergence_agent.py
# title: Emergence Agent for Creative Brainstorming
# description: Orchestrates a multi-expert brainstorming session to generate novel ideas.

from typing import List, Dict, Any, Optional
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent
from services.model_loader import ModelLoaderService
from llama_cpp.llama_types import ChatCompletionRequestMessage

class EmergenceAgent(BaseAgent):
    """
    複数の専門家エージェントによる議論を促進し、
    単一のエージェントでは到達できない創発的なアイデアや解決策を生み出すエージェント。
    """
    def __init__(self, model_loader: ModelLoaderService):
        super().__init__(model_loader)
        self.discussion_rounds = 2 # 議論のターン数

    def execute(self, prompt: str, all_experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        指定されたプロンプトについて、ブレインストーミングセッションを実行する。
        """
        print(f"✨ 創発セッションを開始します: {prompt}")

        # 1. 議論に参加する多様なエキスパートを選出
        participants = self._select_participants(all_experts)
        if len(participants) < 2:
            return {
                "response": "創発セッションに必要なエキスパートが不足しています。",
                "self_evaluation": {"confidence": 0.1, "reasoning": "Could not find enough diverse experts to hold a discussion."}
            }
        
        print(f"👥 参加者: {[p.name for p in participants]}")

        # 2. マルチターンでの議論を実行
        discussion_history = f"# 議題: {prompt}\n\n"
        for i in range(self.discussion_rounds):
            print(f"🔄 議論ラウンド {i+1}/{self.discussion_rounds}")
            for expert in participants:
                print(f"   🗣️ {expert.name} のターン...")
                contribution_prompt = self._create_contribution_prompt(prompt, discussion_history, expert)
                messages: List[ChatCompletionRequestMessage] = [
                    {"role": "system", "content": expert.system_prompt},
                    {"role": "user", "content": contribution_prompt}
                ]
                
                response_data = self._query_llm(expert, messages)
                contribution = response_data.get("response", f"（{expert.name}は応答しませんでした）")

                discussion_history += f"## {expert.name} (専門: {expert.description}) の意見:\n{contribution}\n\n---\n"

        # 3. 最終的な統合役が議論を要約し、創発的な結論を導き出す
        synthesizer = self._find_expert("HRM", all_experts)
        if not synthesizer:
             synthesizer = participants[0] # フォールバック
        
        print(f"✅ 議論が終了しました。統合役 ({synthesizer.name}) が結論をまとめます。")
        synthesis_prompt = self._create_synthesis_prompt(prompt, discussion_history)
        messages_synth: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": "あなたは、複数の専門家による活発な議論を分析し、そこから最も重要で革新的な洞察を抽出し、一つの首尾一貫した結論に統合する、極めて優秀なファシリテーター兼エディターです。"},
            {"role": "user", "content": synthesis_prompt}
        ]
        
        final_result_data = self._query_llm(synthesizer, messages_synth)
        print("✨ 創発セッションが完了しました。")
        
        return final_result_data

    def _select_participants(self, all_experts: List[ExpertModel]) -> List[ExpertModel]:
        """議論のために多様なエキスパートを選択する"""
        selected_experts = []
        # 思考(HRM)、汎用(Jamba)、コーディング(Transformer)を優先的に選出
        participant_names = ["hrm", "jamba", "transformer"]
        for name in participant_names:
            expert = self._find_expert(name, all_experts)
            if expert:
                selected_experts.append(expert)
        return selected_experts

    def _create_contribution_prompt(self, original_prompt: str, history: str, current_expert: ExpertModel) -> str:
        """各エキスパートに意見を求めるためのプロンプトを生成する"""
        return f"""現在、以下の議題についてブレインストーミングを行っています。
これまでの議論を踏まえ、あなたの専門分野である「{current_expert.description}」の観点から、ユニークで建設的な意見、アイデア、または批判的視点を提供してください。

{history}

あなたの意見を簡潔に述べてください。
"""

    def _create_synthesis_prompt(self, original_prompt: str, history: str) -> str:
        """最終的な結論を統合するためのプロンプトを生成する"""
        return f"""以下の議題に関する専門家たちのブレインストーミングの全記録です。

{history}

# あなたへの最終指示
この議論全体を注意深く分析し、以下の点を満たす最終的な結論を一つにまとめてください:
1.  **統合:** 個々の意見をただ並べるのではなく、それらを統合して新しい一つの洞察（創発的アイデア）を形成してください。
2.  **革新性:** 最も革新的で、元の議題に対するユニークな解決策や視点を強調してください。
3.  **明確性:** 誰が読んでも理解できるように、明確かつ簡潔な言葉で記述してください。

最終的な結論のみを出力してください。
"""

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> Optional[ExpertModel]:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        return None

```

### `agents/generator_agent.py`

```python
# path: ./agents/generator_agent.py
# title: GeneratorAgent with Self-Evaluation Handling
# description: エキスパートの応答と自己評価を受け取り、タスクオブジェクトに記録する。

import os
import uuid
import traceback
import json
import re
from typing import List, Dict, Any, cast, Optional, Union
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import SubTask, ExpertModel, Milestone
from services.model_loader import ModelLoaderService
from services.worker_manager import WorkerManagerService, WorkerExecutionError
from agents.base_agent import BaseAgent
from agents.consultant_agent import ConsultantAgent
from diffusers import DiffusionPipeline

class GeneratorAgent(BaseAgent):
    """
    エキスパートの実行戦略に応じてタスクを実行し、自己評価を記録するエージェント (HiPLE-G)
    """
    def __init__(self, model_loader: ModelLoaderService, worker_manager: WorkerManagerService, consultant_agent: ConsultantAgent):
        super().__init__(model_loader)
        self.worker_manager = worker_manager
        self.consultant_agent = consultant_agent

    def execute(self, task: SubTask, expert: ExpertModel, context: Dict[str, Any], all_experts: List[ExpertModel]) -> Dict[str, Any]:
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # Step 1: Check for tool use instruction ONLY if tool results are not yet available in the context
        if not context.get("tool_results"):
            tool_match = re.search(r"ツール\s*`([^`]+)`\s*を使って「([^」]+)」", task.description)
            if tool_match:
                tool_name = tool_match.group(1).strip()
                tool_query = tool_match.group(2).strip()
                print(f"🛠️ ツール利用要求を計画から直接検知: {tool_name}('{tool_query}')")
                return {
                    "status": "tool_request",
                    "tool_name": tool_name,
                    "tool_query": tool_query,
                    "tool_url": None # Planner doesn't specify URL, ToolManager will handle it
                }
        
        # Step 2: Handle image generation if it's a diffusion model
        if expert.chat_format == "diffusion":
            result = self._generate_image(expert, task.description)
            task.self_evaluation = {"confidence": 0.9, "reasoning": "Image generated."}
            return {"status": "completed", "result": result}
        
        # Step 3: Handle normal text generation tasks (now with potential tool results in context)
        consultation_feedback = ""
        if task.consultation_experts:
            consultation_result = self.consultant_agent.execute(
                original_task=task,
                primary_expert=expert,
                all_experts=all_experts
            )
            consultation_feedback = consultation_result.get("response", "")
        
        messages = self._build_messages_with_context(task, expert, context, consultation_feedback)
        
        response_data: Dict[str, Any] = {}
        try:
            if expert.execution_strategy == "worker":
                response_dict_from_worker = self.worker_manager.invoke_llm_worker(expert, messages)
                raw_response_str = response_dict_from_worker.get("choices", [{}])[0].get("message", {}).get("content", "")
                try:
                    parsed_data = self._parse_self_evaluation_from_str(raw_response_str)
                    response_data = parsed_data
                except (json.JSONDecodeError, KeyError):
                    response_data = {"response": raw_response_str, "self_evaluation": {"confidence": 0.75, "reasoning": "Evaluation from worker could not be parsed."}}
            else:
                response_data = self._query_llm(expert, messages)
        except WorkerExecutionError as e:
            print(f"❌ ワーカーの実行に失敗しました: {e}")
            return {"status": "failed", "result": f"エキスパート '{expert.name}' の実行中にエラーが発生しました。"}

        raw_response = response_data.get("response", "")
        task.self_evaluation = response_data.get("self_evaluation")
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # If the LLM asks to use a tool, return that as a special status
        tool_use_match = re.search(r'"tool_use"\s*:', raw_response, re.IGNORECASE)
        if tool_use_match:
            try:
                # Extract the JSON part for tool use
                json_part = raw_response[raw_response.find('{'):raw_response.rfind('}')+1]
                tool_data = json.loads(json_part)
                tool_info = tool_data.get("tool_use")
                if tool_info and "tool_name" in tool_info and "tool_query" in tool_info:
                    print(f"🛠️ ツール利用要求を検知: {tool_info['tool_name']}('{tool_info['tool_query']}')")
                    return {
                        "status": "tool_request",
                        "tool_name": tool_info["tool_name"],
                        "tool_query": tool_info["tool_query"],
                        "tool_url": tool_info.get("tool_url")
                    }
            except (json.JSONDecodeError, KeyError):
                # Fall through to normal completion if JSON is malformed
                pass

        return {"status": "completed", "result": raw_response.strip()}
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def _parse_self_evaluation_from_str(self, raw_str: str) -> Dict[str, Any]:
        """ 文字列から自己評価JSONをパースする """
        json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_str, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            start_index = raw_str.find('{')
            end_index = raw_str.rfind('}')
            if start_index != -1 and end_index != -1:
                json_str = raw_str[start_index:end_index + 1]
            else:
                raise json.JSONDecodeError("No JSON object found", raw_str, 0)
        
        data = json.loads(json_str)
        if "response" not in data or "self_evaluation" not in data:
            raise KeyError("Missing 'response' or 'self_evaluation' key")
        return data

    def _build_messages_with_context(
        self,
        task: SubTask,
        expert: ExpertModel,
        context: Dict[str, Any],
        consultation_feedback: str = ""
    ) -> List[ChatCompletionRequestMessage]:
        
        milestone: Optional[Milestone] = context.get('milestone')
        system_prompt = expert.system_prompt
        dependency_results = context.get("dependency_results", "")
        rag_results_list = context.get("rag_results", [])
        rag_results_str = "\n".join([f"- {r}" for r in rag_results_list])
        ssv_description = context.get('ssv_description', task.description)
        tool_results = context.get("tool_results", "")
        feedback = task.feedback_history[-1].get("feedback") if task.feedback_history else ""

        if tool_results:
            main_instruction = """# あなたのタスク (L3)
先行タスクによって、以下の「ツールからの情報」が収集されました。
この情報を基に、以下のタスク詳細を達成するための応答を生成してください。
"""
        else:
            main_instruction = """# あなたのタスク (L3)
以上の全てのコンテキスト情報を踏まえ、以下のタスクを実行してください。

**【最重要】**
**このタスクが外部ツールの使用を指示している場合（例：「ツール `web_search` を使って〜」）、他の応答は一切せず、必ず以下のJSON形式のみを出力してください。**
{
  "tool_use": {
    "tool_name": "（`description`に書かれているツール名）",
    "tool_query": "（検索や実行のための具体的なキーワードや質問）"
  }
}
**ツール使用の指示がない場合にのみ**、通常の応答と自己評価を生成してください。
"""
        
        user_prompt = f"""# 全体目標 (L1)
{context.get('overall_goal', 'N/A')}

# 現在のマイルストーン (L2)
タイトル: {milestone.title if milestone else 'N/A'}
説明: {milestone.description if milestone else 'N/A'}

# 先行タスクからのコンテキスト
{dependency_results if dependency_results else "先行タスクはありません。"}

# 関連情報 (RAG)
{rag_results_str if rag_results_str else "関連情報はありません。"}

# ツールからの情報
{tool_results if tool_results else "ツールからの情報はありません。"}

# 専門家からの助言 (コンサルテーション)
{consultation_feedback if consultation_feedback else "特になし。"}

#【重要】前回のレビューからのフィードバック
{feedback if feedback else "フィードバックはありません。"}

{main_instruction}

## タスクの核心 (SSV)
**このタスクで最も重要な目的は「{ssv_description}」を達成することです。**

## タスクの詳細
{task.description}
"""
        
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

    def _generate_image(self, expert: ExpertModel, prompt: str) -> str:
        print(f"🎨 拡散モデル '{expert.name}' を使用して画像を生成します...")
        try:
            pipe = cast(DiffusionPipeline, self.model_loader.load_expert(expert))
            image = pipe(prompt=prompt).images[0]
            
            output_dir = "output/images"
            os.makedirs(output_dir, exist_ok=True)
            
            filename = f"{uuid.uuid4()}.png"
            output_path = os.path.join(output_dir, filename)
            image.save(output_path)
            
            absolute_path = os.path.abspath(output_path)
            print(f"🖼️ 画像を保存しました: {absolute_path}")
            return f"画像を {absolute_path} に生成しました。"

        except Exception as e:
            error_message = f"エラー: 画像の生成に失敗しました - {e}"
            print(f"❌ {error_message}")
            traceback.print_exc()
            return error_message
```

### `agents/metacognition_agent.py`

```python
# path: ./agents/metacognition_agent.py
# title: Metacognition Agent
# description: Analyzes the cognitive load of a plan to prevent overly complex or inefficient execution.

from typing import List, Dict, Any, Tuple
from domain.schemas import Plan

class MetacognitionAgent:
    """
    計画の複雑性やリソース消費を予測し、実行前に評価するメタ認知エージェント。
    """
    def __init__(self, task_limit: int = 20, dependency_depth_limit: int = 5):
        self.task_limit = task_limit
        self.dependency_depth_limit = dependency_depth_limit

    def analyze_cognitive_load(self, plan: Plan) -> Tuple[bool, str]:
        """
        計画の認知負荷を分析する。

        Returns:
            Tuple[bool, str]: (実行可能か, 分析メッセージ)
        """
        # 1. タスク数のチェック
        if len(plan.tasks) > self.task_limit:
            return False, f"Cognitive Overload: The plan exceeds the maximum task limit of {self.task_limit}."

        # 2. 依存関係の深さをチェック
        max_depth, path = self._calculate_max_dependency_depth(plan)
        if max_depth > self.dependency_depth_limit:
            path_str = " -> ".join(map(str, path))
            return False, f"Cognitive Overload: The plan's dependency depth ({max_depth}) exceeds the limit of {self.dependency_depth_limit}. Path: {path_str}"

        return True, "Cognitive load analysis passed."

    def _calculate_max_dependency_depth(self, plan: Plan) -> Tuple[int, List[int]]:
        """計画の依存関係の最大の深さを計算する"""
        if not plan.tasks:
            return 0, []

        memo: Dict[int, Tuple[int, List[int]]] = {}
        task_map = {task.task_id: task for task in plan.tasks}
        max_depth = 0
        longest_path: List[int] = []

        def dfs(task_id: int) -> Tuple[int, List[int]]:
            if task_id in memo:
                return memo[task_id]
            
            task = task_map.get(task_id)
            if not task or not task.dependencies:
                memo[task_id] = (1, [task_id])
                return 1, [task_id]

            max_child_depth = 0
            best_path: List[int] = []
            for dep_id in task.dependencies:
                depth, path = dfs(dep_id)
                if depth > max_child_depth:
                    max_child_depth = depth
                    best_path = path
            
            current_depth = max_child_depth + 1
            current_path = best_path + [task_id]
            memo[task_id] = (current_depth, current_path)
            return current_depth, current_path

        for task in plan.tasks:
            depth, path = dfs(task.task_id)
            if depth > max_depth:
                max_depth = depth
                longest_path = path
        
        return max_depth, longest_path
```

### `agents/planner_agent.py`

```python
# path: ./agents/planner_agent.py
# title: Hierarchical PlannerAgent (Self-Evaluation Aware)
# description: エキスパートが利用可能なツールを認識し、計画にツール利用ステップを組み込むことができる。

import json
import re
from typing import List, Optional, Dict, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import Plan, SubTask, ExpertModel, Milestone
from agents.base_agent import BaseAgent
from services.tool_manager_service import ToolManagerService

class PlannerAgent(BaseAgent):
    """
    ユーザーの要求を分析し、階層的な計画（Plan）を生成するエージェント (HiPLE-P)
    エキスパートのパフォーマンス、コスト、速度、利用可能なツールも考慮する。
    """
    def execute(
        self,
        prompt: str,
        experts: List[ExpertModel],
        tool_manager: ToolManagerService,
        failed_plan: Optional[Plan] = None,
        validation_error: Optional[str] = None,
        performance_summary: Optional[str] = None,
    ) -> Plan:
        planner_expert = self._find_planner_expert(experts)
        expert_descriptions = self._format_expert_descriptions(experts)
        tool_descriptions = tool_manager.get_tool_descriptions()

        system_prompt = self._build_system_prompt(expert_descriptions, tool_descriptions, performance_summary)
        user_prompt = self._build_user_prompt(prompt, validation_error, failed_plan)
        
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        response_data = self._query_llm(planner_expert, messages)
        raw_response = response_data.get("response", "")
        
        return self._parse_plan_from_response(raw_response, prompt, planner_expert)

    def _find_planner_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        fallback = next((e for e in experts if e.chat_format != "diffusion"), None)
        if fallback: return fallback
        raise ValueError("利用可能なプランナーエキスパートが見つかりません。")

    def _build_system_prompt(self, expert_descriptions: str, tool_descriptions: str, performance_summary: Optional[str]) -> str:
        prompt_header = """あなたは、ユーザーの曖昧な要求を構造化された階層的計画に変換する、超優秀なAIプロジェクトマネージャーです。
# あなたのタスク
ユーザーの要求と利用可能なリソース（エキスパート、ツール）を分析し、最適なJSON形式の実行計画を立案してください。
"""
        tools_section = f"""
# 利用可能なツール
{tool_descriptions}
"""
        
        experts_section = f"""
# 利用可能なエキスパート (タスクの担当者)
{expert_descriptions}
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        judgement_criteria = """
# 判断基準 (最重要)
1.  **情報検索タスクの計画**: ユーザーの要求が外部情報（Web検索やWikipedia）を必要とする場合、それを実行する**単一のタスク**を作成します。
    - **ツール選択**: 要求内容に応じて最適なツール（`web_search`または`wikipedia_search`）を選択します。
    - **description**: 「「[検索クエリ]」について[ツール名]で調査する」のように具体的に記述します。
    - **後続タスク**: 検索結果をさらに加工する必要がある場合（例：レポートにまとめる、他の情報と組み合わせる）、そのための後続タスクを計画できます。単純な情報提供で完結する場合は、単一タスクで問題ありません。
2.  **エキスパートの選定**: `expert_name` には、必ず上記の「利用可能なエキスパート」リストに存在する名前を指定します。ツール名は指定できません。情報検索タスクの担当は `Jamba` が適任です。
3.  **性能・速度・コスト**: `performance_summary` を参考に、タスク内容に最も適したエキスパートを選択します。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        performance_section = f"""
# エキスパートのパフォーマンス実績 (参考情報)
{performance_summary if performance_summary else "パフォーマンス記録はまだありません。エキスパートの特性に基づいて判断してください。"}
"""
        return (prompt_header + tools_section + experts_section + judgement_criteria + 
                self._get_json_format_section() + self._get_rules_section())

    def _build_user_prompt(self, prompt: str, validation_error: Optional[str], failed_plan: Optional[Plan]) -> str:
        user_prompt = f"以下のユーザー要求に対する階層的実行計画をJSON形式で作成してください:\n\n要求: \"{prompt}\""
        if validation_error:
            user_prompt += f"\n\n#【最重要】前回の計画は以下の検証エラーで失敗しました。このエラーを完全に修正し、論理的に一貫した新しい計画を立て直してください。\nエラー内容: {validation_error}"
        if failed_plan:
            user_prompt += f"\n\n# 警告\n前回の計画は実行に失敗しました。内容を根本的に見直し、新しいアプローチで計画を立て直してください。"
        return user_prompt

    def _parse_plan_from_response(self, raw_response: Any, original_prompt: str, planner_expert: ExpertModel) -> Plan:
        try:
            print(f"--- Hierarchical Planner Raw Response ---\n{raw_response}\n--------------------------")
            
            plan_data: Dict[str, Any]
            if isinstance(raw_response, dict):
                plan_data = raw_response
            elif isinstance(raw_response, str):
                json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_response, re.DOTALL)
                if json_match:
                    json_str = json_match.group(1)
                else:
                    start_index = raw_response.find('{')
                    end_index = raw_response.rfind('}') + 1
                    if start_index != -1:
                        json_str = raw_response[start_index:end_index]
                    else:
                        raise json.JSONDecodeError("No JSON object found", raw_response, 0)
                plan_data = json.loads(json_str)
                if "response" in plan_data and isinstance(plan_data["response"], dict):
                    plan_data = plan_data["response"]
            else:
                raise TypeError(f"Response is not a valid type (string or dictionary), but got {type(raw_response)}")

            milestones = [Milestone(**m) for m in plan_data.get("milestones", [])]
            tasks_data = plan_data.get("tasks", [])
            if not tasks_data:
                 return self._create_fallback_plan(original_prompt, planner_expert)

            for t in tasks_data:
                t.setdefault("ssv_description", t["description"])
                t.setdefault("consultation_experts", [])
                t.setdefault("reviewer_expert", None)
                t["feedback_history"] = []

            tasks = [SubTask(**t) for t in tasks_data]

            return Plan(
                original_prompt=original_prompt,
                overall_goal=plan_data.get("overall_goal", "N/A"),
                milestones=milestones,
                tasks=tasks
            )
        except (json.JSONDecodeError, TypeError, ValueError, AttributeError) as e:
            print(f"❌ 階層的計画のパースに失敗しました: {e}")
            print(f"🔁 フォールバック：元のプロンプトを直接実行します。")
            return self._create_fallback_plan(original_prompt, planner_expert)

    def _create_fallback_plan(self, original_prompt: str, expert: ExpertModel) -> Plan:
        task = SubTask(
            task_id=1,
            milestone_id=1,
            description=original_prompt,
            expert_name=expert.name,
            ssv_description=original_prompt,
            dependencies=[]
        )
        milestone = Milestone(milestone_id=1, title="Direct Execution", description="Execute the user's prompt directly.")
        return Plan(
            original_prompt=original_prompt,
            overall_goal=original_prompt,
            milestones=[milestone],
            tasks=[task]
        )

    def _format_expert_descriptions(self, experts: List[ExpertModel]) -> str:
        return "\n".join(
            [f"- **{e.name}**: {e.description} (Cost: {e.cost_score}/10, Speed: {e.speed_score}/10)" 
             for e in experts if e.name.lower() != "reporter"]
        )

    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    def _get_json_format_section(self) -> str:
        return """
# JSON出力フォーマット (厳守)
あなたの応答は、最終的に自己評価を含むより大きなJSONの一部として解析されます。以下の`response`キーの値として、計画JSONを出力してください。
`response`キーの値は、純粋な計画JSONオブジェクトである必要があります。
{
    "response": {
        "overall_goal": "家庭で簡単に作れるアイスの作り方をユーザーに教える",
        "milestones": [
            {
                "milestone_id": 1,
                "title": "レシピ調査",
                "description": "Webで簡単なアイスクリームのレシピを調査する"
            }
        ],
        "tasks": [
            {
                "task_id": 1,
                "milestone_id": 1,
                "description": "ツール `web_search` を使って「アイスクリーム 簡単 レシピ」を調査する",
                "expert_name": "Jamba",
                "ssv_description": "アイスクリームの簡単レシピ検索と要約",
                "consultation_experts": [],
                "reviewer_expert": null,
                "dependencies": []
            }
        ]
    },
    "self_evaluation": { "confidence": 0.9, "reasoning": "This is a standard information retrieval task." }
}
"""
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def _get_rules_section(self) -> str:
        return """
# ルール
- **ID**: `milestone_id`と`task_id`は1から始まる連番にしてください。
- **依存関係**: `dependencies`には、先行するタスクの`task_id`を**数値の配列**として`[1, 2]`のように指定します。
- **担当者**: `expert_name` と `consultation_experts` には、必ずエキスパートリストの名前を指定してください。ツール名は指定できません。
- **レビュー担当**: `reviewer_expert`は、文章生成やコーディングなど、**品質が問われるタスクにのみ**設定してください。単純な情報検索タスクには`null`を設定してください。
- **報告タスク**: 複雑な要求の場合、最後に'Reporter'を配置し、最終報告書を作成させてください。
- **単純な要求**: 単純な挨拶や質問の場合、マイルストーンは1つ、タスクも1つだけ生成します。
"""
```

### `agents/rag_agent.py`

```python
# path: ./agents/rag_agent.py
# title: RAG Agent (Self-Evaluation Aware)
# description: Determines if retrieval is necessary and provides self-evaluated decision.

import json
import re
from typing import List, Dict, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class RAGAgent(BaseAgent):
    """
    与えられたプロンプトに対して、内部知識ベースの検索(RAG)が必要かどうか、
    また検索する場合の最適なクエリは何かを判断するエージェント。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        プロンプトを分析し、検索の要否と検索クエリを含む辞書を返す。
        """
        router_expert = self._find_expert("HRM", experts)

        system_prompt = """あなたはユーザーのタスク記述を分析し、そのタスクを達成するために内部知識ベース（過去の計画やタスクの文脈）の検索が必要かどうかを判断する、優秀なアシスタントです。
以下のJSONフォーマットで、判断結果のみを答えてください。余計な説明は一切不要です。

# 出力フォーマット
```json
{
  "needs_retrieval": "（trueまたはfalse）",
  "query": "（検索が必要な場合に、内部知識ベースを検索するための最も的確なキーワードや質問文。検索不要の場合はnull）"
}
```

# 判断基準
- `needs_retrieval: true`: タスクが先行するタスクの結果や、計画全体の目標、他のマイルストーンなど、過去の文脈情報を明確に必要としている場合。`query`には、その文脈を最もよく表すキーワードを指定します。（例：タスク「上記の結果を要約する」 -> query: "先行タスクの結果"）
- `needs_retrieval: false`: タスクが自己完結しており、外部の文脈情報なしに実行可能な場合。（例：タスク「Pythonで'Hello World'を出力するコードを書く」）

ユーザーのタスク記述を慎重に読み、上記のJSON形式を、自己評価JSONの`response`キーに含めて応答してください。
"""

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        response_data = self._query_llm(router_expert, messages)
        
        # 応答がJSON文字列で返ってくる場合があるため、パースを試みる
        raw_response_content = response_data.get("response", "{}")
        try:
            if isinstance(raw_response_content, str):
                 # LLMがresponseキーの中にさらにJSON文字列を生成する場合がある
                json_match = re.search(r'\{[\s\S]*\}', raw_response_content)
                if json_match:
                    decision_json = json.loads(json_match.group(0))
                else:
                    decision_json = {}
            else:
                decision_json = raw_response_content

            needs_retrieval = decision_json.get("needs_retrieval", False)
            if not isinstance(needs_retrieval, bool):
                needs_retrieval = str(needs_retrieval).lower() == 'true'
            
            query = decision_json.get("query") if needs_retrieval else None
            
            response_data["response"] = {"needs_retrieval": needs_retrieval, "query": query}
        
        except (json.JSONDecodeError, AttributeError):
             response_data["response"] = {"needs_retrieval": False, "query": None}
        
        return response_data


    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")

```

### `agents/reporter_agent.py`

```python
# path: ./agents/reporter_agent.py
# title: Finalized Reporter Agent
# description: 全タスクの成果を統合し、ユーザーの元の要求に、元の言語で的確に回答する最終版。

from typing import List
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import Plan, ExpertModel
from agents.base_agent import BaseAgent

class ReporterAgent(BaseAgent):
    """
    完了した階層的計画の結果を統合し、最終的な報告書を生成するエージェント
    """
    def execute(self, plan: Plan, experts: List[ExpertModel]) -> str:
        reporter_expert = self._find_reporter_expert(experts)
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        context = self._build_context(plan)
        prompt = self._build_final_prompt(plan.original_prompt, context)
        
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": reporter_expert.system_prompt},
            {"role": "user", "content": prompt}
        ]
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        return self._query_llm(reporter_expert, messages)

    def _find_reporter_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        """レポーター役のエキスパートを見つける"""
        for expert in experts:
            if expert.name.lower() == "reporter":
                return expert
        # HRMは安定したフォールバック先
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        raise ValueError("レポーター役のエキスパートが見つかりません。")

    def _build_context(self, plan: Plan) -> str:
        """レポーターに渡すための、全タスクの結果をまとめたコンテキストを構築する"""
        context = f"# 最終目標: {plan.overall_goal}\n\n# 各エキスパートからの報告サマリー\n---\n"
        # 実行順にタスクをソート
        sorted_tasks = sorted([t for t in plan.tasks if t.status == "completed" and t.expert_name.lower() != 'reporter'], key=lambda t: t.task_id)
        
        for task in sorted_tasks:
            context += f"## タスク {task.task_id}: {task.description} (担当: {task.expert_name})\n"
            context += f"**結果:**\n{task.result}\n\n"
        context += "---\n"
        return context

    def _build_final_prompt(self, original_prompt: str, context: str) -> str:
        """最終的な指示を生成するための、明確で強力なプロンプトを構築する"""
        return f"""\
あなたは、複数のAIエキスパートからの報告を統合し、最終的な一つの回答を作成する、極めて優秀なチーフエディターです。

{context}

# あなたへの最終指示 (最重要)
上記の「各エキスパートからの報告サマリー」を完全に理解し、以下のユーザーからの「元の要求」に、直接的かつ包括的に回答してください。

## 元の要求
「{original_prompt}」

# 厳守すべきルール
1.  **言語の厳守:** 回答は、必ず「元の要求」と同じ言語（この場合は日本語）で記述してください。
2.  **内容の統合:** 単なる報告の連結ではなく、全ての情報を統合・要約し、首尾一貫した一つの文章に再構成してください。
3.  **目的の遵守:** あなたの唯一の目的は、「元の要求」に答えることです。報告サマリーにない情報は、決して含めないでください。
4.  **形式:** 最終的な回答のみを出力してください。思考過程や挨拶などは一切不要です。
"""
```

### `agents/reviewer_agent.py`

```python
# path: ./agents/reviewer_agent.py
# title: Reviewer Agent (Self-Evaluation Aware)
# description: 他のエキスパートが生成した成果物をレビューし、自己評価付きのフィードバックを提供するエージェント。

from typing import List, Dict, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel, SubTask

class ReviewerAgent(BaseAgent):
    """
    成果物をレビューし、フィードバックを提供するエージェント。
    """
    def execute(
        self,
        task: SubTask,
        generated_output: str,
        reviewer_expert: ExpertModel,
        original_expert: ExpertModel
    ) -> Dict[str, Any]:
        """
        生成された成果物をレビューし、改善点を指摘する。
        """
        print(f"🧐 {reviewer_expert.name}が{original_expert.name}の成果物をレビューします...")

        system_prompt = f"""あなたは、他のAIエキスパートが生成した成果物をレビューし、品質を向上させるための具体的で建設的なフィードバックを与える、非常に優秀な品質保証（QA）スペシャリストです。
あなたの専門分野は「{reviewer_expert.description}」です。"""

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        user_prompt = f"""以下のタスクと、それに対してエキスパート「{original_expert.name}」が生成した成果物をレビューしてください。

# 元のタスク
- **目的 (SSV):** {task.ssv_description}
- **詳細:** {task.description}

# 生成された成果物
---
{generated_output}
---

# あなたへの指示
上記の成果物が、元のタスクの目的（SSV）と詳細を完全に満たしているか、あなたの専門的観点から厳しく評価してください。
- **成果物が目的を完全に満たしている場合**: 「承認します。」という一文から始めてください。
- **問題点や改善できる点がある場合**: 具体的な修正案を箇条書きで指摘してください。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        feedback_data = self._query_llm(reviewer_expert, messages)
        print(f"📝 レビューが完了しました。")
        return feedback_data
```

### `agents/safety_director_agent.py`

```python
# path: ./agents/safety_director_agent.py
# title: Safety Director Agent with Confidence Check (Completed)
# description: システムの健全性に加え、各タスクの自己評価（自信度）を監視し、低品質な成果物を検知する。

from typing import List, Dict, Any, Optional
from domain.schemas import Plan, SubTask
from workspace.global_workspace import GlobalWorkspace

class SafetyDirectorAgent:
    """
    システム全体の思考プロセスを監視し、非効率なループや矛盾、
    リスク（低自信度の応答など）を検知して介入する安全監督官エージェント。
    """
    def __init__(self, max_replanning: int = 3, max_feedback_loops: int = 3, confidence_threshold: float = 0.6):
        self.max_replanning = max_replanning
        self.max_feedback_loops = max_feedback_loops
        self.confidence_threshold = confidence_threshold

    def review_thought_process(self, workspace: GlobalWorkspace) -> Optional[str]:
        """
        現在の思考プロセスをレビューし、問題があれば介入指示を返す。
        """
        thought_process = workspace.thought_process

        # 1. 無限再計画ループの検知
        planning_attempts = sum(1 for thought in thought_process if thought.get("type") == "planning_start")
        if planning_attempts > self.max_replanning:
            return f"Safety Alert: Planning has failed {planning_attempts} times. Aborting task to prevent infinite loop."

        # 2. 特定タスクでの無限フィードバックループの検知
        feedback_counts: Dict[int, int] = {}
        for thought in thought_process:
            if thought.get("type") == "review_start":
                task_id = thought.get("content", {}).get("task_id")
                if task_id:
                    feedback_counts[task_id] = feedback_counts.get(task_id, 0) + 1
                    if feedback_counts[task_id] > self.max_feedback_loops:
                        return f"Safety Alert: Task {task_id} is stuck in a feedback loop. Aborting."

        # 3. 低自信度タスクの検知
        for thought in thought_process:
            if thought.get("type") == "task_completed":
                content = thought.get("content", {})
                evaluation = content.get("self_evaluation")
                if evaluation and isinstance(evaluation, dict):
                    confidence = evaluation.get("confidence", 1.0)
                    if isinstance(confidence, (int, float)) and confidence < self.confidence_threshold:
                        task_id = content.get("task_id")
                        reasoning = evaluation.get("reasoning", "No reason provided.")
                        # 重要度が低い警告として返し、処理は続行させる
                        print(f"⚠️ Safety Warning: Task {task_id} completed with low confidence ({confidence:.2f}). Reason: {reasoning}")

        return None

```

### `agents/tool_router_agent.py`

```python
# path: ./agents/tool_router_agent.py
# title: Intelligent Tool Router Agent (Self-Aware)
# description: Uses LLM reasoning to understand user intent, including meta-questions about the AI system itself.

import json
import re
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class ToolRouterAgent(BaseAgent):
    """
    ユーザーの要求の意図を分析し、適切なツールや処理フローを特定するインテリジェントなルーター。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        プロンプトを分析し、ツール、クエリ、URLを含む辞書を返す。
        """
        # ルーティングには思考能力の高いHRMモデルを指名
        router_expert = self._find_expert("HRM", experts)
        if not router_expert:
            # フォールバックとして利用可能な最初のエキスパートを使用
            router_expert = next((e for e in experts if e.chat_format != "diffusion"), None)
        
        if not router_expert:
            raise ValueError("No suitable expert found for routing.")

        print(f"🧠 Router expert selected: {router_expert.name}")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = (
            "あなたはユーザーの要求の意図を深く分析し、その要求を達成するために最も適した処理を判断する、超優秀なディスパッチャーです。\n"
            "以下の思考プロセスに従い、最終的な判断をJSONフォーマットで出力してください。\n\n"
            "# 思考プロセス (Step-by-Step)\n"
            "1.  **要求の核心分析**: ユーザーは何を本当に知りたいのか、または何をしてほしいのか？（例：「作り方を知りたい」「歴史を知りたい」など）\n"
            "2.  **情報源の特定**: その要求に答えるために必要な情報は、外部の普遍的な知識か、最新情報か、あるいはAI自身の内部情報か？\n"
            "3.  **処理の分類**: 上記の分析に基づき、以下の基準で最適な処理を一つだけ選択する。\n"
            "4.  **JSON生成**: 最終的な判断をJSON形式で出力する。思考プロセスは出力に含めないこと。\n\n"
            "# 判断基準\n"
            "- `wikipedia`: **「普遍的で確立された外部の知識」**が求められている場合。一般的な用語、歴史、人物、科学的原理など。\n"
            "    - 例: 「徳川家康とは？」「量子もつれの原理」\n"
            "- `web_search`: **「最新情報」「特定のURLに関する情報」「具体的な手順やレシピ」**が求められている場合。\n"
            "    - 例: 「今日のニュースを教えて」「この記事(URL)を要約して」「アイスクリームの作り方を教えて」\n"
            "- `emergent_task`: **「新しいアイデアや創造的な解決策」**が求められている場合。ブレインストーミングの指示。\n"
            "    - 例: 「新商品のアイデアをブレストして」\n"
            "- `complex_task`: **「AI自身に関する質問」**または**「複数ステップの実行や専門的なコード生成」**が求められている場合。\n"
            "    - 例: 「HRMモデルについて教えて」「君の能力は？」「PythonでWebサーバーを作って」\n"
            "- `greeting`: **「単純な対話」**の場合。挨拶や感謝など。\n"
            "    - 例: 「こんにちは」「ありがとう」\n\n"
            "# 出力フォーマット (厳守)\n"
            "```json\n"
            "{\n"
            '  "tool": "（\'wikipedia\', \'web_search\', \'emergent_task\', \'complex_task\', \'greeting\' のいずれか）",\n'
            '  "query": "（ツールやタスクで使用すべきキーワードや質問文。挨拶の場合はnull）",\n'
            '  "url": "（web_searchの場合のURL。それ以外はnull）"\n'
            "}\n"
            "```"
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        # ToolRouterAgent自身の実行では自己評価は不要なため、内部のLLM呼び出しを直接行う
        raw_response_data = self._query_llm(router_expert, messages)
        raw_response = raw_response_data.get("response", "")
        
        try:
            json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_response, re.DOTALL)
            if json_match:
                response_json_str = json_match.group(1)
            else:
                response_json_str = raw_response[raw_response.find('{'):raw_response.rfind('}')+1]

            data = json.loads(response_json_str)
            tool = data.get("tool", "complex_task")
            query = data.get("query")
            url = data.get("url")
            response = data.get("response") # 挨拶用

            if tool not in ["wikipedia", "web_search", "complex_task", "greeting", "emergent_task"]:
                tool = "complex_task"

            return {"type": tool, "query": query if query else prompt, "url": url, "response": response}

        except (json.JSONDecodeError, AttributeError):
            # パース失敗時は最も安全なcomplex_taskとして処理
            return {"type": "complex_task", "query": prompt, "url": None, "response": None}

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> Optional[ExpertModel]:
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        return None
```

### `agents/web_browser_agent.py`

```python
# path: ./agents/web_browser_agent.py
# title: Web Browser Agent (Synchronous)
# description: WebBrowserServiceを使い、レンダリングされたWebページを調査・分析するエージェント。

from typing import List
from bs4 import BeautifulSoup, NavigableString
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel
from llama_cpp.llama_types import ChatCompletionRequestMessage
import re

class WebBrowserAgent(BaseAgent):
    """
    Webページを調査し、その内容を分析・要約するエージェント。
    """
    def execute(self, content: str, query: str, all_experts: List[ExpertModel]) -> str:
        """
        指定されたHTMLコンテンツを分析し、クエリに基づいて内容を要約する。
        """
        if "エラー:" in content:
            return content

        soup = BeautifulSoup(content, 'html.parser')
        for tag in soup(['script', 'style', 'nav', 'footer', 'aside', 'header', 'link', 'meta']):
            tag.decompose()
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # クエリに関連するキーワードでテキストを絞り込む
        keywords = re.split(r'\s+', query) + ["材料", "作り方", "レシピ", "手順"]
        
        relevant_text = ""
        for element in soup.find_all(string=True):
            if isinstance(element, NavigableString):
                parent = element.parent
                # 親要素が存在し、表示されている要素のみを対象とする
                if parent and parent.name not in ['script', 'style', 'head', 'title']:
                    text_line = element.strip()
                    if any(keyword in text_line for keyword in keywords):
                        # 関連キーワードが含まれる行の周辺テキストを取得
                        context_lines = []
                        # 前後の兄弟要素からテキストを取得して文脈を追加
                        for sibling in element.find_previous_siblings(limit=2):
                            context_lines.insert(0, sibling.get_text(separator=' ', strip=True))
                        context_lines.append(text_line)
                        for sibling in element.find_next_siblings(limit=2):
                            context_lines.append(sibling.get_text(separator=' ', strip=True))
                        
                        relevant_text += " ".join(context_lines) + "\n"
        
        if not relevant_text:
            body_text = soup.get_text(separator='\n', strip=True)
            if not body_text:
                return "エラー: ページからテキストコンテンツを抽出できませんでした。"
            relevant_text = body_text
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        # コンテキストウィンドウを考慮してテキストを切り詰める
        max_length = 8000
        truncated_text = relevant_text[:max_length]

        # 要約には論理的推論が得意なHRMを指名
        summarizer_expert = self._find_expert("HRM", all_experts)
        
        return self._summarize_with_llm(summarizer_expert, truncated_text, query)

    def _summarize_with_llm(self, expert: ExpertModel, text: str, query: str) -> str:
        """LLMを使ってテキストを要約する。"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = "あなたは、与えられたWebページのテキストコンテンツを分析し、ユーザーの質問に的確に答える優秀なアナリストです。テキストの中から関連する情報のみを抽出し、具体的なレシピや手順がわかるように要約してください。"
        user_prompt = f"""以下のWebページの内容を読み、質問に答えてください。

# 質問
{query}

# Webページの内容 (関連部分抜粋)
---
{text}
---

質問に対する回答を、**材料と作り方の手順が明確にわかるように箇条書きで**生成してください。
もし情報が不足していて回答できない場合は、「ウェブページから具体的な作り方を見つけることができませんでした。」と正直に回答してください。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response_data = self._query_llm(expert, messages)
        return response_data.get("response", "要約の生成に失敗しました。")
    
    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")
```

### `agents/wikipedia_agent.py`

```python
# path: ./agents/wikipedia_agent.py
# title: Wikipedia Agent (Improved Keyword Extraction)
# description: Extracts Japanese keywords with high precision to improve search accuracy.

from typing import List, Dict, Any, Optional
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel
from services.wikipedia_service import WikipediaService
from services.model_loader import ModelLoaderService
from llama_cpp.llama_types import ChatCompletionRequestMessage

class WikipediaAgent(BaseAgent):
    """
    Wikipediaを検索し、結果をLLMで要約・整形して返すエージェント。
    """
    def __init__(self, model_loader: ModelLoaderService, wikipedia_service: WikipediaService):
        super().__init__(model_loader)
        self.wikipedia_service = wikipedia_service

    def execute(self, query: str, all_experts: List[ExpertModel]) -> str:
        """
        指定されたクエリでWikipediaを検索し、結果を要約・整形して返す。
        """
        summarizer_expert = self._find_expert("HRM", all_experts)
        if not summarizer_expert:
             return "エラー: Wikipedia検索に必要なHRMエキスパートが見つかりません。"

        search_term_data = self._extract_search_term(query, summarizer_expert)
        search_term = search_term_data.get("response", query) # 抽出失敗時は元のクエリを使用
        
        print(f"🔍 抽出された検索キーワード: '{search_term}'")

        print(f"📖 Wikipediaで '{search_term}' を検索しています...")
        search_results = self.wikipedia_service.search(search_term)

        if not search_results:
            return f"「{query}」に関するWikipedia記事は見つかりませんでした。"

        first_title = search_results[0]
        print(f"📄 最も関連性の高い記事「{first_title}」の要約を取得します。")
        raw_summary = self.wikipedia_service.get_summary(first_title, sentences=15)

        if not raw_summary:
            return f"記事「{first_title}」の要約を取得できませんでした。"

        print(f"✍️ 取得した情報をHRMで整形・要約します...")
        
        system_prompt = "あなたは、与えられたWikipediaの記事の抜粋を分析し、ユーザーの元の質問に対して、ステップバイステップで分かりやすく具体的な手順を説明する優秀な解説者です。"
        user_prompt = f"""以下のテキストは、Wikipediaの記事「{first_title}」からの抜粋です。
この情報を基に、ユーザーからの最初の質問に直接回答する形で、簡潔で明瞭なサマリーを作成してください。

# ユーザーの最初の質問
「{query}」

# 記事の抜粋
---
{raw_summary}
---

# あなたのタスク
上記の抜粋から、ユーザーの質問に答えるために必要な情報だけを抽出し、**具体的な材料と作り方の手順がわかるように**、箇条書きなどを用いて分かりやすい最終的な回答を生成してください。
"""
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        formatted_summary_data = self._query_llm(summarizer_expert, messages)
        formatted_summary = formatted_summary_data.get("response", "要約の生成に失敗しました。")
        
        return f"Wikipediaの記事「{first_title}」を基にした回答:\n\n{formatted_summary}"

    def _extract_search_term(self, query: str, expert: ExpertModel) -> Dict[str, Any]:
        """
        ユーザーの質問文から、日本語Wikipediaの検索に最適な日本語のキーワードを抽出する。
        """
        system_prompt = """あなたは、ユーザーの質問の核心を理解し、日本語の百科事典（Wikipedia）で調べるのに最も適した、具体的で短い「日本語の検索キーワード」を抽出する専門家です。
例えば、「アイスの作り方」という質問であれば、「アイスクリーム 製造」や「氷菓」のような、製造方法や分類に関するキーワードが適切です。
回答は、抽出したキーワード本体のみを含むようにしてください。余計な説明や挨拶、JSONの定型文は一切不要です。
"""
        user_prompt = f"以下の質問文から、日本語のWikipediaで検索するための最も的確なキーワードを一つだけ抽出してください:\n\n「{query}」"

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        response_data = self._query_llm(expert, messages)
        
        response_text = response_data.get("response", "")
        if isinstance(response_text, dict):
            response_text = response_text.get("keyword", "") or str(response_text)

        cleaned_term = response_text.strip().replace('"', '').replace("'", "").replace("`", "")
        response_data["response"] = cleaned_term
        return response_data

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> Optional[ExpertModel]:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        return None
```

### `agents/worker.py`

```python
# path: ./agents/worker.py
# title: Stabilized External LLM Worker with Robust IPC
# description: プロセス間通信をより堅牢にするため、標準出力にバイナリデータを書き込む。

import sys
import os
import json
import traceback
import logging
import psutil
from llama_cpp import Llama
from dotenv import load_dotenv
from pathlib import Path

# (logging設定は変更なし)
# ...

def main() -> None:
    try:
        logging.info("--- Worker process started ---")
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # 標準入力をバイナリで読み取り、UTF-8でデコード
        input_bytes = sys.stdin.buffer.read()
        input_data = json.loads(input_bytes.decode('utf-8'))
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        logging.info("Successfully read from stdin.")

        model_path = input_data.get("model_path")
        messages = input_data.get("messages")
        chat_format = input_data.get("chat_format")
        
        if not all([model_path, messages, chat_format]):
            raise ValueError("入力データに必須キーが不足しています。")

        logging.info(f"Model path: {model_path}")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"モデルファイルが見つかりません: {model_path}")

        load_dotenv()
        
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
        is_apple_silicon = sys.platform == "darwin" and "arm64" in os.uname().machine
        n_gpu_layers = 0
        n_threads = psutil.cpu_count(logical=False)

        llm = Llama(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_threads=n_threads,
            n_ctx=4096,
            use_mmap=False,
            verbose=log_verbose,
            chat_format=chat_format
        )
        
        logging.info("Llama model initialized successfully.")
        
        output = llm.create_chat_completion(
            messages=messages,
            max_tokens=4096,
            temperature=0.7,
            stop=["<|im_end|>", "</s>", "<|endoftext|>"]
        )
        
        logging.info("Chat completion created successfully.")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # 結果をJSON文字列に変換し、UTF-8でエンコードして標準出力（バイナリモード）に書き込む
        output_str = json.dumps(output, ensure_ascii=False)
        sys.stdout.buffer.write(output_str.encode('utf-8'))
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        sys.stdout.flush()
        logging.info("--- Worker process finished successfully ---")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        error_info = {"error": str(e), "traceback": traceback.format_exc()}
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        error_str = json.dumps(error_info, ensure_ascii=False)
        sys.stdout.buffer.write(error_str.encode('utf-8'))
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        sys.stdout.flush()
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### `config/__init__.py`

```python
# /hybrid_llm_system/config/__init__.py
```

### `container/__init__.py`

```python
# /hybrid_llm_system/container/__init__.py
```

### `container/container.py`

```python
# path: ./container/container.py
# title: DI Container with Intelligent ToolRouterAgent
# description: Replaces the simple router with the ToolRouterAgent and injects it into the orchestrator for more intelligent task routing.

from dependency_injector import containers, providers
from domain.model_manager import ModelManager
from services.model_loader import ModelLoaderService
from services.vectorization_service import VectorizationService
from services.worker_manager import WorkerManagerService
from services.plan_evaluation_service import PlanEvaluationService
from services.performance_tracker_service import PerformanceTrackerService
from services.rag_manager_service import RAGManagerService
from services.web_browser_service import WebBrowserService
from services.wikipedia_service import WikipediaService
from services.tool_manager_service import ToolManagerService
from rag.retrievers import FaissRetriever
from orchestrator.hiple_orchestrator import HipleOrchestrator
from agents.tool_router_agent import ToolRouterAgent
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.consultant_agent import ConsultantAgent
from agents.wikipedia_agent import WikipediaAgent
from agents.web_browser_agent import WebBrowserAgent
from agents.rag_agent import RAGAgent
from agents.reviewer_agent import ReviewerAgent
from agents.critic_agent import CriticAgent
from agents.safety_director_agent import SafetyDirectorAgent
from agents.metacognition_agent import MetacognitionAgent
from agents.emergence_agent import EmergenceAgent
from domain.boundary_enforcer import BoundaryConditionEnforcer
from services.evolution_service import EvolutionService
from workspace.global_workspace import GlobalWorkspace
from utils.thought_logger import ThoughtLogger

class Container(containers.DeclarativeContainer):
    config_path = providers.Configuration()

    global_workspace = providers.Singleton(GlobalWorkspace)
    thought_logger = providers.Factory(ThoughtLogger)

    model_loader = providers.Singleton(ModelLoaderService)
    vectorization_service = providers.Singleton(VectorizationService)
    performance_tracker = providers.Singleton(PerformanceTrackerService)
    worker_manager = providers.Singleton(WorkerManagerService)
    web_browser_service = providers.Singleton(WebBrowserService)
    wikipedia_service = providers.Singleton(WikipediaService)
    plan_evaluation_service = providers.Singleton(PlanEvaluationService, vectorization_service=vectorization_service)
    faiss_retriever = providers.Factory(FaissRetriever, vectorization_service=vectorization_service)
    rag_manager = providers.Singleton(RAGManagerService, vectorization_service=vectorization_service)
    model_manager = providers.Singleton(ModelManager, config_path=config_path.model_config_path)
    
    tool_router_agent = providers.Factory(ToolRouterAgent, model_loader=model_loader)

    safety_director_agent = providers.Factory(SafetyDirectorAgent)
    metacognition_agent = providers.Factory(MetacognitionAgent)
    boundary_enforcer = providers.Singleton(BoundaryConditionEnforcer)
    evolution_service = providers.Factory(
        EvolutionService,
        performance_tracker=performance_tracker,
        boundary_enforcer=boundary_enforcer,
        all_experts=model_manager.provided.get_all_experts.call()
    )

    wikipedia_agent = providers.Factory(
        WikipediaAgent, 
        model_loader=model_loader, 
        wikipedia_service=wikipedia_service
    )
    web_browser_agent = providers.Factory(WebBrowserAgent, model_loader=model_loader)
    planner_agent = providers.Factory(PlannerAgent, model_loader=model_loader)
    critic_agent = providers.Factory(CriticAgent, model_loader=model_loader)
    consultant_agent = providers.Factory(ConsultantAgent, model_loader=model_loader)
    generator_agent = providers.Factory(GeneratorAgent, model_loader=model_loader, worker_manager=worker_manager, consultant_agent=consultant_agent)
    reporter_agent = providers.Factory(ReporterAgent, model_loader=model_loader)
    rag_agent = providers.Factory(RAGAgent, model_loader=model_loader)
    reviewer_agent = providers.Factory(ReviewerAgent, model_loader=model_loader)
    emergence_agent = providers.Factory(EmergenceAgent, model_loader=model_loader)
    
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    tool_manager = providers.Singleton(
        ToolManagerService,
        wikipedia_agent=wikipedia_agent,
        web_browser_agent=web_browser_agent,
        web_browser_service=web_browser_service,
    )

    hiple_orchestrator = providers.Factory(
        HipleOrchestrator,
        model_manager=model_manager,
        tool_router_agent=tool_router_agent,
        planner_agent=planner_agent,
        critic_agent=critic_agent,
        generator_agent=generator_agent,
        reporter_agent=reporter_agent,
        reviewer_agent=reviewer_agent,
        plan_evaluation_service=plan_evaluation_service,
        performance_tracker=performance_tracker,
        rag_agent=rag_agent,
        rag_manager=rag_manager,
        faiss_retriever=faiss_retriever,
        tool_manager=tool_manager,
        global_workspace=global_workspace,
        thought_logger=thought_logger,
        safety_director_agent=safety_director_agent,
        metacognition_agent=metacognition_agent,
        evolution_service=evolution_service,
        emergence_agent=emergence_agent
    )
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
```

### `domain/boundary_enforcer.py`

```python
# path: ./domain/boundary_enforcer.py
# title: Boundary Condition Enforcer
# description: Enforces safety constraints on the self-evolution process.

from typing import Dict, Any, Tuple, List

class BoundaryConditionEnforcer:
    """
    自己進化プロセスが安全な境界内で行われることを保証するクラス。
    """
    def __init__(self):
        # システムの機能に不可欠な、無効化してはならないエキスパートのリスト
        self.protected_experts: List[str] = ["hrm", "reporter", "greeter"]

    def validate_evolution(self, proposed_change: Dict[str, Any]) -> Tuple[bool, str]:
        """
        提案された構成変更を検証する。

        Args:
            proposed_change (Dict[str, Any]): e.g., {"action": "disable", "expert_name": "Jamba"}

        Returns:
            Tuple[bool, str]: (検証が通ったか, メッセージ)
        """
        action = proposed_change.get("action")
        expert_name = proposed_change.get("expert_name")

        if not action or not expert_name:
            return False, "Invalid change proposal: 'action' and 'expert_name' are required."

        if action == "disable":
            if expert_name.lower() in self.protected_experts:
                return False, f"Validation failed: Core expert '{expert_name}' cannot be disabled."

        # 今後、コストや速度スコアの急激な変更を制限するルールなどを追加できる
        
        return True, "Proposed change is within safe boundaries."

```

### `domain/evaluation.py`

```python
# path: ./domain/evaluation.py
# title: Expert Performance Metrics Schema (Improved)
# description: Defines the data structure for tracking AI expert performance with more accurate time logging.

from dataclasses import dataclass, field

@dataclass
class PerformanceMetrics:
    """
    エキスパートのパフォーマンス指標を記録するデータクラス
    """
    success_count: int = 0
    failure_count: int = 0
    total_execution_time_on_success: float = 0.0
    total_execution_time_all: float = 0.0
    score: float = 0.0

    @property
    def total_runs(self) -> int:
        return self.success_count + self.failure_count

    @property
    def success_rate(self) -> float:
        if self.total_runs == 0:
            return 0.0
        return self.success_count / self.total_runs

    @property
    def average_execution_time(self) -> float:
        """全実行（成功・失敗問わず）の平均時間"""
        if self.total_runs == 0:
            return 0.0
        return self.total_execution_time_all / self.total_runs

```

### `domain/model_manager.py`

```python
# path: ./domain/model_manager.py
# title: ModelManager with Dynamic Model Assignment (Cost/Speed Aware)
# description: .envとmodels.ymlからエキスパートを動的に読み込む際に、コストと速度のスコアも反映させる。

import os
import yaml
from typing import Dict, List, Optional
from dotenv import load_dotenv
from .schemas import ExpertModel

class ModelManager:
    """
    models.ymlからエキスパートモデルの定義を読み込み、.envの指定に基づいて動的に割り当てるクラス
    """
    def __init__(self, config_path: str):
        load_dotenv()
        self.experts: Dict[str, ExpertModel] = self._load_experts_from_config(config_path)

    def _load_experts_from_config(self, config_path: str) -> Dict[str, ExpertModel]:
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"モデル設定ファイルが見つかりません: {config_path}")
        except Exception as e:
            raise RuntimeError(f"モデル設定ファイルの読み込みに失敗しました: {e}")

        all_definitions = config.get("worker_experts", {})
        
        expert_mapping_str = os.getenv("EXPERT_MAPPING")
        if not expert_mapping_str:
            raise ValueError(".envファイルにEXPERT_MAPPINGが設定されていません。")

        try:
            expert_mapping = dict(item.strip().split(':') for item in expert_mapping_str.split(','))
        except ValueError:
            raise ValueError("EXPERT_MAPPINGの形式が正しくありません。'type:definition, type:definition'の形式で記述してください。")

        loaded_experts: Dict[str, ExpertModel] = {}

        for expert_type, definition_key in expert_mapping.items():
            settings = all_definitions.get(definition_key)

            if not settings:
                print(f"⚠️ 警告: EXPERT_MAPPINGで指定された '{definition_key}' の定義がmodels.ymlに見つかりません。")
                continue

            if not settings.get("enabled", False):
                print(f"ℹ️ エキスパート '{definition_key}' は設定で無効化されています。スキップします。")
                continue
            
            is_diffusion_model = settings.get("chat_format") == "diffusion"
            model_path: Optional[str] = None
            model_id: Optional[str] = None

            if is_diffusion_model:
                model_id = settings.get("model_id")
            else:
                model_env_key = settings.get("model_env_key")
                if model_env_key:
                    model_path = os.getenv(model_env_key)
                
                if not model_path:
                    print(f"⚠️ 警告: エキスパート '{settings.get('name', definition_key)}' のモデルパス (環境変数: {model_env_key}) が見つかりません。スキップします。")
                    continue
            
            expert_name = settings.get("name", expert_type)
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            loaded_experts[expert_name.lower()] = ExpertModel(
                name=expert_name,
                description=settings.get("description", ""),
                model_path=model_path,
                model_id=model_id,
                chat_format=settings.get("chat_format", "default"),
                system_prompt=settings.get("system_prompt", ""),
                execution_strategy=settings.get("execution_strategy", "inline"),
                keywords=settings.get("keywords", []),
                cost_score=settings.get("cost_score", 5),
                speed_score=settings.get("speed_score", 5),
                enabled=True
            )
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        if not loaded_experts:
            raise ValueError("有効なエキスパートが一人も設定されていません。.envとmodels.ymlを確認してください。")
            
        return loaded_experts

    def get_expert(self, name: str) -> Optional[ExpertModel]:
        return self.experts.get(name.lower())

    def get_all_experts(self) -> List[ExpertModel]:
        return list(self.experts.values())
```

### `domain/schemas.py`

```python
# path: ./domain/schemas.py
# title: Data Schemas with Self-Evaluation Field
# description: SubTaskに自己評価（自信度と理由）を記録するフィールドを追加。

from dataclasses import dataclass, field
from typing import List, Optional, Any, Union, Dict, TYPE_CHECKING
from llama_cpp import Llama
import numpy as np

if TYPE_CHECKING:
    from diffusers import DiffusionPipeline

@dataclass
class ExpertModel:
    """
    各エキスパートモデルの設定と状態を管理するデータクラス
    """
    name: str
    description: str
    model_path: Optional[str]
    model_id: Optional[str]
    chat_format: str
    system_prompt: str
    execution_strategy: str = "inline" # "inline" or "worker"
    enabled: bool = False
    keywords: List[str] = field(default_factory=list)
    cost_score: int = 5  # コスト評価 (1: low, 10: high)
    speed_score: int = 5 # 速度評価 (1: slow, 10: fast)
    instance: Optional[Union[Llama, "DiffusionPipeline"]] = None
    is_loaded: bool = False

@dataclass
class SubTask:
    """
    分解されたサブタスクを管理するデータクラス
    """
    task_id: int
    description: str
    expert_name: str
    ssv_description: str # 意味構造を記述した短いテキスト
    consultation_experts: List[str] = field(default_factory=list) # 相談相手のエキスパート名リスト
    reviewer_expert: Optional[str] = None # レビュー担当のエキスパート名
    feedback_history: List[Dict[str, str]] = field(default_factory=list) # レビューと修正の履歴
    dependencies: List[int] = field(default_factory=list)
    result: Optional[str] = None
    status: str = "pending"
    milestone_id: Optional[int] = None
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    self_evaluation: Optional[Dict[str, Any]] = None # 自己評価（自信度、理由など）
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️


@dataclass
class Milestone:
    """
    L2: 主要なマイルストーン（中間目標）を管理するデータクラス
    """
    milestone_id: int
    title: str
    description: str

@dataclass
class Plan:
    """
    実行計画全体を管理するデータクラス
    階層的な情報（L1, L2）と具体的なタスク（L3）を保持する
    """
    original_prompt: str
    overall_goal: str
    milestones: List[Milestone] = field(default_factory=list)
    tasks: List[SubTask] = field(default_factory=list)

```

### `enhanced_python_analyzer.py`

```python
# all_python_tools/enhanced_python_analyzer.py
# title: Enhanced Python Project Structure Aggregator
# role: Aggregates Python project structure with additional analysis for AI comprehension

import os
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Optional, Union, Tuple, Any, cast

def get_project_tree(start_path: Union[str, Path], ignore_dirs: Set[str], indent: str = '') -> str:
    """
    Generates a tree-like string representation of the project structure.
    プロジェクト構造のツリー状の文字列表現を生成します。
    """
    tree_str = ''
    try:
        items = sorted(list(Path(start_path).iterdir()))
    except FileNotFoundError:
        return ""
    valid_items = [item for item in items if item.name not in ignore_dirs]
    
    for i, item in enumerate(valid_items):
        is_last = (i == len(valid_items) - 1)
        tree_str += indent
        if is_last:
            tree_str += '└── '
            next_indent = indent + '    '
        else:
            tree_str += '├── '
            next_indent = indent + '│   '
            
        if item.is_file() and item.suffix == '.py':
            try:
                size = item.stat().st_size
                tree_str += f"{item.name} ({size} bytes)\n"
            except FileNotFoundError:
                tree_str += f"{item.name} (file not found)\n"
        else:
            tree_str += item.name + '\n'
            
        if item.is_dir():
            tree_str += get_project_tree(item, ignore_dirs, next_indent)
    return tree_str

class CustomASTVisitor(ast.NodeVisitor):
    """
    A custom AST visitor to collect detailed information from Python code.
    Pythonコードから詳細な情報を収集するためのカスタムASTビジターです。
    """
    def __init__(self):
        self.imports: List[str] = []
        self.from_imports: List[str] = []
        self.functions: List[str] = []
        self.classes: List[str] = []
        self.constants: List[str] = []
        self.di_container_instantiations: List[str] = []
        self.di_registrations: List[str] = []
        self.injected_dependencies: List[str] = []
        self.langchain_components: List[str] = []

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        module = node.module or ''
        for alias in node.names:
            self.from_imports.append(f"{module}.{alias.name}")
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.classes.append(node.name)
        # Check for constructor injection patterns
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name == '__init__':
                for arg in item.args.args:
                    if arg.arg != 'self':
                        self.injected_dependencies.append(f"{node.name}.__init__({arg.arg})")
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id.isupper():
                self.constants.append(target.id)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        # Detect DI Container instantiations (e.g., Container(), Dependant())
        if isinstance(node.func, ast.Name) and node.func.id in ['Container', 'Provider', 'Dependant', 'Injector']:
            self.di_container_instantiations.append(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            # Detect DI Container registrations (e.g., container.register(), builder.build())
            if node.func.attr in ['register', 'bind', 'provide', 'factory', 'singleton', 'instance', 'build']:
                if isinstance(node.func.value, ast.Name):
                    self.di_registrations.append(f"{node.func.value.id}.{node.func.attr}")
                elif isinstance(node.func.value, ast.Call) and isinstance(node.func.value.func, ast.Name) and node.func.value.func.id == 'Container':
                    self.di_registrations.append(f"Container().{node.func.attr}")
            
            # Detect LangChain component instantiations (common classes)
            langchain_components = [
                'ChatOpenAI', 'OpenAI', 'HuggingFaceHub', 'LlamaCpp', # LLMs
                'PromptTemplate', 'ChatPromptTemplate', # Prompts
                'LLMChain', 'SimpleSequentialChain', 'ConversationalRetrievalChain', # Chains
                'AgentExecutor', 'initialize_agent', # Agents
                'Tool', 'create_tool_calling_agent', # Tools
                'VectorStoreRetriever', 'Chroma', 'FAISS', # Retrievers/Vector Stores
                'RunnableSequence', 'RunnableParallel' # LCEL
            ]
            if node.func.attr in langchain_components:
                if isinstance(node.func.value, ast.Name):
                    # e.g., from langchain.llms import OpenAI; llm = OpenAI()
                    self.langchain_components.append(node.func.attr)
                elif isinstance(node.func.value, ast.Attribute) and node.func.value.attr in ['llms', 'chains', 'agents', 'tools', 'prompts', 'retrievers', 'vectorstores', 'runnables']:
                    # e.g., llm = langchain.llms.OpenAI()
                    self.langchain_components.append(node.func.attr)
        self.generic_visit(node)

    def visit_Decorator(self, node: ast.expr) -> None:
        # Detect @inject decorator (e.g., dependency-injector)
        if isinstance(node, ast.Name) and node.id == 'inject':
            # This decorator usually applies to functions or methods
            # Note: ast.NodeVisitor does not have a 'parent' attribute by default.
            # This part would require a custom AST walker that tracks parents,
            # or a different approach if direct parent access is needed.
            # For simplicity, we'll just note the decorator's presence.
            pass # We handle decorators on FunctionDef/ClassDef directly by checking node.decorator_list
        self.generic_visit(node)

def extract_module_details(file_path: Path) -> Dict[str, Any]:
    """
    Extract imports, function definitions, class definitions, constants,
    DI container related patterns, and LangChain component usage from a Python file.
    Pythonファイルからインポート、関数定義、クラス定義、定数、
    DIコンテナ関連パターン、LangChainコンポーネントの使用状況を抽出します。
    """
    result: Dict[str, Any] = {
        'imports': [],
        'from_imports': [],
        'functions': [],
        'classes': [],
        'constants': [],
        'di_container_instantiations': [],
        'di_registrations': [],
        'injected_dependencies': [],
        'langchain_components': [],
        'parse_error': None
    }
    
    try:
        content = file_path.read_text(encoding='utf-8')
        tree = ast.parse(content)
        
        visitor = CustomASTVisitor()
        visitor.visit(tree)

        result['imports'] = visitor.imports
        result['from_imports'] = visitor.from_imports
        result['functions'] = visitor.functions
        result['classes'] = visitor.classes
        result['constants'] = visitor.constants
        result['di_container_instantiations'] = visitor.di_container_instantiations
        result['di_registrations'] = visitor.di_registrations
        result['injected_dependencies'] = visitor.injected_dependencies
        result['langchain_components'] = visitor.langchain_components

        # Additional check for @inject decorators on functions/classes
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                for decorator in node.decorator_list:
                    if isinstance(decorator, ast.Name) and decorator.id == 'inject':
                        result['injected_dependencies'].append(f"@{decorator.id} applied to {node.name}")
                    elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name) and decorator.func.id == 'inject':
                        result['injected_dependencies'].append(f"@{decorator.func.id} applied to {node.name}")

    except Exception as e:
        result['parse_error'] = str(e)
    
    return result

def analyze_module_dependencies(project_path: Path, ignore_dirs: Set[str]) -> Dict[str, List[str]]:
    """
    Analyze dependencies between modules within the project.
    プロジェクト内のモジュール間の依存関係を分析します。
    """
    dependencies: Dict[str, List[str]] = defaultdict(list)
    all_modules: Set[str] = set()
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith('.py'):
                file_path = Path(root) / file
                relative_path = file_path.relative_to(project_path)
                module_name = str(relative_path.with_suffix('')).replace(os.sep, '.')
                all_modules.add(module_name)
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith('.py'):
                file_path = Path(root) / file
                relative_path = file_path.relative_to(project_path)
                current_module = str(relative_path.with_suffix('')).replace(os.sep, '.')
                
                analysis = extract_module_details(file_path)
                imports_to_check: List[str] = (analysis['imports'] if 'imports' in analysis else []) + \
                                             (analysis['from_imports'] if 'from_imports' in analysis else [])
                
                for imp in imports_to_check:
                    if isinstance(imp, str):
                        for module in all_modules:
                            # Check if the import starts with a project module or is a sub-module
                            # インポートがプロジェクトモジュールで始まるか、サブモジュールであるかを確認します。
                            if imp == module or imp.startswith(f"{module}.") or module.startswith(f"{imp}."):
                                dependencies[current_module].append(imp)
                                break
    
    return dependencies

def get_project_summary(project_path: Path, ignore_dirs: Set[str]) -> Dict[str, Any]:
    """
    Generate a high-level summary of the project.
    プロジェクトの概要を生成します。
    """
    summary: Dict[str, Any] = {
        'total_py_files': 0,
        'total_lines': 0,
        'main_modules': [],
        'test_files': [],
        'config_files': [],
        'largest_files': [],
        'module_test_associations': defaultdict(list)
    }
    
    file_sizes: List[Tuple[str, int]] = []
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            file_path = Path(root) / file
            
            if not file_path.exists():
                continue

            relative_path = file_path.relative_to(project_path)
            
            if file.endswith('.py'):
                summary['total_py_files'] += 1
                size = file_path.stat().st_size
                file_sizes.append((str(relative_path), size))
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = len(f.readlines())
                        summary['total_lines'] += lines
                except Exception:
                    pass
                
                if 'test' in file.lower() or 'test' in str(relative_path).lower():
                    summary['test_files'].append(str(relative_path))
                    # Attempt to associate test file with a module
                    # テストファイルをモジュールに関連付けようと試みます。
                    # Basic heuristic: if test_module.py exists, look for module.py or module/
                    # 基本的なヒューリスティック: test_module.py が存在する場合、module.py または module/ を探します。
                    module_name_guess = file.lower().replace('test_', '').replace('_test', '').replace('.py', '')
                    if module_name_guess and module_name_guess != file.lower().replace('.py', ''):
                        potential_module_path = file_path.parent / f"{module_name_guess}.py"
                        if potential_module_path.exists():
                            summary['module_test_associations'][str(potential_module_path.relative_to(project_path))].append(str(relative_path))
                        else:
                            # Check for module in parent directory (e.g., tests/module/test_module.py)
                            # 親ディレクトリ内のモジュールを確認します (例: tests/module/test_module.py)。
                            potential_module_dir = file_path.parent / module_name_guess
                            if potential_module_dir.is_dir():
                                summary['module_test_associations'][str(potential_module_dir.relative_to(project_path))].append(str(relative_path))

                elif file in ['main.py', 'app.py', '__main__.py', 'run.py']:
                    summary['main_modules'].append(str(relative_path))
            elif file.endswith(('.ini', '.cfg', '.conf', '.yaml', '.yml', '.json', '.toml', '.env')): # Added .env
                summary['config_files'].append(str(relative_path))
    
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    summary['largest_files'] = file_sizes[:5]
    
    return summary

def aggregate_enhanced_project_structure(project_path: str, output_file: str, ignore_dirs: Optional[Set[str]] = None, ignore_files: Optional[Set[str]] = None, include_analysis: bool = True):
    """
    Enhanced aggregation with dependency analysis and project summary.
    依存関係分析とプロジェクト概要を含む強化された集約。
    """
    if ignore_dirs is None:
        ignore_dirs = {'.git', '__pycache__', 'venv', '.venv', 'node_modules', 'dist', 'build', '.pytest_cache'}
    if ignore_files is None:
        ignore_files = {'.DS_Store'}

    project_path_obj = Path(project_path)
    output_path = Path(output_file)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Project Analysis: {project_path_obj.name}\n\n")
        
        if include_analysis:
            summary = get_project_summary(project_path_obj, ignore_dirs)
            f.write("## Project Summary\n\n")
            f.write(f"- **Total Python files**: {summary['total_py_files']}\n")
            f.write(f"- **Total lines of code**: {summary['total_lines']:,}\n")
            f.write(f"- **Main modules**: {', '.join(summary['main_modules']) if summary['main_modules'] else 'None detected'}\n")
            f.write(f"- **Test files**: {len(summary['test_files'])}\n")
            f.write(f"- **Config files**: {len(summary['config_files'])}\n\n")
            
            if summary['largest_files']:
                f.write("### Largest Files\n")
                for file_p, size in summary['largest_files']:
                    f.write(f"- `{file_p}`: {size:,} bytes\n")
                f.write("\n")

            if summary['module_test_associations']:
                f.write("### Module to Test File Associations\n")
                for module, tests in summary['module_test_associations'].items():
                    f.write(f"- `{module}` is tested by: {', '.join(tests)}\n")
                f.write("\n")


        f.write("## 1. Project Directory Structure\n\n")
        f.write("```\n")
        tree_view = get_project_tree(project_path_obj, ignore_dirs)
        f.write(f"{project_path_obj.name}\n{tree_view}")
        f.write("```\n\n")
        
        f.write("## 2. Dependencies\n\n")
        dependency_files = ['requirements.txt', 'pyproject.toml', 'setup.py', 'Pipfile', 'environment.yml']
        found_deps = False
        for dep_file in dependency_files:
            dep_path = project_path_obj / dep_file
            if dep_path.is_file():
                found_deps = True
                f.write(f"### `{dep_file}`\n\n")
                f.write("```\n")
                f.write(dep_path.read_text(encoding='utf-8'))
                f.write("\n```\n\n")
        if not found_deps:
            f.write("No dependency files found.\n\n")

        if include_analysis:
            f.write("## 3. Internal Module Dependencies\n\n")
            dependencies = analyze_module_dependencies(project_path_obj, ignore_dirs)
            if dependencies:
                for module, deps in sorted(dependencies.items()):
                    if deps:
                        f.write(f"### `{module}`\n")
                        f.write("Dependencies:\n")
                        for dep in sorted(list(set(deps))):
                            f.write(f"- {dep}\n")
                        f.write("\n")
            else:
                f.write("No internal dependencies detected.\n\n")
            
            # --- New Sections for DI/LangChain Analysis ---
            f.write("## 4. DI Container and LangChain Analysis Overview\n\n")
            py_files = sorted(project_path_obj.rglob('*.py'))
            
            di_analysis_found = False
            langchain_analysis_found = False

            for file_path in py_files:
                if not any(part in ignore_dirs for part in file_path.parts):
                    relative_path = file_path.relative_to(project_path_obj)
                    analysis = extract_module_details(file_path)
                    
                    if analysis['parse_error']:
                        f.write(f"### `{relative_path}`\n")
                        f.write(f"⚠️ Parse error: {analysis['parse_error']}\n\n")
                        continue
                    
                    if analysis['di_container_instantiations'] or \
                       analysis['di_registrations'] or \
                       analysis['injected_dependencies']:
                        di_analysis_found = True
                        f.write(f"### `{relative_path}` (DI Container Analysis)\n")
                        if analysis['di_container_instantiations']:
                            f.write(f"**DI Container Instantiations**: {', '.join(analysis['di_container_instantiations'])}\n")
                        if analysis['di_registrations']:
                            f.write(f"**DI Registrations/Bindings**: {', '.join(analysis['di_registrations'])}\n")
                        if analysis['injected_dependencies']:
                            f.write(f"**Injected Dependencies**: {', '.join(analysis['injected_dependencies'])}\n")
                        f.write("\n")
                    
                    if analysis['langchain_components']:
                        langchain_analysis_found = True
                        f.write(f"### `{relative_path}` (LangChain Analysis)\n")
                        f.write(f"**LangChain Components Used**: {', '.join(sorted(list(set(analysis['langchain_components']))))}\n")
                        f.write("\n")
            
            if not di_analysis_found:
                f.write("No explicit DI Container patterns detected.\n\n")
            if not langchain_analysis_found:
                f.write("No explicit LangChain components detected.\n\n")

            f.write("## 5. File Analysis Overview\n\n") # Renumbered from 4 to 5
            py_files = sorted(project_path_obj.rglob('*.py'))
            for file_path in py_files:
                if not any(part in ignore_dirs for part in file_path.parts):
                    relative_path = file_path.relative_to(project_path_obj)
                    analysis = extract_module_details(file_path) # Changed to extract_module_details
                    
                    f.write(f"### `{relative_path}`\n")
                    if analysis['parse_error']:
                        f.write(f"⚠️ Parse error: {analysis['parse_error']}\n\n")
                        continue
                        
                    if analysis['classes']:
                        f.write(f"**Classes**: {', '.join(analysis['classes'])}\n")
                    if analysis['functions']:
                        f.write(f"**Functions**: {', '.join(analysis['functions'])}\n")
                    all_imports: List[str] = (analysis['imports'] if 'imports' in analysis else []) + \
                                             (analysis['from_imports'] if 'from_imports' in analysis else [])
                    external_imports = [imp for imp in all_imports if isinstance(imp, str) and not imp.startswith('.')]
                    if external_imports:
                        f.write(f"**External imports**: {', '.join(sorted(list(set(external_imports))))}\n")
                    if analysis['constants']:
                        f.write(f"**Constants**: {', '.join(analysis['constants'])}\n")
                    f.write("\n")
            # --- End of New Sections ---

        f.write("## 6. Source Code\n\n") # Renumbered from 5 to 6
        py_files = sorted(project_path_obj.rglob('*.py'))
        for file_path in py_files:
            if not any(part in ignore_dirs for part in file_path.parts) and file_path.name not in (ignore_files or set()):
                relative_path = file_path.relative_to(project_path_obj)
                
                f.write(f"### `{relative_path}`\n\n")
                f.write("```python\n")
                try:
                    content = file_path.read_text(encoding='utf-8')
                    f.write(content)
                except Exception as e:
                    f.write(f"# Error reading file: {e}")
                f.write("\n```\n\n")

    print(f"✅ Enhanced project structure aggregated into: {output_file}")


if __name__ == '__main__':
    PROJECT_DIRECTORY = '.'
    OUTPUT_MARKDOWN_FILE = 'enhanced_project_structure.md'
    INCLUDE_ANALYSIS = True

    aggregate_enhanced_project_structure(
        PROJECT_DIRECTORY, 
        OUTPUT_MARKDOWN_FILE,
        include_analysis=INCLUDE_ANALYSIS
    )

```

### `hrm_test.py`

```python
# /hybrid_llm_system/hrm_test.py
# HRMモデルの動作を最小構成でテストするためのスクリプト (診断機能付き)

import sys
import os
import traceback
import psutil
from llama_cpp import Llama
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from utils.monitoring import print_memory_usage

def main() -> None:
    """
    HRMモデルの最小環境テストを実行するメイン関数
    """
    print("--- HRMモデルの最小環境テストを開始します ---")
    print_memory_usage("START")
    
    model_path: Optional[str] = None
    try:
        load_dotenv()
        model_path = os.getenv("HRM_MODEL_PATH")

        if not model_path:
            print("❌ エラー: .envファイルにHRM_MODEL_PATHが設定されていません。")
            return
            
        if not os.path.exists(model_path):
            print(f"❌ エラー: モデルファイルが見つかりません。パスを確認してください: {model_path}")
            return

        print(f"モデルパス: {model_path}")
        print_memory_usage("BEFORE_LOAD")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
        is_apple_silicon = sys.platform == "darwin" and "arm64" in os.uname().machine
        n_gpu_layers = -1 if is_apple_silicon else 0
        n_threads = psutil.cpu_count(logical=False)
        
        llm = Llama(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_threads=n_threads,
            use_mmap=False,
            n_ctx=4096,
            verbose=log_verbose,
            chat_format="chatml"
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        print_memory_usage("AFTER_LOAD")
        print("✅ モデルの初期化に成功しました。")

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": "You are a logical reasoner. Think step by step to solve the problem."},
            {"role": "user", "content": "There are three suspects, A, B, and C. A says 'B is the culprit.' B says 'C is the culprit.' C says 'I am not the culprit.' Only one person is telling the truth, and there is only one culprit. Who is the culprit? Please explain your reasoning step by step."}
        ]

        print("\n--- 応答を生成します... ---")
        
        response: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=1024,
            temperature=0.2
        )
        
        print("\n--- 応答の生成に成功しました！ ---")

        if "choices" in response and response["choices"]:
            choice = response["choices"][0]
            if "message" in choice and "content" in choice["message"]:
                content: Optional[str] = choice["message"]["content"]
                if content is not None:
                    print("\n[モデルからの応答]")
                    print(content.strip())
                else:
                    print("応答メッセージにテキストが含まれていません。")
            else:
                print("応答メッセージの形式が正しくありません。")
        else:
            print("応答内容が空か、予期しない形式です。")
            print(f"受信したデータ: {response}")

    except Exception as e:
        print(f"\n❌ テスト中に予期せぬエラーが発生しました: {e}")
        traceback.print_exc()

    print("\n--- テストを終了します ---")
    print_memory_usage("END")

if __name__ == "__main__":
    main()
```

### `jamba_test.py`

```python
# /hybrid_llm_system/jamba_test.py
# Jambaモデルの動作を最小構成でテストするためのスクリプト (最終安定化版)

import sys
import os
import traceback
import psutil
from llama_cpp import Llama
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from utils.monitoring import print_memory_usage

def main() -> None:
    """
    Jambaモデルの最小環境テストを実行するメイン関数
    """
    print("--- Jambaモデルの最小環境テストを開始します ---")
    print_memory_usage("START")
    
    model_path: Optional[str] = None
    try:
        load_dotenv()
        model_path = os.getenv("JAMBA_MODEL_PATH")

        if not model_path:
            print("❌ エラー: .envファイルにJAMBA_MODEL_PATHが設定されていません。")
            return

        if not os.path.exists(model_path):
            print(f"❌ エラー: モデルファイルが見つかりません。パスを確認してください: {model_path}")
            return

        print(f"モデルパス: {model_path}")
        print_memory_usage("BEFORE_LOAD")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
        n_gpu_layers = 0
        n_threads = psutil.cpu_count(logical=False)
        
        llm = Llama(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_threads=n_threads,
            n_ctx=4096,
            use_mmap=False,
            verbose=log_verbose,
            chat_format="chatml"
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        print_memory_usage("AFTER_LOAD")
        print("✅ モデルの初期化に成功しました。")

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": "あなたは、誠実で優秀なAIアシスタントです。"},
            {"role": "user", "content": "こんにちは"}
        ]

        print("\n--- 応答を生成します... ---")
        
        response: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=256,
            temperature=0.7
        )
        
        print("\n--- 応答の生成に成功しました！ ---")

        if "choices" in response and response["choices"]:
            choice = response["choices"][0]
            if "message" in choice and "content" in choice["message"]:
                content: Optional[str] = choice["message"]["content"]
                if content is not None:
                    print("\n[モデルからの応答]")
                    print(content.strip())
                else:
                    print("応答メッセージにテキストが含まれていません。")
            else:
                print("応答メッセージの形式が正しくありません。")
        else:
            print("応答内容が空か、予期しない形式です。")
            print(f"受信したデータ: {response}")

    except Exception as e:
        print(f"\n❌ テスト中に予期せぬエラーが発生しました: {e}")
        traceback.print_exc()

    print("\n--- テストを終了します ---")
    print_memory_usage("END")

if __name__ == "__main__":
    main()
```

### `liquids4_test.py`

```python
# /hybrid_llm_system/liquids4_test.py
# LiquidS4モデルの動作を最小構成でテストするためのスクリプト (mypy対応版)

import sys
import os
from llama_cpp import Llama
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage # 追加

def main() -> None:
    """
    LiquidS4モデルの最小環境テストを実行するメイン関数
    """
    print("--- LiquidS4モデルの最小環境テストを開始します ---")
    
    model_path: Optional[str] = None
    try:
        # .envファイルから環境変数を読み込み
        load_dotenv()
        model_path = os.getenv("LIQUIDS4_MODEL_PATH")

        if not model_path:
            print("🟡 テストをスキップ: .envファイルにLIQUIDS4_MODEL_PATHが設定されていません。")
            return
            
        if not os.path.exists(model_path):
            print(f"❌ エラー: モデルファイルが見つかりません。パスを確認してください: {model_path}")
            return

        print(f"モデルパス: {model_path}")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")

        # モデルの初期化 (llama-2フォーマット)
        llm = Llama(
            model_path=model_path,
            n_ctx=8192,
            n_gpu_layers=-1,
            verbose=log_verbose,
            chat_format="llama-2"
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        print("✅ モデルの初期化に成功しました。")
        
        # チャット形式のプロンプトを作成
        long_text = """
        Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by humans and other animals. 
        Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. 
        Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".
        As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. 
        For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology.
        """
        messages: List[ChatCompletionRequestMessage] = [ # 型を修正
            {"role": "system", "content": "You are an expert in summarizing and analyzing long texts. Provide a clear, concise, and logical summary."},
            {"role": "user", "content": f"Please summarize the following text:\n\n{long_text}"}
        ]
        
        print("\n--- 応答を生成します... ---")
        
        # チャット補完APIを呼び出し
        response: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=512,
            temperature=0.2
        )
        
        print("\n--- 応答の生成に成功しました！ ---")

        if "choices" in response and response["choices"]:
            choice = response["choices"][0]
            if "message" in choice and "content" in choice["message"]:
                content: Optional[str] = choice["message"]["content"]
                if content is not None:
                    print("\n[モデルからの応答]")
                    print(content.strip())
                else:
                    print("応答メッセージにテキストが含まれていません。")
            else:
                print("応答メッセージの形式が正しくありません。")
        else:
            print("応答内容が空か、予期しない形式です。")
            print(f"受信したデータ: {response}")

    except Exception as e:
        print(f"\n❌ テスト中に予期せぬエラーが発生しました: {e}")

    print("\n--- テストを終了します ---")

if __name__ == "__main__":
    main()
```

### `main.py`

```python
# path: ./main.py
# title: Main Entry Point for HiPLE System
# description: HiPLEシステムを起動するメインファイル。非同期処理のエラーを修正し、同期的な対話ループを実装。

import readline
import sys
import os
from container.container import Container
from orchestrator.hiple_orchestrator import HipleOrchestrator
from utils.monitoring import print_memory_usage

# huggingface/tokenizers の警告を抑制し、デッドロックのリスクを低減
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def main() -> None:
    """
    メイン関数
    """
    print("--- HiPLE (Hierarchical Predictive Language Engine) を初期化しています ---")
    print_memory_usage("INITIALIZING")
    try:
        container = Container()
        container.config_path.from_dict({
            'model_config_path': './config/models.yml'
        })
        
        orchestrator: HipleOrchestrator = container.hiple_orchestrator()

    except Exception as e:
        print(f"❌ エラー: 初期化に失敗しました。 - {e}")
        import traceback
        traceback.print_exc()
        print("設定ファイル(models.yml, .env)やモデルのパスを確認してください。")
        return

    print("--- 初期化が完了しました ---")
    print("対話を開始します。終了するには 'exit' または 'quit' と入力してください。")

    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    # 非同期処理をやめ、同期的ながら無限ループで対話を受け付ける
    while True:
        try:
            question: str = input("> ")

            if question.lower() in ["exit", "quit"]:
                print("システムを終了します。")
                break

            if not question.strip():
                continue

            print("\n--- 思考中... ---")
            # awaitを削除し、同期的にメソッドを呼び出す
            response: str = orchestrator.process_task(question)
            print("\n--- 回答 ---")
            print(response)
            print("\n")

        except KeyboardInterrupt:
            print("\nシステムを終了します。")
            break
        except Exception as e:
            print(f"致命的なエラーが発生しました: {e}")
            import traceback
            traceback.print_exc()
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

if __name__ == "__main__":
    main()

```

### `orchestrator/__init__.py`

```python
# /hybrid_llm_system/orchestrator/__init__.py
```

### `orchestrator/hiple_orchestrator.py`

```python
# path: ./orchestrator/hiple_orchestrator.py
# title: Orchestrator with Emergence Task Handling
# description: Integrates the EmergenceAgent to handle creative brainstorming tasks.

import time
import traceback
from typing import Dict, List, Tuple, Any, Optional, cast
from bs4 import BeautifulSoup

from domain.model_manager import ModelManager
from domain.schemas import SubTask, Plan, ExpertModel, Milestone
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.critic_agent import CriticAgent
from agents.rag_agent import RAGAgent
from agents.reviewer_agent import ReviewerAgent
from agents.safety_director_agent import SafetyDirectorAgent
from agents.metacognition_agent import MetacognitionAgent
from agents.emergence_agent import EmergenceAgent
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
# from agents.web_browser_agent import WebBrowserAgent # 不要
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from services.evolution_service import EvolutionService
from services.rag_manager_service import RAGManagerService
from services.plan_evaluation_service import PlanEvaluationService
from services.performance_tracker_service import PerformanceTrackerService
from services.tool_manager_service import ToolManagerService
from rag.retrievers import BaseRetriever
from rag.data_sources import PlanDataSource, Document
from workspace.global_workspace import GlobalWorkspace
from utils.thought_logger import ThoughtLogger
from agents.tool_router_agent import ToolRouterAgent

class HipleOrchestrator:
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    def __init__(
        self,
        model_manager: ModelManager,
        tool_router_agent: ToolRouterAgent,
        planner_agent: PlannerAgent,
        generator_agent: GeneratorAgent,
        reporter_agent: ReporterAgent,
        reviewer_agent: ReviewerAgent,
        plan_evaluation_service: PlanEvaluationService,
        performance_tracker: PerformanceTrackerService,
        rag_agent: RAGAgent,
        rag_manager: RAGManagerService,
        faiss_retriever: BaseRetriever,
        critic_agent: CriticAgent,
        tool_manager: ToolManagerService,
        global_workspace: GlobalWorkspace,
        thought_logger: ThoughtLogger,
        safety_director_agent: SafetyDirectorAgent,
        metacognition_agent: MetacognitionAgent,
        evolution_service: EvolutionService,
        emergence_agent: EmergenceAgent
    ):
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        self.model_manager = model_manager
        self.tool_router_agent = tool_router_agent
        self.planner_agent = planner_agent
        self.generator_agent = generator_agent
        self.reporter_agent = reporter_agent
        self.reviewer_agent = reviewer_agent
        self.plan_evaluation_service = plan_evaluation_service
        self.performance_tracker = performance_tracker
        self.rag_agent = rag_agent
        self.rag_manager = rag_manager
        self.rag_manager.register_retriever("plan_retriever", faiss_retriever)
        self.critic_agent = critic_agent
        self.tool_manager = tool_manager
        self.workspace = global_workspace
        self.thought_logger = thought_logger
        self.safety_director = safety_director_agent
        self.metacognition = metacognition_agent
        self.evolution_service = evolution_service
        self.emergence_agent = emergence_agent
        self.task_counter_for_evolution = 0
        self.evolution_check_interval = 3 # 3回の複雑なタスクごとに進化サイクルを実行
        self.max_replanning_attempts = 3
        self.max_feedback_loops = 2
        self.max_tool_uses_per_task = 3

    def process_task(self, prompt: str) -> str:
        if prompt.strip().lower() == "show performance":
            return self.performance_tracker.get_performance_summary()
        if prompt.strip().lower() == "show thoughts":
            return self.thought_logger.format_thoughts(self.workspace.thought_process)

        self.workspace.clear()
        self.workspace.set_initial_prompt(prompt)
        
        print(f"▶️ HiPLEタスク開始: {prompt}")
        try:
            active_experts = self.model_manager.get_all_experts()
            if not active_experts: return "エラー: 利用可能なエキスパートがいません。"

            self.workspace.add_thought("orchestrator", "routing_start", "Phase 0: Routing")
            route_result = self.tool_router_agent.execute(prompt, active_experts)
            task_type = route_result["type"]
            self.workspace.add_thought("orchestrator", "routing_result", {"task_type": task_type, "query": route_result.get("query")})
            
            print(f"🧠 ルーティング結果: {task_type.upper()}")
            
            result = ""
            is_complex = False

            if task_type == "greeting":
                result = cast(str, route_result["response"])
            else:
                query = cast(str, route_result["query"])
                if task_type in ["wikipedia", "web_search", "complex_task"]:
                    result = self._process_complex_task(prompt, active_experts)
                    is_complex = True
                elif task_type == "simple_chat":
                    result = self._process_simple_task(query, active_experts)
                elif task_type == "emergent_task":
                    response_data = self.emergence_agent.execute(query, active_experts)
                    result = response_data.get("response", "創発的タスクの実行に失敗しました。")
                else:
                    result = f"エラー: 不明なタスクタイプ '{task_type}'"

            if is_complex:
                self.task_counter_for_evolution += 1
                if self.task_counter_for_evolution % self.evolution_check_interval == 0:
                    print("\n🔬 自己進化サイクルを実行しています...")
                    evolution_proposal = self.evolution_service.run_evolution_cycle()
                    if evolution_proposal:
                        result += "\n\n" + evolution_proposal
            return result

        except Exception as e:
            traceback.print_exc()
            self.workspace.add_thought("orchestrator", "fatal_error", {"error": str(e), "traceback": traceback.format_exc()})
            return f"致命的なエラーが発生しました: {e}"
        finally:
            self.tool_manager.web_browser_service.close_browser()

    def _process_simple_task(self, prompt: str, experts: List[ExpertModel]) -> str:
        self.workspace.add_thought("orchestrator", "simple_task_start", "Dynamic Generation for Simple Task")
        expert = next((e for e in experts if e.name.lower() == "greeter"), None)
        if not expert:
            expert = self.performance_tracker.get_best_expert(experts, task_type="simple_task")
        
        if not expert:
            return "エラー: 単純応答用のエキスパートが見つかりません。"
        
        self.workspace.add_thought("orchestrator", "expert_selection", {"expert": expert.name, "reason": "Simple Chat"})
        
        task = SubTask(
            task_id=1,
            description=prompt,
            expert_name=expert.name,
            ssv_description=prompt,
        )
        context = self._build_minimal_context(prompt)

        start_time = time.time()
        response_dict = self.generator_agent.execute(task, expert, context, experts)
        result = cast(str, response_dict.get("result", "エラー: 応答がありません。"))
        execution_time = time.time() - start_time
        
        success = result is not None and result.strip() != "" and "エラー" not in result
        self.performance_tracker.update_performance(expert.name, execution_time, success)
        self.workspace.add_thought("orchestrator", "simple_task_end", {"result": result, "success": success, "self_evaluation": task.self_evaluation})

        return result


    def _process_complex_task(self, prompt: str, experts: List[ExpertModel]) -> str:
        failed_plan: Optional[Plan] = None
        validation_error: Optional[str] = None

        for attempt in range(self.max_replanning_attempts):
            safety_check_result = self.safety_director.review_thought_process(self.workspace)
            if safety_check_result and "Aborting" in safety_check_result:
                self.workspace.add_thought("safety_director", "intervention", {"reason": safety_check_result})
                return f"安全性エラー: {safety_check_result}"

            self.workspace.add_thought("orchestrator", "planning_start", f"Phase 1: Hierarchical Planning (Attempt {attempt + 1})")
            performance_summary = self.performance_tracker.get_performance_summary()
            
            current_plan = self.planner_agent.execute(
                prompt, experts, self.tool_manager, failed_plan, validation_error, performance_summary
            )
            self.workspace.add_thought("planner_agent", "plan_generated", {"goal": current_plan.overall_goal, "milestones": [m.title for m in current_plan.milestones], "task_count": len(current_plan.tasks)})

            is_executable, cognitive_load_msg = self.metacognition.analyze_cognitive_load(current_plan)
            if not is_executable:
                self.workspace.add_thought("metacognition_agent", "plan_rejected", {"reason": cognitive_load_msg})
                validation_error = cognitive_load_msg
                failed_plan = current_plan
                continue
            self.workspace.add_thought("metacognition_agent", "plan_approved", cognitive_load_msg)

            is_struct_valid, struct_error = self._validate_plan_structure(current_plan, experts)
            if not is_struct_valid:
                self.workspace.add_thought("orchestrator", "plan_validation_failed", {"reason": "Structural error", "error": struct_error})
                validation_error = f"構造的エラー: {struct_error}"
                failed_plan = current_plan
                continue

            self.workspace.add_thought("orchestrator", "plan_validation_succeeded", "Plan structure is valid.")

            is_semantic_valid, semantic_error = self.plan_evaluation_service.check_semantic_coherence(current_plan.tasks)
            if not is_semantic_valid:
                self.workspace.add_thought("orchestrator", "plan_validation_failed", {"reason": "Semantic coherence error", "error": semantic_error})
                validation_error = f"意味的一貫性エラー: {semantic_error}"
                failed_plan = current_plan
                continue

            self.workspace.add_thought("orchestrator", "plan_validation_succeeded", "Plan semantic coherence is valid.")

            self.workspace.add_thought("orchestrator", "critic_phase_start", "Phase 1c: Strategic Review by Critic Agent")
            critic_feedback = self.critic_agent.execute(current_plan, experts)

            if not critic_feedback.startswith("承認します。"):
                self.workspace.add_thought("critic_agent", "plan_criticism_received", {"feedback": critic_feedback})
                print(f"⚠️ 批評家からの指摘を受信: {critic_feedback}")
                validation_error = f"批評家からの指摘: {critic_feedback}"
                failed_plan = current_plan
                continue
            
            self.workspace.add_thought("critic_agent", "plan_approved", "The plan was approved by the critic.")
            print("✅ 計画は批評家によって承認されました。")

            return self._execute_plan(current_plan, experts)

        self.workspace.add_thought("orchestrator", "planning_failed", f"Failed to create a valid plan after {self.max_replanning_attempts} attempts.")
        return "エラー: 実行可能な計画を立案できませんでした。プロンプトを具体的にして再度お試しください。"

    def _execute_plan(self, plan: Plan, experts: List[ExpertModel]) -> str:
        self.workspace.add_thought("orchestrator", "execution_start", "Phase 2a: Modular RAG Indexing")
        plan_data_source = PlanDataSource(plan)
        self.rag_manager.build_index_from_source("plan_retriever", plan_data_source)
        
        self.workspace.add_thought("orchestrator", "execution_phase_start", "Phase 2b: Context-Aware Generation (HiPLE-G)")
        completed_tasks: Dict[int, SubTask] = {}
        worker_tasks = [t for t in plan.tasks if t.expert_name.lower() != 'reporter']
        task_context_storage: Dict[int, Dict[str, Any]] = {}

        while len(completed_tasks) < len(worker_tasks):
            safety_check_result = self.safety_director.review_thought_process(self.workspace)
            if safety_check_result and "Aborting" in safety_check_result:
                self.workspace.add_thought("safety_director", "intervention", {"reason": safety_check_result})
                return f"安全性エラー: {safety_check_result}"

            executable_tasks = [t for t in worker_tasks if t.status == "pending" and all(d in completed_tasks for d in t.dependencies)]

            if not executable_tasks:
                if len(completed_tasks) < len(worker_tasks):
                    for task in worker_tasks:
                        if task.status != "completed":
                            expert = self.model_manager.get_expert(task.expert_name)
                            if expert: self.performance_tracker.update_performance(expert.name, 0, False)
                    self.workspace.add_thought("orchestrator", "execution_error", "Circular dependency or dead-end in plan.")
                    return "エラー: タスクの依存関係が循環しているか、計画に問題があります。"
                break

            for task in executable_tasks:
                expert = self.model_manager.get_expert(task.expert_name)
                if not expert:
                    task.result = f"エラー: エキスパート '{task.expert_name}' が見つかりませんでした。"
                    task.status = "failed"
                    completed_tasks[task.task_id] = task
                    self.workspace.add_thought("orchestrator", "task_failed", {"task_id": task.task_id, "reason": f"Expert '{task.expert_name}' not found."})
                    continue

                execution_time = 0.0
                task_context = task_context_storage.get(task.task_id, {})
                
                for loop_count in range(self.max_feedback_loops + self.max_tool_uses_per_task):
                    rag_decision_data = self.rag_agent.execute(task.ssv_description, experts)
                    rag_decision = cast(Dict[str, Any], rag_decision_data.get("response", {}))
                    rag_results: List[Document] = []
                    if isinstance(rag_decision, dict) and rag_decision.get("needs_retrieval"):
                        query = rag_decision.get("query", task.ssv_description)
                        rag_results = self.rag_manager.query("plan_retriever", query, k=3)
                        self.workspace.add_thought("rag_agent", "retrieval_performed", {"query": query, "results_count": len(rag_results)})
                    
                    current_context = self._build_context_for_task(task, plan, completed_tasks, rag_results, task_context.get("tool_results", ""))

                    self.workspace.add_thought("orchestrator", "task_execution_start", {"task_id": task.task_id, "expert": expert.name, "attempt": loop_count + 1, "description": task.description})
                    task.status = "in_progress"
                    
                    start_time = time.time()
                    response_dict = self.generator_agent.execute(task, expert, current_context, experts)
                    execution_time += time.time() - start_time

                    if response_dict.get("status") == "tool_request":
                        tool_name = response_dict.get("tool_name", "")
                        tool_query = response_dict.get("tool_query", "")
                        tool_url = response_dict.get("tool_url", "")
                        self.workspace.add_thought("generator_agent", "tool_request", {"tool_name": tool_name, "tool_query": tool_query})
                        
                        start_time_tool = time.time()
                        tool_result = self.tool_manager.execute_tool(tool_name, tool_query, tool_url, experts)
                        execution_time += time.time() - start_time_tool

                        self.workspace.add_thought("tool_manager", "tool_result", {"tool_name": tool_name, "result_length": len(tool_result)})
                        
                        task.result = tool_result
                        break

                    generated_output = response_dict.get("result", "")

                    if task.reviewer_expert:
                        reviewer = self.model_manager.get_expert(task.reviewer_expert)
                        if reviewer:
                            self.workspace.add_thought("orchestrator", "review_start", {"task_id": task.task_id, "reviewer": reviewer.name})
                            feedback_data = self.reviewer_agent.execute(task, generated_output, reviewer, expert)
                            feedback = feedback_data.get("response", "")
                            if not feedback.startswith("承認します。"):
                                self.workspace.add_thought("reviewer_agent", "feedback_provided", {"task_id": task.task_id, "feedback": feedback})
                                task.feedback_history.append({"reviewer": reviewer.name, "feedback": feedback})
                                task_context["feedback"] = feedback
                                continue
                            self.workspace.add_thought("reviewer_agent", "review_passed", {"task_id": task.task_id})
                    
                    task.result = generated_output
                    break
                
                success = task.result is not None and task.result.strip() != "" and "エラー" not in task.result
                self.performance_tracker.update_performance(expert.name, execution_time, success)

                task.status = "completed" if success else "failed"
                completed_tasks[task.task_id] = task
                self.workspace.add_thought(
                    "orchestrator", 
                    "task_completed", 
                    {"task_id": task.task_id, "status": task.status, "self_evaluation": task.self_evaluation}
                )
                
                if not success: break
            
            if any(t.status == "failed" for t in completed_tasks.values()):
                self.workspace.add_thought("orchestrator", "execution_halted", "A task failed, halting plan execution.")
                break
        
        reporter_tasks = [t for t in plan.tasks if t.expert_name.lower() == 'reporter']
        if reporter_tasks:
             self.workspace.add_thought("orchestrator", "reporting_start", "Phase 3: Reporting")
             final_report = self.reporter_agent.execute(plan, experts)
             self.workspace.set_final_answer(final_report)
             return final_report
        else:
            if not completed_tasks: return "タスクは実行されましたが、結果がありませんでした。"
            succeeded_tasks = [t for t in completed_tasks.values() if t.status == "completed"]
            if succeeded_tasks:
                last_task = max(succeeded_tasks, key=lambda t: t.task_id)
                final_result = last_task.result or "完了しましたが結果がありません。"
                self.workspace.set_final_answer(final_result)
                return final_result
            else:
                return "エラー: 全てのタスクが失敗しました。"

    def _validate_plan_structure(self, plan: Plan, experts: List[ExpertModel]) -> Tuple[bool, str]:
        if not plan.tasks: return False, "計画にタスクが含まれていません。"
        task_ids = {task.task_id for task in plan.tasks}
        milestone_ids = {m.milestone_id for m in plan.milestones}
        valid_expert_names = {expert.name.lower() for expert in experts}

        for task in plan.tasks:
            if task.expert_name.lower() not in valid_expert_names:
                return False, f"タスク {task.task_id} のエキスパート '{task.expert_name}' が不正です。"
            if task.milestone_id is not None and task.milestone_id not in milestone_ids:
                 return False, f"タスク {task.task_id} のマイルストーンID '{task.milestone_id}' が不正です。"
            for dep_id in task.dependencies:
                if dep_id not in task_ids:
                    return False, f"タスク {task.task_id} の依存先 {dep_id} が不正です。"
        return True, "計画は構造的に妥当です。"

    def _build_context_for_task(self, task: SubTask, plan: Plan, completed_tasks: Dict[int, SubTask], rag_results: List[Document], tool_results: str = "") -> Dict[str, Any]:
        current_milestone = next((m for m in plan.milestones if m.milestone_id == task.milestone_id), None)
        dependency_results = ""
        if task.dependencies:
            for dep_id in sorted(task.dependencies):
                if dep_id in completed_tasks and completed_tasks[dep_id].status == "completed":
                    result = completed_tasks[dep_id].result
                    dependency_results += f"【先行タスク{dep_id}の結果】:\n{result}\n\n"
        
        return {
            "original_prompt": plan.original_prompt,
            "overall_goal": plan.overall_goal,
            "milestone": current_milestone,
            "ssv_description": task.ssv_description,
            "dependency_results": dependency_results,
            "rag_results": [doc.content for doc in rag_results],
            "tool_results": tool_results
        }

    def _build_minimal_context(self, prompt: str) -> Dict[str, Any]:
        return {
            "original_prompt": prompt,
            "overall_goal": prompt,
            "milestone": Milestone(milestone_id=1, title="Direct Task", description=prompt),
            "dependency_results": "",
            "rag_results": []
        }
```

### `orchestrator/router.py`

```python
# path: ./orchestrator/router.py
# title: Simple Router with Emergent Task Recognition
# description: A simple, keyword-based router that now recognizes requests for brainstorming.

from typing import Dict, Any, List

class SimpleRouter:
    """
    キーワードとヒューリスティクスに基づいてユーザーの要求をルーティングする、
    LLMに依存しないシンプルなルーター。
    """
    def __init__(self):
        self.greetings: Dict[str, str] = {
            "こんにちは": "こんにちは！何かお役に立てることはありますか？",
            "おはよう": "おはようございます！良い一日を。",
            "こんばんは": "こんばんは。いかがお過ごですか？",
            "ありがとう": "どういたしまして！"
        }
        
        self.tool_keywords: Dict[str, List[str]] = {
            "emergent_task": ["ブレインストーミング", "ブレストして", "新しいアイデア", "革新的な", "創造的な解決策", "発想して"],
            "wikipedia": ["教えて", "とは", "誰", "何", "どこ", "原理", "メカニズム", "歴史", "について"],
            "complex_task": ["作成して", "実装して", "分析して", "書いて", "作って", "計画して", "要約して", "翻訳して", "比較して"]
        }

    def route(self, prompt: str) -> Dict[str, Any]:
        """
        プロンプトを分析し、タスクの種類とクエリを決定する。
        """
        normalized_prompt = prompt.strip().lower()

        # 1. 挨拶のチェック
        for greeting, response in self.greetings.items():
            if greeting in normalized_prompt:
                return {"type": "greeting", "response": response}

        # 2. ツールキーワードのチェック (創発タスクを先に評価)
        for tool, keywords in self.tool_keywords.items():
            for keyword in keywords:
                if keyword in normalized_prompt:
                    if tool == "wikipedia":
                        return {"type": "wikipedia", "query": prompt}
                    elif tool == "emergent_task":
                        return {"type": "emergent_task", "query": prompt}
                    
                    query = prompt.replace(keyword, "").strip()
                    return {"type": tool, "query": query if query else prompt}

        # 3. 上記に当てはまらない場合は、複雑なタスクとして計画立案に回す
        return {"type": "complex_task", "query": prompt}

```

### `rag/__init__.py`

```python
# path: ./rag/__init__.py
# title: RAG Package Initializer
# description: This file makes the 'rag' directory a Python package.
```

### `rag/data_sources.py`

```python
# path: ./rag/data_sources.py
# title: RAG Data Source Schemas and Interfaces
# description: Defines the standardized Document schema and the base class for all data sources.

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Iterator
from dataclasses import dataclass, field
from domain.schemas import Plan

@dataclass
class Document:
    """
    RAGシステム内で扱われる、分割されたテキスト情報の標準単位。
    """
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

class DataSource(ABC):
    """
    すべてのデータソースの基底クラスとなる抽象クラス。
    """
    @abstractmethod
    def load_documents(self) -> Iterator[Document]:
        """
        データソースからドキュメントを読み込み、イテレータとして返す。
        """
        pass

class PlanDataSource(DataSource):
    """
    HiPLEの実行計画(Plan)をデータソースとして扱うクラス。
    """
    def __init__(self, plan: Plan):
        self.plan = plan

    def load_documents(self) -> Iterator[Document]:
        """
        Planオブジェクトの各階層からDocumentを生成する。
        """
        # L1: Overall Goal
        yield Document(
            content=f"全体の目標: {self.plan.overall_goal}",
            metadata={"type": "L1_GOAL", "source": "plan"}
        )

        # L2: Milestones
        for m in self.plan.milestones:
            yield Document(
                content=f"マイルストーン「{m.title}」: {m.description}",
                metadata={"type": "L2_MILESTONE", "id": m.milestone_id, "source": "plan"}
            )
        
        # L3: Tasks
        for t in self.plan.tasks:
            yield Document(
                content=f"タスク {t.task_id} ({t.expert_name}): {t.description} (目的: {t.ssv_description})",
                metadata={"type": "L3_TASK", "id": t.task_id, "source": "plan"}
            )

```

### `rag/retrievers.py`

```python
# path: ./rag/retrievers.py
# title: RAG Retriever Interfaces and Implementations
# description: Defines the retriever interface and a Faiss-based implementation for vector search.

from abc import ABC, abstractmethod
from typing import List, Optional
import numpy as np
import faiss
from rag.data_sources import Document
from services.vectorization_service import VectorizationService

class BaseRetriever(ABC):
    """
    すべてのリトリーバーの基底クラス。
    """
    @abstractmethod
    def build_index(self, documents: List[Document]) -> None:
        """
        ドキュメントのリストから検索インデックスを構築する。
        """
        pass

    @abstractmethod
    def retrieve(self, query: str, k: int = 3) -> List[Document]:
        """
        クエリに最も関連するドキュメントをk個検索する。
        """
        pass

class FaissRetriever(BaseRetriever):
    """
    FAISSを利用したベクトル検索リトリーバー。
    """
    def __init__(self, vectorization_service: VectorizationService):
        self.vector_service = vectorization_service
        self.index: Optional[faiss.IndexFlatL2] = None
        self.documents: List[Document] = []

    def build_index(self, documents: List[Document]) -> None:
        """
        ドキュメントをベクトル化し、FAISSインデックスを構築する。
        """
        print("🔄 FAISSインデックスを構築しています...")
        self.documents = documents
        
        if not self.documents:
            self.index = None
            print("🟡 ドキュメントが空のため、インデックスは構築されませんでした。")
            return

        contents = [doc.content for doc in self.documents]
        vectors = self.vector_service.encode_batch(contents)
        
        if vectors.size == 0:
            self.index = None
            print("🟡 ベクトルが生成されなかったため、インデックスは構築されませんでした。")
            return

        dimension = vectors.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(vectors)
        print(f"✅ FAISSインデックスの構築が完了しました。(次元数: {dimension}, データ数: {len(self.documents)})")

    def retrieve(self, query: str, k: int = 3) -> List[Document]:
        """
        クエリベクトルに意味的に近いドキュメントを検索する。
        """
        if self.index is None or not self.documents:
            return []

        query_vector = self.vector_service.encode(query).reshape(1, -1)
        distances, indices = self.index.search(query_vector, k)
        
        results = []
        for i in indices[0]:
            # 検索結果のインデックスがドキュメントリストの範囲内にあるか確認
            if 0 <= i < len(self.documents):
                results.append(self.documents[i])
        
        return results

```

### `services/__init__.py`

```python
# /hybrid_llm_system/services/__init__.py
```

### `services/evolution_service.py`

```python
# path: ./services/evolution_service.py
# title: Self-Evolution Service
# description: Manages the self-evolution loop based on performance metrics and safety constraints.

from typing import Dict, Any, Optional, List
from services.performance_tracker_service import PerformanceTrackerService
from domain.boundary_enforcer import BoundaryConditionEnforcer
from domain.schemas import ExpertModel

class EvolutionService:
    """
    エキスパートのパフォーマンスに基づき、システムの自己進化を管理するサービス。
    """
    def __init__(
        self,
        performance_tracker: PerformanceTrackerService,
        boundary_enforcer: BoundaryConditionEnforcer,
        all_experts: List[ExpertModel]
    ):
        self.performance_tracker = performance_tracker
        self.boundary_enforcer = boundary_enforcer
        self.all_experts = {expert.name.lower(): expert for expert in all_experts}
        # 進化の提案をセッション内で一度だけ行うためのフラグ
        self.evolution_proposed_this_session: Dict[str, bool] = {}

    def run_evolution_cycle(self) -> Optional[str]:
        """
        進化サイクルを実行し、改善提案があれば文字列として返す。
        """
        # 1. パフォーマンスが低いエキスパートを特定
        underperforming_experts = self.performance_tracker.get_underperforming_experts()
        if not underperforming_experts:
            return None

        # 2. 改善策を提案
        for expert_name, metrics in underperforming_experts:
            if self.evolution_proposed_this_session.get(expert_name):
                continue # このセッションでは既に提案済み

            # 今は「無効化」のみを提案する
            proposed_change = {
                "action": "disable",
                "expert_name": expert_name,
                "reason": f"Success rate is {metrics.success_rate:.2%} over {metrics.total_runs} runs."
            }

            # 3. 境界条件エンフォーサーによる検証
            is_valid, message = self.boundary_enforcer.validate_evolution(proposed_change)

            if is_valid:
                print(f"🧬 Evolution Proposal: {message}")
                self.evolution_proposed_this_session[expert_name] = True
                
                # 提案を返す (実際のファイル書き込みは行わない)
                evolution_summary = (
                    f"**[SELF-EVOLUTION PROPOSAL]**\n"
                    f"- **Action:** Disable expert '{expert_name}'.\n"
                    f"- **Reason:** Low performance detected (Success Rate: {metrics.success_rate:.2%}).\n"
                    f"- **Suggestion:** Consider setting `enabled: false` for this expert in `config/models.yml` to improve overall system performance."
                )
                return evolution_summary
            else:
                print(f"🧬 Evolution Proposal for '{expert_name}' was rejected. Reason: {message}")
                # 却下された提案も記録し、再提案しないようにする
                self.evolution_proposed_this_session[expert_name] = True

        return None

```

### `services/model_loader.py`

```python
# path: ./services/model_loader.py
# title: Model Loader Service with Stabilized Parameters
# description: jamba_test.pyの設定を参考に、モデルロード時のパラメータを安定化させる。

import os
import gc
import sys
import traceback
from typing import Optional, Any, Union
import psutil
from llama_cpp import Llama
from domain.schemas import ExpertModel
import torch
from diffusers import DiffusionPipeline, AutoencoderKL
from utils.monitoring import print_memory_usage

class ModelLoaderService:
    """
    エキスパートモデルのロードとアンロード（スワッピング）を管理する
    """
    def __init__(self, memory_threshold_gb: int = 2) -> None:
        self.currently_loaded_expert: Optional[ExpertModel] = None
        self.memory_threshold_bytes = memory_threshold_gb * 1024 * 1024 * 1024

    def _check_memory(self) -> None:
        available_memory = psutil.virtual_memory().available
        if available_memory < self.memory_threshold_bytes:
            raise MemoryError(f"利用可能なメモリ ({available_memory / (1024**3):.2f}GB) が閾値を下回っています。")
        print(f"✅ メモリチェックOK (Available: {available_memory / (1024**3):.2f}GB)")

    def load_expert(self, expert: ExpertModel) -> Union[Llama, DiffusionPipeline]:
        if expert.is_loaded and expert.instance:
            if self.currently_loaded_expert and self.currently_loaded_expert.name != expert.name:
                self.unload_expert(self.currently_loaded_expert)
            self.currently_loaded_expert = expert
            print(f"✅ エキスパート '{expert.name}' は既にロード済みです。")
            if isinstance(expert.instance, Llama):
                expert.instance.reset()
            return expert.instance

        if self.currently_loaded_expert:
            self.unload_expert(self.currently_loaded_expert)

        self._check_memory()
        print(f"🔄 エキスパート '{expert.name}' をロードします...")
        print_memory_usage(f"BEFORE_LOAD_{expert.name.upper()}")

        try:
            instance: Union[Llama, DiffusionPipeline]
            if expert.chat_format == "diffusion":
                if not expert.model_id: raise ValueError("拡散モデルのmodel_idが未設定")
                device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
                vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16)
                pipe = DiffusionPipeline.from_pretrained(expert.model_id, vae=vae, torch_dtype=torch.float16, variant="fp16", use_safetensors=True)
                instance = pipe.to(device)
            else:
                if not expert.model_path: raise ValueError("LLMのmodel_pathが未設定")
                log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
                is_apple_silicon = sys.platform == "darwin" and "arm64" in os.uname().machine
                n_gpu_layers = -1 if is_apple_silicon else 0
                
                # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
                # jamba_test.pyを参考に、安定動作するパラメータ設定に統一
                n_threads = psutil.cpu_count(logical=False)
                instance = Llama(
                    model_path=expert.model_path, 
                    n_gpu_layers=n_gpu_layers, 
                    n_ctx=4096, 
                    use_mlock=True, 
                    use_mmap=False, # メモリマップを無効化
                    n_threads=n_threads, # スレッド数を明示
                    verbose=log_verbose, 
                    chat_format=expert.chat_format
                )
                # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

            expert.instance = instance
            expert.is_loaded = True
            self.currently_loaded_expert = expert
            print(f"✅ エキスパート '{expert.name}' の準備が完了しました。")
            print_memory_usage(f"AFTER_LOAD_{expert.name.upper()}")
            return instance
        except Exception as e:
            print(f"❌ エキスパート '{expert.name}' のロード中にエラー: {e}")
            traceback.print_exc()
            raise

    def unload_expert(self, expert: Optional[ExpertModel]) -> None:
        if expert and expert.instance:
            print(f"🧹 エキスパート '{expert.name}' をアンロードしメモリを解放します。")
            print_memory_usage(f"BEFORE_UNLOAD_{expert.name.upper()}")
            del expert.instance
            expert.instance = None
            expert.is_loaded = False
            if self.currently_loaded_expert and self.currently_loaded_expert.name == expert.name:
                self.currently_loaded_expert = None
            gc.collect()
            if torch.backends.mps.is_available(): torch.mps.empty_cache()
            elif torch.cuda.is_available(): torch.cuda.empty_cache()
            print_memory_usage(f"AFTER_UNLOAD_{expert.name.upper()}")
```

### `services/performance_tracker_service.py`

```python
# path: ./services/performance_tracker_service.py
# title: Performance Tracker Service (with Underperformer Detection)
# description: AIエキスパートのパフォーマンスを追跡・評価し、低パフォーマンスのエキスパートを特定する機能を追加。

import time
from typing import Dict, Optional, List, Tuple
from domain.evaluation import PerformanceMetrics
from domain.schemas import ExpertModel

class PerformanceTrackerService:
    """
    エキスパートのパフォーマンスを記録・管理するサービス
    """
    def __init__(self):
        self.performance_records: Dict[str, PerformanceMetrics] = {}

    def update_performance(
        self,
        expert_name: str,
        execution_time: float,
        success: bool
    ) -> None:
        """
        指定されたエキスパートのパフォーマンスを更新する
        """
        if expert_name not in self.performance_records:
            self.performance_records[expert_name] = PerformanceMetrics()

        record = self.performance_records[expert_name]
        
        record.total_execution_time_all += execution_time
        
        if success:
            record.success_count += 1
            record.total_execution_time_on_success += execution_time
        else:
            record.failure_count += 1

        self._recalculate_score(expert_name)
        print(f"📊 Performance updated for '{expert_name}': Score={record.score:.2f}, SuccessRate={record.success_rate:.2f}, AvgTime={record.average_execution_time:.2f}s")

    def _recalculate_score(self, expert_name: str) -> None:
        """
        エキスパートのスコアを再計算する
        """
        record = self.performance_records.get(expert_name)
        if not record or record.total_runs == 0:
            return

        all_avg_times = [r.average_execution_time for r in self.performance_records.values() if r.total_runs > 0]
        max_avg_time = max(all_avg_times) if all_avg_times else 1.0
        if max_avg_time == 0: max_avg_time = 1.0
        
        normalized_time = record.average_execution_time / max_avg_time
        time_penalty = min(normalized_time, 1.0)

        record.score = record.success_rate * (1.0 - (time_penalty * 0.2))

    def get_best_expert(self, experts: List[ExpertModel], task_type: str = "general") -> Optional[ExpertModel]:
        """
        現在最もスコアの高い、利用可能なエキスパートを返す。
        """
        best_expert: Optional[ExpertModel] = None
        highest_score = -1.0

        eligible_experts = [e for e in experts if e.name in self.performance_records and e.chat_format != "diffusion"]

        for expert in eligible_experts:
            score = self.performance_records[expert.name].score
            if score > highest_score:
                highest_score = score
                best_expert = expert
        
        if best_expert:
            print(f"🏆 Best expert selected for '{task_type}': '{best_expert.name}' (Score: {highest_score:.2f})")
            return best_expert

        print(f"🟡 No expert with a positive score for '{task_type}'. Using fallback strategy.")
        
        hrm_expert = next((e for e in experts if e.name.lower() == "hrm"), None)
        if hrm_expert:
            print("↪️ Fallback to default reasoner: 'HRM'")
            return hrm_expert
            
        jamba_expert = next((e for e in experts if e.name.lower() == "jamba"), None)
        if jamba_expert:
            print("↪️ Fallback to generalist: 'Jamba'")
            return jamba_expert

        return next((e for e in experts if e.chat_format != "diffusion"), None)

    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    def get_underperforming_experts(self, run_threshold: int = 3, success_rate_threshold: float = 0.5) -> List[Tuple[str, PerformanceMetrics]]:
        """
        パフォーマンスが基準値を下回るエキスパートのリストを返す。

        Args:
            run_threshold (int): 評価の対象となる最小実行回数。
            success_rate_threshold (float): この成功率を下回ると「低パフォーマンス」と見なされる。

        Returns:
            List[Tuple[str, PerformanceMetrics]]: (エキスパート名, パフォーマンスメトリクス) のタプルのリスト。
        """
        underperformers = []
        for name, record in self.performance_records.items():
            if record.total_runs >= run_threshold and record.success_rate < success_rate_threshold:
                underperformers.append((name, record))
        
        return underperformers
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def get_performance_summary(self) -> str:
        """
        全エキスパートのパフォーマンスサマリーを文字列として返す
        """
        summary_lines = ["# Expert Performance Summary"]
        if not self.performance_records:
            return "# Expert Performance Summary\nNo performance records yet."
            
        for name, record in sorted(self.performance_records.items(), key=lambda item: item[1].score, reverse=True):
            summary_lines.append(
                f"- **{name}**: "
                f"Score={record.score:.2f}, "
                f"SuccessRate={record.success_rate * 100:.1f}%, "
                f"AvgTime={record.average_execution_time:.2f}s, "
                f"Runs={record.total_runs}"
            )
        return "\n".join(summary_lines)

```

### `services/plan_evaluation_service.py`

```python
# path: ./services/plan_evaluation_service.py
# title: Plan Evaluation Service
# description: 計画の意味的一貫性をベクトル空間で評価するサービス。

from typing import List, Tuple
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from services.vectorization_service import VectorizationService
from domain.schemas import SubTask

class PlanEvaluationService:
    """
    計画の意味的な妥当性を評価するサービス。
    """
    def __init__(self, vectorization_service: VectorizationService):
        self.vector_service = vectorization_service

    def check_semantic_coherence(
        self,
        tasks: List[SubTask],
        threshold: float = 0.5
    ) -> Tuple[bool, str]:
        """
        計画のステップ間の意味的な一貫性を検証する。
        連続するタスクのSSV（意味構造ベクトル）間のコサイン類似度が
        しきい値を下回った場合に警告する。

        Args:
            tasks (List[SubTask]): 評価対象のタスクリスト。
            threshold (float): 一貫性の警告を出すコサイン類似度のしきい値。

        Returns:
            Tuple[bool, str]: (一貫性が保たれているか, 評価メッセージ)
        """
        if len(tasks) <= 1:
            return True, "計画は単一ステップのため、一貫性チェックは不要です。"

        # SSV記述からベクトルを一括生成
        ssv_descriptions = [task.ssv_description for task in tasks]
        ssv_vectors = self.vector_service.encode_batch(ssv_descriptions)

        coherence_issues = []
        # 実行順にタスクをソート
        sorted_tasks = sorted(tasks, key=lambda t: t.task_id)
        
        for i in range(len(sorted_tasks) - 1):
            # 隣接するタスクのベクトルを取得
            vec1 = ssv_vectors[i].reshape(1, -1)
            vec2 = ssv_vectors[i+1].reshape(1, -1)
            similarity = cosine_similarity(vec1, vec2)[0][0]

            if similarity < threshold:
                issue = (
                    f"ステップ {i+1} から {i+2} への意味的な飛躍が検出されました (類似度: {similarity:.2f})。\n"
                    f"  - Step {i+1}: '{sorted_tasks[i].description}' (SSV: {sorted_tasks[i].ssv_description})\n"
                    f"  - Step {i+2}: '{sorted_tasks[i+1].description}' (SSV: {sorted_tasks[i+1].ssv_description})\n"
                    "これらのタスク間の関連性が低い可能性があります。計画を見直してください。"
                )
                coherence_issues.append(issue)

        if coherence_issues:
            error_message = "計画の意味的一貫性に問題があります:\n" + "\n".join(coherence_issues)
            return False, error_message

        return True, "計画は意味的に一貫しています。"
```

### `services/rag_manager_service.py`

```python
# path: ./services/rag_manager_service.py
# title: RAG Manager Service
# description: Manages multiple retrievers and data sources for the RAG pipeline.

from typing import Dict, List, Iterator
from rag.data_sources import Document, DataSource
from rag.retrievers import BaseRetriever
from services.vectorization_service import VectorizationService

class RAGManagerService:
    """
    RAGパイプライン全体を管理するサービス。
    複数のリトリーバーを保持し、適切なリトリーバーを介して検索を実行する。
    """
    def __init__(self, vectorization_service: VectorizationService):
        self._retrievers: Dict[str, BaseRetriever] = {}
        self._vectorization_service = vectorization_service

    def register_retriever(self, name: str, retriever: BaseRetriever) -> None:
        """
        リトリーバーをマネージャーに登録する。
        """
        self._retrievers[name] = retriever
        print(f"🔍 RAGリトリーバー '{name}' を登録しました。")

    def build_index_from_source(self, retriever_name: str, data_source: DataSource) -> None:
        """
        指定されたデータソースからドキュメントを読み込み、指定されたリトリーバーのインデックスを構築する。
        """
        if retriever_name not in self._retrievers:
            raise ValueError(f"リトリーバー '{retriever_name}' は登録されていません。")
        
        documents = list(data_source.load_documents())
        retriever = self._retrievers[retriever_name]
        retriever.build_index(documents)

    def query(self, retriever_name: str, query_text: str, k: int = 3) -> List[Document]:
        """
        指定されたリトリーバーを使ってクエリを実行し、関連ドキュメントを取得する。
        """
        if retriever_name not in self._retrievers:
            raise ValueError(f"リトリーバー '{retriever_name}' は登録されていません。")
        
        retriever = self._retrievers[retriever_name]
        return retriever.retrieve(query_text, k=k)

```

### `services/tool_manager_service.py`

```python
# path: ./services/tool_manager_service.py
# title: Tool Manager Service
# description: A centralized service for registering and executing available tools.

import traceback
from typing import Dict, Any, List, cast

# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from agents.wikipedia_agent import WikipediaAgent
from agents.web_browser_agent import WebBrowserAgent
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from services.web_browser_service import WebBrowserService
from domain.schemas import ExpertModel
import googlesearch

class ToolManagerService:
    """
    システムで利用可能なツールを登録し、実行を管理するサービス。
    """
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    def __init__(
        self,
        wikipedia_agent: WikipediaAgent,
        web_browser_agent: WebBrowserAgent,
        web_browser_service: WebBrowserService
    ):
        self.web_browser_service = web_browser_service
        self.wikipedia_agent = wikipedia_agent
        self.web_browser_agent = web_browser_agent
        self.tools: Dict[str, Any] = {
            "wikipedia_search": self.wikipedia_agent,
            "web_search": self.web_browser_agent,
        }
        print(f"🛠️ ToolManagerServiceが初期化され、{list(self.tools.keys())} が登録されました。")
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def get_tool_descriptions(self) -> str:
        """
        PlannerAgentのプロンプト用に、利用可能なツールの一覧と説明を文字列で返す。
        """
        return """- **wikipedia_search**: 普遍的で確立された知識（人物、場所、歴史的出来事、科学理論など）を調べる。
- **web_search**: 最新の情報、ニュース、トレンド、特定の製品レビュー、レシピなど、時間と共に変化する情報を調べる。"""

    def execute_tool(self, tool_name: str, query: str, url: str, experts: List[ExpertModel]) -> str:
        """
        指定されたツールを実行する。
        """
        if tool_name not in self.tools:
            return f"エラー: 不明なツール '{tool_name}' が指定されました。"

        print(f"🔧 ツール '{tool_name}' を実行します。Query: '{query}'")
        try:
            if tool_name == "wikipedia_search":
                return self.tools[tool_name].execute(query, experts)
            
            elif tool_name == "web_search":
                if not url:
                    print(f"🔍 URLが指定されていないため、Googleで '{query}' を検索します...")
                    try:
                        search_results = list(googlesearch.search(query, num=1, stop=1, pause=2))
                        if not search_results:
                            return f"エラー: '{query}' に関連するWebページが見つかりませんでした。"
                        url = search_results[0]
                        print(f"🔗 最初の検索結果を使用します: {url}")
                    except Exception as e:
                        return f"エラー: Google検索中にエラーが発生しました - {e}"
                
                page_content = self.web_browser_service.get_page_content(url)
                if "エラー:" in page_content:
                    return page_content
                
                # エージェントにコンテンツ処理を委任
                return self.tools[tool_name].execute(page_content, query, experts)
            
            else:
                return f"エラー: ツール '{tool_name}' の実行ロジックが定義されていません。"
        except Exception as e:
            traceback.print_exc()
            return f"エラー: ツール '{tool_name}' の実行中に問題が発生しました - {e}"
```

### `services/vectorization_service.py`

```python
# path: ./services/vectorization_service.py
# title: Vectorization Service
# description: テキストを意味ベクトル（Embedding）に変換するサービス。mypyエラー修正済み。

from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class VectorizationService:
    """
    テキストのベクトル化を担当するサービス。
    SentenceTransformerモデルを使用して、テキストを密なベクトル表現に変換します。
    """
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        サービスの初期化時に、指定されたモデルをロードします。
        
        Args:
            model_name (str): Hugging Face HubからロードするSentenceTransformerモデル名。
        """
        try:
            print(f"🔄 ベクトル化モデル '{model_name}' をロードしています...")
            self.model = SentenceTransformer(model_name)
            print("✅ ベクトル化モデルのロードが完了しました。")
        except Exception as e:
            print(f"❌ ベクトル化モデルのロードに失敗しました: {e}")
            raise

    def encode(self, text: str) -> np.ndarray:
        """
        単一のテキストをベクトルに変換します。
        
        Args:
            text (str): ベクトル化するテキスト。
        
        Returns:
            np.ndarray: 生成されたベクトル。
        """
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        return self.model.encode(text, convert_to_numpy=True)
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def encode_batch(self, texts: List[str]) -> np.ndarray:
        """
        テキストのリストをまとめてベクトルに変換します。
        
        Args:
            texts (List[str]): ベクトル化するテキストのリスト。
        
        Returns:
            np.ndarray: 生成されたベクトルのリスト。
        """
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        return self.model.encode(texts, convert_to_numpy=True)
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
```

### `services/web_browser_service.py`

```python
# path: ./services/web_browser_service.py
# title: Web Browser Service (Synchronous Implementation)
# description: Playwrightを使用してヘッドレスブラウザを制御し、Webページのコンテンツを取得するサービス。非同期処理に起因するエラーを解消するため、同期APIを使用。

from typing import Optional
from playwright.sync_api import sync_playwright, Browser, Page, Playwright

class WebBrowserService:
    """
    Playwrightをラップして、同期的なブラウザ操作を提供するサービス。
    """
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None

    def launch_browser(self) -> None:
        """ブラウザを起動する"""
        if self.browser and self.browser.is_connected:
            return
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        print("🖥️ ブラウザを起動しました。")

    def close_browser(self) -> None:
        """ブラウザを閉じる"""
        if self.browser:
            self.browser.close()
            self.browser = None
        if self.playwright:
            self.playwright.stop()
            self.playwright = None
        print("🖥️ ブラウザを終了しました。")

    def get_page_content(self, url: str) -> str:
        """
        指定されたURLのレンダリング済みHTMLコンテンツを取得する。
        """
        if not self.browser or not self.browser.is_connected:
            self.launch_browser()
        
        page: Optional[Page] = None
        try:
            # self.browserがNoneでないことをアサーションで確認
            assert self.browser is not None
            page = self.browser.new_page()
            print(f"📄 ページにアクセスしています: {url}")
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            content = page.content()
            print(f"✅ コンテンツの取得に成功しました。(文字数: {len(content)})")
            return content
        except Exception as e:
            print(f"❌ ページのコンテンツ取得に失敗しました: {e}")
            return f"エラー: {url} のコンテンツ取得に失敗しました。理由: {e}"
        finally:
            if page:
                page.close()
```

### `services/wikipedia_service.py`

```python
# path: ./services/wikipedia_service.py
# title: Wikipedia Service (mypy compatible)
# description: Wikipedia APIをラップし、記事の検索や要約の取得を行うサービス。mypyエラーを修正。

import wikipedia
from typing import List, Optional, cast

class WikipediaService:
    """
    Wikipediaライブラリをラップして、言語設定やエラーハンドリングを行うサービス。
    """
    def __init__(self, lang: str = "ja"):
        """
        サービスの初期化時に、検索言語を設定します。
        """
        try:
            wikipedia.set_lang(lang)
            self.lang = lang
            print(f"🌍 Wikipediaの検索言語を '{lang}' に設定しました。")
        except Exception as e:
            print(f"⚠️ Wikipediaの言語設定に失敗しました: {e}。デフォルトの'en'を使用します。")
            wikipedia.set_lang("en")
            self.lang = "en"

    def search(self, query: str, results: int = 3) -> Optional[List[str]]:
        """
        指定されたクエリでWikipediaの記事を検索し、候補のタイトルリストを返す。

        Args:
            query (str): 検索クエリ。
            results (int): 取得する候補の数。

        Returns:
            Optional[List[str]]: 記事タイトルのリスト。見つからない場合はNone。
        """
        try:
            search_results = wikipedia.search(query, results=results)
            if not search_results:
                return None
            return cast(List[str], search_results)
        except Exception as e:
            print(f"❌ Wikipediaでの検索中にエラーが発生しました: {e}")
            return None

    def get_summary(self, title: str, sentences: int = 5) -> Optional[str]:
        """
        指定されたタイトルの記事の要約を取得する。

        Args:
            title (str): 記事の正式タイトル。
            sentences (int): 要約の文の数。

        Returns:
            Optional[str]: 記事の要約。見つからない、または曖昧な場合はNone。
        """
        try:
            summary = wikipedia.summary(title, sentences=sentences, auto_suggest=False)
            return cast(str, summary)
        except wikipedia.exceptions.PageError:
            print(f"🟡 記事 '{title}' が見つかりませんでした。")
            return None
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"🟡 記事名 '{title}' は曖昧です。候補: {e.options[:3]}")
            try:
                first_option = e.options[0]
                print(f"↪️ 最初の候補 '{first_option}' で再試行します。")
                summary = wikipedia.summary(first_option, sentences=sentences, auto_suggest=False)
                return cast(str, summary)
            except Exception as inner_e:
                print(f"❌ 再試行中にエラーが発生しました: {inner_e}")
                return None
        except Exception as e:
            print(f"❌ 記事の要約取得中にエラーが発生しました: {e}")
            return None

    def get_page_content(self, title: str) -> Optional[str]:
        """
        指定されたタイトルの記事の全文コンテンツを取得する。
        """
        try:
            page = wikipedia.page(title, auto_suggest=False, preload=True)
            return cast(str, page.content)
        except wikipedia.exceptions.PageError:
            print(f"🟡 記事 '{title}' が見つかりませんでした。")
            return None
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"🟡 記事名 '{title}' は曖昧です。候補: {e.options[:3]}")
            try:
                first_option = e.options[0]
                print(f"↪️ 最初の候補 '{first_option}' で再試行します。")
                page = wikipedia.page(first_option, auto_suggest=False, preload=True)
                return cast(str, page.content)
            except Exception as inner_e:
                print(f"❌ 再試行中にエラーが発生しました: {inner_e}")
                return None
        except Exception as e:
            print(f"❌ 記事のコンテンツ取得中にエラーが発生しました: {e}")
            return None
```

### `services/worker_manager.py`

```python
# path: ./services/worker_manager.py
# title: External Worker Manager Service with Robust IPC
# description: プロセス間通信をより堅牢にするため、バイナリでデータを受け取り、明示的にUTF-8でデコードする。

import sys
import json
import subprocess
import traceback
from typing import List, Any, Dict, cast
from domain.schemas import ExpertModel
from llama_cpp.llama_types import ChatCompletionRequestMessage
import torch
from diffusers import DiffusionPipeline, AutoencoderKL

class WorkerExecutionError(Exception):
    """ワーカープロセスの実行エラー"""
    pass

class WorkerManagerService:
    """
    外部ワーカープロセスを呼び出し、LLMや拡散モデルの推論を実行するサービス
    """
    def invoke_llm_worker(self, expert: ExpertModel, messages: List[ChatCompletionRequestMessage]) -> Dict[str, Any]:
        """
        LLMワーカーをサブプロセスとして実行し、結果を返す
        """
        if not expert.model_path:
            raise ValueError(f"エキスパート '{expert.name}' に model_path が設定されていません。")

        payload = {
            "model_path": expert.model_path,
            "messages": messages,
            "chat_format": expert.chat_format,
        }

        try:
            python_executable = sys.executable
            timeout_seconds = 180 

            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            process = subprocess.run(
                [python_executable, "-m", "agents.worker"],
                input=json.dumps(payload, ensure_ascii=False).encode('utf-8'), # 明示的にUTF-8でエンコード
                capture_output=True,
                check=True,
                timeout=timeout_seconds
                # text=True と encoding='utf-8' を削除し、バイナリでやり取りする
            )
            
            # ワーカーからの標準出力をUTF-8でデコードしてからJSONとしてパース
            response_str = process.stdout.decode('utf-8')
            response_data = cast(Dict[str, Any], json.loads(response_str))
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            
            if "error" in response_data:
                raise WorkerExecutionError(f"ワーカープロセスでエラーが発生しました: {response_data['error']}\nTrace: {response_data.get('traceback', '')}")

            return response_data
        
        except subprocess.TimeoutExpired:
            raise WorkerExecutionError(
                f"思考エンジンの応答がタイムアウトしました ({timeout_seconds}秒)。"
                "エンジンがハングアップした可能性があります。"
                "詳細はプロジェクト内の logs/worker.log ファイルを確認してください。"
            )
        except FileNotFoundError:
            raise WorkerExecutionError(f"ワーカープロセス '{python_executable} -m agents.worker' を実行できません。パスを確認してください。")
        except subprocess.CalledProcessError as e:
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            # エラー出力もデコードして表示
            stderr_str = e.stderr.decode('utf-8') if e.stderr else "No stderr"
            raise WorkerExecutionError(f"ワーカープロセスの実行に失敗しました。\nStderr: {stderr_str}")
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        except json.JSONDecodeError as e:
            raise WorkerExecutionError(f"ワーカーからの応答がJSON形式ではありませんでした。Raw output: {e.doc}")
        except Exception as e:
            raise WorkerExecutionError(f"ワーカー管理中に予期せぬエラーが発生しました: {e}")

    def invoke_diffusion_worker(self, expert: ExpertModel, prompt: str) -> Any:
        """
        拡散モデルを直接ロードして実行（こちらは比較的安定しているためプロセス分離しない）
        """
        if not expert.model_id:
            raise ValueError("拡散モデルのmodel_idが設定されていません。")
        
        try:
            device = "cpu"
            if torch.backends.mps.is_available(): device = "mps"
            elif torch.cuda.is_available(): device = "cuda"
            
            vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16)
            pipe = DiffusionPipeline.from_pretrained(
                expert.model_id, vae=vae, torch_dtype=torch.float16, variant="fp16", use_safetensors=True
            )
            pipe = pipe.to(device)
            
            image = pipe(prompt=prompt).images[0]
            return image
        except Exception as e:
            print(f"❌ 拡散モデルの実行中にエラーが発生しました: {e}")
            traceback.print_exc()
            raise
```

### `transformer_test.py`

```python
# /hybrid_llm_system/transformer_test.py
# Transformerモデルの動作を最小構成でテストするためのスクリプト (mypy対応版)

import sys
import os
from llama_cpp import Llama
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage # 追加

def main() -> None:
    """
    Transformerモデルの最小環境テストを実行するメイン関数
    """
    print("--- Transformerモデルの最小環境テストを開始します ---")

    model_path: Optional[str] = None
    try:
        # .envファイルから環境変数を読み込み
        load_dotenv()
        model_path = os.getenv("TRANSFORMER_MODEL_PATH")

        if not model_path:
            print("❌ エラー: .envファイルにTRANSFORMER_MODEL_PATHが設定されていません。")
            return
        
        if not os.path.exists(model_path):
            print(f"❌ エラー: モデルファイルが見つかりません。パスを確認してください: {model_path}")
            return

        print(f"モデルパス: {model_path}")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
        
        # モデルの初期化 (gemmaフォーマット)
        llm = Llama(
            model_path=model_path,
            n_ctx=8192,
            n_gpu_layers=-1,  # -1で全てのレイヤーをGPUに割り当てる
            verbose=log_verbose,
            chat_format="gemma" 
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        print("✅ モデルの初期化に成功しました。")

        # チャット形式のプロンプトを作成
        messages: List[ChatCompletionRequestMessage] = [ # 型を修正
            {"role": "system", "content": "You are a helpful and intelligent assistant for coding. Provide clean, efficient, and well-commented code."},
            {"role": "user", "content": "Could you please implement a simple web server in Python?"}
        ]
        
        print("\n--- 応答を生成します... ---")
        
        # チャット補完APIを呼び出し
        response: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=1024,
            temperature=0.7
        )
        
        print("\n--- 応答の生成に成功しました！ ---")

        if "choices" in response and response["choices"]:
            choice = response["choices"][0]
            if "message" in choice and "content" in choice["message"]:
                content: Optional[str] = choice["message"]["content"]
                if content is not None:
                    print("\n[モデルからの応答]")
                    print(content.strip())
                else:
                    print("応答メッセージにテキストが含まれていません。")
            else:
                print("応答メッセージの形式が正しくありません。")
        else:
            print("応答内容が空か、予期しない形式です。")
            print(f"受信したデータ: {response}")

    except Exception as e:
        print(f"\n❌ テスト中に予期せぬエラーが発生しました: {e}")

    print("\n--- テストを終了します ---")

if __name__ == "__main__":
    main()
```

### `utils/__init__.py`

```python
# /hybrid_llm_system/utils/__init__.py
# (このファイルは空のままで構いません)
```

### `utils/monitoring.py`

```python
# /hybrid_llm_system/utils/monitoring.py
# システムリソース（メモリ、CPU）を監視するためのユーティリティ

import psutil
import os

def print_memory_usage(context: str = "CURRENT") -> None:
    """
    現在のプロセスのメモリ使用状況を詳細に表示する
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    
    # メガバイト単位に変換
    rss_mb = mem_info.rss / (1024 * 1024)
    vms_mb = mem_info.vms / (1024 * 1024)
    
    print(
        f"--- 📊 Memory Usage ({context}) ---\n"
        f"  - RSS: {rss_mb:.2f} MB (物理メモリ)\n"
        f"  - VMS: {vms_mb:.2f} MB (仮想メモリ)\n"
        f"------------------------------------"
    )
```

### `utils/thought_logger.py`

```python
# path: ./utils/thought_logger.py
# title: Thought Process Logger
# description: Formats and displays the thought process stored in the GlobalWorkspace.

from typing import List, Dict, Any

class ThoughtLogger:
    """
    思考プロセスを人間が読みやすい形式で表示するためのクラス
    """

    @staticmethod
    def format_thoughts(thought_process: List[Dict[str, Any]]) -> str:
        """
        思考プロセスのリストを整形された文字列に変換する
        """
        if not thought_process:
            return "思考の記録はありません。"

        formatted_lines = ["# HiPLE Thought Process Log"]
        
        for i, thought in enumerate(thought_process):
            source = thought.get("source", "Unknown")
            thought_type = thought.get("type", "Generic")
            content = thought.get("content", "")

            header = f"\n--- Step {i+1}: [{source.upper()}] - {thought_type.replace('_', ' ').title()} ---"
            formatted_lines.append(header)

            if isinstance(content, dict):
                for key, value in content.items():
                    # Noneや空のリストは表示しない
                    if value is not None and value != []:
                        formatted_lines.append(f"  - {key.replace('_', ' ').title()}: {value}")
            elif isinstance(content, list):
                 for item in content:
                    formatted_lines.append(f"  - {item}")
            else:
                content_str = str(content)
                if len(content_str) > 150:
                    indented_content = "\n".join(["    " + line for line in content_str.splitlines()])
                    formatted_lines.append(f"  Content:\n{indented_content}")
                else:
                    formatted_lines.append(f"  {content_str}")

        return "\n".join(formatted_lines)
```

### `visualizer_test.py`

```python
# /hybrid_llm_system/visualizer_test.py
# 拡散モデル(Stable Diffusion)の動作を最小構成でテストするスクリプト

import os
import torch
from dotenv import load_dotenv
from diffusers import DiffusionPipeline, AutoencoderKL
from typing import Optional

def main() -> None:
    """
    拡散モデルの最小環境テストを実行するメイン関数
    """
    print("--- 拡散モデル(Stable Diffusion)の最小環境テストを開始します ---")
    
    try:
        load_dotenv()
        # .envファイルからHugging FaceのモデルIDを取得
        model_id: Optional[str] = os.getenv("VISUALIZER_MODEL_ID")

        if not model_id or not model_id.strip():
            print("❌ エラー: .envファイルにVISUALIZER_MODEL_IDが設定されていません。")
            print("   (例: VISUALIZER_MODEL_ID=\"stabilityai/stable-diffusion-xl-base-1.0\")")
            return
        
        # GGUFファイルパスが誤って設定されていないかチェック
        if ".gguf" in model_id.lower():
            print(f"❌ エラー: VISUALIZER_MODEL_IDにはGGUFファイルのパスではなく、Hugging FaceのリポジトリIDを設定してください。")
            print(f"   現在の値: {model_id}")
            print(f"   正しい例: \"stabilityai/stable-diffusion-xl-base-1.0\"")
            return

        print(f"Hugging Face モデルID: {model_id}")

        # デバイスの自動選択 (MPS > CUDA > CPU)
        device = "cpu"
        if torch.backends.mps.is_available():
            device = "mps"
        elif torch.cuda.is_available():
            device = "cuda"
        
        print(f"使用デバイス: {device}")

        # VAE (Variational Auto Encoder) を個別にロード
        # これにより、特定の環境での黒い画像が出力される問題を回避
        vae = AutoencoderKL.from_pretrained(
            "madebyollin/sdxl-vae-fp16-fix", 
            torch_dtype=torch.float16
        )

        # 拡散モデルのパイプラインを初期化
        # 'from_pretrained'はリポジトリIDを元にHugging Face Hubからモデルをダウンロードします
        pipe = DiffusionPipeline.from_pretrained(
            model_id,
            vae=vae,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True
        )
        pipe = pipe.to(device)
        
        print("✅ モデルの初期化に成功しました。")

        # 画像生成用のプロンプト
        prompt = "A cinematic shot of a baby raccoon wearing an intricate italian mafioso suit, saying 'oh no'."

        print(f"\n--- 以下のプロンプトで画像を生成します... ---\n{prompt}")
        
        # 画像を生成
        image = pipe(prompt=prompt).images[0]
        
        print("\n--- 画像の生成に成功しました！ ---")

        # 出力ディレクトリを作成
        output_dir = "output/images"
        os.makedirs(output_dir, exist_ok=True)
        
        # ファイルを保存
        output_path = os.path.join(output_dir, "visualizer_test_output.png")
        image.save(output_path)
        
        print(f"\n🖼️ 画像を保存しました: {os.path.abspath(output_path)}")

    except Exception as e:
        print(f"\n❌ テスト中に予期せぬエラーが発生しました: {e}")
        import traceback
        traceback.print_exc()

    print("\n--- テストを終了します ---")

if __name__ == "__main__":
    main()
```

### `workspace/__init__.py`

```python
# /hybrid_llm_system/workspace/__init__.py
```

### `workspace/global_workspace.py`

```python
# path: ./workspace/global_workspace.py
# title: Global Workspace with Clear Functionality
# description: 思考の履歴と状態を管理する。新しい対話サイクルを開始するためにクリア機能を追加。

import copy
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage

class GlobalWorkspace:
    """
    エキスパート間の思考プロセスと履歴を共有・管理するグローバル・ワークスペース
    """
    def __init__(self) -> None:
        self.original_prompt: str = ""
        self.thought_process: List[Dict[str, Any]] = []
        self.final_answer: Optional[str] = None
        self.chat_histories: Dict[str, List[ChatCompletionRequestMessage]] = {}

    def clear(self) -> None:
        """ワークスペースの状態をリセットする"""
        self.original_prompt = ""
        self.thought_process = []
        self.final_answer = None
        # chat_historiesはセッション間で維持するためクリアしない

    def set_initial_prompt(self, prompt: str) -> None:
        """ユーザーからの最初のプロンプトを設定する"""
        self.original_prompt = prompt
        self.add_thought("user", "initial_prompt", prompt)
    
    def add_thought(self, source: str, thought_type: str, content: Any) -> None:
        """思考プロセスに新しいステップを追加する"""
        self.thought_process.append({
            "source": source,       # "user", "orchestrator", "expert:jamba", etc.
            "type": thought_type,   # "initial_prompt", "plan", "expert_query", "expert_response"
            "content": content
        })

    def get_last_thought(self) -> Optional[Dict[str, Any]]:
        """最後の思考ステップを取得する"""
        return self.thought_process[-1] if self.thought_process else None

    def get_full_history_for_expert(self, expert_name: str) -> List[ChatCompletionRequestMessage]:
        """特定のエキスパートの完全な会話履歴を取得する"""
        return copy.deepcopy(self.chat_histories.get(expert_name, []))

    def update_expert_history(self, expert_name: str, user_content: str, assistant_content: str) -> None:
        """特定のエキスパートの会話履歴を更新する"""
        if expert_name in self.chat_histories:
            self.chat_histories[expert_name].append({"role": "user", "content": user_content})
            self.chat_histories[expert_name].append({"role": "assistant", "content": assistant_content})

    def set_final_answer(self, answer: str) -> None:
        """最終的な回答を設定する"""
        self.final_answer = answer
        self.add_thought("orchestrator", "final_answer", answer)
```

