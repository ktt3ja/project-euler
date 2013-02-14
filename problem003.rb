n = 600851475143
prime_factors = Array.new
(2..Math.sqrt(n).to_i).each do |d|
  while n % d == 0
    prime_factors.push(d)
    n /= d
    if n <= 1
      break
    end
  end
end

puts prime_factors[-1]
