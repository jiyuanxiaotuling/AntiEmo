<template>
  <div id="contanier">
    <div id="__next">
      <div class="overflow-hidden w-full h-full relative">
        <div class="flex h-full flex-1 flex-col md:pl-[260px]">
          <div
            class="sticky top-0 z-10 flex items-center border-b border-white/20 bg-gray-800 pl-1 pt-1 text-gray-200 sm:pl-3 md:hidden"
          >
            <div>
              <button
                @click="showSlideMethod"
                type="button"
                class="-ml-0.5 -mt-0.5 inline-flex h-10 w-10 items-center justify-center rounded-md hover:text-gray-900 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white dark:hover:text-white"
              >
                <span class="sr-only">Open sidebar</span>
                <svg
                  stroke="currentColor"
                  fill="none"
                  stroke-width="1.5"
                  viewBox="0 0 24 24"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="h-6 w-6"
                  height="1em"
                  width="1em"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <line x1="3" y1="12" x2="21" y2="12"></line>
                  <line x1="3" y1="6" x2="21" y2="6"></line>
                  <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
              </button>
            </div>
            <h1 class="flex-1 text-center text-base font-normal">
              {{ chatTitle }}
            </h1>
            <button @click.stop="newChat" type="button" class="px-3">
              <svg
                stroke="currentColor"
                fill="none"
                stroke-width="1.5"
                viewBox="0 0 24 24"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="h-6 w-6"
                height="1em"
                width="1em"
                xmlns="http://www.w3.org/2000/svg"
              >
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
            </button>
          </div>

          <main
            class="relative h-full w-full transition-width flex flex-col overflow-hidden items-stretch flex-1"
          >
            <!-- 聊天窗 -->
            <div class="flex-1 overflow-hidden">
              <div
                class="react-scroll-to-bottom--css-ncqif-79elbk h-full dark:bg-gray-800"
              >
                <div
                  ref="chatContainer"
                  class="react-scroll-to-bottom--css-krija-1n7m0yu"
                >
                  <div
                    class="flex flex-col items-center text-sm dark:bg-gray-800"
                  >
                    <!-- 对话item -->
                    <template v-for="conv, idx in conversation">
                      <!-- human -->
                      <div v-if="conv.speaker == 'human'"
                        class="w-full border-b border-black/10 dark:border-gray-900/50 text-gray-800 dark:text-gray-100 group dark:bg-gray-800">
                        <div
                          class="text-base gap-4 md:gap-6 m-auto md:max-w-2xl lg:max-w-2xl xl:max-w-3xl p-4 md:py-6 flex lg:px-0">
                          <div class="w-[30px] flex flex-col relative items-end">
                            <div class="relative flex">
                              <span
                                style="box-sizing: border-box; display: inline-block; overflow: hidden; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; position: relative; max-width: 100%;">
                                <span
                                  style="box-sizing: border-box; display: block; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; max-width: 100%;">
                                  <img aria-hidden="true" :src="require('../assets/imgs/human' + avatarIdx + '.png')"
                                    alt="huamn"
                                    style="display: block; max-width: 100%; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px;">
                                </span>
                              </span>
                            </div>
                          </div>
                          <div class="relative flex w-[calc(100%-50px)] flex-col gap-1 md:gap-3 lg:w-[calc(100%-115px)]">
                            <div class="flex flex-grow flex-col gap-3">
                              <div class="min-h-[20px] flex flex-col items-start gap-4 whitespace-pre-wrap">{{
                                conv.speech
                              }}
                              </div>
                            </div>
                            <div v-if="false"
                              class="text-gray-400 flex self-end lg:self-center justify-center mt-2 gap-3 md:gap-4 lg:gap-1 lg:absolute lg:top-0 lg:translate-x-full lg:right-0 lg:mt-0 lg:pl-2 visible">
                              <button
                                class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400 md:invisible md:group-hover:visible">
                                <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
                                  stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em"
                                  xmlns="http://www.w3.org/2000/svg">
                                  <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                                  <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                                </svg>
                              </button>
                            </div>
                            <div class="flex justify-between"></div>
                          </div>
                        </div>
                      </div>
                      <!-- AI -->
                      <div
                        v-if="conv.speaker == 'AI'"
                        :key="`AI-${idx}`"
                        class="w-full border-b border-black/10 dark:border-gray-900/50 text-gray-800 dark:text-gray-100 group bg-gray-50 dark:bg-[#444654]"
                      >
                        <div
                          class="text-base gap-4 md:gap-6 m-auto md:max-w-2xl lg:max-w-2xl xl:max-w-3xl p-4 md:py-6 flex lg:px-0"
                        >
                          <div
                            class="w-[30px] flex flex-col relative items-end"
                          >
                            <div
                              class="relative h-[30px] w-[30px] p-1 rounded-sm text-white flex items-center justify-center"
                              style="background-color: rgb(16, 163, 127)"
                            >
                              <svg
                                t="1741586176569"
                                class="icon"
                                viewBox="0 0 1024 1024"
                                version="1.1"
                                xmlns="http://www.w3.org/2000/svg"
                                p-id="3758"
                                width="200"
                                height="200"
                              >
                                <path
                                  d="M378.253061 617.012245m-42.840816 0a42.840816 42.840816 0 1 0 85.681633 0 42.840816 42.840816 0 1 0-85.681633 0Z"
                                  fill="#333333"
                                  p-id="3759"
                                ></path>
                                <path
                                  d="M645.746939 617.012245m-42.840817 0a42.840816 42.840816 0 1 0 85.681633 0 42.840816 42.840816 0 1 0-85.681633 0Z"
                                  fill="#333333"
                                  p-id="3760"
                                ></path>
                                <path
                                  d="M509.910204 532.897959c-121.208163 0-216.293878-13.583673-261.746939-21.420408-21.420408-3.657143-40.75102-15.673469-53.289796-33.959184-12.538776-17.763265-17.240816-39.706122-13.583673-61.12653l42.318367-237.714286c6.269388-35.526531 35.526531-63.216327 71.57551-67.395918 8.881633-1.044898 16.718367-2.089796 24.555103-3.657143l3.134693-0.522449c31.869388-5.22449 67.395918-11.493878 189.126531-11.493878 121.730612 0 157.779592 6.269388 189.126531 11.493878 8.359184 1.567347 17.240816 3.134694 28.212245 4.179592 35.526531 4.179592 65.306122 31.869388 71.57551 67.395918l41.795918 237.191837c3.657143 21.420408-1.044898 43.363265-13.583673 61.648979-12.538776 17.763265-31.346939 29.779592-53.289796 33.436735-47.020408 8.359184-144.195918 21.942857-265.926531 21.942857z m2.089796-395.493877c-118.073469 0-152.032653 5.746939-182.334694 10.971428l-3.134694 0.522449c-8.359184 1.567347-16.718367 3.134694-27.167347 4.179592-17.240816 2.089796-31.869388 15.673469-35.004081 32.914286l-42.318368 237.714285c-2.089796 10.44898 0.522449 21.420408 6.791837 30.302041 6.269388 8.881633 15.15102 14.628571 26.122449 16.718368 44.408163 7.836735 136.881633 20.897959 254.955102 20.897959 118.595918 0 213.159184-13.061224 259.134694-20.897959 10.44898-2.089796 19.853061-7.836735 26.122449-16.718368 6.269388-8.881633 8.881633-19.330612 6.791837-30.302041l-41.795919-237.714285c-3.134694-17.240816-17.763265-30.82449-35.004081-32.914286-12.016327-1.567347-21.420408-3.134694-30.302041-4.702041-30.302041-5.22449-64.261224-10.971429-182.857143-10.971428z"
                                  fill="#333333"
                                  p-id="3761"
                                ></path>
                                <path
                                  d="M512 928.391837c-62.693878 0-133.746939-27.689796-195.395918-75.755102-55.379592-43.363265-97.697959-99.265306-120.163266-159.346939-58.514286-10.971429-102.4-65.306122-102.4-129.567347 0-66.35102 46.497959-122.253061 108.669388-130.612245 9.404082-1.044898 18.285714 4.179592 21.942857 12.538776 1.044898 2.612245 2.612245 5.22449 4.179592 7.836734 6.269388 8.881633 15.15102 14.628571 26.122449 16.718368 44.408163 7.836735 136.881633 20.897959 254.955102 20.897959 118.595918 0 213.159184-13.061224 259.134694-20.897959 10.44898-2.089796 19.853061-7.836735 26.122449-16.718368 1.567347-2.089796 3.134694-4.702041 4.179592-7.836734 3.657143-8.881633 12.538776-14.106122 21.942857-12.538776 62.171429 8.359184 108.669388 64.261224 108.669388 130.612245 0 64.261224-43.885714 118.595918-102.4 129.567347-22.465306 59.559184-64.783673 115.983673-120.163266 159.346939-61.64898 48.065306-132.702041 75.755102-195.395918 75.755102zM194.873469 477.518367c-34.481633 10.971429-59.036735 45.97551-59.036734 86.204082 0 47.542857 33.959184 86.726531 77.322449 89.861224 8.359184 0.522449 15.673469 6.269388 18.285714 14.106123 18.808163 56.946939 57.991837 110.759184 110.759184 152.032653 54.334694 42.318367 115.983673 66.873469 169.795918 66.873469 53.289796 0 115.461224-24.555102 169.273469-66.873469 52.767347-41.273469 91.95102-95.085714 110.759184-152.032653 2.612245-7.836735 9.926531-13.583673 18.285714-14.106123 43.363265-3.134694 77.322449-42.318367 77.322449-89.861224 0-40.228571-24.555102-75.232653-59.036734-86.204082-12.538776 17.763265-31.346939 29.779592-53.289796 33.436735-47.020408 8.359184-144.195918 21.942857-265.926531 21.942857-121.208163 0-216.293878-13.583673-261.746939-21.420408-21.420408-3.657143-40.228571-15.673469-52.767347-33.959184zM603.428571 334.889796h-182.857142c-11.493878 0-20.897959-9.404082-20.89796-20.897959s9.404082-20.897959 20.89796-20.897959h182.857142c11.493878 0 20.897959 9.404082 20.89796 20.897959s-9.404082 20.897959-20.89796 20.897959z"
                                  fill="#333333"
                                  p-id="3762"
                                ></path>
                                <path
                                  d="M512 426.318367c-11.493878 0-20.897959-9.404082-20.897959-20.897959v-182.857143c0-11.493878 9.404082-20.897959 20.897959-20.897959s20.897959 9.404082 20.897959 20.897959v182.857143c0 11.493878-9.404082 20.897959-20.897959 20.897959z"
                                  fill="#333333"
                                  p-id="3763"
                                ></path>
                              </svg>
                            </div>

                            <!-- 多个消息 -->
                            <div
                              v-if="conv.speeches.length > 1"
                              class="text-xs flex items-center justify-center gap-1 invisible absolute left-0 top-2 -ml-4 -translate-x-full group-hover:visible"
                            >
                              <button
                                @click.stop="last(conv)"
                                :disabled="!(conv.idx > 0)"
                                class="dark:text-white disabled:text-gray-300 dark:disabled:text-gray-400"
                              >
                                <svg
                                  stroke="currentColor"
                                  fill="none"
                                  stroke-width="1.5"
                                  viewBox="0 0 24 24"
                                  stroke-linecap="round"
                                  stroke-linejoin="round"
                                  class="h-3 w-3"
                                  height="1em"
                                  width="1em"
                                  xmlns="http://www.w3.org/2000/svg"
                                >
                                  <polyline points="15 18 9 12 15 6"></polyline>
                                </svg>
                              </button>
                              <span class="flex-grow flex-shrink-0"
                                >{{ conv.idx + 1 }} /
                                {{ conv.speeches.length }}</span
                              >
                              <button
                                @click.stop="next(conv)"
                                :disabled="
                                  !(conv.idx < conv.speeches.length - 1)
                                "
                                class="dark:text-white disabled:text-gray-300 dark:disabled:text-gray-400"
                              >
                                <svg
                                  stroke="currentColor"
                                  fill="none"
                                  stroke-width="1.5"
                                  viewBox="0 0 24 24"
                                  stroke-linecap="round"
                                  stroke-linejoin="round"
                                  class="h-3 w-3"
                                  height="1em"
                                  width="1em"
                                  xmlns="http://www.w3.org/2000/svg"
                                >
                                  <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                              </button>
                            </div>
                          </div>
                          <div
                            class="relative flex w-[calc(100%-50px)] flex-col gap-1 md:gap-3 lg:w-[calc(100%-115px)]"
                          >
                            <div class="flex flex-grow flex-col gap-3">
                              <!--  whitespace-pre-wrap -->
                              <div
                                class="min-h-[20px] flex flex-col items-start gap-4"
                              >
                                <div
                                  v-html="
                                    mdToHtml(conv.speeches[conv.idx], conv)
                                  "
                                  :class="{ 'result-streaming': conv.loading }"
                                  class="markdown prose-r w-full break-words dark:prose-invert light"
                                ></div>
                              </div>
                            </div>
                            <div class="flex justify-between">
                              <div
                                class="text-gray-400 flex self-end lg:self-center justify-center mt-2 gap-3 md:gap-4 lg:gap-1 lg:absolute lg:top-0 lg:translate-x-full lg:right-0 lg:mt-0 lg:pl-2 visible"
                              >
                                <button
                                  @click.stop="suitable(idx, conv, 1)"
                                  v-if="
                                    conv.suitable[conv.idx] == 0 ||
                                    conv.suitable[conv.idx] == 1
                                  "
                                  :class="{
                                    suitable_selected:
                                      conv.suitable[conv.idx] == 1,
                                  }"
                                  class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400"
                                >
                                  <svg
                                    stroke="currentColor"
                                    fill="none"
                                    stroke-width="2"
                                    viewBox="0 0 24 24"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="h-4 w-4"
                                    height="1em"
                                    width="1em"
                                    xmlns="http://www.w3.org/2000/svg"
                                  >
                                    <path
                                      d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"
                                    ></path>
                                  </svg>
                                </button>
                                <button
                                  @click.stop="suitable(idx, conv, -1)"
                                  v-if="
                                    conv.suitable[conv.idx] == 0 ||
                                    conv.suitable[conv.idx] == -1
                                  "
                                  :class="{
                                    suitable_selected:
                                      conv.suitable[conv.idx] == -1,
                                  }"
                                  class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400"
                                >
                                  <svg
                                    stroke="currentColor"
                                    fill="none"
                                    stroke-width="2"
                                    viewBox="0 0 24 24"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="h-4 w-4"
                                    height="1em"
                                    width="1em"
                                    xmlns="http://www.w3.org/2000/svg"
                                  >
                                    <path
                                      d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"
                                    ></path>
                                  </svg>
                                </button>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </template>

                    <div
                      v-if="conversation.length == 0"
                      class="text-gray-800 w-full md:max-w-2xl lg:max-w-3xl md:h-full md:flex md:flex-col px-6 dark:text-gray-100"
                    >
                      <h1
                        class="text-4xl font-semibold text-center mt-6 sm:mt-[20vh] ml-auto mr-auto mb-10 sm:mb-16 flex gap-2 items-center justify-center"
                      >
                        AntiEmo——你的心理健康医生
                      </h1>
                    </div>

                    <div class="w-full h-32 md:h-48 flex-shrink-0"></div>
                  </div>

                  <transition name="el-fade-in-linear">
                    <!-- 回到底部 -->
                    <button
                      v-show="isShowGoBottom"
                      @click="handleScrollBottom"
                      class="cursor-pointer absolute right-6 bottom-[124px] md:bottom-[120px] z-10 rounded-full border border-gray-200 bg-gray-50 text-gray-600 dark:border-white/10 dark:bg-white/10 dark:text-gray-200"
                    >
                      <svg
                        stroke="currentColor"
                        fill="none"
                        stroke-width="2"
                        viewBox="0 0 24 24"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="h-4 w-4 m-1"
                        height="1em"
                        width="1em"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <line x1="12" y1="5" x2="12" y2="19"></line>
                        <polyline points="19 12 12 19 5 12"></polyline>
                      </svg>
                    </button>
                  </transition>
                </div>
              </div>
            </div>

            <!-- 底部输入 -->
            <div
              class="absolute bottom-0 left-0 w-full border-t md:border-t-0 dark:border-white/20 md:border-transparent md:dark:border-transparent md:bg-vert-light-gradient bg-white dark:bg-gray-800 md:!bg-transparent dark:md:bg-vert-dark-gradient"
            >
              <form
                class="stretch mx-2 flex flex-row gap-3 pt-2 last:mb-2 md:last:mb-6 lg:mx-auto lg:max-w-3xl lg:pt-6"
              >
                <div class="relative flex h-full flex-1 md:flex-col">
                  <div
                    class="flex ml-1 md:w-full md:m-auto md:mb-2 gap-0 md:gap-2 justify-center"
                  >
                    

                    <button
                      v-if="convLoading"
                      @click.stop.prevent="stopChat"
                      id="stopChat"
                      class="btn relative btn-neutral border-0 md:border"
                    >
                      <div
                        class="flex w-full items-center justify-center gap-2"
                      >
                        <svg
                          stroke="currentColor"
                          fill="none"
                          stroke-width="1.5"
                          viewBox="0 0 24 24"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          class="h-3 w-3"
                          height="1em"
                          width="1em"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <rect
                            x="3"
                            y="3"
                            width="18"
                            height="18"
                            rx="2"
                            ry="2"
                          ></rect></svg
                        >Stop generating
                      </div>
                    </button>
                  </div>
                  <div
                    class="flex flex-col w-full py-2 flex-grow md:py-3 md:pl-4 relative border border-black/10 bg-white dark:border-gray-900/50 dark:text-white dark:bg-gray-700 rounded-md shadow-[0_0_10px_rgba(0,0,0,0.10)] dark:shadow-[0_0_15px_rgba(0,0,0,0.10)]"
                  >
                    <textarea
                      v-model="chatMsg"
                      ref="inputChat"
                      @keydown="judgeInput"
                      tabindex="0"
                      data-id="root"
                      style="
                        max-height: 200px;
                        height: 24px;
                        overflow-y: hidden;
                      "
                      rows="1"
                      class="m-0 w-full resize-none border-0 bg-transparent p-0 pl-2 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent md:pl-0"
                    ></textarea>
                    <button
                      @click.stop.prevent="send"
                      :disabled="convLoading"
                      class="absolute p-1 rounded-md text-gray-500 bottom-1.5 right-1 md:bottom-2.5 md:right-2 hover:bg-gray-100 dark:hover:text-gray-400 dark:hover:bg-gray-900 disabled:hover:bg-transparent dark:disabled:hover:bg-transparent"
                    >
                      <div
                        v-if="convLoading"
                        class="text-2xl"
                        style="line-height: 1.3rem"
                      >
                        <span class="load_dot1">·</span
                        ><span class="load_dot2">·</span
                        ><span class="load_dot3">·</span>
                      </div>
                      <svg
                        v-else
                        stroke="currentColor"
                        fill="none"
                        stroke-width="2"
                        viewBox="0 0 24 24"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="h-4 w-4 mr-1"
                        height="1em"
                        width="1em"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <line x1="22" y1="2" x2="11" y2="13"></line>
                        <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                      </svg>
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </main>
        </div>

        <!-- 菜单导航 -->
        <div
          class="dark hidden bg-gray-900 md:fixed md:inset-y-0 md:flex md:w-[260px] md:flex-col"
        >
          <div class="flex h-full min-h-0 flex-col">
            <div
              ref="menu"
              class="scrollbar-trigger flex h-full w-full flex-1 items-start border-white/20"
            >
              <nav
                ref="navEle"
                class="flex h-full flex-1 flex-col space-y-1 p-2"
              >
              <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap" rel="stylesheet">
              <div style="width: 100%; height: 60px; text-align: center;">
                <h1 style="margin-top: 10px; font-family: 'Poppins', sans-serif; font-size: 28px; font-weight: 500; color: #2c3e50; letter-spacing: 1px; text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);">
                  AntiEmo
                </h1>
              </div>
              
                <a
                  @click.stop="newChat"
                  class="fancy-button flex py-3 px-3 items-center gap-3 rounded-md text-white cursor-pointer text-sm mb-2 flex-shrink-0 border border-white/20"
                >
                  <svg
                    stroke="currentColor"
                    fill="none"
                    stroke-width="2"
                    viewBox="0 0 24 24"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    height="1em"
                    width="1em"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <line x1="12" y1="5" x2="12" y2="19"></line>
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                  </svg>
                  新建对话
                </a>

                <!-- 对话列表 -->
                <div
                  class="flex-col flex-1 overflow-y-auto border-b border-white/20"
                  style="padding-bottom: 5px"
                >
                  <div class="flex flex-col gap-2 text-gray-100 text-sm">
                    <template v-for="(conversation, cidx) in conversations">
                      <div
                        v-if="conversation.editable"
                        class="m-focus flex py-3 px-3 items-center gap-3 relative rounded-md cursor-pointer hover:pr-14 break-all pr-14 bg-gray-800 hover:bg-gray-800"
                      >
                        <svg
                          stroke="currentColor"
                          fill="none"
                          stroke-width="2"
                          viewBox="0 0 24 24"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          class="h-4 w-4 flex-shrink-0"
                          height="1em"
                          width="1em"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"
                          ></path>
                        </svg>
                        <input
                          id="titleInput"
                          v-model="convTitletmp"
                          @blur="titleInputBlur(cidx, conversation)"
                          type="text"
                          class="text-sm border-none bg-transparent p-0 m-0 w-full mr-0"
                          autofocus="true"
                        />
                        <div
                          class="absolute flex right-1 z-10 text-gray-300 visible"
                        >
                          <button
                            @click="changeConvTitle(cidx, conversation)"
                            class="p-1 hover:text-white"
                          >
                            <svg
                              stroke="currentColor"
                              fill="none"
                              stroke-width="2"
                              viewBox="0 0 24 24"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="h-4 w-4"
                              height="1em"
                              width="1em"
                              xmlns="http://www.w3.org/2000/svg"
                            >
                              <polyline points="20 6 9 17 4 12"></polyline>
                            </svg>
                          </button>
                          <button
                            @click="cancelChangeConvTitle(cidx, conversation)"
                            class="p-1 hover:text-white"
                          >
                            <svg
                              stroke="currentColor"
                              fill="none"
                              stroke-width="2"
                              viewBox="0 0 24 24"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="h-4 w-4"
                              height="1em"
                              width="1em"
                              xmlns="http://www.w3.org/2000/svg"
                            >
                              <line x1="18" y1="6" x2="6" y2="18"></line>
                              <line x1="6" y1="6" x2="18" y2="18"></line>
                            </svg>
                          </button>
                        </div>
                      </div>

                      <a
                        v-else-if="conversation.delete"
                        @blur="cancelDelConv(cidx, conversation)"
                        class="m-focus flex py-3 px-3 items-center gap-3 relative rounded-md cursor-pointer break-all pr-14 bg-gray-800 hover:bg-gray-800 group"
                      >
                        <svg
                          stroke="currentColor"
                          fill="none"
                          stroke-width="2"
                          viewBox="0 0 24 24"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          class="h-4 w-4"
                          height="1em"
                          width="1em"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <polyline points="3 6 5 6 21 6"></polyline>
                          <path
                            d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                          ></path>
                          <line x1="10" y1="11" x2="10" y2="17"></line>
                          <line x1="14" y1="11" x2="14" y2="17"></line>
                        </svg>
                        <div
                          class="flex-1 text-ellipsis max-h-5 overflow-hidden break-all relative"
                        >
                          Delete "{{ conversation.title }}"?
                          <div
                            class="absolute inset-y-0 right-0 w-8 z-10 bg-gradient-to-l from-gray-800"
                          ></div>
                        </div>
                        <div
                          class="absolute flex right-1 z-10 text-gray-300 visible"
                        >
                          <button
                            @click="delConv(cidx)"
                            class="p-1 hover:text-white"
                          >
                            <svg
                              stroke="currentColor"
                              fill="none"
                              stroke-width="2"
                              viewBox="0 0 24 24"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="h-4 w-4"
                              height="1em"
                              width="1em"
                              xmlns="http://www.w3.org/2000/svg"
                            >
                              <polyline points="20 6 9 17 4 12"></polyline>
                            </svg>
                          </button>
                          <button
                            @click="cancelDelConv(cidx, conversation)"
                            class="p-1 hover:text-white"
                          >
                            <svg
                              stroke="currentColor"
                              fill="none"
                              stroke-width="2"
                              viewBox="0 0 24 24"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="h-4 w-4"
                              height="1em"
                              width="1em"
                              xmlns="http://www.w3.org/2000/svg"
                            >
                              <line x1="18" y1="6" x2="6" y2="18"></line>
                              <line x1="6" y1="6" x2="18" y2="18"></line>
                            </svg>
                          </button>
                        </div>
                      </a>

                      <a
                        v-else
                        @click.stop.prevent="
                          selectConversation(conversation, true)
                        "
                        :class="{
                          'bg-gray-800 hover:bg-gray-800 pr-14':
                            conversation.selected,
                          'hover:bg-[#2A2B32] hover:pr-4':
                            !conversation.selected,
                        }"
                        class="flex py-3 px-3 items-center gap-3 relative rounded-md cursor-pointer break-all group"
                      >
                        <svg
                          stroke="currentColor"
                          fill="none"
                          stroke-width="2"
                          viewBox="0 0 24 24"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          class="h-4 w-4"
                          height="1em"
                          width="1em"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"
                          ></path>
                        </svg>
                        <div
                          class="flex-1 text-ellipsis max-h-5 overflow-hidden break-all relative"
                        >
                          {{ conversation.title }}
                          <div
                            :class="{
                              'from-gray-800': conversation.selected,
                              'from-gray-900 group-hover:from-[#2A2B32]':
                                !conversation.selected,
                            }"
                            class="absolute inset-y-0 right-0 w-8 z-10 bg-gradient-to-l"
                          ></div>
                        </div>
                        <div
                          v-show="conversation.selected"
                          class="absolute flex right-1 z-10 text-gray-300 visible"
                        >
                          <button
                            @click="editTitle(cidx, conversation)"
                            class="p-1 hover:text-white"
                          >
                            <svg
                              stroke="currentColor"
                              fill="none"
                              stroke-width="2"
                              viewBox="0 0 24 24"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="h-4 w-4"
                              height="1em"
                              width="1em"
                              xmlns="http://www.w3.org/2000/svg"
                            >
                              <path d="M12 20h9"></path>
                              <path
                                d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"
                              ></path>
                            </svg>
                          </button>
                          <button
                            @click="conversation.delete = true"
                            class="p-1 hover:text-white"
                          >
                            <svg
                              stroke="currentColor"
                              fill="none"
                              stroke-width="2"
                              viewBox="0 0 24 24"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="h-4 w-4"
                              height="1em"
                              width="1em"
                              xmlns="http://www.w3.org/2000/svg"
                            >
                              <polyline points="3 6 5 6 21 6"></polyline>
                              <path
                                d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                              ></path>
                              <line x1="10" y1="11" x2="10" y2="17"></line>
                              <line x1="14" y1="11" x2="14" y2="17"></line>
                            </svg>
                          </button>
                        </div>
                      </a>
                    </template>
                  </div>
                </div>

                <a
                  v-if="conversations.length > 0"
                  @click.stop.prevent="clearConversations"
                  class="flex py-3 px-3 items-center gap-3 rounded-md hover:bg-gray-500/10 transition-colors duration-200 text-white cursor-pointer text-sm"
                >
                  <svg
                    stroke="currentColor"
                    fill="none"
                    stroke-width="2"
                    viewBox="0 0 24 24"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    height="1em"
                    width="1em"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path
                      d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                    ></path>
                    <line x1="10" y1="11" x2="10" y2="17"></line>
                    <line x1="14" y1="11" x2="14" y2="17"></line>
                  </svg>
                  清除历史对话
                </a>
                <a
                  v-if="theme == 'light'"
                  @click="changeTheme('dark')"
                  class="flex py-3 px-3 items-center gap-3 rounded-md hover:bg-gray-500/10 transition-colors duration-200 text-white cursor-pointer text-sm"
                >
                  <svg
                    stroke="currentColor"
                    fill="none"
                    stroke-width="2"
                    viewBox="0 0 24 24"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    height="1em"
                    width="1em"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"
                    ></path>
                  </svg>
                  深色模式
                </a>

                <a
                  v-if="theme == 'dark'"
                  @click="changeTheme('light')"
                  class="flex py-3 px-3 items-center gap-3 rounded-md hover:bg-gray-500/10 transition-colors duration-200 text-white cursor-pointer text-sm"
                >
                  <svg
                    stroke="currentColor"
                    fill="none"
                    stroke-width="2"
                    viewBox="0 0 24 24"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    height="1em"
                    width="1em"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <circle cx="12" cy="12" r="5"></circle>
                    <line x1="12" y1="1" x2="12" y2="3"></line>
                    <line x1="12" y1="21" x2="12" y2="23"></line>
                    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                    <line x1="1" y1="12" x2="3" y2="12"></line>
                    <line x1="21" y1="12" x2="23" y2="12"></line>
                    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                  </svg>
                  Light mode</a
                >

                <button
                  @click="goToCharacter"
                  class="flex py-3 px-3 items-center gap-3 rounded-md hover:bg-gray-500/10 transition-colors duration-200 text-white cursor-pointer text-sm"
                >
                  <svg
                    stroke="currentColor"
                    fill="currentColor"
                    stroke-width="2"
                    viewBox="0 0 640 512"
                    class="h-4 w-4"
                    height="1em"
                    width="1em"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M524.531,69.836a1.5,1.5,0,0,0-.764-.7A485.065,485.065,0,0,0,404.081,32.03a1.816,1.816,0,0,0-1.923.91,337.461,337.461,0,0,0-14.9,30.6,447.848,447.848,0,0,0-134.426,0,309.541,309.541,0,0,0-15.135-30.6,1.89,1.89,0,0,0-1.924-.91A483.689,483.689,0,0,0,116.085,69.137a1.712,1.712,0,0,0-.788.676C39.068,183.651,18.186,294.69,28.43,404.354a2.016,2.016,0,0,0,.765,1.375A487.666,487.666,0,0,0,176.02,479.918a1.9,1.9,0,0,0,2.063-.676A348.2,348.2,0,0,0,208.12,430.4a1.86,1.86,0,0,0-1.019-2.588,321.173,321.173,0,0,1-45.868-21.853,1.885,1.885,0,0,1-.185-3.126c3.082-2.309,6.166-4.711,9.109-7.137a1.819,1.819,0,0,1,1.9-.256c96.229,43.917,200.41,43.917,295.5,0a1.812,1.812,0,0,1,1.924.233c2.944,2.426,6.027,4.851,9.132,7.16a1.884,1.884,0,0,1-.162,3.126,301.407,301.407,0,0,1-45.89,21.83,1.875,1.875,0,0,0-1,2.611,391.055,391.055,0,0,0,30.014,48.815,1.864,1.864,0,0,0,2.063.7A486.048,486.048,0,0,0,610.7,405.729a1.882,1.882,0,0,0,.765-1.352C623.729,277.594,590.933,167.465,524.531,69.836ZM222.491,337.58c-28.972,0-52.844-26.587-52.844-59.239S193.056,219.1,222.491,219.1c29.665,0,53.306,26.82,52.843,59.239C275.334,310.993,251.924,337.58,222.491,337.58Zm195.38,0c-28.971,0-52.843-26.587-52.843-59.239S388.437,219.1,417.871,219.1c29.667,0,53.307,26.82,52.844,59.239C470.715,310.993,447.538,337.58,417.871,337.58Z"
                    ></path>
                  </svg>
                  虚拟人对话
                </button>
                <a
                  href="https://help.openai.com/en/collections/3742473-chatgpt"
                  target="_blank"
                  class="flex py-3 px-3 items-center gap-3 rounded-md hover:bg-gray-500/10 transition-colors duration-200 text-white cursor-pointer text-sm"
                >
                  <svg
                    stroke="currentColor"
                    fill="none"
                    stroke-width="2"
                    viewBox="0 0 24 24"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    height="1em"
                    width="1em"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"
                    ></path>
                    <polyline points="15 3 21 3 21 9"></polyline>
                    <line x1="10" y1="14" x2="21" y2="3"></line>
                  </svg>
                  个人信息</a
                >
              </nav>
            </div>
          </div>
        </div>
      </div>
      <div class="absolute top-0 left-0 right-0 z-[2]"></div>
    </div>

    <div v-show="showSlide" class="semi-portal" style="z-index: 1000">
      <div class="">
        <div class="semi-modal-mask"></div>
        <div role="none" class="semi-modal-wrap">
          <div
            class="semi-modal semi-modal-small"
            id="dialog-3"
            style="width: 0px"
          >
            <div
              role="dialog"
              aria-modal="true"
              aria-labelledby="semi-modal-title"
              aria-describedby="semi-modal-body"
              class="semi-modal-content"
            >
              <div class="semi-modal-body-wrapper">
                <div class="semi-modal-body" x-semi-prop="children">
                  <div class="fixed inset-0 z-40 flex">
                    <div
                      class="relative flex w-full max-w-xs flex-1 flex-col bg-gray-900 translate-x-0"
                      id="headlessui-dialog-panel-:r1:"
                      data-headlessui-state="open"
                    >
                      <div
                        class="absolute top-0 right-0 -mr-12 pt-2 opacity-100"
                      >
                        <button
                          @click="closeShowSlide"
                          type="button"
                          class="ml-1 flex h-10 w-10 items-center justify-center focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                        >
                          <span class="sr-only">Close sidebar</span>
                          <svg
                            stroke="currentColor"
                            fill="none"
                            stroke-width="1.5"
                            viewBox="0 0 24 24"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            class="h-6 w-6 text-white"
                            height="1em"
                            width="1em"
                            xmlns="http://www.w3.org/2000/svg"
                          >
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                          </svg>
                        </button>
                      </div>
                      <div
                        ref="slideNavContainer"
                        style="width: 320px"
                        class="flex h-full flex-1 items-start border-white/20"
                      ></div>
                    </div>
                    <div
                      @click="closeShowSlide"
                      style="width: calc(100% - 320px)"
                      class="flex-shrink-0"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div portal-container="">
      <span
        class="pointer-events-none fixed inset-0 z-[60] mx-auto my-2 flex max-w-[560px] flex-col items-stretch justify-start md:pb-5"
      >
      </span>
    </div>

    <!-- 弹窗 -->
    <div id="headlessui-portal-root" v-if="popupShow">
      <div data-headlessui-portal="">
        <button
          type="button"
          aria-hidden="true"
          style="
            position: fixed;
            top: 1px;
            left: 1px;
            width: 1px;
            height: 0px;
            padding: 0px;
            margin: -1px;
            overflow: hidden;
            clip: rect(0px, 0px, 0px, 0px);
            white-space: nowrap;
            border-width: 0px;
          "
        ></button>
        <div>
          <div
            class="relative z-50"
            id="headlessui-dialog-:r3:"
            role="dialog"
            aria-modal="true"
            data-headlessui-state="open"
            aria-labelledby="headlessui-dialog-title-:r5:"
          >
            <div
              class="fixed inset-0 bg-gray-500/90 transition-opacity dark:bg-gray-800/90"
            ></div>
            <div class="fixed inset-0 z-50 overflow-y-auto">
              <div
                class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
              >
                <div
                  v-if="false"
                  class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all dark:bg-gray-900 sm:my-8 sm:w-full sm:p-6 sm:max-w-lg"
                  id="headlessui-dialog-panel-:r4:"
                  data-headlessui-state="open"
                >
                  <div class="flex items-center sm:flex">
                    <div
                      class="mr-4 flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full sm:h-10 sm:w-10 bg-green-100"
                    >
                      <svg
                        stroke="currentColor"
                        fill="none"
                        stroke-width="1.5"
                        viewBox="0 0 24 24"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="h-6 w-6 text-green-700"
                        height="1em"
                        width="1em"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"
                        ></path>
                      </svg>
                    </div>
                    <div class="mt-3 text-center sm:mt-0 sm:text-left">
                      <h3
                        class="text-lg font-medium leading-6 text-gray-900 dark:text-gray-200"
                        id="headlessui-dialog-title-:r5:"
                        data-headlessui-state="open"
                      >
                        Provide additional feedback
                      </h3>
                    </div>
                  </div>
                  <form>
                    <textarea
                      id="feedback-other"
                      placeholder="What would the ideal answer have been?"
                      rows="3"
                      class="mt-4 mb-1 w-full rounded-md dark:bg-gray-800 dark:focus:border-white dark:focus:ring-white"
                      tabindex="0"
                      style="height: 89.4815px; overflow-y: hidden"
                    ></textarea>
                  </form>
                  <div
                    class="mt-5 flex flex-col gap-3 sm:mt-4 sm:flex-row-reverse"
                  >
                    <button class="btn flex justify-center gap-2 btn-neutral">
                      Submit feedback
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <button
          type="button"
          aria-hidden="true"
          style="
            position: fixed;
            top: 1px;
            left: 1px;
            width: 1px;
            height: 0px;
            padding: 0px;
            margin: -1px;
            overflow: hidden;
            clip: rect(0px, 0px, 0px, 0px);
            white-space: nowrap;
            border-width: 0px;
          "
        ></button>
      </div>
    </div>
  </div>
</template>

<script>
import { marked } from "marked";
import hljs from "highlight.js";
import "../assets/index.css";
import "highlight.js/styles/github.css";
import axios from "axios";
import router from "../router";

axios.defaults.baseURL = "http://localhost:8000";
const renderer = {
  code(code, infostring, escaped) {
    var codeHtml = code;
    if (infostring && infostring == "html") {
      codeHtml = encodeURIComponent(code);
    }
    if (infostring) {
      codeHtml = hljs.highlightAuto(code).value;
    }

    console.log(code, infostring, escaped, codeHtml);

    return `<div class="bg-black mb-4 rounded-md">
      <div class="code_header flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans">
        <span>${infostring || ""}</span>
        <button onclick="copy(this)" class="flex ml-auto gap-2">
          <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
          </svg>
          <span>Copy code</span>
          <code style="display:none">${encodeURIComponent(code)}</code>
        </button>
      </div>
      <div class="p-4 overflow-y-auto">
        <code class="!whitespace-pre hljs language-${infostring}">${codeHtml}</code>
      </div>
    </div>`;
  },
  paragraph(text) {
    return `<p style="white-space:pre-wrap;">${text}</p>`;
  },
};
marked.use({ renderer });

export default {
  data() {
    return {
      theme: "light",
      avatarIdx: 1,
      conversations: [],
      conversation: [],
      chatMsg: "",
      tempMsg: "",
      chatTitle: "New chat",
      convLoading: false,
      showSlide: false,
      isShowGoBottom: false,
      oldConv: undefined,
      convTitletmp: "",
      username: "user123", // 示例用户ID，可动态生成或从登录信息获取
      session_id: "session_001", // 会话ID，初始为空，动态生成
      popupShow: false, // 添加 popupShow，初始为 false
    };
  },
  methods: {

    goToCharacter() {
      router.push('/character');
    },
    closeSource() {
      var that = this;
      if (that.source) {
        that.source.close();
        that.source = undefined;
      }
      if (that.tsource) {
        that.tsource.close();
        that.tsource = undefined;
      }
      if (that.rsource) {
        that.rsource.close();
        that.rsource = undefined;
      }
    },
    stopChat() {
      var that = this;
      this.axios
        .put(`/stop/chat/${this.session_id}`, {})
        .then((result) => {
          var rconv = that.conversation[that.conversation.length - 1];
          rconv["loading"] = false;
          that.convLoading = false;

          if (that.conversation.length == 2 && rconv["speeches"].length == 1) {
            var newConv = {
              id: that.session_id,
              title: "New chat",
            };

            that.generateConvTitle(newConv);
            that.conversations.unshift(newConv);
            that.selectConversation(newConv, false);
            that.saveConversations();
          }

          that.refrechConversation();
          that.closeSource();
        })
        .catch((err) => {
          that.closeSource();
        });
    },
    closeShowSlide() {
      this.showSlide = false;
      this.$refs.menu.appendChild(this.$refs.navEle);
    },
    showSlideMethod() {
      this.showSlide = true;
      this.$refs.slideNavContainer.appendChild(this.$refs.navEle);
    },
    changeHeight() {
      var elem = this.$refs.inputChat;
      elem.style.height = "24px";
      var scrollHeight = elem.scrollHeight;
      if (24 >= scrollHeight || this.chatMsg.length == 0) {
        this.resetHeight();
        return;
      }

      elem.style.removeProperty("overflow-y");
      elem.style.height = scrollHeight + "px";
    },
    resetHeight() {
      var elem = this.$refs.inputChat;
      elem.style.height = "24px";
      elem.style["overflow-y"] = "hidden";
    },
    closePopup() {
      this.popupShow = false;
    },
    vueCopy(node) {
      var code = node.getElementsByTagName("code")[0].innerHTML;
      var text = decodeURIComponent(code);
      this.$copyText(text).then(
        (res) => {
          var svg = `<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                        <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    <span>Copied!</span>`;
          const nodeInnerHtml = node.innerHTML;
          node.innerHTML = svg;

          setTimeout(() => {
            node.innerHTML = nodeInnerHtml;
          }, 1000);
        },
        (err) => {
          console.log("复制失败");
        }
      );
    },
    changeTheme(theme) {
      this.theme = theme;
      var html = document.getElementsByTagName("html")[0];
      html.classList.remove("light", "dark");
      html.classList.add(theme);
      html.style["color-scheme"] = theme;
      localStorage.setItem("theme", theme);
    },
    initConvs(convs) {
      if (!Array.isArray(convs)) {
        console.warn("initConvs: convs is not an array", convs);
        return [];
      }
      const formattedConvs = [];
      for (let i = 0; i < convs.length; i++) {
        const conv = convs[i];
        // 添加人类消息
        formattedConvs.push({
          speaker: "human",
          speech: conv.input,
        });
        // 添加 AI 消息
        formattedConvs.push({
          speaker: "AI",
          speeches: [conv.output], // output 转为数组
          suitable: [0], // 添加默认 suitable
          idx: 0, // 设置初始 idx
        });
      }
      return formattedConvs;
    },
    last(conv) {
      if (conv.idx == 0) {
        return;
      }
      conv.idx--;
      this.refrechConversation();
    },
    suitable(idx, conv, suit) {
      var that = this;
      var cdate = {
        idx: idx,
        msg_idx: conv.idx,
        suitable: suit,
      };
      conv.suitable[conv.idx] = suit;

      this.axios
        .put(`/AI/suitable/${this.session_id}`, cdate)
        .then((result) => {
          console.log(result);

          that.refrechConversation();
        })
        .catch((err) => {});
    },
    next(conv) {
      if (conv.idx == conv["speeches"].length - 1) {
        return;
      }
      conv.idx++;
      this.refrechConversation();
    },
    inputChat(msg) {
      console.log(msg);
      this.chatMsg = msg;
    },
    countAndConcat(str, substr) {
      // 使用正则表达式的全局匹配来查找子字符串
      const matches = str.match(new RegExp(substr, "g"));

      // 判断子字符串的个数是奇数还是偶数
      const count = matches ? matches.length : 0;
      const isOdd = count % 2 === 1;

      // 根据判断结果返回相应的字符串
      return isOdd ? str + "\n" + substr : str;
    },
    mdToHtml(md, conv) {
      if (md == "") {
        return "<p></p>";
      }

      md = this.countAndConcat(md, "```");

      var htmlMD = marked.parse(md);
      htmlMD = htmlMD.trim();
      return htmlMD;
    },
    refrechConversation() {
      this.conversation = JSON.parse(JSON.stringify(this.conversation));
    },
    async chatRepeat() {
      if (this.convLoading) {
        return;
      }

      var that = this;
      this.convLoading = true;

      // 获取最后一条对话并初始化新重复生成的内容
      var rconv = this.conversation[this.conversation.length - 1];
      rconv["idx"] = rconv["suitable"].length;
      rconv["loading"] = true;
      rconv["suitable"].push(0);
      rconv["speeches"].push(""); // AI 占位消息
      that.refrechConversation();

      try {
        // 使用 axios 获取重复生成的内容
        const response = await axios
          .post("/chat", {
            username: this.username,
            session_id: this.session_id, // 如果没有 session_id，生成一个临时值
            text: this.tempMsg,
          })
          .then((response) => {
            console.log(response);

            var fullContent = response.data.response || "重复生成失败";

            // 处理换行符
            if (fullContent.includes("[ENTRY]")) {
              fullContent = fullContent.replaceAll("[ENTRY]", "\n");
            }

            // 模拟逐步更新
            let currentContent = "";
            const chunks = fullContent.split(""); // 按字符分割，模拟流式效果
            let index = 0;

            const updateInterval = setInterval(() => {
              if (index < chunks.length) {
                currentContent += chunks[index];
                rconv["speeches"][rconv["idx"]] = currentContent;
                that.handleScrollBottom();
                that.refrechConversation();
                index++;
              } else {
                // 更新完成
                clearInterval(updateInterval);
                rconv["loading"] = false;
                that.convLoading = false;
                that.refrechConversation();
              }
            }, 50); // 每 50ms 更新一次，模拟流式效果
          });
      } catch (error) {
        console.error(
          "Error repeating chat:",
          error.response ? error.response.data : error
        );
        rconv["speeches"][rconv["idx"]] = "错误：无法重复生成";
        rconv["loading"] = false;
        that.convLoading = false;
        that.refrechConversation();
      }
    },
    judgeInput(e) {
      if (!e.shiftKey && e.keyCode == 13) {
        e.cancelBubble = true; //ie阻止冒泡行为
        e.stopPropagation(); //Firefox阻止冒泡行为
        e.preventDefault(); //取消事件的默认动作*换行
        this.send();
      }
    },
    send() {
      if (this.chatMsg.trim().length == 0 || this.convLoading) {
        return;
      }

      this.convLoading = true;
      var chatMsg = this.chatMsg.trim().replace(/\n/g, "");
      this.tempMsg = chatMsg;
      this.chatMsg = "";

      var first = this.conversation.length == 0;

      // 添加用户消息
      this.conversation.push({
        speaker: "human",
        speech: chatMsg,
      });

      // 添加 AI 占位消息
      var conv = {
        idx: 0,
        loading: true,
        speaker: "AI",
        suitable: [0],
        speeches: [""],
      };
      this.conversation.push(conv);

      // 滚动到底部
      this.handleScrollBottom();

      var that = this;

      if (!this.session_id) {
        this.loadId();
        setTimeout(() => this.send(), 100); // 延迟重新调用 send
        return;
      }

      // 添加调试日志
      console.log("Sending request with:", {
        username: this.username,
        session_id: this.session_id,
        text: chatMsg,
      });

      // 发送请求到后端
      axios
        .post("/chat", {
          username: this.username,
          session_id: this.session_id,
          text: chatMsg,
        })
        .then((response) => {
          console.log("Response:", response.data);

          // 更新AI消息
          var aiConv = that.conversation[that.conversation.length - 1];
          aiConv.speeches[0] = response.data.response; // 后端返回的 response
          aiConv.loading = false;
          that.convLoading = false;

          // 如果是首次对话，初始化 session_id 和 conversations
          if (first) {
            that.session_id = that.session_id || `session_${Date.now()}`;
            var newConv = {
              id: that.session_id,
              title: "New chat",
            };
            that.generateConvTitle(newConv); // 可选：生成标题
            that.conversations.unshift(newConv);
            that.selectConversation(newConv, false);
            that.saveConversations();
          }

          that.refrechConversation();
        })
        .catch((error) => {
          console.error("Error:", error);
          var aiConv = that.conversation[that.conversation.length - 1];
          aiConv.speeches[0] = "错误：无法获取回复";
          aiConv.loading = false;
          that.convLoading = false;
          that.refrechConversation();
        });
    },
    async generateConvTitle(conv) {
      var that = this;
      try {
        const response = await axios.get(`/chat/title/${this.session_id}`);
        conv.title = response.data.title || "默认标题";

        // 更新会话并保存
        that.selectConversation(conv, false);
        that.saveConversations();
      } catch (error) {
        console.error(
          "Error generating title:",
          error.response ? error.response.data : error
        );
        conv.title = "标题生成失败"; // 错误时的默认标题
        that.selectConversation(conv, false);
        that.saveConversations();
      }
    },
    newChat() {
      if (this.conversation.length == 0) {
        return;
      }

      this.chatTitle = "New chat";
      document.title = "New chat";
      var conversations = this.conversations;
      for (let idx in conversations) {
        var conv = conversations[idx];
        delete conv.editable;
        delete conv.selected;
        delete conv.delete;
      }

      this.loadId();
    },
    loadId() {
      var that = this;
      this.axios
        .get("/generate/id", {})
        .then((result) => {
          console.log(result);
          var resp = result.data;
          that.session_id = resp.data; // 假设后端返回 session_id
          that.conversation = [];
        })
        .catch((err) => {
          console.error(err);
        });
    },
    loadConversations() {
      let convs = localStorage.getItem("conversations") || "[]";
      this.conversations = JSON.parse(convs);
    },
    saveConversations() {
      var conversations = JSON.parse(JSON.stringify(this.conversations));
      for (let idx in conversations) {
        var conv = conversations[idx];
        delete conv.editable;
        delete conv.selected;
        delete conv.delete;
      }
      let convs = JSON.stringify(conversations);
      localStorage.setItem("conversations", convs);
    },
    clearConversations() {
      this.conversations = [];
      this.saveConversations();
    },
    selectConversation(conv, loadConv) {
      var that = this;
      if (this.oldConv) {
        this.oldConv.selected = false;
      }
      conv.selected = true;
      this.oldConv = conv;

      document.title = conv.title || "chatai";
      this.chatTitle = conv.title || "chatai";
      this.session_id = conv.id; // 设置当前 session_id

      if (!loadConv) {
        return;
      }
      this.username = "user123";
      this.session_id = "e00dd1d0-267b-4f3c-97e6-0d77504eb1ef";
      // 假设后端提供接口获取历史对话
      this.axios
        .get(`/history/${this.username}/${this.session_id}`)
        .then((result) => {
          console.log(result.data.conversations);
          var resp = result.data;
          that.conversation = that.initConvs(resp.conversations); // 假设返回 conversations 数组
          setTimeout(() => {
            that.isScrollAndNotBottom();
          }, 300);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    editTitle(idx, conv) {
      this.convTitletmp = conv.title;
      conv.editable = true;
      this.$set(this.conversations, idx, conv);
      setTimeout(() => {
        document.getElementById("titleInput").focus();
      }, 150);
    },
    titleInputBlur(idx, conv) {
      setTimeout(() => {
        this.cancelChangeConvTitle(idx, conv);
      }, 100);
    },
    changeConvTitle(idx, conv) {
      conv.title = this.convTitletmp;
      this.saveConversations();
      this.cancelChangeConvTitle(idx, conv);
    },
    cancelChangeConvTitle(idx, conv) {
      conv.editable = false;
      this.$set(this.conversations, idx, conv);
    },
    delConv(cidx) {
      this.conversations.splice(cidx, 1);
      this.saveConversations();
    },
    cancelDelConv(idx, conv) {
      conv.delete = false;
      this.$set(this.conversations, idx, conv);
    },
    loadAvatar() {
      let avatar =
        localStorage.getItem("avatar") || Math.ceil(Math.random() * 9);
      this.avatarIdx = avatar;
    },
    handleScrollBottom() {
      this.$nextTick(() => {
        let scrollElem = this.$refs.chatContainer;
        scrollElem.scrollTo({
          top: scrollElem.scrollHeight,
          behavior: "smooth",
        });
      });
    },
    isScrollAndNotBottom() {
      let chatDivEle = this.$refs.chatContainer;
      if (!chatDivEle) {
        return;
      }

      if (chatDivEle.scrollHeight <= chatDivEle.clientHeight) {
        this.isShowGoBottom = false;
        return;
      }

      const scrollTop = chatDivEle.scrollTop;
      const windowHeight = chatDivEle.clientHeight;
      const scrollHeight = chatDivEle.scrollHeight;
      if (scrollTop + windowHeight >= scrollHeight - 50) {
        this.isShowGoBottom = false;
        return;
      }

      this.isShowGoBottom = true;
    },
  },
  computed: {},
  watch: {
    chatMsg(newVal, oldVal) {
      if (newVal === oldVal) {
        return;
      }
      this.changeHeight();
    },
  },
  mounted: function () {
    var theme = localStorage.getItem("theme") || "light";
    this.changeTheme(theme);
    this.loadId();
    this.loadConversations();
    this.loadAvatar();

    let chatDivEle = this.$refs.chatContainer;
    chatDivEle.addEventListener("scroll", this.isScrollAndNotBottom, true);

    window.copy = this.vueCopy;
  },
};
</script>


<style lang="scss">
html,
body {
  height: 100%;
  width: 100%;
}

#container {
  height: 100%;
}

.flex_row_c_c {
  display: flex;
  align-content: center;
  flex-direction: row;
  justify-items: center;
}

.react-scroll-to-bottom--css-krija-1n7m0yu {
  height: 100%;
  overflow-y: auto;
  width: 100%;
}

.code_header {
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}

.prose :where(code):not(:where([class~="not-prose"] *)):before {
  content: "" !important;
}

.prose :where(code):not(:where([class~="not-prose"] *)):after {
  content: "" !important;
}

#chatRepeat:focus {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0
    var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0
    calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  --tw-ring-offset-width: 0px;
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow),
    0 0 transparent;
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow),
    var(--tw-shadow, 0 0 transparent);
}

.suitable_selected {
  --tw-text-opacity: 1 !important;
  cursor: auto !important;
}

.load_dot1 {
  -webkit-animation: blink 1s steps(2, start) infinite;
  animation: blink 1s steps(2, start) infinite;
}

.load_dot2 {
  -webkit-animation: blink 1s steps(3, start) infinite;
  animation: blink 1s steps(3, start) infinite;
}

.load_dot3 {
  -webkit-animation: blink 1s steps(4, start) infinite;
  animation: blink 1s steps(4, start) infinite;
}

#container .markdown h1 {
  margin-bottom: 0rem;
  margin-top: 0rem;
}

#container .markdown h2 {
  margin-bottom: 0rem;
  margin-top: 0rem;
}

#container .markdown h3 {
  margin-bottom: 0rem;
  margin-top: 0rem;
}

#container .markdown h4 {
  margin-bottom: 0rem;
  margin-top: 0rem;
}

#container .markdown h5 {
  margin-bottom: 0rem;
  margin-top: 0rem;
}

#container .markdown h6 {
  margin-bottom: 0rem;
  margin-top: 0rem;
}

@media (max-width: 640px) {
  #container .none {
    display: none;
  }
}

.w-180px {
  width: 180px;
}

.prose-r {
  font-size: 1rem;
  line-height: 1.75;
}


/* 新建对话样式 */
.fancy-button {
  background: #4b5563;
  position: relative;
  transition: background 0.3s ease;

  &:hover {
    background: #6b7280;
  }

  &::after {
    content: '';
    position: absolute;
    width: 20px;
    height: 20px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    transform: scale(0);
    animation: ripple 0.6s linear;
    pointer-events: none;
  }

  &:active::after {
    animation: none;
    transform: scale(10);
    opacity: 0;
    transition: transform 0.6s ease, opacity 0.6s ease;
  }
}

@keyframes ripple {
  to {
    transform: scale(10);
    opacity: 0;
  }
}
</style>
