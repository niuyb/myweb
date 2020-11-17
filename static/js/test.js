


function test_Vue(){
    new Vue({
        el: "#test",
        // mixins: [Pagination_mixin],
        delimiters: ["[[", "]]"],
        data(){
            return{
                page_tools_data:[],
            }
        },
        methods: {
          open() {
            this.$alert('        <div class="naccs">\n' +
                '            <div class="grid">\n' +
                '                <div class="gc gc--1-of-3">\n' +
                '                    <div class="menu">\n' +
                '                        <div class="active"><span class="light"></span><span>投稿电影</span>\n' +
                '                        </div>\n' +
                '                        <div><span class="light"></span><span>投稿图片</span>\n' +
                '                        </div>\n' +
                '                        <div><span class="light"></span><span>投稿工具</span>\n' +
                '                        </div>\n' +
                '                        <div><span class="light"></span><span>投稿生活记录</span>\n' +
                '                        </div>\n' +
                '                    </div>\n' +
                '                </div>\n' +
                '                <div class="gc gc--2-of-3" id="upload">\n' +
                '                    <ul class="nacc">\n' +
                '                        <li class="active">\n' +
                '                            <div id="movies">\n' +
                '                                <div>*电影名称:\n' +
                '                                    <el-input v-model="movies_name" placeholder="电影名称,你必须给我写上"\n' +
                '                                              style="width: 600px"></el-input>\n' +
                '                                </div>\n' +
                '                                <div><br>封面:\n' +
                '\n' +
                '                                    <el-upload\n' +
                '                                            action="/contribution/test"\n' +
                '                                            :show-file-list="false"\n' +
                '                                            :on-success="handleAvatarSuccess"\n' +
                '                                            :before-upload="beforeAvatarUpload"\n' +
                '                                            list-type="picture-card"\n' +
                '                                            :on-preview="handlePictureCardPreview"\n' +
                '                                            :on-remove="handleRemove"\n' +
                '                                    >\n' +
                '                                        <img v-if="imageUrl" :src="imageUrl" class="avatar"\n' +
                '                                             style="max-height: 140px;max-width: 100px">\n' +
                '                                        <i v-else class="el-icon-plus avatar-uploader-icon"></i>\n' +
                '                                    </el-upload>\n' +
                '\n' +
                '\n' +
                '                                    <br/>\n' +
                '                                </div>\n' +
                '\n' +
                '                                <div>电影简介:\n' +
                '                                    <el-input\n' +
                '                                            type="textarea"\n' +
                '                                            autosize\n' +
                '                                            placeholder="给点作用啊,来个介绍吧"\n' +
                '                                            maxlength="400"\n' +
                '                                            v-model="movies_text"\n' +
                '                                            style="width: 600px">\n' +
                '                                    </el-input>\n' +
                '                                </div>\n' +
                '                                <br/>\n' +
                '                                <div>资源链接:\n' +
                '                                    <el-input v-model="movies_url" placeholder="不是吧,资源都要我自己去找么?!"\n' +
                '                                              style="width: 600px"></el-input>\n' +
                '                                </div>\n' +
                '                                <br/>\n' +
                '                                <div>为什么推荐这部电影?\n' +
                '                                    <el-input\n' +
                '                                            type="textarea"\n' +
                '                                            autosize\n' +
                '                                            maxlength="500"\n' +
                '                                            placeholder="why why why? 怎么就喜欢这个了?"\n' +
                '                                            v-model="movies_text_p"\n' +
                '                                            style="width: 600px">\n' +
                '                                    </el-input>\n' +
                '                                </div>\n' +
                '                                <br/>\n' +
                '                                <div style="position: relative; right: -70%">\n' +
                '                                    <el-row>\n' +
                '                                        <el-button type="primary" plain @click="reset">重置</el-button>\n' +
                '                                        <el-button type="success" plain @click="submit">投稿&nbsp!</el-button>\n' +
                '                                    </el-row>\n' +
                '                                </div>\n' +
                '                            </div>\n' +
                '                        </li>\n' +
                '                        <li>\n' +
                '                            <div>\n' +
                '                                <div id="picture">\n' +
                '                                    <div>*图片标题:\n' +
                '                                        <el-input v-model="movies_name" placeholder="你这图挺好看,叫啥啊"\n' +
                '                                                  style="width: 600px"></el-input>\n' +
                '                                    </div>\n' +
                '                                    <div><br>图片:\n' +
                '\n' +
                '                                        <el-upload\n' +
                '                                                action="/contribution/test"\n' +
                '                                                :show-file-list="false"\n' +
                '                                                list-type="picture-card"\n' +
                '                                                :on-success="handleAvatarSuccess"\n' +
                '                                                :before-upload="beforeAvatarUpload"\n' +
                '                                                list-type="picture-card"\n' +
                '                                                :on-preview="handlePictureCardPreview"\n' +
                '                                                :on-remove="handleRemove"\n' +
                '                                        >\n' +
                '                                            <img v-if="imageUrl" :src="imageUrl" class="avatar"\n' +
                '                                                 style="max-height: 140px;max-width: 100px">\n' +
                '                                            <i v-else class="el-icon-plus avatar-uploader-icon"></i>\n' +
                '                                        </el-upload>\n' +
                '\n' +
                '{#                                        <el-upload#}\n' +
                '{#                                        action="/contribution/test"#}\n' +
                '{#                                        :show-file-list="false"#}\n' +
                '{#                                        list-type="picture-card"#}\n' +
                '{#                                        :on-success="handleAvatarSuccess"#}\n' +
                '{#                                        :before-upload="beforeAvatarUpload"#}\n' +
                '{#                                        :on-preview="handlePictureCardPreview"#}\n' +
                '{#                                        :on-remove="handleRemove"#}\n' +
                '{#                                        >#}\n' +
                '{#                                        <img v-if="imageUrl" :src="imageUrl" class="avatar" style="max-height: 140px;max-width: 100px">#}\n' +
                '{#                                        <i class="el-icon-plus avatar-uploader-icon"></i>#}\n' +
                '{#                                        </el-upload>#}\n' +
                '{#                                        <el-dialog :visible.sync="dialogVisible">#}\n' +
                '{#                                          <img width="100%" :src="imageUrl" alt="">#}\n' +
                '{#                                        </el-dialog>#}\n' +
                '\n' +
                '\n' +
                '                                        <br/>\n' +
                '                                    </div>\n' +
                '                                    <div>\n' +
                '                                        <p>图片类型?</p>\n' +
                '                                        <br/>\n' +
                '                                        <el-radio v-model="image_radio" label="1" border style="background-color: #FFB6C1">自然</el-radio>\n' +
                '                                        <el-radio v-model="image_radio" label="2" border style="background-color: #FFB6C1">城市</el-radio>\n' +
                '                                        <el-radio v-model="image_radio" label="3" border style="background-color: #FFB6C1">美丽的皮囊</el-radio>\n' +
                '                                        <br/><br/>\n' +
                '                                        <el-radio v-model="image_radio" label="4" border style="background-color: #FFB6C1">孤寂</el-radio>\n' +
                '                                        <el-radio v-model="image_radio" label="5" border style="background-color: #FFB6C1">动漫</el-radio>\n' +
                '                                        <el-radio v-model="image_radio" label="6" border style="background-color: #FFB6C1">其他</el-radio>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div>资源链接:\n' +
                '                                        <el-input v-model="movies_url" placeholder="你这要不是高清文件,链接给我我自己去下"\n' +
                '                                                  style="width: 600px"></el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div>为什么推荐这部电影?\n' +
                '                                        <el-input\n' +
                '                                                type="textarea"\n' +
                '                                                autosize\n' +
                '                                                maxlength="500"\n' +
                '                                                placeholder="这么拽哦?喜欢这个图片的原因?"\n' +
                '                                                v-model="movies_text_p"\n' +
                '                                                style="width: 600px">\n' +
                '                                        </el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div style="position: relative; right: -70%">\n' +
                '                                        <el-row>\n' +
                '                                            <el-button type="primary" plain @click="reset">重置</el-button>\n' +
                '                                            <el-button type="success" plain @click="submit">投稿&nbsp!</el-button>\n' +
                '                                        </el-row>\n' +
                '                                    </div>\n' +
                '                                </div>\n' +
                '                            </div>\n' +
                '                        </li>\n' +
                '                        <li>\n' +
                '                            <div>\n' +
                '                                <div id="tools">\n' +
                '                                    <div>*工具文件名称:\n' +
                '                                        <el-input v-model="movies_name" placeholder="你不写,意思是让我给他起名字?!"\n' +
                '                                                  style="width: 600px"></el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div>工具作用简介:\n' +
                '                                        <el-input\n' +
                '                                                type="textarea"\n' +
                '                                                autosize\n' +
                '                                                placeholder="这究竟是个什么玩意?"\n' +
                '                                                maxlength="500"\n' +
                '                                                v-model="movies_text"\n' +
                '                                                style="width: 600px">\n' +
                '                                        </el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div>资源链接:\n' +
                '                                        <el-input v-model="movies_url" placeholder="你必须给我整上,不整上你别想投稿"\n' +
                '                                                  style="width: 600px"></el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div>\n' +
                '                                        <p>是否亲自使用过?</p>\n' +
                '                                        <el-radio v-model="tools_radio" label="1" border>使用过,推荐给你</el-radio>\n' +
                '                                        <el-radio v-model="tools_radio" label="2" border>没有,你自己试</el-radio>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div>如何使用这个工具?\n' +
                '                                        <el-input\n' +
                '                                                type="textarea"\n' +
                '                                                autosize\n' +
                '                                                maxlength="500"\n' +
                '                                                placeholder="咋用啊,你写给我瞅瞅"\n' +
                '                                                v-model="movies_text_p"\n' +
                '                                                style="width: 600px">\n' +
                '                                        </el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div style="position: relative; right: -70%">\n' +
                '                                        <el-row>\n' +
                '                                            <el-button type="primary" plain @click="reset">重置</el-button>\n' +
                '                                            <el-button type="success" plain @click="submit">投稿&nbsp!</el-button>\n' +
                '                                        </el-row>\n' +
                '                                    </div>\n' +
                '                                </div>\n' +
                '                            </div>\n' +
                '                        </li>\n' +
                '                        <li>\n' +
                '                            <div>\n' +
                '                                <div id="life">\n' +
                '                                    <div>*记录标题:\n' +
                '                                        <el-input v-model="movies_name" placeholder="请输入电影名称,必填"\n' +
                '                                                  style="width: 600px"></el-input>\n' +
                '                                    </div>\n' +
                '                                    <div><br>封面:\n' +
                '\n' +
                '                                        <el-upload\n' +
                '                                                action="/contribution/test"\n' +
                '                                                :show-file-list="false"\n' +
                '                                                :on-success="handleAvatarSuccess"\n' +
                '                                                :before-upload="beforeAvatarUpload"\n' +
                '                                                list-type="picture-card"\n' +
                '                                                :on-preview="handlePictureCardPreview"\n' +
                '                                                :on-remove="handleRemove"\n' +
                '                                        >\n' +
                '                                            <img v-if="imageUrl" :src="imageUrl" class="avatar"\n' +
                '                                                 style="max-height: 140px;max-width: 100px">\n' +
                '                                            <i v-else class="el-icon-plus avatar-uploader-icon"></i>\n' +
                '                                        </el-upload>\n' +
                '\n' +
                '\n' +
                '                                        <br/>\n' +
                '                                    </div>\n' +
                '\n' +
                '                                    <div>电影简介:\n' +
                '                                        <el-input\n' +
                '                                                type="textarea"\n' +
                '                                                autosize\n' +
                '                                                placeholder="给点作用啊,来个介绍吧"\n' +
                '                                                maxlength="500"\n' +
                '                                                v-model="movies_text"\n' +
                '                                                style="width: 600px">\n' +
                '                                        </el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div>资源链接:\n' +
                '                                        <el-input v-model="movies_url" placeholder="不是吧,资源都要我自己去找么?!"\n' +
                '                                                  style="width: 600px"></el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div>为什么推荐这部电影?\n' +
                '                                        <el-input\n' +
                '                                                type="textarea"\n' +
                '                                                autosize\n' +
                '                                                maxlength="500"\n' +
                '                                                placeholder="why why why? 怎么就喜欢这个了?"\n' +
                '                                                v-model="movies_text_p"\n' +
                '                                                style="width: 600px">\n' +
                '                                        </el-input>\n' +
                '                                    </div>\n' +
                '                                    <br/>\n' +
                '                                    <div style="position: relative; right: -70%">\n' +
                '                                        <el-row>\n' +
                '                                            <el-button type="primary" plain @click="reset">重置</el-button>\n' +
                '                                            <el-button type="success" plain @click="submit">投稿&nbsp!</el-button>\n' +
                '                                        </el-row>\n' +
                '                                    </div>\n' +
                '                                </div>\n' +
                '                            </div>\n' +
                '                        </li>\n' +
                '                    </ul>\n' +
                '                </div>\n' +
                '            </div>\n' +
                '        </div>'


                , 'HTML 片段', {
              dangerouslyUseHTMLString: true
            });
          }
        },
        created() {
            // this.tools_infos();
        },

    });
}

test_Vue()

