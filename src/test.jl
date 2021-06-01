a = 1 
println(1)
println(typeof(a))
b = Float16(a)
println(b, ' ', typeof(b))
c = Int(b)
println(c, '\n', typeof(c))
d = 0x1;  println(d, "\n", typeof(d)) # hexadecimal (base 16)
e = 0xff; println(e, ' ', typeof(e))
f = 0x11112222333344445555666677778888
println(f, ' ', typeof(f))
g = 0b10000000000 # binary (base 2)
println(g, ' ', typeof(g))
h = 0o100  # octal (base 8)
println(h, ' ', typeof(h))

println(-0x2, ' ', -0b1, ' ', -0o3, ' ', -0xff) # UInt8でmod
println(-0x0ff) # UInt16でmod

println(typemin(Int64), ' ', typemax(Int64))
for T in [Int8,Int16,Int32,Int64,Int128,UInt8,UInt16,UInt32,UInt64,UInt128]
  println("$(rpad(T,7)): [$(typemin(T)),$(typemax(T))]")
end

println(typemax(Int64) + 1 == typemin(Int64))
println(10^19)

println(5 ⊻ 3) # type: \xor