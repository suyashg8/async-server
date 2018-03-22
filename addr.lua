local addrs = 9999



request = function()
   entry = math.random(9999)
   url_path = "/ep?id=" .. entry
   
   return wrk.format(nil, url_path)
end
