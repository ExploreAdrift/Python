let showPark = document.getElementById("onePark")

async function getOnePark(){
    const response = await(await fetch("/api/show_park")).json();
    const {data} = response
    const activities = nameGrab(data[0].activities);
    console.log(data);
    // for(park in data){
        console.log(data[0].fullName)


        showPark.innerHTML +=

        `
        <div class="parkCard">
                <h1 class="text-center text-decoration-underline text-light">${data[0].fullName}</h1> <br>
                
                <div class="d-flex justify-content-evenly text-dark" style="height:overflow;">
                <div class="parkWebsite p-2">
                <p class="fs-4 text-decoration-underline">Park Website</p>
                    <p class="fs-5 text-wrap" style="width:300px ;"><a href="${data[0].url}" class="btn btn-outline-dark text-light">Offical Park Website</a></p>
                    </div>
                    <div class="entranceFee p-2">
                    <p class="fs-4 text-decoration-underline">Entrance Fees</p>
                    <p class="fs-5 text-wrap" style="width:300px ;">${data[0].entranceFees[0].description}</p>
                </div>
                </div>

                <div class="d-flex justify-content-between text-dark mt-3" style="height:overflow;">
                <div class="weather p-2">
                <p class="fs-4 text-light text-decoration-underline">Weather Information</p>
                    <p class="fs-5 text-wrap" style="width:300px ;">${data[0].weatherInfo}</p>
                    </div>
                    <div class="directions p-2">
                    <p class="fs-4 text-light text-decoration-underline">Accessibility</p>
                    <p class="fs-5 text-wrap" style="width:300px ;">${data[0].directionsInfo}</p>
                    </div>
                    <div class="activities p-2">
                    <p class="fs-4 text-light text-decoration-underline">Activities</p>
                    <p class="fs-5 text-wrap" style="width:300px ;">${activities}</p>
                </div>
                </div>
                    <div class="description p-2 text-light mt-3">
                    <h3 class="text-light text-decoration-underline">Description</h3>
                    <p class="fs-4">${data[0].description}</p>
                    </div>
            </div>
            
    
            `
            // }
}
getOnePark();

// this is where we left off. destructing. Info is going into the databse, but not being
    


function nameGrab(list){
    let stufflist = "";
    for( i = 0; i <list.length; i++){
        stufflist += list[i].name + ", "
    }
    return stufflist
}