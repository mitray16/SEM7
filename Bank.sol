pragma solidity ^0.4.24;(>= 0.5.8)
contract Bank{
int balance;
constructor() public {
balance=0;}
function withdraw(int amount) public{
if (balance>amount)
{balance = balance - amount;
}
}

function bal() public view returns(int) {
return balance;}
function deposit(int amount) public{
balance = balance+amount;
}
}