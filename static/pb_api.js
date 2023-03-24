const POCKETBASE_URL = "https://pocketbase.gjk.cat";

function fetch_collection(table) {
    return async function (client) {
        return await client.collection(table).getFullList(200, {
            sort: "-created",
        });
    };
}

function add_entry(table) {
    return async function (client, data) {
        return await client.collection(table).create(data);
    };
}

function update_entry(table) {
    return async function (client, data) {
        await client.collection(table).update(data.id, data);
    };
}

function remove_entry(table) {
    return async function (client, id) {
        await client.collection(table).delete(id);
    };
}

const add_user_investment = async (c, d) => {
    d.user_id = c.authStore.model.id;
    return await add_entry("user_investments")(c, d);
};
const remove_user_investment = remove_entry("user_investments");

const fetch_investments = fetch_collection("investments");
const add_investment = add_entry("investments");
const update_investments = update_entry("investments");
const remove_investment = remove_entry("investments");

const fetch_average = fetch_collection("state_levies_average");
const add_average = add_entry("state_levies_average");
const update_average = update_entry("state_levies_average");
const remove_average = remove_entry("state_levies_average");

const fetch_expenses = fetch_collection("expenses");
const add_expenses = add_entry("expenses");
const update_expenses = update_entry("expenses");
const remove_expenses = remove_entry("expenses");

const fetch_budgets = fetch_collection("budgets");
const add_budgets = add_entry("budgets");
const update_budgets = update_entry("budgets");
const remove_budgets = remove_entry("budgets");

async function resolve_valid_years(client) {
    let budgets = await fetch_budgets(client);
    let expenses = await fetch_expenses(client);

    let budget_years = budgets.map((b) => b.year);
    let expense_years = expenses.map((e) => e.year);

    let years = budget_years.filter((element) =>
        expense_years.includes(element)
    );

    return years.sort();
}
