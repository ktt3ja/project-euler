def is_palindrome(s)
  if s.length <= 1
    return true
  end
  if s[0] != s[-1]
    return false
  end
  return is_palindrome(s[1..-2])
end

three_digits_pal = Array.new
999.downto 100 do |x_1|
  999.downto 100 do |x_2|
    if is_palindrome((x_1*x_2).to_s)
      three_digits_pal.push(x_1 * x_2)
    end
  end
end

puts three_digits_pal.sort()[-1]

