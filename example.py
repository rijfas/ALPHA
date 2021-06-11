from alpha import Alpha 

alpha = Alpha.instance(actions={
   'hi' : 'hello there',
   'who are you' : 'im alpha',
})
alpha.run()