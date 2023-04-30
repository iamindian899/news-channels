var channelName = 'UCvfH3RaugUbIqY-80iOED4Q';
var thumbsize = '1.jpg';
var iiid = '';
$(document).ready(function () {
    $.get(
        "https://www.googleapis.com/youtube/v3/channels", {

            part: 'contentDetails',
            id: channelName,
            key: 'AIzaSyDaYB_AObzgjlp0iODo6WBE818wcXDWhkg'
        },

            function (data) {
                $.each(data.items, function (i, item) {
                    //console.log(item);
                    pid = item.contentDetails.relatedPlaylists.uploads;
                    getVids(pid);
                });
            }
    );
    function getVids(pid) {
        $.get(
       "https://www.googleapis.com/youtube/v3/playlistItems", {

           part: 'snippet',
           maxResults: 4,
           playlistId: pid,
                key: 'AIzaSyDaYB_AObzgjlp0iODo6WBE818wcXDWhkg'},
           function (data) {
               var output;
               $.each(data.items, function (i, item) {
                   console.log(item);
                   videtitle = item.snippet.title;
                   videoId = item.snippet.resourceId.videoId;
                   output = '<div class="video-container"><iframe frameborder="0" src=\"//www.youtube.com/embed/' + videoId + '"></ifram></div>';
                   //thumbnailbig = '<img  src=\"https://img.youtube.com/vi/' + videoId + '/0.jpg" alt="img" width="680px" height="400px"><a class="js-video-button" data-video-id=' + videoId + ' href="https://www.youtube.com/watch?v=' + videoId + '"><i class="play-icon fa fa-play-circle-o"></i></a>';
                   //thumbnail = '<img src=\"https://img.youtube.com/vi/' + videoId + '/' + thumbsize + '" alt="img" width="108px" height="104px"><a class="js-video-button" data-video-id=' + videoId + ' href="https://www.youtube.com/watch?v=' + videoId + '"><i class="play-icon fa fa-play-circle-o"></i></a>';
                   //vtitle = '<h4 class="entry-title"><a href=\"//www.youtube.com/watch?v=' + videoId + '">' + videtitle + '</a></h4>';
                   thumbnailbig = '<img  src=\"https://img.youtube.com/vi/' + videoId + '/0.jpg" alt="img" width="680px" height="400px"><a class="js-video-button" data-video-id=' + videoId + ' href="#"><i class="play-icon fa fa-play-circle-o"></i></a>';
                   thumbnail = '<img src=\"https://img.youtube.com/vi/' + videoId + '/' + thumbsize + '" alt="img" width="108px" height="104px"><a class="js-video-button" data-video-id=' + videoId + ' href="#"><i class="play-icon fa fa-play-circle-o"></i></a>';
                   vtitle = '<h4 class="entry-title"><a class="js-video-button" data-video-id=' + videoId + ' href="#">' + videtitle + '</a></h4>';
                   
                   // Append to results item
                   if (i == 0) {
                       //$('#leadresult').append(output);
                       $('#leadresult').append(thumbnailbig);
                       $('#leadingtitle').append(vtitle);
                   }
                   if (i == 1) {
                       $('#thumba').append(thumbnail);
                       $('#titlea').append(vtitle);
                   }
                   if (i == 2) {
                       $('#thumbb').append(thumbnail);
                       $('#titleb').append(vtitle);
                   }
                   if (i == 3) {
                       $('#thumbc').append(thumbnail);
                       $('#titlec').append(vtitle);
                   }

               });
               $(".js-video-button").modalVideo({
                   youtube: {
                       controls: 0,
                       nocookie: true
                   }
               });
           }
       );
    }
});