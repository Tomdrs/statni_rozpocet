/*
 * Pocketbase
 */

async function pb_login(client, email, pass) {
    console.log("login");

    let user_result;

    try {
        client.authStore.clear();
        client = new PocketBase(POCKETBASE_URL);
        window.localStorage.removeItem("pocketbase_auth");
        window.localStorage.removeItem("pb_admin");
        let user = await client
            .collection("users")
            .authWithPassword(email, pass);
        setTimeout(() => (window.location = "/"), 3000);
        user_result = "success";
    } catch (err) {
        console.log(err.message);
        user_result = "error";
    }

    if (user_result == "error") {
        try {
            client.authStore.clear();
            client = new PocketBase(POCKETBASE_URL);
            window.localStorage.removeItem("pocketbase_auth");
            window.localStorage.removeItem("pb_admin");
            let user = await client.admins.authWithPassword(email, pass);
            setTimeout(() => (window.location = "/"), 2000);
            window.localStorage.setItem("pb_admin", "true");
        } catch (err) {
            console.log(err.message);
            return "error";
        }
    }
    return "success";
}

async function pb_signup(client, email, pass, pass_again) {
    console.log("signup");
    try {
        let user = await client.collection("users").create({
            email: email,
            password: pass,
            passwordConfirm: pass_again,
        });
        setTimeout(() => window.location.reload(), 1000);
        return "success";
    } catch (err) {
        if (err.message) {
            let error = err.message;
            return error;
        } else {
            return "other error";
        }
    }
}

function pb_logout(client) {
    client.authStore.clear();
    window.localStorage.removeItem("pocketbase_auth");
    window.localStorage.removeItem("pb_admin");
    window.location = "/";
}

async function restore_login(client) {
    let get_auth = window.localStorage.getItem("pocketbase_auth");

    if (get_auth) {
        let auth = JSON.parse(window.localStorage.getItem("pocketbase_auth"));
        client.authStore.save(auth.token, auth.model);
    }
}

function pb_client() {
    let client = new PocketBase(POCKETBASE_URL);
    client.autoCancellation(false);
    client.afterSend = (r, d) => {
        if (r.status === 401) {
            window.localStorage.removeItem("pocketbase_auth");
            window.localStorage.removeItem("pb_admin");
        }
        return d;
    };
    return client;
}
