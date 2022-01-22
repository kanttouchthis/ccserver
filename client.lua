upurl = "http://localhost:1234/up"
downurl = "http://localhost:1234/down"
 
function put(source, target, data)
  data = textutils.serialise(data)
  data = textutils.urlEncode(data)
  args = "?source="..source.."&target="..target.."&data="..data
  r = http.get(upurl..args)
end
 
function get(target, source)
  args = "?target="..target.."&source="..source
  r = http.get(downurl..args)
  data = r.readAll()
  data = textutils.unserialise(data)
  return data
end
 
