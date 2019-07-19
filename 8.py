import turtle

ts = turtle.getscreen()
turtle.ht()

fname = 'graph.eps'
# Prime numbers forming the final number
nums = [2, 3, 5, 7, 11, 13, 17, 19]
# The final number
n = 1
for i in nums:
    n *= i
# You can change the tuple in the first line of dictionary, based on your own resolution.
# Must be less than half of your width
available = {n: (0, -330)}
directions = {2: 0,
              3: 45,
              5: 90,
              7: 135,
              11: 22.5,
              13: 67.5,
              17: 112.5,
              19: 157.5,}

turtle.speed(0)
for i in range (n, 0, -1):
    if n % i==0:
        turtle.up()
        turtle.setpos(available[i])
        turtle.down()
        for num in nums:
             if i%num == 0:
                turtle.seth(directions[num])
                turtle.forward(100)
                available[i//num] = turtle.pos()
                turtle.goto(available[i])

ts.getcanvas().postscript(file=fname)

print ('Saved image to: ', fname)
print ('All done. Click image to exit.')

turtle.exitonclick()
