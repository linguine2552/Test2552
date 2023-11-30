<section class="py-5">
    <div class="container">
        <h2 class="fw-bolder text-center"><b><?= isset($id) ? "Edit Message" : "Create New Message" ?></b></h2>
        <hr>
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10 col-sm-12 col-xs-12">
                <form action="" id="message-form">
                    <input type="hidden" name="id" value="<?= isset($id) ? $id : '' ?>">
                    <input type="hidden" name="to_user" value="<?= isset($to_user) ? $to_user : '' ?>">
                    <div id="filter-holder">
                        <div class="input-group mb-3 input-group-dynamic <?= isset($name) ? 'is-filled' : '' ?>">
                            <label for="user" class="form-label">Recipient <span class="text-primary">*</span></label>
                            <input type="search" id="user" name="user" value="" autofocus class="form-control">
                        </div>
                        <div class="list-group mt-n3 mb-3 bg-light position-relative border rounded-0 d-none" id="user-filter"></div>
                    </div>
                    <div class="form-group mb-3 d-none" id="uselected-holder">
                        <label for="user" class="form-label">Recipient <span class="text-primary">*</span></label> <br>
                        <div class="d-flex align-items-center justify-content-between bg-light bg-gradient border px-2 py-1 rounded-pill w-auto">
                            <span>
                                <span>
                                    <img src="" id="selected-img" class="border rounded-circle" alt="">
                                </span> 
                                <span id="selected-username" class="ms-4"></span>
                            </span>
                            <a class="text-muted d-flex align-items-bottom" id="close-selected" href="javascript:void(0)"><span class="material-icons">close</span></a>
                        </div>
                    </div>
                    <div class="input-group input-group-dynamic mb-3 <?= isset($name) ? 'is-filled' : '' ?>">
                        <label for="subject" class="form-label">Subject <span class="text-primary">*</span></label>
                        <input type="text" id="subject" name="subject" value="" class="form-control" required="required">
                    </div>
                    <div class="form-group mb-3">
                        <label for="message" class="form-label">Message <span class="text-primary">*</span></label>
                        <textarea rows="10" id="message" name="message" class="form-control" required="required"></textarea>
                    </div>
                    <div class="row">
                        <div class="col-md-12 text-center">
                            <button type="submit" class="btn bg-primary bg-gradient btn-sm text-light w-25"><span class="material-icons">send</span> Send</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</section>
<noscript id="user-filter-clone">
<a href="javascript:void(0)" class="list-group-item list-group-item"></div>
    <div class="d-flex w-100 align-items-center">
        <div class="col-1 text-center">
            <img src="" class="image-thumbnail border rounded-circle image-user-avatar-filter" alt="">
        </div>
        <div class="col-11">
            <div class="lh-1">
                <h4 class="fw-bolder uname mb-0">Mark Cooper</h4>
                <small class="username">mcooper</small>
            </div>
        </div>
    </div>
</a>
</noscript>
<script>
    var fuser_ajax;
    $(function(){
        $('#message').summernote({
            placeholder: 'Write your message here',
            tabsize: 2,
            height: '40vh',
            toolbar: [
                ['style', ['style']],
                ['font', ['bold', 'underline', 'clear']],
                ['color', ['color']],
                ['para', ['ul', 'ol', 'paragraph']],
                ['table', ['table']],
                ['insert', ['link', 'picture', 'video']],
                ['view', ['fullscreen', 'codeview', 'help']]
            ]
      });
        $('#message-form').submit(function(e){
            e.preventDefault()
            $('.pop-alert').remove()
            var _this = $(this)
            var el = $('<div>')
            el.addClass("pop-alert alert alert-danger text-light")
            el.hide()
            if($('[name="to_user"]').val() == ''){
                el.text('Recepient is required.')
                _this.prepend(el)
                el.show('slow')
                $('html, body').scrollTop(_this.offset().top - '150')
                return false;
            }
            start_loader()
            $.ajax({
                url:'./classes/Master.php?f=save_message',
                method:'POST',
                data:$(this).serialize(),
                dataType:'json',
                error:err=>{
                    console.error(err)
                    el.text("An error occured while saving data")
                    _this.prepend(el)
                    el.show('slow')
                    $('html, body').scrollTop(_this.offset().top - '150')
                    end_loader()
                },
                success:function(resp){
                    if(resp.status == 'success'){
                        location.href= './?page=inbox';
                    }else if(!!resp.msg){
                        el.text(resp.msg)
                        _this.prepend(el)
                        el.show('slow')
                        $('html, body').scrollTop(_this.offset().top - '150')
                    }else{
                        el.text("An error occured while saving data")
                        _this.prepend(el)
                        el.show('slow')
                        $('html, body').scrollTop(_this.offset().top - '150')
                    }
                    end_loader()
                    console

                }
            })
        })

        $('#user').on('input', function(){
            var search = $(this).val();
            if(search == '' || search == null){
               if($('#user-filter').hasClass('d-none') == false)
                $('#user-filter').addClass('d-none');
                return false;
            }
            if(fuser_ajax){
                fuser_ajax.abort()
            }
            fuser_ajax = $.ajax({
                url:'classes/Master.php?f=find_user',
                method:'POST',
                data:{search:search},
                dataType:'json',
                error:err=>{
                    console.log(err)
                },
                success:function(resp){
                    if(resp.status == 'success'){
                        var data = resp.data
                        $('#user-filter').html('')
                        Object.keys(data).map(k=>{
                            var li = $($('noscript#user-filter-clone').html()).clone()
                            li.find('.uname').text(data[k].name)
                            li.find('.username').text(data[k].username)
                            li.find('.image-user-avatar-filter').attr('src',data[k].avatar)
                            $('#user-filter').append(li)
                            li.click(function(){
                                $('[name="to_user"]').val(data[k].id)
                                $('#selected-img').attr('src', data[k].avatar)
                                $('#selected-username').text(data[k].username)
                                $('#user-filter').html('')
                                $('#user').val('').trigger('input')
                                $('#uselected-holder').removeClass('d-none')
                                $('#filter-holder').addClass('d-none')
                            })
                        })
                        $('#user-filter').removeClass('d-none')
                    }
                }
            })
        })
        $('#close-selected').click(function(){
            $('[name="to_user"]').val('')
            $('#selected-img').attr('src', '')
            $('#selected-username').text('')
            $('#user-filter').html('')
            $('#uselected-holder').addClass('d-none')
            $('#filter-holder').removeClass('d-none')
            $('#user').val('').trigger('input').focus()
        })
    })
</script>