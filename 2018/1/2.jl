
count = 0
saw = Set([count])
open("1.txt") do file
  counts = map(x -> parse(Int, x), readlines(file))
  while true
    for c in counts
      global count += c
      if count in saw
        println(count)
        exit(0)
      end
      push!(saw, count)
    end
  end
end
