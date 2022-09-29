class Base{
	say(){return 'say';}
}

class Derived extends Base{
	say(){
    	return super.say();
    }
}

console.log(Derived);