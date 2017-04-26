local addrs = 100000



request = function()
   entry = math.random(100000)
   url_path = "/ep?id=" .. entry
   
   return wrk.format(nil, url_path)
end
