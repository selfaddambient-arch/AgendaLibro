### 3-4　Building for Everyone from the Start

I make a tool for my own shop, then hand it out to other shops too. It sounds simple when you say it, but to do it, the way you decide things before you start building has to change.

If I were building only for Tamuro, the quickest way would be to write Tamuro's business hours and Tamuro's name directly into the program. But then no other shop could use it. If you try to make it general-purpose later, you end up hunting down every hard-coded spot and fixing them one by one.

So the tools in the Agenda series are specified from the beginning on the premise that everyone can use them. I start from a problem at Tamuro, but at the requirements stage I separate two questions: "Is this only true of Tamuro, or is it true of every shop?" Don't put the shop's name on the sign. Let people choose the language. Make it pasteable into any website. I settled decisions like these while writing the requirements document for the Light Notebook.

This is another use for the requirements definition I relearned in Chapter 2. If you decide these things first, you can use the tool at Tamuro and hand it out to other shops as it is.

The problems in my shop are also the problems in other shops. I'm not the only owner who wants to tell customers that closing time is running late. An owner of an independent shop builds a tool out of their own problem, then hands it out to other shops. That is the idea behind the Agenda series.

### 3-5　The Democratization of Technology

The Agenda series now has more than 10 products. I build them and run them alone, while standing behind the bar.

A few years ago, this would have been unthinkable. To build one product, you needed someone to plan it, someone to design the screens, someone to write the code, someone to test it, and someone to operate it. Without a team and funding, you couldn't put a product into the world.

That is no longer true. The owner tells the AI the requirements, the AI writes the code, the AI tests it, and another AI audits it. What the owner does is decide what to build, judge whether the AI's results fit the shop's purpose, and do only the operations that humans alone can do.

This kind of change is generally called the "democratization of technology." The power to build is no longer the property of a few people or companies.

But let me be honest here. As I wrote in the Introduction, I worked as a systems engineer for about 16 years. I knew requirements definition, how to think about databases, and how to run tests, all from experience. So I won't claim that someone who has never written a line of code could do the same starting tomorrow.

Even so, a great deal has changed. I can now build, on my own and in the gaps between my main job, things at a scale that once took a team. And for people with no experience, the entrance has certainly gotten lower. AI will teach you if you ask about something you don't understand. It will give shape to what you tell it in words. What's missing is not technique but the ability to decide what to build and the words to tell the AI. Those are abilities that people who run shops use every day anyway.

### 3-6　The "Death of SaaS" Debate

Software that people use over the internet for a monthly fee, like the Agenda series, is called SaaS (Software as a Service). Accounting software, time and attendance management, reservation management. Restaurants today run on a lot of SaaS.

Will AI put an end to SaaS? In 2026, that debate flared up in a big way.

One trigger was a remark by Microsoft CEO Satya Nadella. On a podcast in December 2024, Nadella said that SaaS applications would collapse in the age of AI agents. His reasoning: once AI agents take over the decision-making part of business work, software built for people to operate through screens will no longer be needed.

Then in February 2026, Anthropic announced Claude Cowork (an AI tool that carries out business tasks autonomously), and shares of American software companies were sold off heavily. On Wall Street, the plunge came to be called the "SaaSpocalypse." What investors feared was that if AI agents do the work, the SaaS model of earning a fee per person (per-seat pricing) would fall apart.

There are counterarguments, too. Nvidia CEO Jensen Huang said that AI agents will not replace software but will use software on people's behalf, and called the selloff an overreaction. Quite a few others also see SaaS that absorbs AI as getting stronger, if anything.

Will SaaS really die? Here is what I think.

What dies is the middle layer of SaaS: the kind that charges a high monthly fee per seat and assumes people operate it through screens. If AI does the work in place of people, you don't need seats for each person. If no one is operating a screen, you don't need an elaborate screen.

What remains are tools that are cheap and do one thing reliably. And tools that are easy for AI to use.

This is exactly the three principles of the Agenda series. It runs automatically, it is left to the owner's AI (relying on others), and it does only one thing (single function). AgendaTurno leaves the work of building the shift schedule to the owner's AI, which is just the "AI uses the software" form Huang describes. Tamuro's reservation system opens a window through MCP to customers' AIs, and that is the same idea.

Of course, there may seem to be a contradiction here. I talk about the death of SaaS, yet the Agenda series is itself SaaS. But the Agenda series is a set of tools an owner built for their own shop and then made public at a low price. It is not a model that charges a high monthly fee per seat, and it does not assume that people sit glued to a screen every day. It is built from the start on the premise that AI will use it.

#### "The Death of SaaS" for Restaurants

This debate may sound like a story about investors and the IT industry. But for restaurants, the same thing is about to happen in a much more familiar form.

Many independent shops pay a monthly fee to gourmet sites and reservation sites, and on top of that pay a referral commission for every reservation. In exchange for bringing in customers, the site holds the connection to the customer, and it is not unusual for the shop to lack even the customer's contact information. If prices go up, the shop has no choice but to follow, and if the ranking system changes, the flow of customers changes.

As I wrote in Chapter 1, in 2026 the age began in which customers have their own AI search for shops. If the entrance shifts to AI, the whole arrangement of paying a site monthly fees and commissions to be placed high in its listings starts to wobble. If a shop opens a window to AI on its own, customers can reach it without going through the big sites. The reservation records and the relationship with the customer stay in the shop's hands.

If I put "the death of SaaS" in an independent shop's words, it is "the end of the era when paying got you listed." Tamuro opened its window through MCP, and keeps its reservations and CRM on its own specifications, as preparation for that.

Whether SaaS will die, no one knows yet. But the shape of the tools that will remain in the age of AI is gradually coming into view. That is what I think.

### 3-7　Monetization: Small, Many, Cheap

I build the Agenda series with the aim of making it stand as a business. The aim is to make it a second pillar of income, separate from the restaurant.

I set the prices small and low. Monthly fees start from a few hundred yen. The Time Clock, for example, is ¥500 per month. I also mix in free tools, such as the Profit Planner, the Light Notebook and Recipe Costing. The free tools serve as the entrance by which people get to know the Agenda series. The Light Notebook uses neither a map API nor generative AI, so it costs almost nothing to run. That's why I can give it away free.

There is one account. With a shared account called AgendaID, you can use every tool in the series. You don't need to register again for each tool. Paid tools come with a three-month free period and can be started without registering a card. The free period is available only once per combination of shop and product. If you refer another shop, you get a bonus.

The reason I can keep prices low is in how I build. I build alone, I have AI do the building, and I reuse a shared foundation. The database cost is kept to about $35 per month for the whole series. If the cost to build and the cost to run are both small, a business can stand even on small sales.

Let me be honest. As I write this book, some shops have tried the tools, but there are almost no paid registrations. The system for building is in place, but the system for getting known is still ahead. This book is also meant to be a volume for that purpose, for getting known.

#### Building Something and Keeping People Using It Are Different Things

Let me be honest about one more thing. Being able to build a tool and having someone keep using it are separate matters.

Building has gotten faster thanks to AI. But getting people to keep using it takes other work. Answering questions about how to use it (the Support Guide exists for this). Sending a notice before the free period ends. Explaining the reason when raising a price. Properly deleting the data when someone asks to cancel. And above all, keeping it running without the owner touching it.

Of the three principles of the Agenda series, "automatic" is the principle for this "keep them using it." A tool that doesn't work unless the owner touches it every day will eventually be canceled. It isn't finished when it's built. It becomes a business only when it keeps being used. Adding, one by one, shops that keep using it: that is my job after publishing this book.

#### If You Want to Start at Your Own Shop

For those who read this book and want to try it at their own shop, there are three steps.

1. Open https://bontallc.com/agenda?via=b2-en-{{FMT}} and log in with a Google account (AgendaID will be created. No card registration is needed)
2. First, add one free notebook. I recommend the Light Notebook. You just paste the sign component into your website, and it works in 10 minutes. If you haven't opened yet, try the Profit Planner
3. If it seems to suit you, try the Time Clock free for three months. A notice arrives as the deadline approaches, so you won't be charged even if you leave it alone

If you have questions, ask through the Support Guide (AgendaQA). The AI answers operating questions instantly, and I read questions about specifications and bugs myself.

A restaurant's sales depend on the weather and the season. The number of seats and the business hours both have limits. Tool sales, on the other hand, have no limit on seats. Running a shop while handing out tools born from your own shop's problems, and having that slowly become income: I believe this can become another way for an independent shop to earn.

#### Staying a Small Company, Going Global

There is one more thing I decided about the Agenda series from the start. I would not build it in Japanese alone.

The Time Clock, the Profit Planner and the Support Guide can all be used in 20 languages. The screen text and the frequently asked questions, all of it. A tool built for a 19-seat bar in Tokyo works the same way in English, in Korean, in Vietnamese.

There are two reasons. One is that the problems of restaurants don't change when the country changes. You want to record when staff come and go. You want to know your profitability before opening. You want to tell customers that closing time has been extended. These are all problems that independent shops around the world share. The other is that the number of independent shops in Japan keeps falling. If I served only the Japanese-language market, tool sales would have a ceiling.

In the past, for a small company to sell products overseas, it needed local agents, translation firms and legal entities. Now AI helps with translation and proofreading. Shared payment systems work all over the world. For delivery you only need a server, and there is no stock or warehouse in each country. A tool made by one owner can be on the shelves of the world in 20 languages the day after it's made. In the past, only large companies could do that.

A very small company that does business with multiple countries from the start: such companies are sometimes called micro-multinationals (tiny multinational companies). Bonta LLC aims for exactly that, with one shop in Higashi-Nakano ⟦a residential neighborhood in western Tokyo, just west of Shinjuku⟧ and one owner.

Of course, translating into 20 languages doesn't mean owners abroad will start using it right away. Some of the translations still await review by native speakers to sound natural. Even so, by removing the language barrier from the start, the ceiling on how far the tools can reach disappears, just as the ceiling on seats does.

How I am building that foundation is the story of Chapter 4.

【Figure 3-5】Language switching in the Support Guide. 20 languages are listed ⟦The screen is in Japanese.⟧

## Chapter 4: Technology - A System for Building Products Alone, Continuously

Key points of this chapter

- I turned the procedure for launching a new product into a document, in a form (a skill) that an AI can read and carry out. What humans do is only judgment and the operations that only humans can do
- The shared parts, such as login, billing, introduction pages and guides to other products, are built once and reused across all products. The database cost of that foundation is about $35 per month
- The system is still being grown. I keep adding to the procedure document the failures, such as a design being rejected five times in a row

(This is a chapter with a lot of technical terms. If you aren't interested in the technology, you can skip to Chapter 5 and the story still connects.)

### 4-1　ProductBootstrap: Handing the Launch Procedure Itself to the AI

Every time I built a product, I repeated the same preparation and the same mistakes. Create a repository (a storehouse for programs). Connect login. Decide the design colors. Set up the testing system. Prepare the production environment. I had surely done all of it for the previous product, but I'd forgotten the details and stumbled in the same places.

So I turned the procedure for launching a new product into a document. A form of it that the AI that writes code (Claude Code) can read and carry out is what I call a "skill." The name of this skill is ProductBootstrap. "Bootstrap" is a common term in the computer world for starting up on your own from a minimal mechanism, and I applied it to launching products.

I keep no template program. I copy the most recently completed product and start the new product from it. That way, the newest lessons are automatically passed on to the next product. There is no need to keep maintaining an old template, either.

#### The Flow of the Procedure

1. Hand over the requirements document. If the required fields (product name, what it does, who uses it, price, pricing unit, identifying color, location of the master design, and so on) are left blank, the AI does not start. The rule is that it does not ask the owner questions along the way. If everything isn't in place at the start, it doesn't begin
2. Decide the product's color. Each product in the Agenda series has one identifying color. The AI measures the colors of the existing products, proposes about four candidates that don't overlap, and the owner chooses
3. Fix the design. I have a design AI (Claude Design) create proposals for the screens. The AI runs its self-check up to three rounds, and only proposals that pass the check are shown to the owner
4. Leave the implementation to the AI through to the end. The AI builds and fixes on its own until it meets the set acceptance conditions (type checks, style checks, all tests green, passing every screen check, and database changes going through cleanly in the test environment)
5. The owner approves only when going to production. Everything up to the test environment proceeds unattended, and the owner judges only the production operation

I built the implementation stage so that it doesn't stop midway to wait for the owner's approval. In the early days, I proceeded by asking for approval at each stage, but nothing moved forward that way. When there are several AI work windows, each one stops waiting for approval, and the owner has to go around to every window making judgments. So I changed it: I hand over in advance the range that is already approved and the acceptance conditions that a machine can judge, and it stops only on failure.

The stopping conditions are also set. When the procedure document and the owner's ruling conflict. When an operation only a human can do becomes necessary. When it fails to progress on the same error three times in a row. When authentication lapses, permissions are insufficient, or an irreversible operation is needed. Otherwise, the AI proceeds on its own. The state of the work is recorded in a small file, so even if it crashes midway, it can resume from there.

#### Humans Do Only Two Things

I wrote this in the procedure document: the AI carries out every step. The owner may be asked for only the following two things.

- Judgment itself. Approving, ruling, deciding which of two options to take
- Operations only a human can do. Keys that can be issued only from an external service's admin screen, applications that involve identity verification, operations on a real device and visual judgment

If the AI hands anything else to the owner, that is a violation of the procedure document. In the procedure table, I added an "executor" column to each row, and any row whose owner entry can't state a reason gets switched to the AI's side.

I had a reason for making this rule. When I sorted out the remaining work for one product, the AI lined up "create the server project," "register the login destination," "enter the environment variables," and "build the test environment," all as the owner's tasks. Every one of them was an operation the AI could carry out itself. "Why am I the one doing this?" was my honest reaction at the time. The AI does things itself if you ask. But if you don't ask, it passes them to a person. That's why I had to write it into the procedure document.

I put every failure of the reservation system that I described in Chapter 2 into this procedure document's checklist. Put the tests in first. Don't keep production data in the development environment. Build the test environment first. The next product avoids the same pain from the start.

#### Still Growing

This procedure document is not a finished product. It is something I keep adding to every time something fails.

For example, there was a time when I had the design AI create the screen for one product five times in a row, and all five were rejected. That includes the rounds where I handed it the series-wide design rules (DESIGN.md).

At first, the AI diagnosed the cause as "the color scheme itself." I denied that. The actual causes were two. One was that colors with no definition in the rules were being used freely. The other was that three sections with different roles were stacked vertically with the same background color and the same margins, with no boundary between them. No rule had been violated, yet the roles had disappeared from the look.

So I added clauses to the design rules. Don't give things with different roles the same look. Don't separate them by color alone. The most important thing comes first in the line of sight. Only things that are truly equal may be lined up at the same weight. Don't make a layout that just stacks things vertically.

There was one more lesson from failure. If you convey the "default look to avoid" only as a list of prohibitions, the AI swings entirely to another default that isn't on the list. When I banned cards, shadows and rounded corners all at once, what came back was a newspaper-like screen made of nothing but rules and margins. Since then, I have the request materials written in three columns: "the pattern to avoid," "what I wanted to prohibit," and "what to do instead."

I also changed how I decide identifying colors partway through. Around when products exceeded eight, the band of dark colors was filled by existing products, and the ninth and later products could no longer get a dark color for lines and buttons without colliding with the existing ones. So I revised the rule: a product's identifying color is used only for light surface colors, and lines, rules, icons and main buttons are all unified in the series' shared ink color. It was a constraint that became clear only once the products multiplied.

Every time something fails, I fix the procedure document. The next product gets easier by that much. I believe growing the procedure document is the best investment for continuing to build products alone.

【Figure 4-2】The stages of the launch procedure, and who carries them out (the AI or the owner) ⟦The screen is in Japanese.⟧

【Figure 4-3】The identifying colors of the Agenda series. One color per product, used only on surfaces ⟦The screen is in Japanese.⟧

### 4-2　AgendaHub: The Front Door

As products multiply, you end up building the same things again and again. Login, billing, introduction pages, guides to other products. To run this alone, you need to build the shared parts once and reuse them across all products.

AgendaHub is the place where those shared parts are gathered. I call it the "front door."

First, it is the entrance that routes from one address to every product. Under a single domain, bontallc.com, an entrance for each product is lined up: /agendatimbro, /agendaoro, /agendaluce. To customers it looks as if the products sit inside one site, but in fact a separate program runs behind each.

Next, it is where the product introduction pages are placed. There is one introduction page for the series, and within it a section for each product. Each section holds the product name and its nickname, the price, a problem stated in the owner's own words starting with "When you...," a description of what it can do, and a link to the detail page. When I release a new product, adding this section is included in the launch procedure.

And it is the home of the design rules and the launch procedures. The master of the identifying colors, the screen rules (DESIGN.md), the ProductBootstrap skill I described in 4-1, the skill that checks screens, and the skill that makes database changes safely. For every rule that spans the series, the actual content lives here, and each product reads it by reference.

【Figure 4-1】The structure of the Agenda series. From the front door (AgendaHub) to each notebook, and every notebook connects to one account (AgendaID) ⟦The screen is in Japanese.⟧

### 4-3　AgendaID: Shared Accounts and Billing

AgendaID is the series' shared system for accounts and billing.

An owner who logs in once with a Google account can use every product. There is no need to create an account for each product. I also plan to eventually carry language settings across products.

Billing is also a single system. Instead of building the connection to the payment service (Stripe) for each product, AgendaID takes it all on. There are four pricing categories: a light product at ¥300 per month, a pay-as-you-use product, a one-time purchase product at ¥600, and a free product. Paid products have a three-month free period without card registration, usable once per combination of shop and product. There is also a mechanism that adds three months of free period each to the referrer and the person referred.

Before the free period ends, notification emails arrive seven days and one day ahead. I first built these emails inside the Time Clock too, but as products multiplied I realized it was wasteful to give every product the same mechanism, so I consolidated it on the AgendaID side.

#### Cancellation and Deletion Under Shared Rules, Too

There is a part that is plain but important: cancellation and data deletion.

When a customer cancels, which data is deleted, and when? If you build it separately for each product, something will certainly be missed somewhere. What's more, the Agenda series includes products that handle especially sensitive data, such as the one that identifies regular customers by face recognition.

So I split the granularity of deletion into four levels and made it a rule shared across the series. They are canceling a product, deleting a shop, withdrawing an account (leaving the whole series), and a request for deletion from an individual staff member. The upper levels cascade to the lower ones, and each product registers its own data-deletion procedure with the shared system. The grace period for deletion is 30 days, and during that time it can be undone.

A time axis comes with this. Attendance records, for example, are required by law to be kept for five years. Even if a former staff member requests deletion, within the retention period the record must be kept, with names and the like anonymized, rather than physically erased. I needed to decide the line between "delete" and "keep" by checking it against the law.

#### A Test Login for Keeping the AI from Contaminating Production

I added one more mechanism to AgendaID, for the AI: a test login entrance.

To have the AI check that things work, the AI has to log in and operate the screens. But login is done with a Google account, so the AI can't log in by itself. And I can't hand the owner's account to the AI either. There is a danger that the AI's tests would contaminate production data.

So I built an entrance that issues synthetic accounts (personas) usable only in the test environment. It doesn't work in production. The test environment's database is a separate project from production and contains only synthetic data. The AI logs in through this entrance, operates the screens, and confirms that things work. The test accounts are rebuilt every day, and old ones are deleted.

With this, the AI can carry out even the final check on its own, in an environment built exactly like production, without touching production.