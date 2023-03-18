let POCKETBASE_URL = "https://pocketbase.gjk.cat";

async function remove_user_investment(client, id) {
    await client.collection('user_investments').delete(id);
    return await client.collection('user_investments').getFullList(200, {
        sort: '-created',
        filter: get_user_query(client),
    });
}

async function add_user_investment(client, data) {
    data.user_id = client.authStore.model.id;
    await client.collection('user_investments').create(data);
    return await client.collection('user_investments').getFullList(200, {
        sort: '-created',
        filter: get_user_query(client),
    });
}
async function remove_investment(client, id) {
    await client.collection('investments').delete(id);
    return await client.collection('investments').getFullList(200, {
        sort: '-created',
    });
}

async function add_investment(client, data) {
    await client.collection('investments').create(data);
    return await client.collection('investments').getFullList(200, {
        sort: '-created',
    });
}

async function fetch_budgets(client) {
    return await client.collection('budgets').getFullList(200, {
        sort: '-created',
    });
}
async function fetch_expenses(client) {
    return await client.collection('expenses').getFullList(200, {
        sort: '-created',
    });
}

async function fetch_average(client) {
    return await client.collection('state_levies_average').getFullList(200, {
        sort: '-created',
    });
}

async function fetch_investments(client) {
    return await client.collection('investments').getFullList(200, {
        sort: '-created',
    });
}

async function add_average(client, data) {
    await client.collection('state_levies_average').create(data);
    return await client.collection('state_levies_average').getFullList(200, {
        sort: '-created',
    });
}

async function remove_average(client, id) {
    await client.collection('state_levies_average').delete(id);
    return await client.collection('state_levies_average').getFullList(200, {
        sort: '-created',
    });
}

async function add_expenses(client, data) {
    await client.collection('expenses').create(data);
    return await client.collection('expenses').getFullList(200, {
        sort: '-created',
    });
}

async function remove_expenses(client, id) {
    await client.collection('expenses').delete(id);
    return await client.collection('expenses').getFullList(200, {
        sort: '-created',
    });
}

async function add_budgets(client, data) {
    await client.collection('budgets').create(data);
    return await client.collection('budgets').getFullList(200, {
        sort: '-created',
    });
}

async function remove_budgets(client, id) {
    await client.collection('budgets').delete(id);
    return await client.collection('budgets').getFullList(200, {
        sort: '-created',
    });
}

async function update_investments(client, data) {
    await client.collection('investments').update(data.id, data);
    return await client.collection('investments').getFullList(200, {
        sort: '-created',
    });
}
