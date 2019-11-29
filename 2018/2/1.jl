
arrs = [
"abcdef",
"bababc",
"abbcde",
"abcccd",
"aabcdd",
"abcdee",
"ababab",
]
arrs = open("1") do file
  readlines(file)
end

c0 = 0
c1 = 0
for line in arrs
  counts = map(i -> count(j -> j == i, line), collect(Set(line)))
  d0 = false
  d1 = false
  for c in counts
    if c == 2 && !d0
      d0 = true
      global c0 += 1
    end
    if c == 3 && !d1
      d1 = true
      global c1 += 1
    end
  end
end

println(c0)
println(c1)
