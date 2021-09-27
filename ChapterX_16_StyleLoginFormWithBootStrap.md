# Style Login form

- We come back to [www.getbootstrap.com](https://getbootstrap.com/docs/5.1/forms/layout/) to add a Form with password input to out login form

## login.html in the members\templates\registration
- First with run the current login and capture the name of the inputs
- Capture the name of username and name="password"
```html
<input type="text" name="username" autofocus="" autocapitalize="none" autocomplete="username" maxlength="150" required="" id="id_username">
<input type="password" name="password" autocomplete="current-password" required="" id="id_password">
```
- We apply form of password input form bootstrap to our login
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Login</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Login</h1>
<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST">
    {% csrf_token %} 
    
    <div class="row mb-3">
        <label for="username" class="col-sm-2 col-form-label">User Name</label>
        <div class="col-sm-10">
          <input 
            type="text" 
            class="form-control" 
            id="username"
            name = "username">
        </div>
      </div>
      <div class="row mb-3">
        <label for="password" class="col-sm-2 col-form-label">Password</label>
        <div class="col-sm-10">
          <input 
            type="password" 
            class="form-control" 
            id="password"
            name = "password">
        </div>
      </div>

     <button type="submit" class="btn btn-primary">Login</button>

  </form>
</div>

{% endblock%}

```
## Contributing
[TrungNEMO](https://www.facebook.com/trungnemo)

## License
[MIT](https://choosealicense.com/licenses/mit/)
