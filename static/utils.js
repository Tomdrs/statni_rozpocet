function display_number(number, zero_if_undef = true, allow_negative = false) {
    if (number)
        return (allow_negative ? number : Math.max(number, 0)).toFixed(2);
    else
        return (zero_if_undef ? 0 : "");
}

function random_string() {
    return (Math.random() + 1).toString(36).substring(7);
}

function get_user_query(client) {
    return `user_id.id = \"${client.authStore.model.id}\"`;
}
