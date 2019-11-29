
count = 0
open("1.txt") do file
  for line in eachline(file)
    global count += parse(Int, line)
  end
end
println(count)
