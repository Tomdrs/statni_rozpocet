function display_number(number, zero_if_undef = true, allow_negative = false) {
    if (number)
        return (allow_negative ? number : Math.max(number, 0)).toFixed(2);
    else return zero_if_undef ? 0 : "";
}

function random_string() {
    return (Math.random() + 1).toString(36).substring(7);
}

function get_user_query(client) {
    return `user_id.id = \"${client.authStore.model.id}\"`;
}

function remove_first_match(arr, condition) {
    let index;

    for (const element of arr.entries()) {
        if (condition(element[1])) {
            index = element[0];
            break;
        }
    }

    if (typeof index !== "undefined") {
        arr.splice(index, 1);
    }
}


// https://stackoverflow.com/questions/9038625/detect-if-device-is-ios
// ...
// Apple is run by bad people who hate fun
function detect_ios_method2() {
    return [
    'iPad Simulator',
    'iPhone Simulator',
    'iPod Simulator',
    'iPad',
    'iPhone',
    'iPod'
    ].includes(navigator.platform)
    // iPad on iOS 13 detection
    || (navigator.userAgent.includes("Mac") && "ontouchend" in document)
}

// https://stackoverflow.com/questions/9038625/detect-if-device-is-ios
// ...
// Agony
function detect_ios_method3() {
    var iosQuirkPresent = function () {
        var audio = new Audio();

        audio.volume = 0.5;
        return audio.volume === 1;   // volume cannot be changed from "1" on iOS 12 and below
    };

    var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
    var isAppleDevice = navigator.userAgent.includes('Macintosh');
    var isTouchScreen = navigator.maxTouchPoints >= 1;   // true for iOS 13 (and hopefully beyond)

    return isIOS || (isAppleDevice && (isTouchScreen || iosQuirkPresent()));
}

function detect_mobile() {
    // https://stackoverflow.com/questions/3007480/determine-if-user-navigated-from-mobile-safari
    var ua = window.navigator.userAgent;
    var iOS = !!ua.match(/iPad/i) || !!ua.match(/iPhone/i);
    var webkit = !!ua.match(/WebKit/i);
    var iOSSafari = iOS && webkit && !ua.match(/CriOS/i);

    return (
        screen.orientation.type == "portrait-primary" ||
        screen.orientation.type == "portrait-secondary" ||
        iOSSafari ||
        detect_ios_method2() ||
        detect_ios_method3()
    );
}
