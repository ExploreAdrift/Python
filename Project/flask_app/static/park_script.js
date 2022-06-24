const parkList = document.getElementById("parkCard")

async function getParkList(){
    const response = await(await fetch('/api/choose_park')).json();
    const {data} = response
    for(const park of data){
        const activities = nameGrab(park.activities);
        
        parkList.innerHTML += 

        `
        <form action="/submit_park" method="post" class="border-bottom">
            <input type="hidden" name="park_id" value="${park.parkCode}">
            <div class="parkCard text-light">
                <h1 class="text-center mt-4 text-decoration-underline">${park.fullName}</h1> <br>
                <div class="d-flex justify-content-evenly text-decoration-underline me-5" style="height:overflow;">
                    
                    
                </div>
                <div class=" row1 d-flex justify-content-evenly mb-5" style="height:overflow;">
                <div class="parkWebsite p-2">
                <p class="fs-4 me-5">Park Website</p>
                <p class="fs-5 text-wrap" style="width:200px ;"><a href="${park.url}" class="btn btn-outline-light">Official Park Website</a></p>
                </div>
                <div class="entranceFee p-2">
                <p class="fs-4">Entrance Fees</p>
                <p class="fs-5 text-wrap" style="width:400px ;">${park.entranceFees[0].description}</p>
                </div>

                </div>
                
                <div class="d-flex justify-content-between ms-5 me-5  gap: 10%;" style="height:overflow;">
                <div class="weather p-2">
                <p class="fs-4">Weather Information</p>
                    <p class="fs-5 text-wrap mb-4" style="width:400px ;">${park.weatherInfo}</p>
                    </div>
                    <div class="directions p-2">
                    <p class="fs-4">Accessibility</p>
                    <p class="fs-5 text-wrap" style="width:400px ;">${park.directionsInfo}</p>
                    </div>
                    <div class="activities p-2">
                    <p class="fs-4">Activities</p>
                    <p class="fs-5 text-wrap" style="width:400px ;">${activities}</p>
                    </div>
                </div>
                <div class="description p-2 text-light mt-3 ms-5 me-5">
                    <h3>Description</h3>
                    <p class="fs-5">${park.description}</p>
                </div>
            </div>
            <div>
            <button type="submit" class="btn btn-info text-light ms-5 mt-3" >Choose this park</button>
            <div>
                <a href="/choose_park" class="btn btn-info text-light ms-5 mt-2 mb-5">Back to top</a>
        </div>
        
        </form>
        
        `


    } 

}
getParkList();


function nameGrab(list){
    let stufflist = "";
    for( i = 0; i <list.length; i++){
        stufflist += list[i].name + ", "
    }
    return stufflist
}
