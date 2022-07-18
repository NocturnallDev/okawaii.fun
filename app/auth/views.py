from . import auth

from app.utils import verify_credentials, protected
 
from quart import request, session, redirect, flash, render_template, abort


@auth.route("/login", methods=["GET","POST"])
async def login():
    if request.method == "POST":
        form = await request.form 

        username = form.get("username")
        password = form.get("password")

        if not username and not password:
            return abort(400)

        if verify_credentials(username, password):
            session["authorized"] = True 
            return redirect("/admin")

        await flash("Invalid credentials.")
        return redirect("/auth/login")
    
    return await render_template("login.html")

@auth.route("/logout")
@protected
async def logout():
    session.clear()
    return redirect("/auth/login")