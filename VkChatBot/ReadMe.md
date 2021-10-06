# VkChatBot

<h2 align="center"> 
   ⇝ Files Description ⇜
</h2>

<h4>100.jpeg - temp file</h4>
<h4>_token.py - secret info, keep it in .gitignore</h4>
<h4>bot.py - the main code</h4>
<h4>generate_ticket.py - it draws the ticket</h4>
<h4>handlers.py - validation</h4>
<h4>settings.py - scenarions and bot scripts</h4>
<h4>ticket_template.png - it is a template of a ticket, but you can add your own generate_ticket.py</h4>

<h2 align="center"> 
   ⇝ Preparation ⇜
</h2>

<h3 align="center"> 
Install packages to your venv (you can pass the step):
</h3>

```console
pip3 install -r requirements.txt
```

<h2 align="center"> 
    ⇝ Run the bot ⇜
</h2>

```console
python3 bot.py
```

<h2 align="center"> 
    Be sure that you already have secret key and your group id. You have to add it to _token.py. Otherwise it won't work.
</h2>



<h2 align="center"> 
    ⇝ Sample ⇜
</h2>
<a href="https://ibb.co/J2WY10J"><img src="https://i.ibb.co/VD0F1r4/ticket-example.png" alt="ticket-example" border="0" align="center"></a>

<h2 align="center"> 
    ⇝ How it works ⇜
</h2>

<h4 align="center"> 
    User: "Ugh"
</h4>
<h4 align="center"> 
    Bot: "IDK how to answer. But I know where the conference is held and I can send you all the information I know, just ask me" (it was an exception)
</h4>
<h4 align="center"> 
    User: "Register me, please"
</h4>
<h4 align="center"> 
    Bot: "Write your name to register. It will be shown on your badge"
</h4>
<h4 align="center"> 
    User: "Valerii"
</h4>
<h4 align="center"> 
    Bot: "Send your e-mail, we will send all the required information to this address."
</h4>
<h4 align="center"> 
    User: "email@email.com"
</h4>
<h4 align="center"> 
    Бот: "Thanks for your time, Valerii! Your ticket is below, also, we sent the ticket to your email@email.com, print it"
</h4>
<a href="https://ibb.co/J2WY10J"><img src="https://i.ibb.co/VD0F1r4/ticket-example.png" alt="ticket-example" border="0" align="center"></a>
