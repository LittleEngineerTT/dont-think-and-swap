const route_mapping = {
    example: {
        route: "example",
        method: "GET",
        content_type: "application/json",
        response_type: "json"
    }
}


export async function send_request(url, target, data){
    const route_info = route_mapping[target];
    const route = route_info["route"];
    const method = route_info["method"];
    const content_type = route_info["content_type"];

    let request_data = {};
    if (Object.keys(data).length > 0) {
        request_data = {
            method: method,
            headers: {
                "Content-Type": content_type
            },
            body: JSON.stringify(data)
        }
    } else {
        request_data = {
            method: method
        }
    }

    return await fetch(url + "/" + route, request_data);
}