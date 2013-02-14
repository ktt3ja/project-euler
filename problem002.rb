sum, first, second = 0, 1, 1
while second <= 4000000
  first, second = second, first + second
  if second % 2 == 0
    sum += second
  end
end

puts sum
