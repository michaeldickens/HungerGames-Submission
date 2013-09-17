Hunger Games Strategy
=====================

Author: Michael Dickens

Created: 2013-07-25

This document describes the process by which I devised my strategy for Brilliant's Hunger Games (https://brilliant.org/competitions/hunger-games/).

Special thanks to Chad Miller for writing a test program.

The Importance of Context
-------------------------
In the process of designing my strategy, I created about ten different strategies and pitted them against each other. I found that which strategy won depended heavily on who was competing.

I found that there are two main types of strategies: "mostly-slack" and "friendly". The "mostly-slack" players will slack off most or all of the time, while the "friendly" players will usually hunt (although they may choose to slack for certain specific reasons). If close to half of the players use "mostly-slack" strategies, certain types of players will tend to win; if not very many players use "mostly-slack" strategies, entirely different types of players will perform well.

In particular, the Freeloader strategy (i.e. the strategy that slacks every time) wins in a "mostly-slack" environment, but loses where most players use "friendly" strategies. I found that Freeloaders usually win if they make up about 3/8 or more of the total population, and lose otherwise.

I expect that fewer than 3/8 of teams will submit "mostly-slack" strategies, so I should not submit a "mostly-slack" strategy myself.

Unfortunately, this does not do much to narrow down the solution space. When I made small tweaks to the players in my simulated competition, it radically altered the outcome. Among players `[A, B, C, D, E, F]`, player `A` wins, but among players `[A, B, C, D, F, G]`, player `B` wins instead.

The real challenge of this competition, then, is not to design a winning strategy; there is no strategy that wins in the general case. Rather, one must *predict the other players' strategies* and then design a strategy that wins *against them*. In other words, determine what the *context* will be, and use a strategy that wins in that context.

This is how I decided on a strategy.

Reciprocity
-----------

Many contestants in The Hunger Games probably know about how the legendary Tit-for-Tat strategy conquered all others with its simple principle of reciprocity. I expect that many teams will learn a certain lesson from this: reciprocate others' actions, and you will go far. Indeed, I attempted to implement a variant of Tit-for-Tat as soon as I started working on the contest.

How exactly should Tit-for-Tat be adapted for The Hunger Games? Players are anonymous, so you can't reciprocate directly. But players *do* have reputation. A reciprocating player hunts with other players who have a reputation for hunting, and slacks against players with a reputation for slacking.

This was the first strategy I implemented. Even as I implemented more strategies, the reciprocating strategy continued to win in most cases.

How to Outperform a Reciprocator
--------------------------------

A Reciprocator can be tricked.

Consider a strategy called the Lazy Hunter. The Lazy Hunter maintains a certain reputation (say, 0.5) in order to get Reciprocators to hunt with him; within this constraint, it slacks off as much as possible. If it chooses the correct reputation cutoff, it tricks Reciprocators into hunting with it and then takes advantage of them.

Based on my tests, Lazy Hunters beat Reciprocators and perform reasonably well against various other strategies, assuming they choose the correct reputation to maintain.

If a Lazy Hunter chooses a reputation that's too low, it will lose to Reciprocators. If it chooses a reputation that's too high, it will hunt too often when it could get away with slacking off. Some Reciprocators may anticipate the existence of Lazy Hunters, and only choose to reciprocate with players who have a reputation at some level *above* 0.5 (perhaps 0.51 or 0.6). I can counter this by setting my Lazy Hunter to maintain a reputation slightly above 0.51 or 0.6.

Will Reciprocators anticipate my counter against their counter? Probably not. In [this Prisoner's Dilemma tournament](http://lesswrong.com/lw/7f2/prisoners_dilemma_tournament_results/), most users tried to counter their opponents. Only one strategy countered the others' counters, and this strategy ended up winning. From this, we learn that most people think one step ahead; you can win by thinking two steps ahead. Thinking three steps ahead is probably unnecessary.

How to Win
----------

I expect to see a lot of players play both the Reciprocator and the Lazy Hunter strategies. I talked to a friend of mine and he independently came up with the Lazy Hunter strategy, which makes me think it's more likely to be played.

If the tribe contains no Reciprocators, then Lazy Hunters lose badly to Freeloaders -- the Lazy Hunters don't penalize the Freeloaders for slacking off every time. However, when there are even a small number of Reciprocators, Lazy Hunters win. The best-performing Lazy Hunter is the one that accurately predicts about how "forgiving" most of the Reciprocators will be.

So what strategy will perform best? To know that, I'd need to know what strategies the other players are using.

I can't know what the other players will do, but I can make an educated guess. I read about some different Iterated Prisoner's Dilemma strategeis and converted them into Hunger Games strategies; I also spoke to a few friends about what strategies they would use. Then I threw all of these strategies into a pool to see who would win.

Based on my tests, it looks like a Lazy Hunter will win; any time I try to develop a more sophisticated strategy, it doesn't perform as well. This makes sense: as we have learned from previous game theory competitions, a simple algorithm usually wins.

I expect that many players will submit a Lazy Hunter or some similar strategy, and I expect that one of these strategies will win. My best bet is to be one of these submitters, and hopefully mine will be the one that wins.
