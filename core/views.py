from django.shortcuts import render
from blog.models import Post


def index(request):
    titles = [
        "Road Trip Through California",
        "New York City",
        "Discovering the Grand Canyon",
        "The Best of Miami",
        "Yellowstone National Park",
        "Route 66",
        "Las Vegas",
        "Chicago’s Skyline and Deep-Dish Pizza",
        "The Magic of New Orleans",
        "Exploring the Great Smoky Mountains",
        "Washington, D.C.",
        "Seattle and the Pacific Northwest",
        "Texas Road Trip",
        "Paradise Islands for Adventure and Relaxation",
        "The Alaskan Wilderness",
        "Boston’s Historic Freedom Trail",
        "Exploring Utah’s National Parks",
        "The Charm of Charleston and Savannah",
        "Winter Wonderland in Colorado",
        "Top Hidden Gems in the USA"
    ]

    descriptions = [
        "California is a paradise for road trip lovers! Starting in Los Angeles, visit Malibu, drive the iconic Pacific Coast Highway, and finish in San Francisco with Golden Gate Bridge and Alcatraz. Stop at Monterey for 17-Mile Drive views.",
        "New York City is packed with landmarks! Don’t miss the Statue of Liberty, Times Square, Central Park, the Empire State Building, and the Brooklyn Bridge.",
        "Explore the breathtaking Grand Canyon, one of the seven natural wonders of the world. Hike, take a helicopter tour, or just admire the stunning views from the South Rim.",
        "Miami offers white sandy beaches, vibrant nightlife, and incredible Cuban food. Don’t miss South Beach, Wynwood Walls, and Little Havana.",
        "Yellowstone is a wonderland of geysers, hot springs, and wildlife. Visit Old Faithful, the Grand Prismatic Spring, and look for bison roaming freely.",
        "Route 66 is the classic American road trip. Travel from Chicago to Santa Monica, stopping at quirky roadside attractions and historic towns along the way.",
        "Las Vegas is more than casinos! Visit the Neon Museum, Red Rock Canyon, and enjoy world-class shows and dining experiences.",
        "Chicago boasts a stunning skyline and the best deep-dish pizza. Visit Millennium Park, the Art Institute, and take an architecture river cruise.",
        "New Orleans offers jazz, beignets, and rich history. Stroll through the French Quarter, visit a jazz club, and enjoy Creole and Cajun cuisine.",
        "The Great Smoky Mountains are perfect for hiking, wildlife spotting, and scenic drives. Don’t miss Clingmans Dome and Cades Cove.",
        "Washington, D.C. is a treasure trove of history. Visit the Lincoln Memorial, Smithsonian museums, and the U.S. Capitol.",
        "Seattle is a hub for coffee lovers and nature enthusiasts. Visit Pike Place Market, the Space Needle, and nearby Mount Rainier.",
        "Texas is full of surprises! Explore Austin’s live music scene, Dallas’s historic sites, and Houston’s Space Center.",
        "Hawaii offers a mix of adventure and relaxation. Visit active volcanoes, lush rainforests, and enjoy pristine beaches on the islands of Oahu and Maui.",
        "Alaska is an untamed wilderness. Go whale watching, see glaciers, and experience the Northern Lights in the last frontier.",
        "Boston’s Freedom Trail takes you through America’s revolutionary history. Don’t miss Paul Revere’s House and the Boston Tea Party Museum.",
        "Utah’s national parks are breathtaking. Hike through Arches’ iconic rock formations and Zion’s dramatic canyons.",
        "Charleston and Savannah charm visitors with cobblestone streets, historic mansions, and Southern hospitality.",
        "Colorado transforms into a winter paradise. Ski in Aspen, visit hot springs, and enjoy snowshoeing in the Rockies.",
        "Discover lesser-known treasures like Oregon’s Crater Lake, South Dakota’s Badlands, and the hidden beaches of California."
    ]

    return render(
        request=request,
        template_name="core/index.html",
        context={
            "title": "Home",
            "posts": Post.objects.all(),
        }
    )
