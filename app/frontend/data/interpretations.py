"""Interpretation texts for natal chart positions and aspects."""

# ── Planet in Sign ────────────────────────────────────────────────────────────
# keyed (planet, sign)

PLANET_IN_SIGN: dict[tuple[str, str], str] = {

    # Sun
    ("Sun", "Aries"):       "Identity burns bright and impulsive, leading with instinct over strategy. Born to initiate, you are most alive when going first.",
    ("Sun", "Taurus"):      "The self is grounded in pleasure, endurance, and what can be built to last. Power comes through patience and an unshakeable sense of your own worth.",
    ("Sun", "Gemini"):      "Identity is fluid, curious, and perpetually in motion. You shine brightest in conversation and thrive on the play of ideas.",
    ("Sun", "Cancer"):      "The self is deeply tied to feeling, family, and the sanctuary of home. Creative expression runs through the emotional body — when you feel safe, you shine.",
    ("Sun", "Leo"):         "Born to radiate, your identity craves creative expression and an audience. Generosity and pride walk side by side in everything you do.",
    ("Sun", "Virgo"):       "The self finds purpose through service, craft, and discernment. Identity is expressed through what you improve, not what you display.",
    ("Sun", "Libra"):       "Identity is most alive in relationship — you see yourself clearly in the mirror of others. Harmony and fairness are not just preferences; they are core needs.",
    ("Sun", "Scorpio"):     "The self runs deep, magnetic, and transformative. Power is your currency, and nothing stays surface-level for long.",
    ("Sun", "Sagittarius"): "Identity expands through exploration — of lands, ideas, and belief systems. You are at your most alive when pursuing a horizon.",
    ("Sun", "Capricorn"):   "The self is forged through discipline and ambition. You shine by building lasting things and earning respect through effort over time.",
    ("Sun", "Aquarius"):    "Identity is bound up with a vision of what could be — you are a natural outsider-turned-visionary. Individual expression paradoxically serves the collective.",
    ("Sun", "Pisces"):      "The self is permeable, empathic, and spiritually attuned. Identity can be elusive, but your gift is seeing the world as one unbroken whole.",

    # Moon
    ("Moon", "Aries"):       "Emotional responses are fast and fiery — you feel first, reflect later. Needs center on autonomy and the freedom to act on instinct.",
    ("Moon", "Taurus"):      "Security comes through the senses — comfort, beauty, and stability soothe the inner world. Emotions run deep and slow, built to last.",
    ("Moon", "Gemini"):      "The emotional life moves at the speed of thought, restless and curious. Talking through feelings is how you process and release them.",
    ("Moon", "Cancer"):      "At home in the depths of feeling, nurturing and being nurtured are instinctive needs. The home and family are the emotional core of your world.",
    ("Moon", "Leo"):         "You need to be seen and appreciated to feel emotionally secure. Warmth and drama color the inner life in equal measure.",
    ("Moon", "Virgo"):       "Emotions are processed analytically — feelings get sorted, named, and put to use. You feel safest when things are working properly.",
    ("Moon", "Libra"):       "Harmony and beauty are emotional necessities, not optional comforts. You feel most settled in an atmosphere of fairness and aesthetic calm.",
    ("Moon", "Scorpio"):     "Feelings run bottomless and intense — there is no shallow end to your emotional life. You crave true intimacy or none at all.",
    ("Moon", "Sagittarius"): "Freedom is an emotional need, not a luxury. You feel most alive when there is a sense of possibility and forward motion ahead.",
    ("Moon", "Capricorn"):   "Emotional restraint comes naturally, and security is found in structure and accomplishment. Vulnerability takes time and earned trust.",
    ("Moon", "Aquarius"):    "You process emotions from a slight remove, feeling through ideas before feelings. Connection to the group matters as much as individual bonds.",
    ("Moon", "Pisces"):      "The boundary between your feelings and those of others is thin by nature. Compassion and dreaminess are innate; grounding takes intention.",

    # Mercury
    ("Mercury", "Aries"):       "Thought is fast, direct, and rarely filtered — you arrive at conclusions first and justify them later. Words come like darts.",
    ("Mercury", "Taurus"):      "The mind moves deliberately, preferring to arrive at conclusions slowly and solidly. Once formed, opinions rarely budge.",
    ("Mercury", "Gemini"):      "Thinking is nimble and multidirectional — you hold contradictions easily and delight in the play of ideas. Communication is a native gift.",
    ("Mercury", "Cancer"):      "The mind works through feeling and association, absorbing information emotionally. Memory is long, especially for things with personal resonance.",
    ("Mercury", "Leo"):         "Thought is dramatic and generous — you speak with flair and enjoy holding an audience. Ideas are expressed with conviction and warmth.",
    ("Mercury", "Virgo"):       "The mind is precise, analytical, and drawn to the detail others miss. Communication tends toward clarity, craft, and practical application.",
    ("Mercury", "Libra"):       "Thinking is balanced, fair-minded, and perpetually weighing both sides. Decisions can come late, but they tend to be well-considered.",
    ("Mercury", "Scorpio"):     "The mind probes beneath every surface, looking for what is concealed. Communication can be incisive or strategic — silence is also a tool.",
    ("Mercury", "Sagittarius"): "Thinking operates on a large scale, interested in principles rather than particulars. Communication is direct, enthusiastic, and occasionally blunt.",
    ("Mercury", "Capricorn"):   "The mind is disciplined, structured, and oriented toward practical results. Words are carefully chosen and tend to carry real weight.",
    ("Mercury", "Aquarius"):    "Thinking is original, systems-oriented, and often ahead of its time. You communicate ideas that challenge the status quo.",
    ("Mercury", "Pisces"):      "The mind works through imagery, symbol, and intuition rather than linear logic. Communication can be poetic, elusive, or beautifully imprecise.",

    # Venus
    ("Venus", "Aries"):       "Love is exciting, direct, and pursued with zeal. You are drawn to the chase and express affection through bold, spontaneous action.",
    ("Venus", "Taurus"):      "Beauty, comfort, and physical pleasure are the language of love. You are loyal and sensual — slow to warm but enduring once committed.",
    ("Venus", "Gemini"):      "Variety and wit are what attract — you fall for minds first. Love needs conversation and fresh stimulation to stay alive.",
    ("Venus", "Cancer"):      "Affection runs deep, nurturing, and protective. You love through acts of care and need to feel emotionally safe before opening up.",
    ("Venus", "Leo"):         "Love is theatrical, generous, and in need of an audience. You want to be adored and give back that same warmth in full.",
    ("Venus", "Virgo"):       "Love is expressed through acts of service and meticulous attention. You show you care by making things work better for the people you love.",
    ("Venus", "Libra"):       "Beauty, harmony, and partnership are native needs. You are a natural romantic who thrives in the graceful energy of togetherness.",
    ("Venus", "Scorpio"):     "Love is all-consuming, magnetic, and capable of great depth. You crave intensity and have little interest in anything superficial.",
    ("Venus", "Sagittarius"): "Love is expansive and freedom-loving — you are drawn to the adventure a relationship can provide. Philosophical alignment matters more than domestic comfort.",
    ("Venus", "Capricorn"):   "Love is serious, loyal, and built for the long haul. You prefer substance over style and show care through reliability and commitment.",
    ("Venus", "Aquarius"):    "Friendship is the foundation of love — you are attracted to the unusual and independent. Emotional space is non-negotiable.",
    ("Venus", "Pisces"):      "Love is boundless, imaginative, and spiritually attuned. You dissolve into connection easily and feel everything the beloved feels.",

    # Mars
    ("Mars", "Aries"):       "Energy is direct, impulsive, and unapologetically self-focused. You act first and formulate the plan in motion.",
    ("Mars", "Taurus"):      "Drive is slow to ignite but nearly impossible to stop once moving. You pursue what you want with steady, relentless determination.",
    ("Mars", "Gemini"):      "Energy scatters in many directions at once — enthusiasm runs high until novelty fades. You fight with words as readily as with actions.",
    ("Mars", "Cancer"):      "Drive operates through emotional motivation — you act to protect what you love. Energy can be indirect, moving sideways toward the goal.",
    ("Mars", "Leo"):         "Action is dramatic, confident, and oriented toward recognition. You fight for center stage and for what you believe in with full-hearted commitment.",
    ("Mars", "Virgo"):       "Energy is channeled into precision and improvement. You get things done through methodical effort and a sharp eye for what needs fixing.",
    ("Mars", "Libra"):       "Drive is filtered through consideration of others — action rarely happens without weighing the relational consequences. Conflict is approached diplomatically.",
    ("Mars", "Scorpio"):     "Will is focused, intense, and strategically deployed. You move toward your objectives with ruthless patience and rarely reveal your hand early.",
    ("Mars", "Sagittarius"): "Energy is enthusiastic, far-ranging, and driven by principle. You act on belief and thrive when there is a cause worth fighting for.",
    ("Mars", "Capricorn"):   "Drive is disciplined, strategic, and long-sighted. You work harder than almost anyone and measure success by what you actually build.",
    ("Mars", "Aquarius"):    "Energy is channeled into ideas and collective causes. You fight for freedom — your own and others' — and resist being controlled.",
    ("Mars", "Pisces"):      "Drive flows through imagination and empathy. Energy can be elusive or all-enveloping depending on the cause — you need to believe in what you are chasing.",

    # Jupiter
    ("Jupiter", "Aries"):       "Luck arrives through boldness and initiative — the more you lead, the more opens up. Growth comes through direct, courageous action.",
    ("Jupiter", "Taurus"):      "Abundance flows when you cultivate patience and invest in quality. Good fortune is tied to the material and the sensory.",
    ("Jupiter", "Gemini"):      "Growth multiplies through learning, connecting, and communicating. Curiosity is your most reliable path to expansion.",
    ("Jupiter", "Cancer"):      "Luck and growth flow through emotional intelligence, home, and family. Care and nurturing open doors that ambition alone cannot.",
    ("Jupiter", "Leo"):         "Abundance arrives through creative self-expression and the courage to be seen. Generosity attracts more generosity.",
    ("Jupiter", "Virgo"):       "Growth comes through mastery, service, and attention to fine detail. The more useful you are, the more the world opens up.",
    ("Jupiter", "Libra"):       "Fortune flows through relationship, partnership, and the cultivation of harmony. Collaboration reliably multiplies results.",
    ("Jupiter", "Scorpio"):     "Luck comes through transformation and the willingness to go deep. Hidden resources and shared power open up when you stop holding back.",
    ("Jupiter", "Sagittarius"): "Jupiter in its home sign — growth comes through exploration, philosophy, and faith. Your optimism tends to become self-fulfilling.",
    ("Jupiter", "Capricorn"):   "Fortune grows through disciplined effort and long-term strategy. The more seriously you work, the more structure rewards you.",
    ("Jupiter", "Aquarius"):    "Growth flows through community, originality, and progressive thinking. Connecting with the wider world reliably brings opportunity.",
    ("Jupiter", "Pisces"):      "Luck arrives through compassion, surrender, and spiritual openness. The less you grasp, the more tends to come to you.",

    # Saturn
    ("Saturn", "Aries"):       "The lesson is learning to act with discipline rather than impulse. True independence is earned through patient self-development.",
    ("Saturn", "Taurus"):      "Security must be built, not inherited — the lesson is earning and sustaining material stability through consistent effort. Overattachment to comfort is the shadow.",
    ("Saturn", "Gemini"):      "The challenge is learning to focus the restless mind and communicate with precision and depth. Scattered thinking must eventually be disciplined.",
    ("Saturn", "Cancer"):      "Emotional security requires intentional cultivation — the lesson is learning to nurture without losing yourself. Family history may carry obligations or wounds to work through.",
    ("Saturn", "Leo"):         "The lesson is developing authentic self-confidence rather than demanding approval. Creative expression is a discipline here, not a given.",
    ("Saturn", "Virgo"):       "Perfectionism can become paralysis — the lesson is learning when good enough truly is. Mastery of craft and service are the real domains of growth.",
    ("Saturn", "Libra"):       "The challenge is learning to build true partnership rather than performing harmony. Commitment carries weight here and should not be taken lightly.",
    ("Saturn", "Scorpio"):     "Power, vulnerability, and shared resources are the domains of challenge and eventual mastery. The lesson is learning to trust through the fear of loss.",
    ("Saturn", "Sagittarius"): "The lesson is developing wisdom rooted in experience rather than belief. Too much freedom can scatter; discipline in philosophy brings real authority.",
    ("Saturn", "Capricorn"):   "Saturn in its own sign — the lessons of ambition, structure, and responsibility are especially pronounced. Success is possible but comes through sustained effort and delayed gratification.",
    ("Saturn", "Aquarius"):    "The challenge is building community while honoring individuality. Learning to lead collectives without losing the self inside is a lifetime's work.",
    ("Saturn", "Pisces"):      "The lesson is learning to work with the boundary between the real and the imagined. Developing structure without crushing sensitivity brings lasting stability.",

    # Uranus
    ("Uranus", "Aries"):       "Collective awakening arrives through radical individuality and a willingness to break precedent. Revolution is personal before it is political.",
    ("Uranus", "Taurus"):      "Upheaval moves through the material realm — economics, land, and resources are disrupted and reinvented. The body and nature are being revolutionized.",
    ("Uranus", "Gemini"):      "Ideas and communication are disrupted and revitalized en masse. A generation invents new languages and new ways of knowing.",
    ("Uranus", "Cancer"):      "The revolution is emotional and domestic — family structures, home, and belonging are radically reimagined. What it means to nurture and be nurtured changes.",
    ("Uranus", "Leo"):         "Creative expression and individuality are the engines of collective change. A generation insists on being seen on its own terms.",
    ("Uranus", "Virgo"):       "The revolution is methodological — systems of work, health, and service are overhauled. Precision and technology become tools of liberation.",
    ("Uranus", "Libra"):       "Partnership and justice are radically renegotiated by this generation. Old models of relationship and fairness are dismantled and rebuilt.",
    ("Uranus", "Scorpio"):     "Collective transformation goes into the depths — sexuality, power, death, and shared resources are disrupted and reframed. The taboo becomes visible.",
    ("Uranus", "Sagittarius"): "A generation questions belief systems, institutions, and the nature of truth. Radical freedom of thought expands the collective horizon.",
    ("Uranus", "Capricorn"):   "Authority, institutions, and the rules of success are disrupted and rebuilt. A generation rewrites the structures of power from the ground up.",
    ("Uranus", "Aquarius"):    "Uranus in its home sign — a generation of innovators bent on remaking society through technology and collective vision. The future is being prototyped now.",
    ("Uranus", "Pisces"):      "The dissolution of boundaries between the self and the collective reaches a breaking point. Spirituality, art, and the unconscious become vectors of liberation.",

    # Neptune
    ("Neptune", "Aries"):       "Idealism meets impulse — a generation animated by spiritual courage and naive heroism. Dreams are bold and sometimes reckless.",
    ("Neptune", "Taurus"):      "The ideal is beauty, material harmony, and a return to natural rhythms. Spiritual longing finds expression in art, land, and sensory grace.",
    ("Neptune", "Gemini"):      "A generation dissolves the line between fact and fiction — language, information, and perception are all subject to collective glamour or confusion.",
    ("Neptune", "Cancer"):      "Home and family become idealized, mythologized. A generation dreams of belonging and roots, and the past is tenderly romanticized.",
    ("Neptune", "Leo"):         "A generation reaches for creative transcendence — the ideal is glamour, artistic greatness, and the shining individual. Inspiration and illusion run equally high.",
    ("Neptune", "Virgo"):       "Collective idealism filters through the practical — the dream is perfection, purity, and service. Disillusionment follows when reality fails to meet the ideal.",
    ("Neptune", "Libra"):       "A generation dreams of perfect harmony and justice. Idealism in relationships and a longing for beauty can veer into illusion and codependence.",
    ("Neptune", "Scorpio"):     "The collective unconscious surfaces through power, sexuality, and transformation. Hidden forces are romanticized or feared beyond their actual size.",
    ("Neptune", "Sagittarius"): "Spiritual and philosophical hunger sweeps a generation — the search for meaning through travel, religion, or ideology. Both inspiration and mass delusion are possible.",
    ("Neptune", "Capricorn"):   "Collective dreams center on success, legacy, and the institutions that shape society. Disillusionment with authority figures is a defining generational theme.",
    ("Neptune", "Aquarius"):    "Idealism flows through technology and the collective dream of a better, more connected world. Virtual reality and social illusions blur the line between community and performance.",
    ("Neptune", "Pisces"):      "Neptune in its home sign — collective spiritual longing and dissolution of boundaries reach their height. The generation is deeply empathic and prone to both transcendence and escapism.",

    # Pluto
    ("Pluto", "Aries"):       "Transformation is driven by the assertion of raw will. A generation destroys and rebuilds through conquest and radical individualism.",
    ("Pluto", "Taurus"):      "Deep collective change moves through economics, land, and the foundations of material life. The old order of wealth and resource is dismantled.",
    ("Pluto", "Gemini"):      "Transformation arrives through information and the power of ideas. Communication is both the site of decay and the engine of renewal.",
    ("Pluto", "Cancer"):      "A generation transforms through home, family, and emotional roots. The structure of domestic life and nationhood is fundamentally altered.",
    ("Pluto", "Leo"):         "Collective power concentrates around individual will and creative expression. A generation demands recognition and reshapes the world around the force of personality.",
    ("Pluto", "Virgo"):       "Deep transformation moves through systems of work, health, and daily life. A generation dismantles inefficiency and rebuilds through rigorous improvement.",
    ("Pluto", "Libra"):       "Transformation reaches into relationship, justice, and the social contract. A generation rewrites the rules of partnership and equality.",
    ("Pluto", "Scorpio"):     "Pluto in its home sign — transformation goes as deep as it gets. A generation confronts power, death, sexuality, and the collective shadow head-on.",
    ("Pluto", "Sagittarius"): "Collective transformation arrives through the collapse and renewal of belief systems — religion, philosophy, and the search for meaning all undergo profound upheaval.",
    ("Pluto", "Capricorn"):   "Institutions, governments, and the structures of power are dismantled and rebuilt. A generation tears down what is not working and replaces it with something built to last.",
    ("Pluto", "Aquarius"):    "Transformation arrives through technology and the collective — a generation rebuilds society around new visions of community and human potential.",
    ("Pluto", "Pisces"):      "The deepest collective transformation — old spiritual frameworks dissolve and new ones emerge. The boundary between the individual and the whole finally gives way.",

    # North Node — growth direction by sign
    ("North Node", "Aries"):       "Growth calls toward courage, self-assertion, and the willingness to act without needing consensus. The soul is learning to trust its own instincts and pioneer its own path rather than defer to others.",
    ("North Node", "Taurus"):      "The soul is growing toward simplicity, embodiment, and the quiet power of what endures. Learning to find security in the physical world — pleasure, steadiness, and trust in the here and now — is the work.",
    ("North Node", "Gemini"):      "Growth comes through curiosity, adaptability, and the honest exchange of ideas. The soul is learning to hold multiple perspectives without needing a single grand theory to tie them all together.",
    ("North Node", "Cancer"):      "The soul is growing toward emotional depth, vulnerability, and the courage to need and be needed. Nurturing oneself and others — rather than achieving and performing — is the evolutionary path.",
    ("North Node", "Leo"):         "Growth calls toward creative self-expression, warmth, and the courage to be genuinely seen. The soul is learning to lead with heart rather than idea, and to invest deeply in the personal rather than the collective.",
    ("North Node", "Virgo"):       "The soul is growing toward discernment, service, and the satisfaction of doing things well. Learning to be useful in concrete, practical ways — and to distinguish reality from illusion — is the evolutionary work.",
    ("North Node", "Libra"):       "Growth calls toward partnership, diplomacy, and the art of genuine cooperation. The soul is learning that true strength includes the ability to consider others and seek harmony without losing itself.",
    ("North Node", "Scorpio"):     "The soul is growing toward depth, transformation, and the willingness to meet loss and intensity without flinching. Shared resources — emotional, financial, and psychological — are the arena of growth.",
    ("North Node", "Sagittarius"): "Growth calls toward vision, philosophy, and the willingness to commit to a truth and follow it to the horizon. The soul is learning to move from gathering information to living by wisdom.",
    ("North Node", "Capricorn"):   "The soul is growing toward discipline, responsibility, and the building of lasting structures in the world. Taking authority over one's own life — rather than waiting to be held or rescued — is the evolutionary call.",
    ("North Node", "Aquarius"):    "Growth calls toward collective vision, humanitarian ideals, and the willingness to serve something larger than personal glory. The soul is learning to release ego-investment and find meaning in the greater pattern.",
    ("North Node", "Pisces"):      "The soul is growing toward compassion, surrender, and spiritual trust. Learning to release the grip of analysis and allow the deeper currents of life to carry you forward is the evolutionary invitation.",

    # South Node — past-life comfort zone by sign
    ("South Node", "Aries"):       "The past holds a warrior energy — self-reliance, impulsivity, and the habit of going it alone. The invitation is to channel that directness into relationship and cooperation rather than opposition.",
    ("South Node", "Taurus"):      "A past of comfort, stability, and self-sufficiency has left a deeply ingrained desire for security and the familiar. The invitation is to release attachment to what is safe and allow genuine transformation.",
    ("South Node", "Gemini"):      "The past is rich with wit, adaptability, and the restless collecting of facts and connections. The invitation is to move beyond clever commentary and toward meaning — from data to wisdom.",
    ("South Node", "Cancer"):      "Deep roots in emotional security, family, and the comforts of belonging have left a pull toward dependency and the familiar nest. The invitation is to bring that emotional richness into the world through mature responsibility.",
    ("South Node", "Leo"):         "The past holds a natural comfort with being the center — with recognition, creative expression, and the warmth of personal power. The invitation is to shift from personal radiance to collective contribution.",
    ("South Node", "Virgo"):       "A past steeped in service, precision, and careful analysis has left a tendency toward criticism, worry, and the need for control. The invitation is to dissolve those boundaries into faith and compassionate flow.",
    ("South Node", "Libra"):       "The comfort zone is deep — a past steeped in diplomacy, partnership, and the art of accommodation. Moving forward means releasing the compulsion to balance every scale and learning that independence is not selfishness.",
    ("South Node", "Scorpio"):     "A past rich with intensity, transformation, and the hidden depths of power and loss runs deep. Growth means releasing the need to excavate everything and allowing life to be uncomplicated and trusting.",
    ("South Node", "Sagittarius"): "A past of seeking the big picture — philosophy, travel, and ultimate truth — has left a comfortable certainty that can harden into dogma. The invitation is toward openness, nuance, and genuine curiosity over fixed belief.",
    ("South Node", "Capricorn"):   "Competence, ambition, and emotional self-sufficiency are deeply ingrained from the past. The invitation is to let go of the need to prove worth through achievement and allow genuine feeling and vulnerability to guide the way.",
    ("South Node", "Aquarius"):    "A cool, visionary detachment — a comfort in the group, the cause, and the principle over the personal — runs through the past. The invitation is to risk being singular, passionate, and fully present as an individual.",
    ("South Node", "Pisces"):      "A past steeped in spirituality, compassion, and the dissolution of boundaries has left a tendency toward vagueness, escapism, or self-sacrifice. The invitation is to bring sensitivity into practical, grounded, and discerning service.",
}


# ── Planet in House ───────────────────────────────────────────────────────────
# keyed (planet, house_number)

PLANET_IN_HOUSE: dict[tuple[str, int], str] = {

    # Sun
    ("Sun", 1):  "Identity is expressed outward naturally — you arrive in any room with immediate, undeniable presence. The self and the persona are closely aligned.",
    ("Sun", 2):  "The life force is channeled into building resources and establishing self-worth. Identity is closely tied to what you earn, own, and value.",
    ("Sun", 3):  "The self shines through thought and communication — you are at your best in conversation and exchange. Writing, teaching, or connecting ideas is a natural calling.",
    ("Sun", 4):  "Identity is rooted in the private world — family, home, and ancestry define the core. Public success often grows from a solid private foundation.",
    ("Sun", 5):  "The self expresses through creativity, play, and romance. Joy is not optional — it is how you come most fully alive.",
    ("Sun", 6):  "Purpose is found through service, craft, and the rhythm of daily work. Identity is forged in the unglamorous but essential routines of a life.",
    ("Sun", 7):  "The self is most fully expressed through partnership — you discover who you are in relation to others. Marriage and close alliances carry particular weight.",
    ("Sun", 8):  "Identity is shaped by transformation, intensity, and the confrontation with depth. Power, shared resources, and psychological complexity are defining themes.",
    ("Sun", 9):  "The self expands through travel, learning, and the quest for meaning. Philosophy, higher education, and foreign cultures genuinely light you up.",
    ("Sun", 10): "Identity is tied to career, public standing, and the mark you leave on the world. Ambition and the desire for lasting respect run deep.",
    ("Sun", 11): "The self finds purpose in community and collective vision. Friends, networks, and the larger social good are central to who you are.",
    ("Sun", 12): "Identity is quietly internalized — the self develops in solitude and spiritual work. Unseen contributions carry as much weight as public achievements.",

    # Moon
    ("Moon", 1):  "Emotions show on the face — your inner life is legible, and you project a naturally nurturing or moody quality. The persona is emotionally responsive.",
    ("Moon", 2):  "Security needs revolve around material stability — feeling financially grounded is an emotional necessity. The relationship with money is tied directly to the inner world.",
    ("Moon", 3):  "The emotional life flows through words, curiosity, and the local environment. Siblings and nearby relationships carry significant emotional weight.",
    ("Moon", 4):  "The home is the emotional center — you need a sanctuary you can return to. Family dynamics run deep and shape emotional patterns for life.",
    ("Moon", 5):  "The emotional world is playful, romantic, and creatively alive. Children, art, and love affairs stir the deepest feelings.",
    ("Moon", 6):  "Emotions are processed through work and daily routine. Health and the body reflect the inner emotional state directly and quickly.",
    ("Moon", 7):  "Emotional security is found in partnership — you need a close other to feel whole. Relationships carry tremendous weight and must be chosen carefully.",
    ("Moon", 8):  "Feelings run to the depths and rarely stay on the surface. Intimacy, shared resources, and hidden emotional currents define the inner life.",
    ("Moon", 9):  "Emotional nourishment comes through exploration — of places, ideas, and belief systems. Wandering satisfies something deep and genuine inside you.",
    ("Moon", 10): "Emotions find expression in public life and career. The mother or a maternal figure may have strongly influenced your ambitions and public persona.",
    ("Moon", 11): "Emotional security comes from belonging to a tribe or cause. Friends feel like family, and group dynamics carry more emotional weight than you might expect.",
    ("Moon", 12): "Feelings are often private, hidden, or processed in solitude. Emotional strength is quiet and deep, though sometimes invisible even to yourself.",

    # Mercury
    ("Mercury", 1):  "The mind and tongue are front and center — first impressions are formed through how you think and speak. Communication is the primary tool of self-presentation.",
    ("Mercury", 2):  "The mind is oriented toward practical value — you think in terms of what things are worth and how ideas can be put to material use. Voice may be a financial asset.",
    ("Mercury", 3):  "A natural communicator and intellectual — the mind is at home in conversation, writing, and daily exchange. This placement amplifies the house's native energy.",
    ("Mercury", 4):  "Thinking is rooted in family history, memory, and private reflection. The mind works well at home and often returns to personal or ancestral themes.",
    ("Mercury", 5):  "Thoughts are playful, creative, and romantically inflected. Children, games, and artistic expression engage the intellect with genuine delight.",
    ("Mercury", 6):  "The mind excels at analysis, organization, and practical problem-solving. Health and work benefit from an especially analytical and methodical approach.",
    ("Mercury", 7):  "The mind works best in partnership — you think more clearly when bouncing ideas off others. Contracts, negotiation, and dialogue are where mental gifts shine.",
    ("Mercury", 8):  "The intellect probes the hidden, the taboo, and the psychologically complex. Research, investigation, and transformative inquiry are native strengths.",
    ("Mercury", 9):  "The mind reaches toward the big picture — philosophy, foreign languages, and the search for meaning engage the intellect most fully.",
    ("Mercury", 10): "The mind is employed in service of career and reputation. Public speaking, writing, or any communication-based profession supports your life purpose.",
    ("Mercury", 11): "Ideas flourish in community — you think better in groups and have a gift for communicating visions and ideals to the collective.",
    ("Mercury", 12): "The mind works in private, through dreams, or in the margins. Intuition and hidden knowledge often inform conscious thought more than logic does.",

    # Venus
    ("Venus", 1):  "Beauty and charm are expressed through the physical self — you present naturally attractive, socially graceful energy. Love and aesthetic pleasure come easily.",
    ("Venus", 2):  "Love and money are intertwined — the more secure you feel financially, the more you can open your heart. You attract material abundance through Venusian gifts.",
    ("Venus", 3):  "Affection is expressed through words — you love to talk, to write, and to communicate beautifully. The local environment and sibling relationships carry warmth.",
    ("Venus", 4):  "The home is a space of beauty and love — you invest in making your sanctuary welcoming and aesthetically pleasing. Family relationships are a deep source of affection.",
    ("Venus", 5):  "Love and creativity feed each other here — romance, art, children, and pleasure are all lit up by Venus. This is one of the most playfully romantic placements.",
    ("Venus", 6):  "Affection is shown through service and practical care. Beauty in the workspace and loving attention to daily routines support both wellbeing and connection.",
    ("Venus", 7):  "Partnership is the primary arena for love — you thrive in committed relationship and attract significant others through charm and genuine fairness. Venus is at home here.",
    ("Venus", 8):  "Love runs deep and transformative — relationships are intense and marked by profound emotional intimacy. Shared finances and power dynamics must be navigated with care.",
    ("Venus", 9):  "Love is expansive and philosophical — you are attracted to those from different cultures or worldviews. Romance and travel often intersect in meaningful ways.",
    ("Venus", 10): "Beauty and social grace support the career. You may attract success through charm, artistry, or a public persona that people find genuinely pleasing.",
    ("Venus", 11): "Friendships are beautiful and important — you attract warm, aesthetically aligned companions. Love often begins as friendship before deepening.",
    ("Venus", 12): "Love is private, secret, or tied to spiritual longing. You may love quietly from a distance or seek connection in solitude and contemplation.",

    # Mars
    ("Mars", 1):  "Drive and energy are expressed directly through the physical body — you act with force and urgency, and others notice immediately. Assertion comes naturally.",
    ("Mars", 2):  "Energy is directed toward acquiring resources and securing material foundations. You fight for what you value and will not easily give it up.",
    ("Mars", 3):  "Drive is channeled into communication, debate, and the exchange of ideas. The mind is competitive, quick-tongued, and never far from a good argument.",
    ("Mars", 4):  "Energy and conflict can run through the home — either tremendous drive to build a domestic life or friction within it. The private world is rarely at rest.",
    ("Mars", 5):  "Drive is channeled into creative output, romance, and play. You compete in love and pour genuine energy into what you create and enjoy.",
    ("Mars", 6):  "Hard work is a point of pride — you push in the daily routine and thrive when there is a clear goal to pursue at work. Health responds strongly to physical activity.",
    ("Mars", 7):  "Partnerships may be marked by conflict, competition, or the attraction of assertive others. You bring energy to relationships and tend to attract forceful partners.",
    ("Mars", 8):  "Drive is directed toward transformation, power, and the hidden depths. Sexuality, shared finances, and the investigation of taboo are energized areas.",
    ("Mars", 9):  "Energy flows toward exploration, belief, and the pursuit of meaning. You may fight for your philosophy or express drive through bold adventure.",
    ("Mars", 10): "Ambition runs hot — career is where you pour your energy and competitive drive. Public life is marked by initiative and the will to lead.",
    ("Mars", 11): "Drive is channeled into group efforts and collective causes. You fight for the ideals of your community and can be a forceful presence in networks.",
    ("Mars", 12): "Energy and desire operate beneath the surface — drive may be hidden, unconscious, or expressed through solitary effort. Spiritual warrior energy lives here.",

    # Jupiter
    ("Jupiter", 1):  "Good fortune flows through the self — you project natural optimism and largeness of spirit. Others experience you as lucky, and often you genuinely are.",
    ("Jupiter", 2):  "Abundance grows through material investment and the development of your gifts. Financial fortune is possible when generosity and self-worth align.",
    ("Jupiter", 3):  "Learning, communication, and local connections multiply your opportunities. Teaching and writing are reliable paths of expansion.",
    ("Jupiter", 4):  "Home life is abundant and expansive — you may have a large home, a generous family, or simply a deep sense of inner security that supports everything above it.",
    ("Jupiter", 5):  "Joy, creativity, and romance are magnified. Luck arrives through children, artistic expression, and the genuine willingness to play.",
    ("Jupiter", 6):  "Growth comes through mastery of work and service. Health tends to be robust, and the daily routine can become a path to real abundance.",
    ("Jupiter", 7):  "Partnership brings expansion — you attract generous, growth-oriented partners. Committed relationships open doors that would otherwise stay closed.",
    ("Jupiter", 8):  "Luck arrives through shared resources, transformation, and the deep end of life. Inheritances, financial partnerships, and psychological breakthroughs all carry real potential.",
    ("Jupiter", 9):  "Jupiter in its natural house — expansion flows through travel, philosophy, and higher learning. The world opens up with every horizon you pursue.",
    ("Jupiter", 10): "Career is blessed and expansive. Public recognition, a prominent platform, and the ability to achieve meaningful success are all strongly supported.",
    ("Jupiter", 11): "Friends and networks are sources of opportunity and growth. Collective visions flourish, and you may benefit significantly from the people you align yourself with.",
    ("Jupiter", 12): "Hidden luck supports you in ways you may not always recognize. Spiritual practice and solitary retreat are where your deepest expansion happens.",

    # Saturn
    ("Saturn", 1):  "The self-image carries a weight of responsibility and tends toward seriousness. Authority and maturity come early, along with lessons about the body and the persona.",
    ("Saturn", 2):  "Material security is earned slowly and with effort — this placement rarely delivers wealth easily. The lesson is building self-worth independently of what you own.",
    ("Saturn", 3):  "Communication may feel effortful or inhibited until discipline turns it into a real skill. The lesson is learning to speak with precision and earned authority.",
    ("Saturn", 4):  "Home life carries weight — family expectations or emotional restrictions may have shaped the foundation. Building a genuine sanctuary becomes a defining achievement over time.",
    ("Saturn", 5):  "Creative expression and play may feel constrained — the inner child carries a burden of seriousness. The lesson is learning to enjoy life without guilt or constant self-judgment.",
    ("Saturn", 6):  "Work ethic is formidable, but overwork and health can become the challenge. The lesson is building sustainable routines that serve rather than deplete.",
    ("Saturn", 7):  "Partnership carries responsibility and comes with lessons — relationships may take longer to establish or require consistent effort. Once committed, loyalty is enduring.",
    ("Saturn", 8):  "Power, shared resources, and vulnerability are domains of hard-won learning. Transformation is slow and sometimes painful here, but deeply lasting.",
    ("Saturn", 9):  "Beliefs and philosophies are tested against reality — dogma is eventually stripped away in favor of hard-won wisdom. Long journeys face obstacles but teach much.",
    ("Saturn", 10): "Career is a central challenge and eventual achievement — recognition comes through years of sustained effort. The calling is to build something of lasting significance.",
    ("Saturn", 11): "Social belonging may feel effortful or slow to develop. The lesson is earning genuine community through authenticity rather than performance.",
    ("Saturn", 12): "Hidden fears and unconscious patterns carry real weight. Spiritual discipline and solitude are where the real work happens — the shadow, once faced, becomes quiet strength.",

    # Uranus
    ("Uranus", 1):  "The self is unconventional, electric, and hard to categorize. First impressions land as surprising, original, or slightly unpredictable.",
    ("Uranus", 2):  "Financial life follows an erratic pattern — windfalls and reversals both. The lesson is building security in ways that do not depend on a linear income.",
    ("Uranus", 3):  "The mind operates on its own frequency — thinking is innovative and prone to sudden insight. Sibling relationships and local connections may be unusual.",
    ("Uranus", 4):  "Home life is disrupted or unconventional — sudden moves or unusual living arrangements. Freedom is needed even in domestic life.",
    ("Uranus", 5):  "Creative expression is boldly original, even provocative. Children may be unusual, romance tends to be unorthodox, and play leans toward the experimental.",
    ("Uranus", 6):  "Work and health routines need flexibility to function — rigid regimes tend to break down. Innovation in the workplace is where you genuinely thrive.",
    ("Uranus", 7):  "Partnership tends toward the unusual — you attract unconventional others and may resist traditional relationship structures. Freedom within commitment is the key.",
    ("Uranus", 8):  "Transformation arrives suddenly and completely. Shared finances and psychological breakthroughs can be destabilizing but ultimately liberating.",
    ("Uranus", 9):  "Your philosophy is original and ever-evolving. You resist inherited belief systems and prefer to construct your own truth through direct experience.",
    ("Uranus", 10): "The career path is unconventional, often reinvented multiple times. You are drawn to innovation and may make your mark in technology, reform, or disruption.",
    ("Uranus", 11): "Friendship groups are eclectic and forward-thinking — Uranus's natural domain. You work for collective liberation and attract genius or eccentric companions.",
    ("Uranus", 12): "Revolution happens in private — unusual insights emerge from solitude and dreams. Hidden rebellions quietly reshape the inner landscape.",

    # Neptune
    ("Neptune", 1):  "The physical self is hard to pin down — ethereal, sensitive, and chameleon-like. You absorb the atmosphere around you and project a quality of mystery.",
    ("Neptune", 2):  "The relationship with money and material security is subject to illusion or dissolution. The lesson is grounding values in something real and durable.",
    ("Neptune", 3):  "Communication can be poetic, indirect, or at times confused — the mind works through imagery and impression. Listening deeply is as important as speaking.",
    ("Neptune", 4):  "The home or family carries a mystical, sorrowful, or idealized quality. The private self is permeable and absorbs emotional atmospheres easily.",
    ("Neptune", 5):  "Creative gifts are significant and spiritually inflected. Romance can be idealistic or prone to confusion — distinguishing projection from reality is the key lesson.",
    ("Neptune", 6):  "Work and health are sensitive areas prone to idealization or confusion. The call is to serve from genuine compassion without losing yourself in the process.",
    ("Neptune", 7):  "Relationships are prone to idealization — seeing partners as they could be rather than as they are. Spiritual partnership or healing through relationship is a recurring theme.",
    ("Neptune", 8):  "The hidden realms — death, sexuality, shared resources — carry a mystical or dissolving quality. Dreams and psychic impressions may carry real information.",
    ("Neptune", 9):  "Philosophy and spirituality are primary concerns, but the line between inspiration and illusion needs constant tending. Long journeys may be as much inner as outer.",
    ("Neptune", 10): "The career has a spiritual, artistic, or service-oriented quality. Public life may be subject to illusion from others or from oneself.",
    ("Neptune", 11): "The social ideal is beautiful but can be elusive — you dream of community and collective transcendence. Distinguishing genuine connection from projection is ongoing work.",
    ("Neptune", 12): "Neptune in its natural house — deep spiritual sensitivity and the capacity for genuine dissolution of ego boundaries. Solitude and contemplation are where you touch the infinite.",

    # Pluto
    ("Pluto", 1):  "The self radiates intensity, magnetism, and transformative power. Others sense your depth even before you speak — nothing about you is superficial.",
    ("Pluto", 2):  "Resources and self-worth undergo radical transformation. Power may concentrate around financial control, or security may be periodically stripped away and rebuilt.",
    ("Pluto", 3):  "Communication carries intensity — words are used to probe, persuade, or dismantle. The mind undergoes periodic rebuilding as old certainties are replaced.",
    ("Pluto", 4):  "The foundations of home and family carry tremendous transformative weight. Deep ancestral patterns may be dismantled and reconstructed across a lifetime.",
    ("Pluto", 5):  "Creative expression is powerful, obsessive, and potentially transformative. Relationships with children or lovers involve profound psychological intensity.",
    ("Pluto", 6):  "Daily life and work are zones of deep transformation. Health challenges, if they arise, tend to be intense and ultimately regenerative.",
    ("Pluto", 7):  "Partnership is where transformation happens — relationships bring power struggles, psychological depth, and eventual rebuilding. Others serve as mirrors of the shadow.",
    ("Pluto", 8):  "Pluto in its natural house — intensity, transformation, and the confrontation with death and power are defining themes. Nothing hidden stays hidden for long.",
    ("Pluto", 9):  "The search for meaning is a relentless transformative drive. Beliefs that once organized life are periodically destroyed and rebuilt on deeper foundations.",
    ("Pluto", 10): "Career and public life are marked by tremendous power, ambition, or dramatic rises and falls. The relationship with authority is rarely simple or static.",
    ("Pluto", 11): "Social change is a driving mission — you operate as a catalyst for collective transformation. Friendships carry intensity and are never truly casual.",
    ("Pluto", 12): "The hidden self is the most powerful self — deep unconscious forces shape everything above the surface. Solitary inner work, over time, transforms the entire chart.",
}


# ── Natal Aspects ─────────────────────────────────────────────────────────────
# keyed (*sorted([p1, p2]), aspect)
# Covers planet-planet AND planet-angle pairs.

NATAL_ASPECT: dict[tuple[str, str, str], str] = {

    # ── Moon–Sun ────────────────────────────────────────────────────────────────
    ("Moon", "Sun", "conjunction"):  "The heart and the identity speak in the same voice — emotion and purpose are unified. You feel most yourself when you are moving toward what matters.",
    ("Moon", "Sun", "sextile"):      "Feelings and goals align with natural ease, making you both emotionally resilient and purposeful. Creative projects thrive when heart and mind agree.",
    ("Moon", "Sun", "square"):       "Inner conflict between what you feel and what you want to become creates productive tension. The emotional life and the ego push against each other until both grow.",
    ("Moon", "Sun", "trine"):        "Emotional and creative forces flow together in harmony. You express your authentic self with relative ease and natural confidence.",
    ("Moon", "Sun", "opposition"):   "The head and the heart occupy opposite poles — desire and feeling may pull in different directions. Integrating these two forces is a lifetime's art.",

    # ── Mercury–Sun ─────────────────────────────────────────────────────────────
    ("Mercury", "Sun", "conjunction"): "Mind and identity are inseparable — you think, therefore you are. Communication is a primary mode of self-expression.",
    ("Mercury", "Sun", "sextile"):     "Thinking supports the life purpose, and ideas flow into action with ease. Writing, speaking, or teaching comes naturally.",
    ("Mercury", "Sun", "square"):      "Tension between how you think and who you are can generate restless mental energy. The challenge is letting ideas serve the self rather than dominate it.",
    ("Mercury", "Sun", "trine"):       "Thought and identity work in seamless partnership. Your mind reflects who you are, and you express yourself clearly and with conviction.",
    ("Mercury", "Sun", "opposition"):  "The mind and the will see things from different angles, creating productive inner debate. Learning to speak your truth without over-thinking it is the key.",

    # ── Sun–Venus ───────────────────────────────────────────────────────────────
    ("Sun", "Venus", "conjunction"): "Identity and love are intertwined — you need to create and relate to feel fully alive. Warmth, charm, and aesthetic sensibility are core to who you are.",
    ("Sun", "Venus", "sextile"):     "Creative self-expression and the capacity for love support each other with graceful ease. Social life and artistic pursuits naturally advance your sense of self.",
    ("Sun", "Venus", "square"):      "There can be tension between what you want for yourself and what you want in love. Learning to honor both without sacrificing either is an ongoing practice.",
    ("Sun", "Venus", "trine"):       "Self-expression and love flow together harmoniously. You radiate a natural attractiveness and find it easy to both enjoy and share beauty.",
    ("Sun", "Venus", "opposition"):  "What you desire for yourself and what you seek in relationship may pull in different directions. The lesson is learning to be an individual within the context of partnership.",

    # ── Mars–Sun ────────────────────────────────────────────────────────────────
    ("Mars", "Sun", "conjunction"): "Drive and identity are fused — you act from a unified center of will and purpose. Energy can be enormous, but overreach is a risk.",
    ("Mars", "Sun", "sextile"):     "Action and self-expression support each other — you get things done without burning yourself out. Confidence and drive are well integrated.",
    ("Mars", "Sun", "square"):      "Ego and drive are in productive conflict — frustration fuels the engine of achievement. Learning to direct this fire constructively is the central challenge.",
    ("Mars", "Sun", "trine"):       "Will and identity work in natural alignment. You pursue your goals with confidence and rarely waste energy fighting yourself.",
    ("Mars", "Sun", "opposition"):  "Drive and identity can pull in opposing directions — the self you project and the self that acts may feel like different people. The work is integrating assertion with authenticity.",

    # ── Jupiter–Sun ─────────────────────────────────────────────────────────────
    ("Jupiter", "Sun", "conjunction"): "Expansive optimism and a generous sense of self make you naturally magnetic. Life tends to offer more than its share of opportunities.",
    ("Jupiter", "Sun", "sextile"):     "Growth comes naturally when you pursue what you genuinely love. Luck and identity align — being yourself opens doors.",
    ("Jupiter", "Sun", "square"):      "Ambition can outpace capacity, and the desire to be more can lead to overextension. The lesson is learning when enough is actually enough.",
    ("Jupiter", "Sun", "trine"):       "Life flows with a sense of natural abundance and possibility. Your generosity and confidence tend to be self-fulfilling.",
    ("Jupiter", "Sun", "opposition"):  "Expansion and the sense of self can pull against each other — too much outward growth can dilute identity. Finding the center amid the largeness is the work.",

    # ── Saturn–Sun ──────────────────────────────────────────────────────────────
    ("Saturn", "Sun", "conjunction"): "Identity is shaped by discipline, responsibility, and a serious sense of purpose. Recognition comes slowly but is built on solid foundations.",
    ("Saturn", "Sun", "sextile"):     "Structure and purpose work together productively — discipline serves rather than limits the self. Achievements tend to be durable and well-earned.",
    ("Saturn", "Sun", "square"):      "The self is tested by limitation, responsibility, or a critical inner voice. The friction between who you are and what is expected builds real character over time.",
    ("Saturn", "Sun", "trine"):       "Discipline and authenticity reinforce each other. You build lasting things without having to sacrifice who you are to do it.",
    ("Saturn", "Sun", "opposition"):  "Authority, limitation, or external demands can feel like they stand against the self. The work is learning to honor both ambition and the constraints that shape it.",

    # ── Sun–Uranus ──────────────────────────────────────────────────────────────
    ("Sun", "Uranus", "conjunction"): "Identity is inseparable from originality — you were born to disrupt and innovate. Conformity feels like a kind of death.",
    ("Sun", "Uranus", "sextile"):     "Creative originality enhances rather than endangers the self. You bring fresh thinking to your goals with ease.",
    ("Sun", "Uranus", "square"):      "The desire to be free conflicts with the need for stability or recognition. Breakthroughs come through, but rarely on anyone else's schedule.",
    ("Sun", "Uranus", "trine"):       "Individuality and innovation flow naturally through the identity. You are comfortably ahead of your time without needing to fight for it.",
    ("Sun", "Uranus", "opposition"):  "The self and the force of disruption stand in opposition — freedom may feel at odds with who others expect you to be. Integrating both is the ongoing creative challenge.",

    # ── Neptune–Sun ─────────────────────────────────────────────────────────────
    ("Neptune", "Sun", "conjunction"): "Identity is deeply spiritual and somewhat permeable — the self dissolves easily into ideals, art, or other people. Vision and empathy are native gifts.",
    ("Neptune", "Sun", "sextile"):     "Imagination and spiritual sensitivity enhance the life purpose. Creative and intuitive gifts flow smoothly into self-expression.",
    ("Neptune", "Sun", "square"):      "The self can be undermined by illusion, escapism, or the difficulty of knowing where you end and others begin. Clarity of identity must be actively cultivated.",
    ("Neptune", "Sun", "trine"):       "Spiritual depth and creative imagination are integrated seamlessly into who you are. Empathy and vision feel like natural extensions of the self.",
    ("Neptune", "Sun", "opposition"):  "The self and the ideal can occupy very different territories — who you are may clash with who you dream of being. Learning to live in the real without losing the vision is the work.",

    # ── Pluto–Sun ───────────────────────────────────────────────────────────────
    ("Pluto", "Sun", "conjunction"): "Identity carries enormous transformative power — you are not the same person you were a decade ago, and you will not be the same a decade from now. The self is an ongoing process of deep regeneration.",
    ("Pluto", "Sun", "sextile"):     "Personal power and the will to transform are accessible and productively channeled. You evolve without being destroyed by the process.",
    ("Pluto", "Sun", "square"):      "Power struggles, crises, or forces beyond your control periodically reshape the self from the ground up. The phoenix rising is a living metaphor.",
    ("Pluto", "Sun", "trine"):       "Transformative power flows through the identity with relative ease. You handle deep change better than most, and others can feel your intensity even when you are still.",
    ("Pluto", "Sun", "opposition"):  "External power or the force of transformation stands in opposition to the self. Learning to wield power without being controlled by it is the lifetime challenge.",

    # ── Mercury–Moon ────────────────────────────────────────────────────────────
    ("Mercury", "Moon", "conjunction"): "Thinking and feeling operate together — emotions become thoughts and thoughts become feelings in one continuous flow. You need to talk through your inner life.",
    ("Mercury", "Moon", "sextile"):     "Mind and heart cooperate naturally — you can articulate emotions clearly and think empathically. Counseling, writing, or teaching comes with ease.",
    ("Mercury", "Moon", "square"):      "The rational mind and the emotional life are often at odds — analysis can block feeling, and feeling can cloud analysis. The work is learning to use both without letting either dominate.",
    ("Mercury", "Moon", "trine"):       "Emotional intelligence and verbal articulation flow together harmoniously. You can express what you feel clearly and receive others' feelings with genuine understanding.",
    ("Mercury", "Moon", "opposition"):  "Thought and feeling occupy different poles — what the mind concludes and what the heart knows may contradict each other. Integration brings a kind of emotional wisdom that logic alone cannot reach.",

    # ── Moon–Venus ──────────────────────────────────────────────────────────────
    ("Moon", "Venus", "conjunction"): "Emotional needs and the capacity for love are deeply aligned — you feel most yourself when giving and receiving affection. Warmth and beauty are fundamental needs.",
    ("Moon", "Venus", "sextile"):     "The heart and the love nature cooperate easily — relationships feel nourishing and emotionally satisfying. Aesthetic pleasure comes naturally.",
    ("Moon", "Venus", "square"):      "Emotional security needs and desires in love can pull against each other. The tension between needing to be cared for and needing to be desired is real and worth attending to.",
    ("Moon", "Venus", "trine"):       "Feeling and love flow together in natural harmony. Relationships tend to feel emotionally supportive, and beauty nourishes the soul.",
    ("Moon", "Venus", "opposition"):  "The need to be nurtured and the desire to attract love can feel like they are asking for different things. The work is learning to receive care and give beauty without losing either.",

    # ── Mars–Moon ───────────────────────────────────────────────────────────────
    ("Mars", "Moon", "conjunction"): "Feelings and actions are fused — emotions drive the will directly, sometimes before the mind has a say. Passion and protectiveness are formidable forces.",
    ("Mars", "Moon", "sextile"):     "Emotional energy flows into purposeful action with relative ease. You act on what you feel and feel validated by what you accomplish.",
    ("Mars", "Moon", "square"):      "Emotional reactivity and frustration can generate impulsive or defensive behavior. The charge between feeling and action is productive when channeled consciously.",
    ("Mars", "Moon", "trine"):       "Drive and emotional depth work together in productive harmony. You act with feeling and feel the power of what you do.",
    ("Mars", "Moon", "opposition"):  "The will to act and the need to feel safe stand in opposition — aggression or assertion can feel threatening to the inner world. Learning to protect without attacking is the work.",

    # ── Jupiter–Moon ────────────────────────────────────────────────────────────
    ("Jupiter", "Moon", "conjunction"): "Emotional life is expansive, generous, and tends toward the optimistic. You have a large capacity for feeling and an equally large desire to share it.",
    ("Jupiter", "Moon", "sextile"):     "Emotional generosity and a sense of abundance flow naturally into daily life. Relationships benefit from your natural warmth and willingness to give.",
    ("Jupiter", "Moon", "square"):      "Emotional excess and overreach can be the shadow — too much feeling, too much caretaking, too much sensitivity to everything. The lesson is proportionality.",
    ("Jupiter", "Moon", "trine"):       "Emotional abundance and a sense of inner security flow freely. You tend to approach feeling states with generosity and trust.",
    ("Jupiter", "Moon", "opposition"):  "Expansive desire and the need for emotional security can pull in different directions. The work is learning to feel widely without losing the ground beneath you.",

    # ── Moon–Saturn ─────────────────────────────────────────────────────────────
    ("Moon", "Saturn", "conjunction"): "Emotional life is shaped by restraint, responsibility, or early experiences of limitation. Feelings run deep but are carefully controlled, and security is earned not given.",
    ("Moon", "Saturn", "sextile"):     "Emotional discipline and the capacity for sustained care work together productively. You can hold difficult feelings without being overwhelmed by them.",
    ("Moon", "Saturn", "square"):      "There is friction between the need to feel and the inner critic that says feeling is unsafe. Learning to allow the emotional life without policing it is the central work.",
    ("Moon", "Saturn", "trine"):       "Emotional maturity and the capacity for sustained commitment flow together with relative ease. You can be relied upon and tend to take the inner life seriously.",
    ("Moon", "Saturn", "opposition"):  "The desire for emotional warmth and the pull toward control or containment stand in opposition. The work is learning to be both responsible and genuinely open-hearted.",

    # ── Moon–Uranus ─────────────────────────────────────────────────────────────
    ("Moon", "Uranus", "conjunction"): "Emotional life is electric, unpredictable, and prone to sudden shifts in feeling. The inner world is innovative and restless, craving freedom even from itself.",
    ("Moon", "Uranus", "sextile"):     "Emotional originality and the capacity for independence work together productively. You bring fresh perspective to the inner life and to your closest relationships.",
    ("Moon", "Uranus", "square"):      "Emotional security and the need for freedom are in constant tension. Disruption in domestic life or the inner world often precedes liberation.",
    ("Moon", "Uranus", "trine"):       "Emotional independence and genuine originality flow naturally through the inner life. You can feel deeply without being bound by convention.",
    ("Moon", "Uranus", "opposition"):  "The need for emotional security and the pull toward freedom stand in direct opposition. The work is learning to belong without giving up the self.",

    # ── Moon–Neptune ────────────────────────────────────────────────────────────
    ("Moon", "Neptune", "conjunction"): "The emotional world is fluid, empathic, and highly permeable — you feel the feelings of others as readily as your own. Psychic sensitivity and spiritual attunement are real gifts here.",
    ("Moon", "Neptune", "sextile"):     "Emotional sensitivity and imaginative depth support each other. You have a gift for compassionate understanding and creative emotional expression.",
    ("Moon", "Neptune", "square"):      "The boundary between your feelings and the feelings of others is thin to the point of confusion. The lesson is learning to feel without losing yourself in the feeling.",
    ("Moon", "Neptune", "trine"):       "Spiritual sensitivity and emotional depth flow together in natural harmony. You feel the invisible dimensions of any situation and communicate them with grace.",
    ("Moon", "Neptune", "opposition"):  "The emotional self and the ideal of dissolution stand in opposition — the inner life wants both security and boundlessness. Learning to hold both without losing form is the work.",

    # ── Moon–Pluto ───────────────────────────────────────────────────────────────
    ("Moon", "Pluto", "conjunction"): "The emotional world operates at the deepest level of the psyche — feelings are intense, compulsive, and transformative. Power dynamics in relationships with women or caregivers are significant.",
    ("Moon", "Pluto", "sextile"):     "Emotional depth and the capacity for transformation work together productively. You navigate the depths of feeling without being consumed by them.",
    ("Moon", "Pluto", "square"):      "Intense emotional experiences — loss, power struggles, or deep psychological upheaval — are part of the landscape. The shadow, once met, becomes genuine power.",
    ("Moon", "Pluto", "trine"):       "Emotional intensity and transformative depth flow together with surprising ease. You can inhabit the full spectrum of human feeling and emerge regenerated.",
    ("Moon", "Pluto", "opposition"):  "The inner life and the force of deep transformation stand in opposition — what you feel most deeply may also be what most threatens your sense of security. Integration brings profound emotional authority.",

    # ── Mercury–Venus ────────────────────────────────────────────────────────────
    ("Mercury", "Venus", "conjunction"): "Mind and love are intertwined — you fall in love with ideas and articulate beauty instinctively. Writing, speaking, and aesthetic thinking are native gifts.",
    ("Mercury", "Venus", "sextile"):     "Thought and love cooperate with natural grace — you communicate affection clearly and appreciate beauty in ideas. Social intelligence flows easily.",
    ("Mercury", "Venus", "square"):      "What you think and what you want from love can be at odds — the mind may rationalize or the heart may cloud judgment. Learning to honor both is the practice.",
    ("Mercury", "Venus", "trine"):       "Thinking and the love nature work together harmoniously. You express affection eloquently and find genuine pleasure in intellectual beauty.",
    ("Mercury", "Venus", "opposition"):  "The analytical mind and the desire nature occupy different territories — cool logic and warm feeling may seem to contradict each other. The synthesis brings sophisticated understanding.",

    # ── Mars–Mercury ─────────────────────────────────────────────────────────────
    ("Mars", "Mercury", "conjunction"): "Thought is direct, assertive, and ready for debate — the mind moves like a blade. Communication is forceful and rarely uncertain.",
    ("Mars", "Mercury", "sextile"):     "The assertive mind and the capacity for decisive action cooperate productively. You think quickly and act on ideas without unnecessary delay.",
    ("Mars", "Mercury", "square"):      "The impulse to act conflicts with the need to think things through — words can be sharp or decisions rushed. Learning to pause between the thought and the action pays dividends.",
    ("Mars", "Mercury", "trine"):       "Drive and intellect work in natural alignment. You act on ideas swiftly and communicate with confidence and precision.",
    ("Mars", "Mercury", "opposition"):  "The will to act and the mind that thinks stand in opposition — you may simultaneously think too much and act too quickly. Finding the bridge between them is the ongoing challenge.",

    # ── Jupiter–Mercury ──────────────────────────────────────────────────────────
    ("Jupiter", "Mercury", "conjunction"): "The mind reaches broadly and optimistically — ideas are never small, and learning feels like breathing. Teaching, publishing, and any work with ideas and audiences is naturally supported.",
    ("Jupiter", "Mercury", "sextile"):     "Expansive thinking and the ability to communicate it cooperate with ease. Your mind opens doors through its breadth and enthusiasm.",
    ("Jupiter", "Mercury", "square"):      "Thinking big can tip into overconfidence or scattered focus — the mind wants everything at once. The lesson is learning to develop ideas to their full depth before moving to the next.",
    ("Jupiter", "Mercury", "trine"):       "The intellect and the spirit of expansion flow together in natural harmony. You think in large, generous strokes and communicate that scale with ease.",
    ("Jupiter", "Mercury", "opposition"):  "The broad philosophical view and the detailed analytical mind stand in opposition. The tension between the forest and the trees is productive when both are honored.",

    # ── Mercury–Saturn ───────────────────────────────────────────────────────────
    ("Mercury", "Saturn", "conjunction"): "The mind is disciplined, precise, and structured. Thinking is thorough, sometimes slow, but reliably builds toward genuine depth and authority.",
    ("Mercury", "Saturn", "sextile"):     "Mental discipline and the capacity for careful communication work together productively. You can explain complex things clearly and take the long view.",
    ("Mercury", "Saturn", "square"):      "A critical inner voice or external authority can make self-expression feel difficult or constrained. The lesson is developing genuine mental confidence through the work of sustained practice.",
    ("Mercury", "Saturn", "trine"):       "Disciplined thinking and authoritative communication flow naturally together. You build ideas carefully and speak with the weight of real knowledge.",
    ("Mercury", "Saturn", "opposition"):  "The free flow of thought and the demands of structure or authority stand in opposition. Learning to think rigorously without becoming imprisoned by your own standards is the work.",

    # ── Mercury–Uranus ───────────────────────────────────────────────────────────
    ("Mercury", "Uranus", "conjunction"): "The mind is brilliantly original, electric, and prone to sudden insight. You think in leaps that others often cannot follow — yet.",
    ("Mercury", "Uranus", "sextile"):     "Original thinking and the ability to communicate innovation cooperate with ease. You bring fresh ideas to the table and can articulate them accessibly.",
    ("Mercury", "Uranus", "square"):      "The innovative mind and the demands of conventional communication are in tension. Thinking can be ahead of its time or simply erratic — learning to ground the insight is the practice.",
    ("Mercury", "Uranus", "trine"):       "Originality and communication flow together in natural harmony. You think differently and can explain why that difference matters.",
    ("Mercury", "Uranus", "opposition"):  "Brilliant ideas and the practical need to be understood stand in opposition. The work is bridging the original inner frequency with language others can receive.",

    # ── Mercury–Neptune ──────────────────────────────────────────────────────────
    ("Mercury", "Neptune", "conjunction"): "The mind is imaginative, intuitive, and at home in the symbolic. Poetry, vision, and metaphor are as real as data — sometimes more so.",
    ("Mercury", "Neptune", "sextile"):     "Imagination and clear enough thinking work together productively. You communicate invisible things in ways others can grasp.",
    ("Mercury", "Neptune", "square"):      "Clarity of thought and the pull of the imaginal can undermine each other. The work is learning to give form to the vision without losing it in the process.",
    ("Mercury", "Neptune", "trine"):       "Intuitive and rational knowing flow together harmoniously. You communicate with a poetic quality that makes abstract ideas feel tangible.",
    ("Mercury", "Neptune", "opposition"):  "Clear analytical thinking and the dissolving influence of the imaginal stand in opposition. Grounding the vision in language without reducing it is the central creative challenge.",

    # ── Mercury–Pluto ────────────────────────────────────────────────────────────
    ("Mercury", "Pluto", "conjunction"): "The mind probes ruthlessly and never settles for a surface answer. Research, psychological insight, and the power of words to transform are native gifts.",
    ("Mercury", "Pluto", "sextile"):     "Penetrating insight and the ability to communicate it cooperate productively. You find the lever point of any situation and articulate it with precision.",
    ("Mercury", "Pluto", "square"):      "The obsessive mind and the desire for control through knowledge can create compulsive thinking patterns. The lesson is learning to hold power in thought without being consumed by it.",
    ("Mercury", "Pluto", "trine"):       "Depth of perception and the power of communication flow together naturally. Words carry weight and intention here — you can genuinely change minds.",
    ("Mercury", "Pluto", "opposition"):  "The probing mind and the forces of transformation it uncovers can stand in opposition to simpler comforts. Learning to live with what you know is part of the work.",

    # ── Mars–Venus ───────────────────────────────────────────────────────────────
    ("Mars", "Venus", "conjunction"): "Passion and love operate through the same channel — desire is intense, magnetic, and rarely subtle. The creative and romantic life burns bright.",
    ("Mars", "Venus", "sextile"):     "Drive and the love nature cooperate with natural ease — you pursue what you love with energy and grace. Creative partnerships tend to be productive.",
    ("Mars", "Venus", "square"):      "Desire and the capacity for tenderness can pull against each other — passion and receptivity are both present but not always in sync. The creative tension is real and fertile.",
    ("Mars", "Venus", "trine"):       "Desire and love flow together harmoniously. You can be both assertive and gentle in relationship, and creative energy flows with unusual ease.",
    ("Mars", "Venus", "opposition"):  "The desire to act and the desire to attract stand in opposition — what you want and how you go about getting it may clash. The integration brings magnetic presence.",

    # ── Jupiter–Venus ────────────────────────────────────────────────────────────
    ("Jupiter", "Venus", "conjunction"): "Love and luck are intertwined — generosity attracts abundance in both affection and resources. Social grace and a genuine pleasure in life are your calling cards.",
    ("Jupiter", "Venus", "sextile"):     "Expansion and the love nature cooperate easily — relationships bring growth, and generosity opens doors. You enjoy life and it tends to enjoy you back.",
    ("Jupiter", "Venus", "square"):      "The desire for more in love or luxury can lead to excess or unrealistic expectations. The lesson is learning to appreciate what is here without constantly reaching for what is bigger.",
    ("Jupiter", "Venus", "trine"):       "Love and abundance flow together in natural harmony. You attract what you value and value what you attract with unusual ease.",
    ("Jupiter", "Venus", "opposition"):  "Expansive desire and the capacity for genuine love can be at odds — wanting everything can dilute the depth of particular connection. Learning to commit is as important as staying open.",

    # ── Saturn–Venus ─────────────────────────────────────────────────────────────
    ("Saturn", "Venus", "conjunction"): "Love is serious, slow, and built for the long haul — warmth may be reserved but utterly dependable. The capacity for lasting commitment is genuine and hard-won.",
    ("Saturn", "Venus", "sextile"):     "Commitment and the capacity for love work together productively. You build relationships on real foundations and take beauty and loyalty seriously.",
    ("Saturn", "Venus", "square"):      "Emotional restriction and the desire for connection can be in tension — love may feel conditional or blocked. The lesson is learning to receive as well as to give carefully.",
    ("Saturn", "Venus", "trine"):       "Discipline and the love nature flow together with graceful solidity. Relationships are lasting and built on genuine respect.",
    ("Saturn", "Venus", "opposition"):  "The demand for structure and the desire for warmth and beauty can stand in opposition. Learning to be both responsible and affectionate without choosing is the work.",

    # ── Uranus–Venus ─────────────────────────────────────────────────────────────
    ("Uranus", "Venus", "conjunction"): "Love is electric, unconventional, and prone to sudden beginnings or endings. Attraction is to the unusual, and freedom is as necessary as affection.",
    ("Uranus", "Venus", "sextile"):     "Innovation and the love nature cooperate with relative ease. You bring originality to relationships and find beauty in the unexpected.",
    ("Uranus", "Venus", "square"):      "The need for freedom and the desire for closeness are in productive tension. Relationships that offer both space and genuine connection are the real target.",
    ("Uranus", "Venus", "trine"):       "Originality and the capacity for love flow together harmoniously. You can love freely without losing yourself, and relationships tend to expand your world.",
    ("Uranus", "Venus", "opposition"):  "The desire for independence and the desire for love stand in opposition. The work is discovering that genuine connection does not require giving up who you are.",

    # ── Neptune–Venus ────────────────────────────────────────────────────────────
    ("Neptune", "Venus", "conjunction"): "Love is idealized, spiritual, and prone to beautiful illusions. The capacity for transcendent beauty in art and relationship is genuine — and so is the risk of seeing only what you wish were there.",
    ("Neptune", "Venus", "sextile"):     "Spiritual sensitivity and the love nature cooperate with natural grace. Art, compassion, and imaginative connection come easily.",
    ("Neptune", "Venus", "square"):      "The ideal of perfect love can obscure the real person in front of you. The lesson is learning to love the actual without losing the capacity for the transcendent.",
    ("Neptune", "Venus", "trine"):       "Idealism and the capacity for genuine love flow together harmoniously. You can hold the vision of beauty without losing sight of reality.",
    ("Neptune", "Venus", "opposition"):  "The perfect love and the available love may stand in painful opposition. Learning to find the sacred within the ordinary is the central challenge.",

    # ── Pluto–Venus ──────────────────────────────────────────────────────────────
    ("Pluto", "Venus", "conjunction"): "Love is transformative, obsessive, and capable of remaking everything it touches. The capacity for depth in relationship is enormous — and so is the potential for power struggles.",
    ("Pluto", "Venus", "sextile"):     "Transformative depth and the love nature cooperate productively. You bring genuine intensity to relationship and find that depth attracts depth.",
    ("Pluto", "Venus", "square"):      "Power and love are entangled — relationships may involve control, jealousy, or the compulsive repetition of deep patterns. The shadow of love is where real transformation happens.",
    ("Pluto", "Venus", "trine"):       "Transformative power and the love nature flow together with unusual ease. You bring depth to what you love and receive transformation in return.",
    ("Pluto", "Venus", "opposition"):  "The desire for love and the force of transformation stand in opposition — relationships may feel fated, intense, or fraught with power. Learning to love without needing to possess is the work.",

    # ── Jupiter–Mars ─────────────────────────────────────────────────────────────
    ("Jupiter", "Mars", "conjunction"): "Drive and expansion operate as one — ambition is enormous, enthusiasm knows no ceiling, and the sheer scale of your energy can be both inspiring and overwhelming.",
    ("Jupiter", "Mars", "sextile"):     "Drive and optimism cooperate naturally — you pursue goals with both energy and vision. The scale of your ambition tends to match your capacity.",
    ("Jupiter", "Mars", "square"):      "The desire to expand and the desire to act are in tension — overreach, excess, and restless impatience are the shadows. The lesson is channeling immense energy into focused effort.",
    ("Jupiter", "Mars", "trine"):       "Drive and expansion flow together harmoniously. You pursue what you believe in with both force and wisdom, and your energy tends to multiply rather than waste.",
    ("Jupiter", "Mars", "opposition"):  "The will to act and the impulse to expand stand in opposition — reaching further can undermine what is already in motion. Learning to work in phases is a useful discipline.",

    # ── Mars–Saturn ──────────────────────────────────────────────────────────────
    ("Mars", "Saturn", "conjunction"): "Drive is disciplined and strategic — energy is held carefully before being released with precision. Patience under pressure is one of your genuine gifts.",
    ("Mars", "Saturn", "sextile"):     "Discipline and the ability to act cooperate with productive efficiency. You can work hard over long periods without burning out.",
    ("Mars", "Saturn", "square"):      "Drive and restriction are in direct tension — frustration, blocked action, or the feeling of working against invisible walls is real. The friction, held consciously, builds remarkable determination.",
    ("Mars", "Saturn", "trine"):       "Effort and discipline flow together in natural alignment. You work with consistent, sustainable force and build results that last.",
    ("Mars", "Saturn", "opposition"):  "The impulse to act and the demand for control or caution stand in opposition. Learning to move when the moment is right — neither too early nor too late — is the art.",

    # ── Mars–Uranus ──────────────────────────────────────────────────────────────
    ("Mars", "Uranus", "conjunction"): "Drive is explosive, innovative, and impossible to contain for long — action is sudden, electric, and often surprising even to yourself. The potential for both genius and recklessness is real.",
    ("Mars", "Uranus", "sextile"):     "Inventive energy and the capacity for bold action cooperate with ease. You act quickly on original ideas without being reckless about it.",
    ("Mars", "Uranus", "square"):      "Impulsive action and the disruptive force of innovation are in tension — explosions, accidents, or radical breaks with the plan. The lesson is learning to harness the voltage before switching it on.",
    ("Mars", "Uranus", "trine"):       "Drive and originality flow together in exciting alignment. You act with both speed and innovation, and the results tend to be genuinely surprising.",
    ("Mars", "Uranus", "opposition"):  "The will to act and the force of disruption stand in opposition — breaking free and getting things done may feel like opposite impulses. Learning to use the lightning without burning the house down is the practice.",

    # ── Mars–Neptune ─────────────────────────────────────────────────────────────
    ("Mars", "Neptune", "conjunction"): "Drive is spiritualized — you act from vision, imagination, or compassion as much as from personal ambition. Energy can be elusive when the cause is unclear but massive when inspired.",
    ("Mars", "Neptune", "sextile"):     "Inspired action and the power of imagination cooperate productively. You act from a sense of meaning and are most effective when you believe in what you are doing.",
    ("Mars", "Neptune", "square"):      "The will to act and the dissolving influence of the imaginal can undermine each other. Energy leaks, confused purpose, or acting on illusions rather than reality — the lesson is clarifying what you are actually after.",
    ("Mars", "Neptune", "trine"):       "Inspired drive and creative imagination flow together harmoniously. You pursue your vision with both energy and sensitivity.",
    ("Mars", "Neptune", "opposition"):  "Direct action and the pull of dissolution stand in opposition — the self that wants to do and the self that wants to dissolve may take turns. Learning to act with intention, even in the fog, is the work.",

    # ── Mars–Pluto ───────────────────────────────────────────────────────────────
    ("Mars", "Pluto", "conjunction"): "Will and transformation are fused into a single relentless force — nothing and no one stops you when you are fully committed. Power is enormous here; how it is used defines everything.",
    ("Mars", "Pluto", "sextile"):     "Drive and transformative power cooperate productively. You pursue your goals with depth and persistence, and the results tend to be lasting.",
    ("Mars", "Pluto", "square"):      "Power struggles, compulsive drive, or the confrontation with what cannot be controlled are defining experiences. The immense energy here is most useful when directed consciously rather than explosively.",
    ("Mars", "Pluto", "trine"):       "Will and transformative depth flow together in natural alignment. You pursue what you want with quiet intensity and rarely need to force the outcome.",
    ("Mars", "Pluto", "opposition"):  "The personal will and the force of deep transformation stand in opposition — external power or compulsive inner forces can feel like they own you. Claiming agency over your own depth is the lifetime work.",

    # ── Jupiter–Saturn ───────────────────────────────────────────────────────────
    ("Jupiter", "Saturn", "conjunction"): "Expansion and restriction operate from the same place — the desire to grow and the demand to be responsible are perpetually negotiating. This placement builds real wisdom when the tension is held.",
    ("Jupiter", "Saturn", "sextile"):     "Optimism and discipline cooperate naturally — you know when to push and when to hold. Plans tend to be both ambitious and realistic.",
    ("Jupiter", "Saturn", "square"):      "Growth and limitation are in constant productive friction — too much of one undermines the other. The lesson is finding the rhythm between building and restraining.",
    ("Jupiter", "Saturn", "trine"):       "Expansion and structure flow together in natural harmony. You build in sustainable arcs, knowing when to grow and when to consolidate.",
    ("Jupiter", "Saturn", "opposition"):  "The spirit of expansion and the demand for limitation stand in direct opposition — one foot on the gas, one on the brake. Finding the synthesis brings rare authority.",

    # ── Jupiter–Uranus ───────────────────────────────────────────────────────────
    ("Jupiter", "Uranus", "conjunction"): "A powerful desire for freedom and expansion that regularly produces brilliant, unexpected breakthroughs. The trajectory of your life tends to change suddenly and for the better.",
    ("Jupiter", "Uranus", "sextile"):     "The spirit of innovation and the desire for growth cooperate productively. You find unexpected paths to expansion and tend to land on your feet after each leap.",
    ("Jupiter", "Uranus", "square"):      "The drive for freedom and the desire for more can destabilize what has been built. Breakthrough and overreach sit close together here.",
    ("Jupiter", "Uranus", "trine"):       "Freedom and growth flow together harmoniously. Unexpected opportunities arrive regularly and you have the wisdom to recognize them.",
    ("Jupiter", "Uranus", "opposition"):  "Expansive optimism and the disruptive force of change stand in opposition. The work is learning to grow without blowing everything up in the process.",

    # ── Jupiter–Neptune ──────────────────────────────────────────────────────────
    ("Jupiter", "Neptune", "conjunction"): "Spiritual aspiration and the desire for expansion are fused — the drive for meaning, beauty, and transcendence is enormous. Idealism can be a genuine gift or a source of unrealistic expectation.",
    ("Jupiter", "Neptune", "sextile"):     "Spiritual growth and imaginative expansion cooperate naturally. You are drawn toward the larger meaning in any experience.",
    ("Jupiter", "Neptune", "square"):      "The impulse to expand collides with the dissolving influence of Neptune — grand ideals, boundless hope, or the temptation of escapism. Grounding the vision is the essential work.",
    ("Jupiter", "Neptune", "trine"):       "Spiritual aspiration and the desire for growth flow together in natural harmony. Faith tends to be rewarded and beauty tends to find you.",
    ("Jupiter", "Neptune", "opposition"):  "The drive to expand and the pull toward dissolution stand in opposition. Learning to grow toward something real rather than an ideal that keeps receding is the challenge.",

    # ── Jupiter–Pluto ────────────────────────────────────────────────────────────
    ("Jupiter", "Pluto", "conjunction"): "The drive for power and the desire for growth are fused into a single enormous force. Potential for extraordinary achievement — or extraordinary overreach.",
    ("Jupiter", "Pluto", "sextile"):     "Transformative power and the desire for expansion cooperate productively. You pursue growth with depth and tend to build on what you have cleared away.",
    ("Jupiter", "Pluto", "square"):      "The ambition for power and the force of transformation are in productive tension — growth often comes through destruction of what no longer serves. The lesson is not to confuse expansion with domination.",
    ("Jupiter", "Pluto", "trine"):       "Transformative depth and expansive ambition flow together harmoniously. You build on a deep foundation and tend to emerge from upheaval stronger than before.",
    ("Jupiter", "Pluto", "opposition"):  "The desire for expansion and the force of deep transformation stand in opposition. Learning to grow without needing to control every aspect of the process is the essential practice.",

    # ── Saturn–Uranus ────────────────────────────────────────────────────────────
    ("Saturn", "Uranus", "conjunction"): "Structure and revolution inhabit the same body — the desire to build and the desire to break free are in constant negotiation. This tension, when held, produces genuinely original and lasting work.",
    ("Saturn", "Uranus", "sextile"):     "Discipline and innovation cooperate with practical effect. You can break new ground without destroying the structure needed to support it.",
    ("Saturn", "Uranus", "square"):      "The demand for structure and the drive for freedom are in direct tension — stability and disruption take turns. The friction is real but productive when consciously engaged.",
    ("Saturn", "Uranus", "trine"):       "Structure and innovation flow together in natural alignment. You build new things without needing to demolish everything first.",
    ("Saturn", "Uranus", "opposition"):  "The need for order and the need for liberation stand in direct opposition — you may feel alternately controlled and out of control. Learning to hold both simultaneously is the lifetime discipline.",

    # ── Neptune–Saturn ───────────────────────────────────────────────────────────
    ("Neptune", "Saturn", "conjunction"): "The material and the mystical are in conversation — structure is applied to the invisible, and the ideal is held to real-world standards. Spiritual discipline or disillusionment are both possible outcomes.",
    ("Neptune", "Saturn", "sextile"):     "Discipline and spiritual sensitivity cooperate productively. You can give form to the imaginal and ground your vision in something buildable.",
    ("Neptune", "Saturn", "square"):      "The demand for structure and the dissolving influence of the imaginal are in tension — reality and illusion do not easily agree. The lesson is learning which is which.",
    ("Neptune", "Saturn", "trine"):       "Spiritual depth and structural discipline flow together harmoniously. You can build with a sense of the sacred and dream with a sense of the real.",
    ("Neptune", "Saturn", "opposition"):  "The pull toward the ideal and the demand of the actual stand in opposition. Learning to let the dream inform the structure without replacing it is the essential work.",

    # ── Pluto–Saturn ─────────────────────────────────────────────────────────────
    ("Pluto", "Saturn", "conjunction"): "The builder and the destroyer inhabit the same impulse — what is constructed can be dismantled with equal intensity. Power is the central theme, and it demands to be used wisely.",
    ("Pluto", "Saturn", "sextile"):     "Transformative depth and structural discipline cooperate productively. You rebuild on cleared ground and what you build tends to be durable.",
    ("Pluto", "Saturn", "square"):      "Power and structure are in intense friction — upheaval within systems, the collapse of old orders, or the compulsive rebuilding of what keeps failing. The shadow of authority is the subject.",
    ("Pluto", "Saturn", "trine"):       "Transformative power and the ability to build lasting structures flow together in natural alignment. You work with the long arc of history and tend to outlast obstacles.",
    ("Pluto", "Saturn", "opposition"):  "The force of transformation and the demand for structure stand in opposition — what is built may periodically be dismantled by forces beyond the plan. Learning to build with impermanence in mind is the work.",

    # ── Neptune–Uranus ───────────────────────────────────────────────────────────
    ("Neptune", "Uranus", "conjunction"): "A generational signature — the mystical and the revolutionary are fused into a single wave of collective transformation. This generation dissolves old orders and dreams new ones into being.",
    ("Neptune", "Uranus", "sextile"):     "Spiritual aspiration and innovative thinking cooperate in the collective. A generation finds that revolution and vision are natural allies.",
    ("Neptune", "Uranus", "square"):      "The dissolving force of the imaginal and the disruptive force of revolution are in tension — idealism and liberation do not agree on direction. The friction remakes the collective.",
    ("Neptune", "Uranus", "trine"):       "Spiritual depth and revolutionary impulse flow together harmoniously in the collective. A generation transforms with both compassion and originality.",
    ("Neptune", "Uranus", "opposition"):  "The impulse to dissolve and the impulse to disrupt stand in opposition — the collective is pulled between surrender and rebellion. The synthesis carries enormous cultural power.",

    # ── Pluto–Uranus ─────────────────────────────────────────────────────────────
    ("Pluto", "Uranus", "conjunction"): "A generational signature of explosive, irreversible collective transformation — the old order is dismantled suddenly and completely. What was cannot be restored.",
    ("Pluto", "Uranus", "sextile"):     "Revolutionary change and transformative power cooperate in the collective. A generation clears the ground for something genuinely new.",
    ("Pluto", "Uranus", "square"):      "The force of deep transformation and the disruptive impulse are in intense friction — the collective is torn between the need to rebuild and the compulsion to break free. The tension is a defining generational challenge.",
    ("Pluto", "Uranus", "trine"):       "Revolutionary energy and transformative depth flow together harmoniously in the collective. A generation dismantles and rebuilds with both force and vision.",
    ("Pluto", "Uranus", "opposition"):  "The force of disruption and the depth of transformation stand in direct opposition in the collective — what the generation breaks free from and what it must rebuild are two different things.",

    # ── Neptune–Pluto ────────────────────────────────────────────────────────────
    ("Neptune", "Pluto", "conjunction"): "A rare generational signature of civilizational transformation — the dissolution of one era and the birth of the next. The collective shadow and the collective dream are being remade simultaneously.",
    ("Neptune", "Pluto", "sextile"):     "Spiritual aspiration and transformative power cooperate across an entire generation. Collective ideals and collective shadow are engaged with unusual depth.",
    ("Neptune", "Pluto", "square"):      "The imaginal and the transformative are in tension — the dissolution of old forms meets the compulsive drive to remake the world. What the collective dreams and what it destroys do not yet agree.",
    ("Neptune", "Pluto", "trine"):       "Spiritual depth and transformative power flow together in the collective consciousness. A generation carries the capacity for both genuine transcendence and deep collective healing.",
    ("Neptune", "Pluto", "opposition"):  "The pull toward dissolution and the force of transformation stand in opposition across the collective — the dream and the phoenix are both present but pointing in different directions.",

    # ── ASC–planet aspects ───────────────────────────────────────────────────────

    ("ASC", "Jupiter", "conjunction"): "An expansive, optimistic presence — you arrive in any room as larger than life, and first impressions convey genuine warmth and openness. Luck tends to ride with the persona.",
    ("ASC", "Jupiter", "sextile"):     "The persona and the spirit of growth cooperate easily — you present as approachable and opportunity often follows. Others experience you as a door-opener.",
    ("ASC", "Jupiter", "square"):      "The desire for more and the self you project can be in tension — overpromising, overextending the persona, or simply taking up more space than intended. The lesson is calibrating the scale of the presentation.",
    ("ASC", "Jupiter", "trine"):       "Expansive optimism flows naturally through the persona. First impressions are generous and warm, and growth often arrives through the simple act of showing up.",
    ("ASC", "Jupiter", "opposition"):  "The persona and the pull toward expansion stand in opposition — what you project and what you actually want to grow toward may not fully align. The horizon is always just past where you are standing.",

    ("ASC", "Mars", "conjunction"): "Physical energy and assertive presence are front and center — you arrive with force and urgency, and others notice immediately. The body carries will.",
    ("ASC", "Mars", "sextile"):     "Drive and the persona cooperate naturally — you come across as energetic and capable, and people tend to believe you can get things done.",
    ("ASC", "Mars", "square"):      "The way you present and the force behind it can clash — the persona may come across as aggressive or impulsive even when that is not the intent. Learning to lead with the goal rather than the force is the work.",
    ("ASC", "Mars", "trine"):       "Drive and the physical self work in natural alignment. You project energy and confidence, and others are drawn to your ability to act.",
    ("ASC", "Mars", "opposition"):  "The way you show up and the will that drives you may stand in opposition — the persona may suppress the drive or the drive may overwhelm the presentation. Finding the balance is the ongoing practice.",

    ("ASC", "Mercury", "conjunction"): "The mind and the persona are inseparable — you present as quick, communicative, and intellectually alive. Words are a primary vehicle of first impression.",
    ("ASC", "Mercury", "sextile"):     "Thought and the way you present yourself cooperate naturally. You come across as intelligent and articulate without appearing calculated.",
    ("ASC", "Mercury", "square"):      "The analytical mind and the persona can be at odds — overthinking the presentation or speaking before thinking through the impact. Learning to let expression flow naturally is the practice.",
    ("ASC", "Mercury", "trine"):       "Communication and the persona flow together harmoniously. You present as thoughtful and quick, and the first impression tends to be accurate.",
    ("ASC", "Mercury", "opposition"):  "The mind and the outward self occupy different registers — what you think and how you come across may not fully agree. Integrating the inner voice with the outer presentation is the ongoing work.",

    ("ASC", "Moon", "conjunction"): "Emotional life is written on the body — others read your inner state before you speak a word. The persona is sensitive, responsive, and naturally nurturing.",
    ("ASC", "Moon", "sextile"):     "Emotional attunement and the persona cooperate naturally — you come across as warm and approachable, and others tend to feel safe with you.",
    ("ASC", "Moon", "square"):      "Emotional reactivity and the presented self can be in tension — what you feel and what you show may clash or bleed into each other unexpectedly. Learning to be genuinely present without being overwhelmed is the practice.",
    ("ASC", "Moon", "trine"):       "Emotional warmth and the physical self flow together naturally. You project genuine care and responsiveness, and first impressions tend to feel safe.",
    ("ASC", "Moon", "opposition"):  "The inner emotional life and the outer persona stand in opposition — what you feel and how you come across may be quite different. The integration of private sensitivity with public presence is a central task.",

    ("ASC", "Neptune", "conjunction"): "The persona is elusive, sensitive, and difficult to pin down — you can be all things to all people, for better or worse. An aura of mystery or spiritual depth accompanies you.",
    ("ASC", "Neptune", "sextile"):     "Spiritual sensitivity and the persona cooperate gently. You come across as empathic and imaginative, and others tend to feel understood in your presence.",
    ("ASC", "Neptune", "square"):      "The persona can blur into illusion — others may misread you, or you may project an image that does not fully hold. Clarity of self-presentation must be cultivated rather than assumed.",
    ("ASC", "Neptune", "trine"):       "Spiritual depth flows naturally through the persona. You project an elusive beauty or compassionate presence that is hard to define but easy to feel.",
    ("ASC", "Neptune", "opposition"):  "The idealized self and the actual self may stand in opposition — the persona can attract projection from others or project its own illusions outward. Learning to be seen clearly is the work.",

    ("ASC", "Pluto", "conjunction"): "Intensity radiates from the physical self — others sense your power before you do anything. The persona is magnetic, potentially intimidating, and rarely forgettable.",
    ("ASC", "Pluto", "sextile"):     "Transformative depth and the persona work together productively. You project quiet power and tend to leave a lasting impression.",
    ("ASC", "Pluto", "square"):      "The transformative force within and the self that meets the world are in tension — encounters with power, control, or intensity may mark first impressions in complicated ways. Learning to present depth without threat is the ongoing practice.",
    ("ASC", "Pluto", "trine"):       "Personal power flows naturally through the persona. You project authority and intensity without effort, and others tend to take you seriously.",
    ("ASC", "Pluto", "opposition"):  "The force of deep transformation and the way you present yourself stand in opposition — who you are becoming and who you appear to be may be quite different people. The integration is powerful when it finally arrives.",

    ("ASC", "Saturn", "conjunction"): "Seriousness and restraint color the persona — you come across as mature, responsible, and perhaps older than your years. Trust is earned over time rather than given freely at first meeting.",
    ("ASC", "Saturn", "sextile"):     "Structure and the persona cooperate with quiet effectiveness. You come across as dependable and are taken seriously without having to demand it.",
    ("ASC", "Saturn", "square"):      "The demands of responsibility and the natural expression of the self are in tension — the persona may feel constrained or the physical self may carry a burden it did not ask for. Learning to inhabit the self with authority rather than weight is the practice.",
    ("ASC", "Saturn", "trine"):       "Discipline and the physical self flow together in natural alignment. You project reliability and earned authority, and first impressions tend to be measured and lasting.",
    ("ASC", "Saturn", "opposition"):  "The self that faces the world and the weight of responsibility can feel like opposing forces. Learning to show up with authority rather than burden is the ongoing work.",

    ("ASC", "Sun", "conjunction"): "Identity and persona are one — there is little gap between who you are and how you come across. Vitality and self-expression are immediately legible to others.",
    ("ASC", "Sun", "sextile"):     "The life force and the physical self cooperate naturally. You present with genuine warmth and confidence, and others find you easy to trust.",
    ("ASC", "Sun", "square"):      "The core identity and the way you present yourself can pull in different directions — the ego and the persona may compete. Learning to be yourself without performing being yourself is the work.",
    ("ASC", "Sun", "trine"):       "Identity and the physical self flow together harmoniously. You show up as who you genuinely are, and others tend to find that immediately attractive.",
    ("ASC", "Sun", "opposition"):  "The self and the persona stand in opposition — who you are and who you seem to be may feel like different people to you or to others. Bridging the inner truth with the outer expression is the defining work.",

    ("ASC", "Uranus", "conjunction"): "The persona is electric, unconventional, and surprising — you arrive differently every time, and first impressions land as original, eccentric, or magnetic. Normalcy is not on offer.",
    ("ASC", "Uranus", "sextile"):     "Originality and the persona cooperate naturally. You come across as inventive and independent without being off-putting.",
    ("ASC", "Uranus", "square"):      "The unconventional self and the need to be understood can be in tension — the persona may shock before it connects. Learning to disrupt without alienating is a social skill worth developing.",
    ("ASC", "Uranus", "trine"):       "Originality flows naturally through the persona. You present as genuinely individual and others are curious about you in a productive way.",
    ("ASC", "Uranus", "opposition"):  "The drive for freedom and the way you present yourself stand in opposition — the persona may be conventional while the inner self is revolutionary, or vice versa. Closing the gap is the work.",

    ("ASC", "Venus", "conjunction"): "Charm, beauty, and social grace flow through the physical self — you present as attractive, diplomatic, and easy to be around. The persona is a natural magnet.",
    ("ASC", "Venus", "sextile"):     "Beauty and the persona cooperate naturally. You come across as warm and aesthetically pleasing, and social connections form easily.",
    ("ASC", "Venus", "square"):      "The desire to be liked and the authentic expression of the self can be in tension — pleasantness can become a mask. Learning to be genuinely charming rather than performatively agreeable is the practice.",
    ("ASC", "Venus", "trine"):       "Charm and the physical self flow together in natural harmony. You are at ease in social situations and project genuine warmth.",
    ("ASC", "Venus", "opposition"):  "The desire for beauty and connection and the way you show up in the world may pull in different directions. What you attract and what you project may not always feel like they belong to the same person.",

    # ── DSC–planet aspects ───────────────────────────────────────────────────────

    ("DSC", "Jupiter", "conjunction"): "Partnership brings expansion — you attract generous, growth-oriented partners who genuinely open up your world. The significant others in your life tend to be larger-than-life.",
    ("DSC", "Jupiter", "sextile"):     "The spirit of growth and the partnership house cooperate naturally. Relationships tend to bring opportunities and a sense of possibility.",
    ("DSC", "Jupiter", "square"):      "The desire for expansive partnership and the reality of what relationships actually require can conflict. Overexpecting from others or giving too freely creates its own complications.",
    ("DSC", "Jupiter", "trine"):       "Partnership and growth flow together harmoniously. Significant relationships bring genuine expansion and tend to be characterized by mutual generosity.",
    ("DSC", "Jupiter", "opposition"):  "The expansive pull of relationship and the needs of the self may stand in tension. Learning to grow alongside another rather than through them is the work.",

    ("DSC", "Mars", "conjunction"): "You attract assertive, energetic, or forceful partners — and may project your own drive onto those you pair with. Partnership is never without heat.",
    ("DSC", "Mars", "sextile"):     "Drive and the partnership house cooperate productively. You tend to attract energetic partners whose action-orientation complements your own.",
    ("DSC", "Mars", "square"):      "Conflict, competition, or the clash of wills within partnership is a recurring theme. The friction is productive when both people own their own drive.",
    ("DSC", "Mars", "trine"):       "Drive and partnership flow together naturally. You attract partners who are as energetic and purposeful as you are, and the combination works.",
    ("DSC", "Mars", "opposition"):  "The energy you project outward and the force you attract in partnership stand in direct opposition. What you seek in others may be what you have not yet claimed in yourself.",

    ("DSC", "Mercury", "conjunction"): "Communication is central to partnership — you need a partner who can think and talk with you. Intellectual connection is as important as any other kind.",
    ("DSC", "Mercury", "sextile"):     "The mind and the partnership house cooperate naturally. You attract thoughtful, communicative partners and express yourself well within relationship.",
    ("DSC", "Mercury", "square"):      "Communication within partnership can be a source of friction — what is said, unsaid, or misunderstood can destabilize even strong connections. Learning to listen as well as speak is part of the work.",
    ("DSC", "Mercury", "trine"):       "Thought and partnership flow together harmoniously. You tend to attract partners who are intelligent and communicative, and dialogue comes easily.",
    ("DSC", "Mercury", "opposition"):  "The way you think and the way your partners think may stand in interesting opposition — the intellectual tension between you can be stimulating or exhausting. The work is turning the difference into dialogue.",

    ("DSC", "Moon", "conjunction"): "You seek emotional intimacy in partnership — the ideal other is nurturing, feeling, and genuinely connected to the inner life. Family and home are themes in significant relationships.",
    ("DSC", "Moon", "sextile"):     "Emotional attunement and the partnership house cooperate naturally. You attract caring partners and feel genuinely seen within close relationship.",
    ("DSC", "Moon", "square"):      "Emotional needs and the demands of partnership can be in tension — dependency, emotional reactivity, or the need for care can complicate what would otherwise be straightforward. The work is bringing emotional intelligence to the partnership equation.",
    ("DSC", "Moon", "trine"):       "Emotional warmth and partnership flow together harmoniously. The significant others in your life tend to feel like home.",
    ("DSC", "Moon", "opposition"):  "The inner emotional life and the partnership you seek may stand in opposition — what you need privately and what you attract publicly may not immediately match. Bridging that gap is the work.",

    ("DSC", "Neptune", "conjunction"): "You idealize partners and attract those who project an aura of mystery, spirituality, or artistic depth. The partnership zone is subject to both transcendent beauty and difficult illusion.",
    ("DSC", "Neptune", "sextile"):     "Spiritual sensitivity and the partnership house cooperate gently. You attract partners who are imaginative and compassionate, and connection tends to have a dreamy quality.",
    ("DSC", "Neptune", "square"):      "Illusion, idealization, or confusion in partnership is a recurring theme. The partner may not be who you dreamed, or you may be difficult to truly know within relationship. Clarity is the ongoing practice.",
    ("DSC", "Neptune", "trine"):       "Spiritual depth and partnership flow together harmoniously. You attract partners who are sensitive and visionary, and relationships tend to feel genuinely meaningful.",
    ("DSC", "Neptune", "opposition"):  "The ideal partner and the real one may stand in painful opposition. Learning to love the actual person rather than the projected dream is the central challenge.",

    ("DSC", "Pluto", "conjunction"): "Partnerships carry transformative intensity — relationships do not leave you unchanged. Power, control, and deep psychological encounter are recurring themes in significant connections.",
    ("DSC", "Pluto", "sextile"):     "Transformative depth and the partnership house cooperate productively. You attract partners who challenge you to grow in ways you could not have anticipated.",
    ("DSC", "Pluto", "square"):      "Power struggles, compulsive attraction, or the shadow of control can appear in close relationships. The friction forces a confrontation with what you are projecting onto others.",
    ("DSC", "Pluto", "trine"):       "Transformative depth flows naturally through partnership. Significant relationships bring genuine psychological renewal and tend to change you for the better.",
    ("DSC", "Pluto", "opposition"):  "The force of transformation and the partnership you seek may stand in opposition — what you want and what it costs may not always feel proportionate. The power within relationship is the subject.",

    ("DSC", "Saturn", "conjunction"): "Partnership brings responsibility — you attract serious, committed, or sometimes older partners, and relationships tend to require sustained effort. Loyalty, once given, runs deep.",
    ("DSC", "Saturn", "sextile"):     "Commitment and the partnership house cooperate with quiet effectiveness. You tend to attract reliable partners and take relationship seriously in a productive way.",
    ("DSC", "Saturn", "square"):      "Partnership may feel like a burden or come with limitations — either the relationship requires more than expected, or significant others bring a sense of restriction. The lesson is learning that responsibility and love are not opposites.",
    ("DSC", "Saturn", "trine"):       "Commitment and partnership flow together in natural alignment. You attract partners who are dependable and build relationships that stand the test of time.",
    ("DSC", "Saturn", "opposition"):  "The demands of responsibility and the warmth of genuine partnership may feel in opposition. Learning to be both committed and open-hearted is the practice.",

    ("DSC", "Sun", "conjunction"): "You seek a partner who is vital, confident, and fully themselves — and may attract or project onto partners the qualities of the solar self. Relationship is a mirror for identity.",
    ("DSC", "Sun", "sextile"):     "The vitality you seek in others and the partnership house cooperate naturally. Significant others tend to be warm, confident, and genuinely themselves.",
    ("DSC", "Sun", "square"):      "The self you seek in a partner and your own sense of identity can be in tension — projection, competition, or the struggle to be recognized within relationship is the theme.",
    ("DSC", "Sun", "trine"):       "Vitality and partnership flow together naturally. You tend to attract partners who are confident and whole, and the relationship reflects back something good about who you are.",
    ("DSC", "Sun", "opposition"):  "The self and the partner stand in direct opposition — what you project onto significant others may be what you have not yet integrated in yourself. The partner becomes the teacher.",

    ("DSC", "Uranus", "conjunction"): "Partnership is unconventional by design — you attract original, unpredictable, or freedom-oriented partners. Traditional relationship structures rarely satisfy for long.",
    ("DSC", "Uranus", "sextile"):     "Originality and the partnership house cooperate naturally. You attract innovative partners who keep the relationship alive with fresh perspective.",
    ("DSC", "Uranus", "square"):      "The desire for freedom and the desire for partnership are in tension — commitment can feel like a cage, and the partners you attract may be brilliant but unreliable. The work is creating relationship structures that honor both.",
    ("DSC", "Uranus", "trine"):       "Freedom and partnership flow together harmoniously. You attract partners who respect independence and keep the relationship genuinely alive.",
    ("DSC", "Uranus", "opposition"):  "The unconventional pull within you and the partnership you seek may stand in opposition. What you want from a partner and what you are willing to give may not initially match.",

    ("DSC", "Venus", "conjunction"): "You seek beauty and harmony in partnership and tend to attract charming, aesthetically attuned partners. Relationship and the arts are deeply intertwined.",
    ("DSC", "Venus", "sextile"):     "The love nature and the partnership house cooperate naturally. You attract warm, beautiful partners and find that relationships bring genuine pleasure.",
    ("DSC", "Venus", "square"):      "The desire for harmony in partnership and the reality of what relationship actually requires can be in tension. Avoiding necessary conflict in the name of peace delays real resolution.",
    ("DSC", "Venus", "trine"):       "Love and partnership flow together in natural harmony. Significant relationships are characterized by warmth, beauty, and mutual appreciation.",
    ("DSC", "Venus", "opposition"):  "What you love and what you seek in a partner may stand in opposition. The beloved may reflect back something about your own relationship to beauty and desire.",

    # ── IC–planet aspects ────────────────────────────────────────────────────────

    ("IC", "Jupiter", "conjunction"): "The foundation of life is abundant and expansive — home may be large, the family generous in spirit, and the private inner world marked by genuine optimism. Security feels spacious.",
    ("IC", "Jupiter", "sextile"):     "Growth and the private foundation cooperate naturally. Home and family provide a platform of genuine opportunity and inner confidence.",
    ("IC", "Jupiter", "square"):      "The desire for more and the demands of home and roots can conflict — expansion pulls against the need for rootedness. The lesson is learning that a big life can be built on a secure foundation.",
    ("IC", "Jupiter", "trine"):       "Abundance and the foundation of life flow together harmoniously. Home life tends to feel generous and growth-oriented.",
    ("IC", "Jupiter", "opposition"):  "The private foundation and the pull toward public expansion stand in opposition. Finding what can grow from the roots rather than away from them is the work.",

    ("IC", "Mars", "conjunction"): "Drive and energy live in the private self — the home life carries intensity, and ancestral patterns of assertion or conflict may need to be consciously worked with. The foundation is never passive.",
    ("IC", "Mars", "sextile"):     "Drive and the foundation of life cooperate productively. Energy comes from the roots and the home tends to be an active, forward-moving place.",
    ("IC", "Mars", "square"):      "Conflict or restlessness in the home and the private self are recurring themes. The energy of the foundation can be channeled into building or into fighting — the choice makes all the difference.",
    ("IC", "Mars", "trine"):       "Drive and the foundation flow together naturally. Home life is energetic and actively supportive of your goals.",
    ("IC", "Mars", "opposition"):  "The drive within the private self and the public ambition stand in opposition. The foundation may feel like it pulls against rather than supports the trajectory of your life.",

    ("IC", "Mercury", "conjunction"): "The mind is rooted in family, home, and early experience. Memory and communication are shaped by the private world, and the inner life is perpetually in conversation with its origins.",
    ("IC", "Mercury", "sextile"):     "Thought and the foundation of life cooperate naturally. The home is a place where the mind works well, and family connections support intellectual development.",
    ("IC", "Mercury", "square"):      "Thinking and the private foundation can be in tension — the mind may be in conflict with family values or early conditioning. Learning to think for yourself while honoring where you came from is the work.",
    ("IC", "Mercury", "trine"):       "Communication and the foundation flow together naturally. The home supports thinking and family connections contribute to your intellectual confidence.",
    ("IC", "Mercury", "opposition"):  "The mind and the roots stand in opposition — how you think and where you come from may feel like different countries. Integrating the private origin with the public intellect is the ongoing work.",

    ("IC", "Moon", "conjunction"): "The emotional core and the private foundation are one — home, family, and the deepest instincts are all woven together. Security is found through rootedness, and the past runs very deep.",
    ("IC", "Moon", "sextile"):     "Emotional attunement and the foundation of life cooperate naturally. Home and family provide genuine emotional sustenance.",
    ("IC", "Moon", "square"):      "The emotional inner world and the demands of the private foundation can be in tension — what home means and what you actually need emotionally may not fully agree. Learning what genuine security actually feels like is the work.",
    ("IC", "Moon", "trine"):       "Emotional depth and the foundation of life flow together harmoniously. Home is a genuine sanctuary and family relationships are a source of real nourishment.",
    ("IC", "Moon", "opposition"):  "The inner emotional life and the public persona stand in opposition. The private self and the self that faces the world may feel very different from each other.",

    ("IC", "Neptune", "conjunction"): "The private foundation is infused with mystery, spiritual sensitivity, or idealization — the home and the family carry an ethereal or sometimes elusive quality. Roots may be unclear, romanticized, or genuinely mystical.",
    ("IC", "Neptune", "sextile"):     "Spiritual depth and the foundation of life cooperate gently. The home supports creative and imaginative inner development.",
    ("IC", "Neptune", "square"):      "Illusion or confusion around home, family, or the private foundation is a recurring theme. Learning what is actually real about your roots is the essential work.",
    ("IC", "Neptune", "trine"):       "Spiritual sensitivity and the foundation of life flow together harmoniously. The home and the inner life both carry a quality of depth and imagination.",
    ("IC", "Neptune", "opposition"):  "The ideal of home and the reality of public life may stand in painful opposition. What you dream of in private and what you build in the world may feel like they belong to different people.",

    ("IC", "Pluto", "conjunction"): "The foundation of life carries enormous transformative weight — family history, ancestral patterns, or the private self may be a site of deep psychological power. What the roots hold shapes everything above the surface.",
    ("IC", "Pluto", "sextile"):     "Transformative depth and the foundation cooperate productively. The private self is a source of real power, and working with the roots brings genuine regeneration.",
    ("IC", "Pluto", "square"):      "The power within the private foundation and the demands of the outer world are in intense tension. Ancestral shadows or family dynamics may require real psychological work to metabolize.",
    ("IC", "Pluto", "trine"):       "Transformative depth and the foundation of life flow together naturally. The roots are a source of power, and what has been transformed privately becomes a foundation for outer achievement.",
    ("IC", "Pluto", "opposition"):  "The private transformation and the public ambition stand in direct opposition. What is being rebuilt in the foundations of life shapes and sometimes undermines what is being built above.",

    ("IC", "Saturn", "conjunction"): "The foundation carries the weight of responsibility — family expectations, early discipline, or ancestral obligation shape the private self. Over time, what was a burden can become the bedrock.",
    ("IC", "Saturn", "sextile"):     "Structure and the foundation cooperate productively. The home provides a sense of reliable order, and private discipline builds a solid base for everything above.",
    ("IC", "Saturn", "square"):      "Responsibility within the private foundation and the desire for ease or expansion can conflict. The early home life may have been marked by restriction, and the lesson is building your own security without replicating those limits.",
    ("IC", "Saturn", "trine"):       "Discipline and the foundation flow together naturally. The private self is well-organized, and the home provides a dependable platform for growth.",
    ("IC", "Saturn", "opposition"):  "The weight of the private foundation and the ambitions of the public life stand in opposition. What you carry from the roots may feel like it holds back what you are trying to build.",

    ("IC", "Sun", "conjunction"): "Identity is rooted in the private world — the home and the family are central to who you are. Inner confidence comes from a secure foundation, and the self is most authentic in private.",
    ("IC", "Sun", "sextile"):     "Vitality and the foundation cooperate naturally. The home supports your sense of self and the private life gives energy to the public one.",
    ("IC", "Sun", "square"):      "The identity rooted in home and family and the public life you are building can conflict. Honoring where you come from while becoming who you are is the practice.",
    ("IC", "Sun", "trine"):       "Identity and the foundation flow together harmoniously. Who you are privately and who you are publicly feel like the same person.",
    ("IC", "Sun", "opposition"):  "The private self and the public identity stand in opposition. The self rooted in home and the self facing the world may feel like they need very different things.",

    ("IC", "Uranus", "conjunction"): "The foundation is disrupted or unconventional — the home life may have been marked by sudden changes, unusual circumstances, or a family that did not fit the norm. Freedom is needed even in the most private spaces.",
    ("IC", "Uranus", "sextile"):     "Originality and the foundation cooperate productively. The home is a place where innovation is welcomed and the private self has room to evolve.",
    ("IC", "Uranus", "square"):      "Disruption and the need for stable roots are in tension. The private foundation may be unstable or the desire for freedom conflicts with the need for home. Learning to belong without being trapped is the work.",
    ("IC", "Uranus", "trine"):       "Freedom and the foundation flow together harmoniously. The home is unconventional but genuinely supportive, and the private self has space to be original.",
    ("IC", "Uranus", "opposition"):  "The force of disruption in the private world and the public ambitions stand in opposition. What keeps changing at the foundation makes it harder to build in the world, until both are integrated.",

    ("IC", "Venus", "conjunction"): "The home and the private self are infused with beauty, warmth, and the love of pleasure. The family may have been a source of genuine aesthetic and emotional richness.",
    ("IC", "Venus", "sextile"):     "Beauty and the foundation cooperate naturally. Home is a genuinely warm and aesthetically pleasing sanctuary.",
    ("IC", "Venus", "square"):      "The desire for beauty and ease in the home and the demands of the outer world can conflict. Learning that inner richness and outer success can coexist takes time.",
    ("IC", "Venus", "trine"):       "Love and the foundation of life flow together naturally. The home is a place of genuine warmth and the private self is touched by beauty.",
    ("IC", "Venus", "opposition"):  "The warmth of the private world and the demands of the public one may stand in opposition. What you love in private and what you build in the world may pull toward different values.",

    # ── Jupiter–MC / MC–planet aspects ──────────────────────────────────────────

    ("Jupiter", "MC", "conjunction"): "Career and public life are marked by expansive ambition and the genuine capacity for success. Recognition comes and tends to be of an impressive scale.",
    ("Jupiter", "MC", "sextile"):     "Growth and public reputation cooperate naturally. The career advances with a sense of possibility, and others tend to see you as someone worth backing.",
    ("Jupiter", "MC", "square"):      "Ambition and the desire to be recognized can overreach — the career may expand faster than the infrastructure can support. The lesson is building success that can actually hold its own weight.",
    ("Jupiter", "MC", "trine"):       "Career and the spirit of expansion flow together harmoniously. Public recognition comes with relative ease and tends to feel genuinely deserved.",
    ("Jupiter", "MC", "opposition"):  "Public ambition and the private foundation may stand in tension. Learning to grow professionally without losing the rootedness that makes it sustainable is the work.",

    ("MC", "Mars", "conjunction"): "Ambition and drive flow directly into public life — you pursue the career with force and urgency, and others know you mean business. The will to lead is not subtle.",
    ("MC", "Mars", "sextile"):     "Drive and public reputation cooperate productively. Career advances through energy and initiative, and others respect your capacity for action.",
    ("MC", "Mars", "square"):      "Competitive energy and the demands of the public life can create conflict or friction in the career. The lesson is channeling ambition into sustained effort rather than impulsive assertion.",
    ("MC", "Mars", "trine"):       "Drive and career flow together naturally. You pursue your calling with genuine force and others tend to admire the energy you bring.",
    ("MC", "Mars", "opposition"):  "The drive within you and the public life you are building may stand in opposition. The private ambition and the public role may not fully agree on direction.",

    ("MC", "Mercury", "conjunction"): "The mind and public reputation are aligned — communication, writing, and intellectual work are natural paths to recognition. You are known for how you think and speak.",
    ("MC", "Mercury", "sextile"):     "Thought and public reputation cooperate naturally. The career benefits from clear communication and the ability to articulate ideas that others can use.",
    ("MC", "Mercury", "square"):      "The way you think and the public role you inhabit can be in tension — ideas may not fit the expected form, or the career may demand a kind of precision that cuts against natural style. The work is finding a form that honors both.",
    ("MC", "Mercury", "trine"):       "Communication and career flow together harmoniously. The public role is served well by your mind and your ability to speak with clarity and intelligence.",
    ("MC", "Mercury", "opposition"):  "The intellect and the public ambition may stand in opposition. How you think and what the world expects of you may not initially point in the same direction.",

    ("MC", "Moon", "conjunction"): "Emotional sensitivity and public reputation are intertwined — the career may be in a nurturing, caring, or public-facing field. The emotional life is legible in the professional arena.",
    ("MC", "Moon", "sextile"):     "Emotional attunement and public life cooperate naturally. The career benefits from genuine care for others and a responsive, feeling presence.",
    ("MC", "Moon", "square"):      "The emotional inner world and the demands of public life can conflict — professional expectations may feel at odds with genuine emotional needs. Learning to honor both is the practice.",
    ("MC", "Moon", "trine"):       "Emotional depth and public reputation flow together harmoniously. The career benefits from genuine care and sensitivity, and others experience you as trustworthy.",
    ("MC", "Moon", "opposition"):  "The private emotional self and the public identity stand in opposition. What you feel privately and what the world sees publicly may be quite different.",

    ("MC", "Neptune", "conjunction"): "Career and public reputation carry a spiritual, artistic, or service-oriented quality — you are known for something hard to define but easy to feel. Idealization from or toward the public is part of the landscape.",
    ("MC", "Neptune", "sextile"):     "Spiritual depth and public life cooperate gently. The career benefits from imagination and empathy, and others find your work meaningful.",
    ("MC", "Neptune", "square"):      "Illusion or confusion around the career and public role is a recurring theme. What the world sees and what you are actually doing may not fully agree. Clarity of purpose is the ongoing practice.",
    ("MC", "Neptune", "trine"):       "Spiritual depth and public reputation flow together harmoniously. The career has a quality of vision and compassion that distinguishes it.",
    ("MC", "Neptune", "opposition"):  "The idealized public role and the private reality may stand in opposition. What you dream of achieving publicly and what your private foundation can actually support may need to be reconciled.",

    ("MC", "Pluto", "conjunction"): "Career carries tremendous power — public life is marked by ambition, intensity, and the experience of significant rises or falls. The relationship with authority is central and complex.",
    ("MC", "Pluto", "sextile"):     "Transformative depth and public reputation cooperate productively. The career is marked by the ability to get to the heart of things and build on what has been cleared away.",
    ("MC", "Pluto", "square"):      "Power struggles or intense confrontations with authority are part of the professional landscape. The career may go through dramatic upheaval before finding its true direction.",
    ("MC", "Pluto", "trine"):       "Transformative power flows naturally through the career. You build public authority through depth, and others sense that your work carries real weight.",
    ("MC", "Pluto", "opposition"):  "The force of transformation and the demands of public life stand in opposition. What is being rebuilt privately shapes and sometimes undermines what is being built professionally.",

    ("MC", "Saturn", "conjunction"): "Career is the central domain of discipline and eventual mastery — recognition comes through years of sustained effort and the willingness to be responsible when no one is watching. What you build lasts.",
    ("MC", "Saturn", "sextile"):     "Discipline and public reputation cooperate productively. The career advances through consistent effort, and others respect the seriousness you bring.",
    ("MC", "Saturn", "square"):      "The demands of career and the self that must meet them can be in tension — the path to recognition feels slow, blocked, or laden with responsibility. The lesson is that the long way around is the only road that holds.",
    ("MC", "Saturn", "trine"):       "Discipline and career flow together naturally. You build your public life methodically and what you achieve tends to be both hard-won and durable.",
    ("MC", "Saturn", "opposition"):  "The weight of responsibility and the ambitions of the career may stand in opposition. Learning that what you build can support rather than burden you is the ongoing work.",

    ("MC", "Sun", "conjunction"): "Identity and career are aligned — public life is an expression of who you genuinely are, and the calling feels like the self. Recognition and purpose are tied together.",
    ("MC", "Sun", "sextile"):     "Vitality and public reputation cooperate naturally. The career benefits from your genuine confidence and others experience you as authentically purposeful.",
    ("MC", "Sun", "square"):      "The ego and the demands of public life can conflict — the need for recognition and the reality of what career actually requires may not initially agree. The lesson is finding where the self and the calling genuinely meet.",
    ("MC", "Sun", "trine"):       "Identity and career flow together harmoniously. You show up publicly as who you genuinely are, and the professional world tends to reward the authenticity.",
    ("MC", "Sun", "opposition"):  "The public identity and the private self stand in opposition. Who you are at work and who you are at home may feel like genuinely different people — the work is finding the thread that connects them.",

    ("MC", "Uranus", "conjunction"): "Career is unconventional, innovative, and prone to dramatic shifts in direction. You are known for originality and may remake your professional life multiple times. The world benefits from the disruption.",
    ("MC", "Uranus", "sextile"):     "Originality and public reputation cooperate naturally. The career benefits from innovation and others appreciate that you bring something fresh.",
    ("MC", "Uranus", "square"):      "The drive for professional freedom and the demands of a stable career can conflict. The path to recognition involves disruption — sometimes intentional, sometimes not.",
    ("MC", "Uranus", "trine"):       "Innovation and career flow together harmoniously. You build a public life that is genuinely original and others recognize the difference.",
    ("MC", "Uranus", "opposition"):  "The force of disruption and the demands of the career may stand in opposition. What keeps changing professionally shapes and sometimes complicates what you are trying to build.",

    ("MC", "Venus", "conjunction"): "Career and beauty are intertwined — you are known for charm, artistry, or a graceful public presence. The professional life benefits from the Venusian gifts.",
    ("MC", "Venus", "sextile"):     "Beauty and public reputation cooperate naturally. The career advances through social grace and the cultivation of genuine aesthetic value.",
    ("MC", "Venus", "square"):      "The desire for a beautiful or pleasant career and the reality of what the professional path requires can conflict. Learning that love of the work is compatible with its challenges is the practice.",
    ("MC", "Venus", "trine"):       "Love and career flow together harmoniously. The professional life is marked by beauty, warm relationships, and the satisfaction of doing work you genuinely value.",
    ("MC", "Venus", "opposition"):  "The love of beauty and the demands of the career may stand in opposition. What you want professionally and what you love privately may not initially agree on direction.",

    # ── North Node aspects ────────────────────────────────────────────────────
    # keyed (*sorted([planet, "North Node"]), aspect)

    ("Jupiter", "North Node", "conjunction"): "Expansion and soul growth reinforce each other powerfully. Optimism, generosity, and philosophy are not just gifts — they are evolutionary tools pointing toward your destiny.",
    ("Jupiter", "North Node", "sextile"):     "Abundance and destiny support each other with ease. Growth tends to come with opportunity, and the soul's direction opens doors rather than closing them.",
    ("Jupiter", "North Node", "square"):      "The abundance principle and the soul's direction may create friction. Excess, overreach, or misplaced faith can slow evolutionary progress until wisdom catches up with enthusiasm.",
    ("Jupiter", "North Node", "trine"):       "Growth and good fortune cooperate harmoniously. The path of soul development tends to be paved with well-timed opportunities and genuine expansion.",
    ("Jupiter", "North Node", "opposition"):  "Expansion and soul growth stand across from each other. The challenge is keeping optimism and opportunity in service of genuine development rather than comfortable distraction.",

    ("Mars", "North Node", "conjunction"): "Drive, initiative, and assertiveness are evolutionary tools. Action taken in the direction of your soul's purpose tends to have unusual force and significance.",
    ("Mars", "North Node", "sextile"):     "Will and soul direction work together with ease. Assertive energy can be channeled productively toward growth without requiring enormous effort.",
    ("Mars", "North Node", "square"):      "Desire and destiny create friction. The impulse to fight, push, or compete may need to be redirected before it truly serves the evolutionary path.",
    ("Mars", "North Node", "trine"):       "Action and growth harmonize naturally. You move toward your soul's direction with genuine energy, and assertiveness rarely takes you too far off course.",
    ("Mars", "North Node", "opposition"):  "Drive and soul growth face each other across the axis. The challenge is channeling energy away from old battles and toward the real work of development.",

    ("Mercury", "North Node", "conjunction"): "Communication and learning are central to your evolutionary path. Words, teaching, and the play of ideas are how you grow and help others grow alongside you.",
    ("Mercury", "North Node", "sextile"):     "Intelligence and destiny cooperate naturally. Curiosity leads toward growth, and the mind is a genuine asset in moving forward on your life's path.",
    ("Mercury", "North Node", "square"):      "The way you think or communicate creates friction with your evolutionary direction. Growth involves updating how you process information and express yourself.",
    ("Mercury", "North Node", "trine"):       "Mind and soul direction flow effortlessly together. Learning, writing, and honest conversation are both natural talents and pathways to development.",
    ("Mercury", "North Node", "opposition"):  "Communication patterns and soul growth may pull in opposite directions. The challenge is using words in service of where you are going, not just where you have been.",

    ("Moon", "North Node", "conjunction"): "Emotional instincts are aligned with growth. Nurturing others, following your feelings, and honoring vulnerability are woven into your evolutionary path.",
    ("Moon", "North Node", "sextile"):     "Emotional intelligence supports your soul's direction. Feelings are a useful guide toward the growth experiences that matter most.",
    ("Moon", "North Node", "square"):      "Emotional habits and evolutionary direction create tension. Old comfort patterns can resist the soul's call to expand into new emotional territory.",
    ("Moon", "North Node", "trine"):       "Feeling and destiny flow in harmony. The emotional life naturally carries you in the direction of growth; following your instincts rarely leads you astray.",
    ("Moon", "North Node", "opposition"):  "Emotional needs and soul growth stand across from each other. Learning to balance personal security with relational openness is a central lifetime theme.",

    ("Neptune", "North Node", "conjunction"): "Spirituality, compassion, and the dissolving of boundaries are part of the evolutionary path. Growth comes through surrender and faith rather than control.",
    ("Neptune", "North Node", "sextile"):     "Spiritual sensitivity and soul direction support each other gently. Intuition and imagination are quiet assets on the path forward.",
    ("Neptune", "North Node", "square"):      "Spiritual idealism and evolutionary direction create friction. Illusions or escapism may need to be released before the soul can progress clearly.",
    ("Neptune", "North Node", "trine"):       "Spiritual awareness and destiny flow harmoniously. The path of development often runs through art, healing, or a deepening relationship with the unseen.",
    ("Neptune", "North Node", "opposition"):  "Spiritual longings and soul growth face each other. The challenge is channeling Neptune's dissolving force in service of growth rather than confusion.",

    ("North Node", "Pluto", "conjunction"): "Transformation and soul evolution are deeply intertwined. Radical change, loss, and renewal are part of the design — power moves you toward your destiny.",
    ("North Node", "Pluto", "sextile"):     "Depth and soul direction cooperate. The willingness to confront what is hidden supports forward progress on the evolutionary path.",
    ("North Node", "Pluto", "square"):      "Transformation and soul growth create friction. Power struggles, obsessions, or buried fears may need to be metabolized before real progress becomes possible.",
    ("North Node", "Pluto", "trine"):       "Depth and destiny harmonize. The capacity for radical self-renewal carries you naturally toward your soul's purpose.",
    ("North Node", "Pluto", "opposition"):  "Transformation and soul growth face each other across the axis. The challenge is releasing the grip of power, control, or buried material in service of genuine development.",

    ("North Node", "Saturn", "conjunction"): "Discipline, responsibility, and maturity are central to the evolutionary path. Growth requires effort and patience but yields genuine, lasting achievement.",
    ("North Node", "Saturn", "sextile"):     "Structure and soul direction support each other. Discipline applied in the right areas accelerates growth and builds real foundations.",
    ("North Node", "Saturn", "square"):      "Responsibility and soul growth create friction. Old structures, fears, or limiting beliefs may need to be actively confronted before real progress is possible.",
    ("North Node", "Saturn", "trine"):       "Effort and destiny flow together steadily. Consistent work toward your soul's direction is rewarded, and the path forward is disciplined and purposeful.",
    ("North Node", "Saturn", "opposition"):  "Discipline and soul growth face each other. The challenge is releasing outgrown structures and applying effort toward what the soul is actually calling for.",

    ("North Node", "Sun", "conjunction"): "Identity and destiny align. Your life purpose and personal vitality point toward the same horizon, making growth feel natural and deeply personal.",
    ("North Node", "Sun", "sextile"):     "The self and the soul's direction support each other with ease. There is an innate talent for moving in your evolutionary direction without forcing it.",
    ("North Node", "Sun", "square"):      "Identity and soul growth pull against each other. You may feel torn between who you are now and who you are being called to become.",
    ("North Node", "Sun", "trine"):       "Personal identity and life purpose flow together. You grow into your destiny naturally, and self-expression doubles as spiritual development.",
    ("North Node", "Sun", "opposition"):  "The core self and the soul's direction face each other across the axis. Growth often comes through encounters with others who embody the qualities you are here to develop.",

    ("North Node", "Uranus", "conjunction"): "Innovation, rebellion, and awakening are part of the evolutionary design. Growth often comes through upheaval and the willingness to be radically different.",
    ("North Node", "Uranus", "sextile"):     "Originality and destiny cooperate. Unusual ideas and unconventional paths support forward movement on the soul's journey.",
    ("North Node", "Uranus", "square"):      "Disruption and soul growth create friction. Change may arrive in ways that challenge the direction of development rather than supporting it.",
    ("North Node", "Uranus", "trine"):       "Innovation and soul direction harmonize. The willingness to break with convention carries you naturally toward growth and awakening.",
    ("North Node", "Uranus", "opposition"):  "Awakening and soul growth stand across from each other. The challenge is making peace with disruption and allowing sudden change to serve evolutionary ends.",

    ("North Node", "Venus", "conjunction"): "Love, beauty, and relationships are core to your evolutionary purpose. Growing through genuine connection and developing real values are central themes.",
    ("North Node", "Venus", "sextile"):     "Relational ease supports your path forward. Harmonious relationships and an appreciation of beauty help carry you in your soul's direction.",
    ("North Node", "Venus", "square"):      "Values, pleasure, or relationship patterns may resist the direction of growth. What feels comfortable and attractive may not always align with what the soul needs to explore.",
    ("North Node", "Venus", "trine"):       "Love and destiny move together naturally. Relationships, beauty, and creative work carry you toward growth rather than away from it.",
    ("North Node", "Venus", "opposition"):  "The desire for comfort or harmony and the direction of soul growth can stand in opposition. True intimacy may require stretching toward unfamiliar values.",

    # ── South Node aspects ────────────────────────────────────────────────────
    # keyed (*sorted([planet, "South Node"]), aspect)

    ("Jupiter", "South Node", "conjunction"): "Expansive gifts from past experience are deeply available. Philosophy, travel, or abundance may feel natural and familiar — sometimes so comfortable they become substitutes for genuine growth.",
    ("Jupiter", "South Node", "sextile"):     "Abundance and past life patterns cooperate easily. Natural generosity and optimism are accessible, though the ease of past-life luck can delay the soul from pursuing real development.",
    ("Jupiter", "South Node", "square"):      "Expansion and past life comfort create friction. Over-reliance on old beliefs, cultural assumptions, or past luck may need to be challenged before growth becomes possible.",
    ("Jupiter", "South Node", "trine"):       "Philosophy and past life comfort flow together naturally. Genuine wisdom and optimism are gifts from before, though the temptation to rest in familiar philosophies can arise.",
    ("Jupiter", "South Node", "opposition"):  "Expansion and past life comfort stand across from each other. Growth requires stepping beyond the boundaries of what once felt abundantly comfortable.",

    ("Mars", "South Node", "conjunction"): "Drive, assertiveness, and old battles are deeply rooted. Past life warrior energy is accessible, but the temptation to fight old wars rather than channel energy toward new purpose is real.",
    ("Mars", "South Node", "sextile"):     "Will and past life patterns cooperate. Assertive energy is readily available from deep in the soul, though it may be more comfortable to direct it in familiar rather than growth-oriented ways.",
    ("Mars", "South Node", "square"):      "Drive and past life habits create friction. Old anger, aggression, or competitive patterns may resurface and need to be redirected before energy can serve current evolution.",
    ("Mars", "South Node", "trine"):       "Will and past life comfort flow easily together. Natural drive and courage are genuine gifts, though the temptation to keep fighting old battles rather than pursuing new growth is present.",
    ("Mars", "South Node", "opposition"):  "Assertive energy and past life comfort stand across from each other. Growth comes from channeling drive toward new territory rather than replaying familiar conflicts.",

    ("Mercury", "South Node", "conjunction"): "Communication and thinking patterns are deeply ingrained from past experience. Real intelligence is present, but familiar mental habits may limit openness to genuinely new ideas.",
    ("Mercury", "South Node", "sextile"):     "The mind and past life patterns cooperate easily. Intellectual gifts are accessible, though the risk is relying on old frameworks rather than developing new perspectives.",
    ("Mercury", "South Node", "square"):      "Thinking patterns and past life habits create friction. The way you communicate or process information may need deliberate updating to serve the soul's current direction.",
    ("Mercury", "South Node", "trine"):       "Mind and past life comfort flow naturally together. Natural intelligence is a genuine asset, though it may subtly discourage exploration of unfamiliar intellectual territory.",
    ("Mercury", "South Node", "opposition"):  "Communication patterns and past life comfort stand across from each other. Growth comes through questioning familiar mental habits and risking new forms of expression.",

    ("Moon", "South Node", "conjunction"): "Emotional patterns run deep and familiar. Instinctive responses, family dynamics, and nurturing behaviors are deeply ingrained from a prior chapter of soul experience.",
    ("Moon", "South Node", "sextile"):     "Emotional intelligence and past life patterns cooperate. Inner resources are readily available, though they may anchor the soul in familiar rather than new emotional territory.",
    ("Moon", "South Node", "square"):      "Emotional habits and past life patterns create friction. Old conditioning may need to be actively questioned before the emotional body can grow in a new direction.",
    ("Moon", "South Node", "trine"):       "Feeling and past life comfort flow together easily. Emotional sensitivity is a genuine gift, though it may encourage returning to comfortable patterns rather than new growth.",
    ("Moon", "South Node", "opposition"):  "Emotional needs and past life comfort stand across from each other. The pull between the familiar emotional world and genuine relational growth can be strong.",

    ("Neptune", "South Node", "conjunction"): "Spirituality, fantasy, and dissolution are deeply rooted in past experience. Genuine sensitivity and spiritual awareness are present, but the temptation toward escapism may be strong.",
    ("Neptune", "South Node", "sextile"):     "Spiritual gifts and past life patterns cooperate. Intuition and imagination are readily available, though they may be most comfortable in familiar, past-oriented expressions.",
    ("Neptune", "South Node", "square"):      "Spiritual idealism and past life habits create friction. Old illusions, fantasies, or spiritual bypassing may need to be confronted before the soul can move clearly forward.",
    ("Neptune", "South Node", "trine"):       "Spiritual awareness and past life comfort flow together naturally. Deep sensitivity and imaginative gifts are genuine, though the ease of retreat into familiar spiritual worlds can delay growth.",
    ("Neptune", "South Node", "opposition"):  "Spiritual longing and past life comfort stand across from each other. Growth comes through applying spiritual gifts in service of present reality rather than familiar dissolution.",

    ("Pluto", "South Node", "conjunction"): "Transformation, power, and intensity are deeply ingrained from past experience. The capacity for radical change is genuine, but old power dynamics or destructive patterns may need releasing.",
    ("Pluto", "South Node", "sextile"):     "Depth and past life patterns cooperate. The capacity for transformation is accessible, though old psychological material may surface in familiar rather than new ways.",
    ("Pluto", "South Node", "square"):      "Transformation and past life habits create friction. Old power struggles, compulsions, or buried material may resurface with force before the soul can move toward real renewal.",
    ("Pluto", "South Node", "trine"):       "Depth and past life comfort flow naturally together. The capacity for profound change is a genuine gift from prior experience, though it may be more comfortable in familiar territory.",
    ("Pluto", "South Node", "opposition"):  "Transformation and past life comfort stand across from each other. Growth requires releasing old patterns of power, control, or intensity in favor of genuinely new engagement with depth.",

    ("Saturn", "South Node", "conjunction"): "Discipline, structure, and limitation are deeply ingrained from past experience. Genuine mastery is present, but familiar constraints may need to be questioned rather than simply relied upon.",
    ("Saturn", "South Node", "sextile"):     "Structure and past life patterns cooperate. Natural discipline and responsibility are accessible, though old structures may be more comfort than genuine support.",
    ("Saturn", "South Node", "square"):      "Discipline and past life habits create friction. Old fears, rigid structures, or karmic obligations may surface as obstacles before the soul can move toward genuine freedom.",
    ("Saturn", "South Node", "trine"):       "Effort and past life comfort flow together naturally. Real competence and reliability are present, though the temptation to rely on familiar structures rather than building new ones can limit growth.",
    ("Saturn", "South Node", "opposition"):  "Discipline and past life comfort stand across from each other. Growth requires releasing old authorities, obligations, or self-imposed limitations.",

    ("South Node", "Sun", "conjunction"): "The identity is deeply familiar — perhaps too familiar. Old patterns of self-expression feel comfortable but may limit the soul's forward movement.",
    ("South Node", "Sun", "sextile"):     "The core self and past life patterns support each other. Natural gifts from before are accessible and can be put to good use without requiring significant effort to access.",
    ("South Node", "Sun", "square"):      "Identity and past life patterns create friction. The comfortable self-image may need to be disrupted before the soul can move toward genuine growth.",
    ("South Node", "Sun", "trine"):       "The identity and past life gifts flow easily together. Innate talents come naturally, but the gift can become a crutch that substitutes for new development.",
    ("South Node", "Sun", "opposition"):  "Self-expression and past life comfort stand across from each other. Growth often requires stepping away from the familiar and risking a different kind of identity.",

    ("South Node", "Uranus", "conjunction"): "Rebellion and radical change are deeply familiar. Unconventional behavior may feel second nature, but the comfort of being different can become as limiting as any conformity.",
    ("South Node", "Uranus", "sextile"):     "Originality and past life patterns cooperate. Unconventional gifts are accessible from deep in the soul, though the ease of being different may not always serve the soul's current direction.",
    ("South Node", "Uranus", "square"):      "Disruption and past life habits create friction. Old patterns of rebellion or restlessness may need to be examined before innovation can serve genuine growth.",
    ("South Node", "Uranus", "trine"):       "Innovation and past life comfort flow naturally together. The capacity for original thought is real and accessible, though the comfort of being unconventional may substitute for deeper development.",
    ("South Node", "Uranus", "opposition"):  "Awakening and past life comfort stand across from each other. Growth comes through applying the gift of originality in service of genuine evolution rather than familiar disruption.",

    ("South Node", "Venus", "conjunction"): "Relationship patterns and values are deeply rooted in past experience. Real gifts in love and beauty are present, but familiar relationship dynamics may need to evolve.",
    ("South Node", "Venus", "sextile"):     "Love and past life patterns cooperate naturally. Relational gifts are accessible, though the comfort of familiar attachment styles may limit the soul's relational growth.",
    ("South Node", "Venus", "square"):      "Relationship patterns and past life habits create friction. Old values or ways of relating may need conscious examination before the soul can move toward healthier connection.",
    ("South Node", "Venus", "trine"):       "Love and past life comfort flow together easily. Genuine charm and relational grace are present, though the pull toward comfortable love can resist the deeper relational work of growth.",
    ("South Node", "Venus", "opposition"):  "Relational values and past life comfort stand across from each other. Growth requires moving beyond familiar pleasures and cultivating a more evolved relationship with love.",
}


# ── Transit planet in sign ────────────────────────────────────────────────────
# keyed (planet, sign) — "right now" language for the current sky position

TRANSIT_IN_SIGN: dict[tuple[str, str], str] = {

    # Sun
    ("Sun", "Aries"):       "Right now, the Sun is moving through Aries, charging the collective mood with initiative, drive, and the impulse to begin. Energy runs high and the spirit of going first is in the air.",
    ("Sun", "Taurus"):      "Right now, the Sun is in Taurus, slowing the collective pulse toward patience, pleasure, and what is worth sustaining. It is a time of beauty, deliberate progress, and genuine comfort.",
    ("Sun", "Gemini"):      "Right now, the Sun is moving through Gemini, quickening collective curiosity and the joy of exchanging ideas. Versatility, communication, and mental connection are lit up.",
    ("Sun", "Cancer"):      "Right now, the Sun is in Cancer, turning the collective mood inward toward feeling, home, and what nourishes the soul. Sensitivity is heightened and the inner life quietly calls for attention.",
    ("Sun", "Leo"):         "Right now, the Sun is in Leo, amplifying the collective need for creative expression and the warmth of being genuinely seen. Generosity and the desire to shine are alive in the air.",
    ("Sun", "Virgo"):       "Right now, the Sun is moving through Virgo, turning collective attention toward craft, improvement, and useful work. Practicality and discernment are the qualities of the moment.",
    ("Sun", "Libra"):       "Right now, the Sun is in Libra, orienting collective energy toward balance, partnership, and the search for fairness. The impulse to relate, harmonize, and consider others is heightened.",
    ("Sun", "Scorpio"):     "Right now, the Sun is in Scorpio, deepening the collective atmosphere into intensity and transformation. The stakes of honesty feel higher and what has been hidden tends to surface.",
    ("Sun", "Sagittarius"): "Right now, the Sun is moving through Sagittarius, energizing the collective appetite for meaning, freedom, and big-picture vision. Optimism and the pull toward the horizon are strong.",
    ("Sun", "Capricorn"):   "Right now, the Sun is in Capricorn, focusing collective energy on ambition, discipline, and the building of lasting things. Seriousness of purpose and long-term thinking are in the air.",
    ("Sun", "Aquarius"):    "Right now, the Sun is in Aquarius, orienting collective energy toward innovation, community, and the wider pattern. The impulse to think differently and serve something larger than oneself is heightened.",
    ("Sun", "Pisces"):      "Right now, the Sun is moving through Pisces, softening the collective atmosphere with sensitivity, imagination, and spiritual longing. The boundary between self and other grows more permeable.",

    # Moon
    ("Moon", "Aries"):       "Right now, the Moon is in Aries, sending a wave of emotional urgency and the impulse to act on feeling without delay. The mood runs hot, impatient, and direct for the next day or so.",
    ("Moon", "Taurus"):      "Right now, the Moon is in Taurus, grounding the collective mood in comfort, the senses, and the pleasure of simple things. There is a pull toward slowing down and savoring what is good.",
    ("Moon", "Gemini"):      "Right now, the Moon is in Gemini, quickening emotional responses and the need to talk, connect, and process feelings through words. The mood is curious, light, and changeable.",
    ("Moon", "Cancer"):      "Right now, the Moon is in Cancer, its home sign, amplifying sensitivity, intuition, and the pull toward home and those we love. Feelings run close to the surface.",
    ("Moon", "Leo"):         "Right now, the Moon is in Leo, lifting the emotional atmosphere with warmth, drama, and the desire to feel special. There is a collective impulse toward joy, generosity, and creative expression.",
    ("Moon", "Virgo"):       "Right now, the Moon is in Virgo, turning the collective mood toward precision, helpfulness, and the satisfaction of things done right. The urge to improve and attend to details is emotionally alive.",
    ("Moon", "Libra"):       "Right now, the Moon is in Libra, smoothing the collective emotional field toward harmony, consideration, and the beauty of mutual care. The mood is diplomatic and socially attuned.",
    ("Moon", "Scorpio"):     "Right now, the Moon is in Scorpio, deepening the collective emotional atmosphere into intensity, intuition, and hidden currents. Feelings run deep and the need for truth — or privacy — is heightened.",
    ("Moon", "Sagittarius"): "Right now, the Moon is in Sagittarius, lifting the collective mood with optimism and the longing for freedom. The emotional landscape favors expansion and the feeling that something good is just ahead.",
    ("Moon", "Capricorn"):   "Right now, the Moon is in Capricorn, sobering the collective mood with a sense of duty, restraint, and measured purpose. Practicality and the satisfaction of real accomplishment ground the feelings of the day.",
    ("Moon", "Aquarius"):    "Right now, the Moon is in Aquarius, cooling the collective emotional field and turning the mood toward ideas, community, and the feeling of belonging to something larger. The personal gives way to the collective.",
    ("Moon", "Pisces"):      "Right now, the Moon is in Pisces, softening the collective emotional field into empathy, imagination, and the dissolution of ordinary boundaries. The veil is thin and feelings move easily between people.",

    # Mercury
    ("Mercury", "Aries"):       "Right now, Mercury is in Aries, sharpening the collective mind for quick decisions and blunt speech. Thinking is fast and words are pointed — patience for long explanations is short.",
    ("Mercury", "Taurus"):      "Right now, Mercury is in Taurus, slowing collective thought into careful, deliberate processing. The mind is thorough, stubborn, and drawn to ideas with real, practical application.",
    ("Mercury", "Gemini"):      "Right now, Mercury is in Gemini, its home sign, quickening the collective mind into restless curiosity and fluid communication. Ideas multiply, connections spark, and conversations fly.",
    ("Mercury", "Cancer"):      "Right now, Mercury is moving through Cancer, coloring collective thought with feeling, memory, and intuition. Communication tends to be warm and indirect, trusting the heart over the argument.",
    ("Mercury", "Leo"):         "Right now, Mercury is in Leo, infusing collective communication with confidence and creative flair. People speak to be heard and ideas come packaged in stories and performance.",
    ("Mercury", "Virgo"):       "Right now, Mercury is in Virgo, its home sign, sharpening the collective mind to an analytical edge. Precision, critique, and careful observation are the order of the day.",
    ("Mercury", "Libra"):       "Right now, Mercury is in Libra, orienting collective thought toward fairness and the weighing of every perspective. Conversation tends toward the considered and diplomacy is valued over bluntness.",
    ("Mercury", "Scorpio"):     "Right now, Mercury is in Scorpio, turning the collective mind toward investigation and what lies beneath the surface. Thinking is probing and penetrating — not easily satisfied with the obvious.",
    ("Mercury", "Sagittarius"): "Right now, Mercury is in Sagittarius, broadening collective thinking toward the philosophical and globally minded. People speak in principles and the big picture captures more attention than the detail.",
    ("Mercury", "Capricorn"):   "Right now, Mercury is in Capricorn, focusing collective communication on what is useful, concrete, and strategically sound. Words carry more weight when they come with a plan.",
    ("Mercury", "Aquarius"):    "Right now, Mercury is in Aquarius, electrifying the collective mind with originality and the excitement of unconventional thinking. The most interesting ideas are the ones nobody has thought of before.",
    ("Mercury", "Pisces"):      "Right now, Mercury is moving through Pisces, dissolving sharp distinctions in collective thought. Intuition and metaphor are speaking more truly than logic alone.",

    # Venus
    ("Venus", "Aries"):       "Right now, Venus is in Aries, charging attraction and desire with urgency and the thrill of pursuit. Love is impulsive, beauty is bold, and the need for excitement in connection runs high.",
    ("Venus", "Taurus"):      "Right now, Venus is in Taurus, its home sign, deepening the collective experience of pleasure and love into something slow, sensual, and genuinely satisfying. Comfort and quality matter more than novelty.",
    ("Venus", "Gemini"):      "Right now, Venus is in Gemini, lightening the atmosphere of love and connection with wit and curiosity. Mental chemistry is as attractive as physical chemistry and variety is appealing.",
    ("Venus", "Cancer"):      "Right now, Venus is in Cancer, turning collective desire toward tenderness, familiarity, and the sweetness of being truly cared for. Love expresses itself through nurturing and the small acts of daily devotion.",
    ("Venus", "Leo"):         "Right now, Venus is in Leo, amplifying love and attraction with warmth, romance, and the desire to feel adored. Grand gestures and the feeling of being genuinely special are in the air.",
    ("Venus", "Virgo"):       "Right now, Venus is moving through Virgo, expressing love through attentiveness and the quiet satisfaction of helping well. Devotion shows in the details and care is woven into practical life.",
    ("Venus", "Libra"):       "Right now, Venus is in Libra, its home sign, at its most refined. The impulse toward beauty, fairness in relationship, and genuine aesthetic pleasure is at its height.",
    ("Venus", "Scorpio"):     "Right now, Venus is in Scorpio, intensifying desire and love into something magnetic and all-or-nothing. Attraction runs deep and the need for real intimacy — not just surface warmth — is palpable.",
    ("Venus", "Sagittarius"): "Right now, Venus is in Sagittarius, lightening love with optimism and the joy of freedom. Adventure in relationship and the fun of not knowing what comes next are appealing.",
    ("Venus", "Capricorn"):   "Right now, Venus is in Capricorn, sobering desire into something measured, loyal, and built for longevity. Commitment and reliability are more attractive than excitement.",
    ("Venus", "Aquarius"):    "Right now, Venus is in Aquarius, coloring love with friendship and the pleasure of genuine intellectual connection. The most attractive quality in another person might be their originality.",
    ("Venus", "Pisces"):      "Right now, Venus is moving through Pisces, dissolving the boundaries of love into something boundless and romantically tinged. Compassion is beautiful and the longing for transcendent connection is in the air.",

    # Mars
    ("Mars", "Aries"):       "Right now, Mars is in Aries, its home sign, and collective drive is at maximum directness. The impulse to act, compete, and assert is at full strength — patience is thin and initiative is everywhere.",
    ("Mars", "Taurus"):      "Right now, Mars is in Taurus, slowing collective will into a force that is stubborn and impossible to redirect once set. Energy is applied steadily and the drive toward security and tangible results is strong.",
    ("Mars", "Gemini"):      "Right now, Mars is in Gemini, scattering collective energy across many fronts at once. The drive expresses itself through words, debate, and the restless pursuit of mental stimulation.",
    ("Mars", "Cancer"):      "Right now, Mars is in Cancer, turning collective willpower inward and emotionally. Energy fluctuates with mood and the protective instinct is easily activated.",
    ("Mars", "Leo"):         "Right now, Mars is in Leo, channeling collective drive into creative expression and the desire to be recognized. Passion runs high and the impulse to lead and shine is energized.",
    ("Mars", "Virgo"):       "Right now, Mars is moving through Virgo, directing collective energy toward practical improvement and the satisfaction of doing things precisely right. Work and efficiency are where drive most naturally flows.",
    ("Mars", "Libra"):       "Right now, Mars is in Libra, tempering collective action with diplomacy and the need to weigh consequences. The most effective drive is strategic rather than blunt — cooperation beats going it alone.",
    ("Mars", "Scorpio"):     "Right now, Mars is in Scorpio, its traditional home sign, and collective drive runs deep, focused, and with an edge. Nothing is casual — intensity and strategic power are in the air.",
    ("Mars", "Sagittarius"): "Right now, Mars is in Sagittarius, expanding collective energy into enthusiasm and the pursuit of freedom. Drive is toward the horizon — philosophical, restless, and optimistic.",
    ("Mars", "Capricorn"):   "Right now, Mars is in Capricorn, exalted, channeling collective drive into disciplined, long-term effort. Ambition is serious, patience is possible, and energy applied to real goals yields real results.",
    ("Mars", "Aquarius"):    "Right now, Mars is in Aquarius, directing collective energy toward innovation and group action. The most effective force is one that serves a larger cause.",
    ("Mars", "Pisces"):      "Right now, Mars is moving through Pisces, diffusing collective drive into something fluid and compassionate. The best action flows from intuition and the willingness to surrender control.",

    # Jupiter
    ("Jupiter", "Aries"):       "Right now, Jupiter is in Aries, expanding the collective through courage and the willingness to leap before looking. Optimism favors the bold and starting things tends to go well.",
    ("Jupiter", "Taurus"):      "Right now, Jupiter is in Taurus, expanding through material abundance and the pleasure of what endures. Conditions favor building wealth steadily and enjoying genuine comfort.",
    ("Jupiter", "Gemini"):      "Right now, Jupiter is in Gemini, expanding through knowledge, connection, and the restless pursuit of ideas. Learning, networking, and the diversity of experience are the paths to growth.",
    ("Jupiter", "Cancer"):      "Right now, Jupiter is in Cancer, exalted, expanding through emotional depth and the nourishment of real belonging. Conditions are unusually favorable for inner growth and genuine healing.",
    ("Jupiter", "Leo"):         "Right now, Jupiter is in Leo, expanding through creative expression and the joy of being fully alive. The collective is in an expansive, celebratory mood — play, love, and generosity all benefit.",
    ("Jupiter", "Virgo"):       "Right now, Jupiter is moving through Virgo, expanding through careful improvement and the mastery of practical life. Attention to detail and the willingness to serve yield genuine and lasting growth.",
    ("Jupiter", "Libra"):       "Right now, Jupiter is in Libra, expanding through partnership and the wisdom of considering another's perspective seriously. Collaboration and fairness open the most doors.",
    ("Jupiter", "Scorpio"):     "Right now, Jupiter is in Scorpio, expanding through depth and the willingness to go where others won't. What has been hidden tends to become a source of power and growth.",
    ("Jupiter", "Sagittarius"): "Right now, Jupiter is in Sagittarius, its home sign, and the expansive pull toward wisdom, adventure, and the big picture is at its strongest. Optimism is genuine and the world feels full of possibility.",
    ("Jupiter", "Capricorn"):   "Right now, Jupiter is in Capricorn, expanding through discipline and the patient building of real things. Growth is earned rather than given — and what is built now is built to last.",
    ("Jupiter", "Aquarius"):    "Right now, Jupiter is in Aquarius, expanding through collective vision and the sense of belonging to a larger human story. Progress feels possible and the impulse toward positive change is alive.",
    ("Jupiter", "Pisces"):      "Right now, Jupiter is in Pisces, its traditional home sign, expanding through compassion and spiritual grace. The capacity for forgiveness and faith is unusually heightened.",

    # Saturn
    ("Saturn", "Aries"):       "Right now, Saturn is in Aries, bringing the discipline of patience and consequence to the realm of impulsive action. The collective is learning that real courage requires structure, not just fire.",
    ("Saturn", "Taurus"):      "Right now, Saturn is in Taurus, testing the foundations of material security and collective value. Conditions call for building carefully — excess is corrected and shortcuts don't hold.",
    ("Saturn", "Gemini"):      "Right now, Saturn is moving through Gemini, bringing rigor to the way information is gathered and communicated. Idle talk is less satisfying and the collective is being asked to think before speaking.",
    ("Saturn", "Cancer"):      "Right now, Saturn is in Cancer, bringing restriction and maturation to the realm of emotion, home, and family. The collective is developing emotional self-sufficiency — learning to provide for itself what it once expected from others.",
    ("Saturn", "Leo"):         "Right now, Saturn is in Leo, bringing structure and challenge to the realm of creative expression and recognition. Lasting respect is earned through consistent effort, not performance.",
    ("Saturn", "Virgo"):       "Right now, Saturn is moving through Virgo, deepening the collective commitment to craft and the disciplined improvement of daily life. The bar for quality is raised and sloppy work meets its consequences.",
    ("Saturn", "Libra"):       "Right now, Saturn is in Libra, exalted, bringing maturity and responsibility to the realm of relationship and justice. The collective is learning what fair partnership really requires — real commitment, not just goodwill.",
    ("Saturn", "Scorpio"):     "Right now, Saturn is in Scorpio, bringing discipline and consequence to the realm of power and shared resources. Hidden things are restructured, debts come due, and depth is non-negotiable.",
    ("Saturn", "Sagittarius"): "Right now, Saturn is moving through Sagittarius, testing the realm of belief and the search for meaning. The collective is being asked to back its convictions with real understanding.",
    ("Saturn", "Capricorn"):   "Right now, Saturn is in Capricorn, its home sign, fully expressed and uncompromising. The collective standard for responsibility and accountability is at its highest — and the consequences of cutting corners are real.",
    ("Saturn", "Aquarius"):    "Right now, Saturn is in Aquarius, its traditional home sign, bringing sober realism to collective visions and social ideals. Building a better world requires discipline, not just enthusiasm.",
    ("Saturn", "Pisces"):      "Right now, Saturn is moving through Pisces, bringing structure to the realm of spirituality and the dissolution of boundaries. The collective is being asked to navigate uncertainty with clarity rather than escapism.",

    # Uranus (stays ~7 years per sign — use era language)
    ("Uranus", "Aries"):       "Uranus is currently in Aries — for years now, sudden, radical change has been unleashing through individual will, identity, and the pioneer impulse. This is an era of unexpected breakthroughs in how people assert and define themselves.",
    ("Uranus", "Taurus"):      "Uranus is currently in Taurus, and the foundations of material life — economy, land, the body, and collective values — have been disrupted for years. What seemed most stable proves most subject to change.",
    ("Uranus", "Gemini"):      "Uranus is currently in Gemini, revolutionizing communication and the way ideas travel across society. The very structure of how information is shared and minds are changed is being reinvented.",
    ("Uranus", "Cancer"):      "Uranus is currently in Cancer, disrupting the structures of home, family, and what it means to belong. What it means to be nurtured and to feel safe is being fundamentally reimagined.",
    ("Uranus", "Leo"):         "Uranus is currently in Leo, electrifying the realm of creative expression and the desire for recognition. This is an era of surprising breakthroughs in art, self-expression, and what it means to be a unique individual.",
    ("Uranus", "Virgo"):       "Uranus is currently in Virgo, revolutionizing work, health, and the systems of daily life. Sudden innovations in medicine, technology, and the way labor is organized are reshaping ordinary life.",
    ("Uranus", "Libra"):       "Uranus is currently in Libra, disrupting the structures of relationship, law, and social harmony. The rules of partnership and the meaning of justice are being rewritten across this era.",
    ("Uranus", "Scorpio"):     "Uranus is currently in Scorpio, unleashing radical change in the realms of power, sexuality, and what has been kept hidden. This era strips away taboo and forces collective confrontation with the deepest currents of life.",
    ("Uranus", "Sagittarius"): "Uranus is currently in Sagittarius, revolutionizing belief, religion, and the global vision of what is possible. Sudden expansions of worldview and unexpected challenges to established truth define this era.",
    ("Uranus", "Capricorn"):   "Uranus is currently in Capricorn, disrupting established structures of government and authority. Institutions that seemed permanent are revealed as subject to sudden, radical change.",
    ("Uranus", "Aquarius"):    "Uranus is currently in Aquarius, its home sign, maximally expressed. This era is defined by technological and social revolutions that restructure how communities form and what the future looks like.",
    ("Uranus", "Pisces"):      "Uranus is currently in Pisces, disrupting the realm of spirituality and the collective unconscious. Sudden, surprising shifts in spiritual life and the dissolution of old illusions define this period.",

    # Neptune (stays ~14 years per sign — use era language)
    ("Neptune", "Aries"):       "Neptune is currently in Aries, dissolving and spiritualizing the realm of individual will. The collective dream of this era centers on the visionary hero and the belief that pure intention can change the world.",
    ("Neptune", "Taurus"):      "Neptune is currently in Taurus, dissolving the material world into spiritual longing. The collective imagination is drawn to the natural world and the transcendence available in beauty and physical life.",
    ("Neptune", "Gemini"):      "Neptune is currently in Gemini, dissolving the boundaries of thought and communication. Information blurs and the poetic feels as true as the factual during this era.",
    ("Neptune", "Cancer"):      "Neptune is currently in Cancer, dissolving and idealizing home, family, and emotional belonging. The collective dream centers on sanctuary, innocence, and a perfect place of safety and love.",
    ("Neptune", "Leo"):         "Neptune is currently in Leo, dissolving and romanticizing creative expression and the hunger for glory. The collective imagination is drawn to glamour, myth, and the dream of the extraordinary.",
    ("Neptune", "Virgo"):       "Neptune is currently in Virgo, dissolving rigid distinctions in the realm of work and health. The collective dream is of perfect service and healing — and the gap between that ideal and reality is real.",
    ("Neptune", "Libra"):       "Neptune is currently in Libra, dissolving and idealizing love, justice, and partnership. The collective imagination dreams of perfect harmony, and is tested by the complexity of real relationship.",
    ("Neptune", "Scorpio"):     "Neptune is currently in Scorpio, dissolving the boundaries of what is hidden — power, sexuality, and the deep unconscious become soaked with spiritual longing. The taboo becomes mysteriously appealing.",
    ("Neptune", "Sagittarius"): "Neptune is currently in Sagittarius, dissolving and idealizing the realms of religion and global meaning. Spiritual seeking is widespread during this era, though sometimes ungrounded.",
    ("Neptune", "Capricorn"):   "Neptune is currently in Capricorn, dissolving the structures of authority and material achievement. The collective is both disillusioned with and strangely idealistic about power and institutions.",
    ("Neptune", "Aquarius"):    "Neptune is currently in Aquarius, dissolving the boundaries between individuals into the dream of a better world. The collective imagination centers on utopia and the vision of universal human connection.",
    ("Neptune", "Pisces"):      "Neptune is currently in Pisces, its home sign, at the height of its dissolving power. The veil between the visible and invisible is at its thinnest — compassion and spiritual seeking pervade the collective atmosphere.",

    # Pluto (stays 12–30 years per sign — use era language)
    ("Pluto", "Aries"):       "Pluto is currently in Aries, transforming the collective through the destruction and rebirth of individual power and identity. The force of personal assertion is reshaping what it means to be a pioneer in this era.",
    ("Pluto", "Taurus"):      "Pluto is currently in Taurus, dismantling and rebuilding the foundations of material life — land, economics, the body, and the deepest structures of collective value are all being transformed.",
    ("Pluto", "Gemini"):      "Pluto is currently in Gemini, transforming communication and thought at the deepest level. The very media through which minds are shaped is undergoing death and rebirth.",
    ("Pluto", "Cancer"):      "Pluto is currently in Cancer, transforming home, family, and emotional security at the deepest level. The structures of domestic life and nationhood are being dismantled and rebuilt.",
    ("Pluto", "Leo"):         "Pluto is currently in Leo, transforming the realm of individual will and the hunger for recognition. The very idea of what an individual is — their rights and creative potential — is being profoundly remade.",
    ("Pluto", "Virgo"):       "Pluto is currently in Virgo, transforming work, health, craft, and the systems of daily life. Old approaches to medicine, labor, and the environment are being dismantled and rebuilt from the ground up.",
    ("Pluto", "Libra"):       "Pluto is currently in Libra, transforming the realm of relationship and the social contract. The deepest assumptions about partnership, equality, and fairness are being broken down and rebuilt.",
    ("Pluto", "Scorpio"):     "Pluto is currently in Scorpio, its home sign — transformation at its most intense. The collective is forced into direct confrontation with power, sexuality, death, and what has been most deeply suppressed.",
    ("Pluto", "Sagittarius"): "Pluto is currently in Sagittarius, dismantling the collective's relationship to belief, religion, and the search for ultimate meaning. Old certainties dissolve and new worldviews emerge from the wreckage.",
    ("Pluto", "Capricorn"):   "Pluto is currently in Capricorn, transforming structures of power, government, and institutional authority at the deepest level. The systems that organize collective life are being fundamentally remade.",
    ("Pluto", "Aquarius"):    "Pluto is currently in Aquarius, dismantling and transforming collective life — community, technology, and the vision of the future itself are all being radically remade. Power is shifting from institutions to networks.",
    ("Pluto", "Pisces"):      "Pluto is currently in Pisces, transforming the collective relationship to spirituality and the invisible foundations of existence. The deepest confrontation with what lies beyond the material world is underway.",
}


# ── Sky aspects (transit–transit) ────────────────────────────────────────────
# keyed (*sorted([p1, p2]), aspect) — "world weather" language

SKY_ASPECT: dict[tuple[str, str, str], str] = {

    # Sun–Moon
    ("Moon", "Sun", "conjunction"): "It's a New Moon — the Sun and Moon are united in the sky, and the collective is in a moment of reset and fresh beginning. This is a potent shared window for setting intentions as the cycle begins again.",
    ("Moon", "Sun", "sextile"):     "The Sun and Moon are in a cooperative angle in the sky, creating a brief collective harmony between drive and emotional mood. Action and feeling support each other — a good shared window for what requires both clarity and intuition.",
    ("Moon", "Sun", "square"):      "The Sun and Moon are in tension — a quarter Moon moment when the collective will and emotional needs pull against each other. This shared restlessness tends to prompt action through friction.",
    ("Moon", "Sun", "trine"):       "The Sun and Moon are in a flowing relationship in the sky, creating a smooth collective harmony between drive and the emotional atmosphere. Things tend to flow more easily than usual under this sky.",
    ("Moon", "Sun", "opposition"):  "It's a Full Moon — the Sun and Moon face each other across the sky, and the collective is in a moment of peak illumination and emotional intensity. What has been building reaches its height and the pull between opposing needs is strongest.",

    # Sun–Mercury
    ("Mercury", "Sun", "conjunction"): "The Sun and Mercury are conjunct in the sky, amplifying the collective focus on communication, decisions, and the expression of ideas. Conversations and announcements carry unusual weight right now for everyone.",
    ("Mercury", "Sun", "sextile"):     "The Sun and Mercury are cooperating in the sky — the collective will and the mode of thought are aligned. Ideas flow into action with relative ease for people across the board.",
    ("Mercury", "Sun", "square"):      "The Sun and Mercury are in tension in the sky, creating a shared friction between intention and expression. What is meant and what is said may not match — everyone benefits from extra care in communication right now.",
    ("Mercury", "Sun", "trine"):       "The Sun and Mercury are in a harmonious angle in the sky, making collective communication more fluid and purposeful than usual. Ideas are clearly expressed and intentions align with the way things are said.",
    ("Mercury", "Sun", "opposition"):  "The Sun and Mercury are in opposition across the sky, creating a collective tension between the drive forward and the tendency to second-guess or over-communicate. This is a shared moment that favors perspective over output.",

    # Sun–Venus
    ("Sun", "Venus", "conjunction"): "The Sun and Venus are conjunct in the sky, heightening the collective appreciation for beauty, pleasure, and connection. There is a warmer, more generous quality to the shared atmosphere right now.",
    ("Sun", "Venus", "sextile"):     "The Sun and Venus are cooperating in the sky — the collective will and the desire for harmony support each other. Social interactions benefit and creative endeavors tend to go well across the board.",
    ("Sun", "Venus", "square"):      "The Sun and Venus are in tension in the sky, creating a shared friction between drive and desire. The collective impulse to enjoy and the need to accomplish may not agree — balance is called for.",
    ("Sun", "Venus", "trine"):       "The Sun and Venus are in a harmonious relationship in the sky, lifting the collective atmosphere with ease, beauty, and the satisfaction of things working out. A genuinely pleasant quality is in the shared air.",
    ("Sun", "Venus", "opposition"):  "The Sun and Venus are opposed in the sky, creating a collective tension between assertion and accommodation. Relationships may need more active negotiation than usual as drive and desire pull in different directions.",

    # Sun–Mars
    ("Mars", "Sun", "conjunction"): "The Sun and Mars are conjunct in the sky, amplifying the collective drive, initiative, and desire for action. Energy runs high right now for everyone and the shared impulse to begin and compete is strong.",
    ("Mars", "Sun", "sextile"):     "The Sun and Mars are in a cooperative angle — collective will and the engine of action are aligned. Purposeful shared effort tends to go well right now and the direction is clear.",
    ("Mars", "Sun", "square"):      "The Sun and Mars are in tension in the sky, and the collective atmosphere carries a charge of frustration, competition, or impatience. Energy is high but not easily directed — conflict is more likely across the board.",
    ("Mars", "Sun", "trine"):       "The Sun and Mars are in harmony in the sky, making collective initiative and action flow with unusual ease. The shared drive is strong, the direction is clear, and effort tends to yield results.",
    ("Mars", "Sun", "opposition"):  "The Sun and Mars are opposed in the sky, and the collective energy is charged with a dynamic tension between intention and force. This can mean productive tension or outright conflict — the difference is in how the shared energy is channeled.",

    # Sun–Jupiter
    ("Jupiter", "Sun", "conjunction"): "The Sun and Jupiter are conjunct in the sky, expanding the collective sense of possibility and optimism. This is one of the more buoyant shared sky moments of the year — confidence runs high and generosity is in the air.",
    ("Jupiter", "Sun", "sextile"):     "The Sun and Jupiter are cooperating in the sky, supporting a collective mood of measured optimism and opportunity. Doors tend to open more easily right now and the shared sense that things will work out is reasonable.",
    ("Jupiter", "Sun", "square"):      "The Sun and Jupiter are in tension in the sky, creating a collective tendency toward overreach, overconfidence, or excess. Right now, the gap between shared ambition and reality deserves attention.",
    ("Jupiter", "Sun", "trine"):       "The Sun and Jupiter are in harmony in the sky — one of the more genuinely positive shared sky moments available. Optimism, luck, and the sense of forward movement are in the collective air.",
    ("Jupiter", "Sun", "opposition"):  "The Sun and Jupiter are opposed in the sky, creating a collective tension between modest effort and grand expectation. Enthusiasm and overconfidence may need to be checked against practical reality right now.",

    # Sun–Saturn
    ("Saturn", "Sun", "conjunction"): "The Sun and Saturn are conjunct in the sky, sobering the collective mood with a sense of responsibility and the weight of what needs to be done. The shared atmosphere carries a quality of seriousness and the call to work.",
    ("Saturn", "Sun", "sextile"):     "The Sun and Saturn are cooperating in the sky, supporting collective discipline and patient effort. Structure helps right now — careful, methodical work tends to yield lasting results across the board.",
    ("Saturn", "Sun", "square"):      "The Sun and Saturn are in tension in the sky, creating a collective atmosphere of friction, delay, and the sense that things require more effort than expected. Shared patience and persistence are the appropriate response.",
    ("Saturn", "Sun", "trine"):       "The Sun and Saturn are in harmony in the sky, supporting collective discipline, clarity, and the satisfaction of doing things properly. Effort applied now tends to build lasting results for everyone.",
    ("Saturn", "Sun", "opposition"):  "The Sun and Saturn are opposed in the sky, and the collective is navigating a tension between creative drive and the limits of reality. Shared ambitions are being tested against what is actually achievable.",

    # Sun–Uranus
    ("Sun", "Uranus", "conjunction"): "The Sun and Uranus are conjunct in the sky, sending a sudden electric charge through the collective. The unexpected is more likely than usual for everyone — breakthroughs, disruptions, and the shock of the new are in the shared air.",
    ("Sun", "Uranus", "sextile"):     "The Sun and Uranus are cooperating in the sky, supporting the collective with a current of creative originality. The unusual approach tends to work better than the conventional one right now across the board.",
    ("Sun", "Uranus", "square"):      "The Sun and Uranus are in tension in the sky, creating a collective atmosphere of disruption and restlessness. The unexpected is more likely for everyone and flexibility is essential.",
    ("Sun", "Uranus", "trine"):       "The Sun and Uranus are in harmony in the sky, bringing a refreshing collective current of originality and willingness to change. The new and unconventional are welcomed and things can shift in surprisingly positive directions.",
    ("Sun", "Uranus", "opposition"):  "The Sun and Uranus are opposed in the sky, and the collective is navigating a tension between the established order and the force of disruption. What is comfortable is being challenged by what is new — for everyone.",

    # Sun–Neptune
    ("Neptune", "Sun", "conjunction"): "The Sun and Neptune are conjunct in the sky, dissolving the boundaries of the collective will into something more spiritual, idealistic, or confused. Clarity may be harder to find right now but inspiration runs high for everyone.",
    ("Neptune", "Sun", "sextile"):     "The Sun and Neptune are cooperating in the sky, lending collective action a gentle idealism and spiritual sensitivity. Imagination and intuition support practical effort rather than undermining it.",
    ("Neptune", "Sun", "square"):      "The Sun and Neptune are in tension in the sky, creating a collective atmosphere of confusion and the difficulty of distinguishing what is real from what is desired. Clarity of shared intention benefits from extra effort right now.",
    ("Neptune", "Sun", "trine"):       "The Sun and Neptune are in harmony in the sky, bringing a collective quality of inspiration, compassion, and the ability to see beyond the ordinary. Imagination and reality cooperate in an unusual and productive shared way.",
    ("Neptune", "Sun", "opposition"):  "The Sun and Neptune are opposed in the sky, and the collective is navigating a tension between clear intention and the dissolving force of illusion. What is real and what is wished-for may be difficult to tell apart right now.",

    # Sun–Pluto
    ("Pluto", "Sun", "conjunction"): "The Sun and Pluto are conjunct in the sky, intensifying the collective atmosphere with power, depth, and the force of transformation. What is hidden tends to surface right now and the shared desire for fundamental change is strong.",
    ("Pluto", "Sun", "sextile"):     "The Sun and Pluto are cooperating in the sky, supporting collective depth and the productive application of transformative power. Going deeper tends to be more rewarding than staying on the surface right now.",
    ("Pluto", "Sun", "square"):      "The Sun and Pluto are in tension in the sky, creating a collective atmosphere of intensity and power. What is hidden tends to force its way to the surface in disruptive ways — for everyone.",
    ("Pluto", "Sun", "trine"):       "The Sun and Pluto are in harmony in the sky, supporting collective depth, renewal, and the productive force of genuine change. The power to transform is available and tends to be used constructively.",
    ("Pluto", "Sun", "opposition"):  "The Sun and Pluto are opposed in the sky, and the collective is navigating a sharp tension between individual will and the force of power and transformation. What is deeply hidden tends to confront what is openly expressed.",

    # Moon–Mercury
    ("Mercury", "Moon", "conjunction"): "The Moon and Mercury are conjunct in the sky, aligning the collective emotional mood with the impulse to communicate and think. Feelings want to be named right now and conversations tend to get personal.",
    ("Mercury", "Moon", "sextile"):     "The Moon and Mercury are cooperating in the sky, supporting a collective ease between feeling and expression. Emotional intelligence and clear thinking reinforce each other right now.",
    ("Mercury", "Moon", "square"):      "The Moon and Mercury are in tension in the sky, creating a collective friction between how things feel and how they are being communicated. Misunderstandings are more likely — feelings and logic may not agree.",
    ("Mercury", "Moon", "trine"):       "The Moon and Mercury are in harmony in the sky, making collective communication warmer, more empathic, and emotionally intelligent than usual. It is easier to say what you mean and mean what you say.",
    ("Mercury", "Moon", "opposition"):  "The Moon and Mercury are opposed in the sky, and the collective is navigating a tension between emotional reaction and rational thought. The head and the heart may be telling different stories right now.",

    # Moon–Venus
    ("Moon", "Venus", "conjunction"): "The Moon and Venus are conjunct in the sky, heightening the collective mood with warmth, beauty, and the pleasure of connection. The shared emotional atmosphere is particularly receptive to kindness and aesthetic delight.",
    ("Moon", "Venus", "sextile"):     "The Moon and Venus are cooperating in the sky, creating a pleasant collective harmony between feeling and the desire for beauty and love. Social interactions tend to be warmer and more satisfying than usual.",
    ("Moon", "Venus", "square"):      "The Moon and Venus are in tension in the sky, creating a collective friction between emotional needs and the desire for harmony. What feels good and what is emotionally necessary may not agree right now.",
    ("Moon", "Venus", "trine"):       "The Moon and Venus are in harmony in the sky, lifting the collective emotional atmosphere with beauty, affection, and the quiet pleasure of things going well. A genuinely pleasant quality is in the shared air.",
    ("Moon", "Venus", "opposition"):  "The Moon and Venus are opposed in the sky, and the collective is navigating a tension between emotional needs and the desire for pleasure or relational harmony. Getting what you want may require acknowledging what you actually feel.",

    # Moon–Mars
    ("Mars", "Moon", "conjunction"): "The Moon and Mars are conjunct in the sky, charging the collective emotional field with urgency and the impulse to act on feeling immediately. Emotional reactions are faster and sharper than usual across the board.",
    ("Mars", "Moon", "sextile"):     "The Moon and Mars are cooperating in the sky, lending the collective emotional field a productive current of assertive energy. Action motivated by feeling tends to go in the right direction right now.",
    ("Mars", "Moon", "square"):      "The Moon and Mars are in tension in the sky, and the collective emotional atmosphere is charged with impatience or the urge to react before reflecting. Pausing before acting on strong feelings is wise for everyone right now.",
    ("Mars", "Moon", "trine"):       "The Moon and Mars are in harmony in the sky, supporting collective emotional assertiveness and the courage to act on feeling. The emotional drive and the will to act are more aligned than usual.",
    ("Mars", "Moon", "opposition"):  "The Moon and Mars are opposed in the sky, and the collective is navigating a tension between emotional sensitivity and reactive force. The impulse to strike out emotionally may need to be met with conscious choice.",

    # Moon–Jupiter
    ("Jupiter", "Moon", "conjunction"): "The Moon and Jupiter are conjunct in the sky, expanding the collective emotional field with optimism, generosity, and a buoyant quality. Feelings run large right now and the shared mood tends toward warmth and abundance.",
    ("Jupiter", "Moon", "sextile"):     "The Moon and Jupiter are cooperating in the sky, supporting a collective mood of emotional ease and measured good fortune. The emotional landscape feels a little more spacious than usual for everyone.",
    ("Jupiter", "Moon", "square"):      "The Moon and Jupiter are in tension in the sky, and the collective emotional field may be running a little large — mood swings toward excess or overdoing it. Emotional moderation benefits from attention right now.",
    ("Jupiter", "Moon", "trine"):       "The Moon and Jupiter are in harmony in the sky, and the collective emotional mood is genuinely warm, generous, and expansive. The good feelings tend to spread and the sense of possibility runs high.",
    ("Jupiter", "Moon", "opposition"):  "The Moon and Jupiter are opposed in the sky, and the collective is navigating a tension between emotional needs and the expansive pull of something larger. Feelings may run bigger than circumstances actually call for.",

    # Moon–Saturn
    ("Moon", "Saturn", "conjunction"): "The Moon and Saturn are conjunct in the sky, and the collective emotional field carries a weight of responsibility, restraint, or loneliness. Feelings are more sober and the shared inner landscape is more serious than usual.",
    ("Moon", "Saturn", "sextile"):     "The Moon and Saturn are cooperating in the sky, supporting a collective mood of emotional maturity and realistic assessment. Feelings are grounded rather than runaway and practical care is easier than usual.",
    ("Moon", "Saturn", "square"):      "The Moon and Saturn are in tension in the sky, and the collective emotional atmosphere is weighted with frustration or the sense that what is felt cannot be easily expressed. Emotional patience is tested for everyone right now.",
    ("Moon", "Saturn", "trine"):       "The Moon and Saturn are in harmony in the sky, supporting collective emotional groundedness and the quiet satisfaction of emotional maturity. Feelings are useful guides rather than unruly passengers.",
    ("Moon", "Saturn", "opposition"):  "The Moon and Saturn are opposed in the sky, and the collective is navigating a tension between emotional warmth and the cold clarity of limitation. What is felt and what is possible may not line up easily right now.",

    # Moon–Uranus
    ("Moon", "Uranus", "conjunction"): "The Moon and Uranus are conjunct in the sky, sending an electrical charge through the collective emotional field. Feelings shift without warning, the unexpected is more likely, and the shared mood can change in an instant.",
    ("Moon", "Uranus", "sextile"):     "The Moon and Uranus are cooperating in the sky, lending the collective emotional field a refreshing current of openness. The unexpected tends to be welcome rather than disruptive right now.",
    ("Moon", "Uranus", "square"):      "The Moon and Uranus are in tension in the sky, and the collective emotional atmosphere is restless and prone to sudden shifts. What feels stable may not be — flexibility is the best shared protection right now.",
    ("Moon", "Uranus", "trine"):       "The Moon and Uranus are in harmony in the sky, bringing a collective emotional lightness and openness to change. Novelty and the unexpected are emotionally welcome rather than threatening.",
    ("Moon", "Uranus", "opposition"):  "The Moon and Uranus are opposed in the sky, and the collective is navigating a tension between the need for emotional security and the force of disruption. What is most familiar may suddenly feel less reliable.",

    # Moon–Neptune
    ("Moon", "Neptune", "conjunction"): "The Moon and Neptune are conjunct in the sky, dissolving the boundaries of the collective emotional field into something dreamy and porous. Feelings are amplified and the line between one person's emotions and another's is thin.",
    ("Moon", "Neptune", "sextile"):     "The Moon and Neptune are cooperating in the sky, lending the collective emotional field a gentle spirituality and imaginative depth. Compassion flows easily and the inner life is more richly available than usual.",
    ("Moon", "Neptune", "square"):      "The Moon and Neptune are in tension in the sky, and the collective emotional atmosphere is blurred by confusion or idealism. Emotional clarity may take extra effort right now — more is being felt than is actually there.",
    ("Moon", "Neptune", "trine"):       "The Moon and Neptune are in harmony in the sky, deepening the collective emotional atmosphere with empathy, intuition, and a soft spiritual sensitivity. The emotional world and the invisible world feel unusually close.",
    ("Moon", "Neptune", "opposition"):  "The Moon and Neptune are opposed in the sky, and the collective is navigating a tension between what is emotionally real and what is dreamed or imagined. The line between feeling and fantasy may need watching.",

    # Moon–Pluto
    ("Moon", "Pluto", "conjunction"): "The Moon and Pluto are conjunct in the sky, intensifying the collective emotional field into something deep and powerful. Feelings run to the bottom right now and what is usually kept below the surface tends to rise.",
    ("Moon", "Pluto", "sextile"):     "The Moon and Pluto are cooperating in the sky, supporting a collective emotional depth and the productive processing of difficult material. The capacity to feel through something rather than around it is available right now.",
    ("Moon", "Pluto", "square"):      "The Moon and Pluto are in tension in the sky, and the collective emotional atmosphere carries a charge of intensity or buried feeling surfacing. Emotional reactions can run deeper and more compulsive than expected.",
    ("Moon", "Pluto", "trine"):       "The Moon and Pluto are in harmony in the sky, deepening the collective emotional life in a productive way. The capacity for emotional honesty and genuine transformation is available and can be trusted.",
    ("Moon", "Pluto", "opposition"):  "The Moon and Pluto are opposed in the sky, and the collective is navigating a tension between everyday feeling and the force of deep, transformative emotional content. What has been buried is pressing to the surface.",

    # Mercury–Venus
    ("Mercury", "Venus", "conjunction"): "Mercury and Venus are conjunct in the sky, aligning the collective mind with the desire for beauty, harmony, and relational ease. Communication is more gracious and socially intelligent than usual right now.",
    ("Mercury", "Venus", "sextile"):     "Mercury and Venus are cooperating in the sky, lending collective communication a quality of warmth and aesthetic sensitivity. Words tend to come out more pleasantly and relationships benefit.",
    ("Mercury", "Venus", "square"):      "Mercury and Venus are in tension in the sky, creating a collective friction between what is thought and what is desired. Honest communication and the impulse to keep things pleasant may not agree right now.",
    ("Mercury", "Venus", "trine"):       "Mercury and Venus are in harmony in the sky, making collective communication particularly warm and graceful. The social and intellectual qualities of conversation reinforce each other right now.",
    ("Mercury", "Venus", "opposition"):  "Mercury and Venus are opposed in the sky, and the collective is navigating a tension between honest communication and the desire to maintain harmony. Saying what is true and keeping things pleasant may require deliberate balance.",

    # Mercury–Mars
    ("Mars", "Mercury", "conjunction"): "Mercury and Mars are conjunct in the sky, charging the collective mind with assertiveness and speed. Conversations are faster and sharper right now — the tongue can cut and debates run hot.",
    ("Mars", "Mercury", "sextile"):     "Mercury and Mars are cooperating in the sky, lending collective communication a productive directness and mental energy. The drive to communicate and the content of what is communicated are well aligned.",
    ("Mars", "Mercury", "square"):      "Mercury and Mars are in tension in the sky, and the collective atmosphere carries a charge of debate or communication that moves faster than wisdom. Thinking before speaking is especially valuable for everyone right now.",
    ("Mars", "Mercury", "trine"):       "Mercury and Mars are in harmony in the sky, making collective communication both direct and effective. The mind is sharp, words come quickly, and the drive behind communication serves a real purpose.",
    ("Mars", "Mercury", "opposition"):  "Mercury and Mars are opposed in the sky, and the collective is navigating a tension between careful thought and the force of assertion. The impulse to argue or defend may be louder than the impulse to understand.",

    # Mercury–Jupiter
    ("Jupiter", "Mercury", "conjunction"): "Mercury and Jupiter are conjunct in the sky, expanding the collective mind toward the philosophical and visionary. Thinking is big right now and the shared impulse to communicate ideas widely is strong.",
    ("Jupiter", "Mercury", "sextile"):     "Mercury and Jupiter are cooperating in the sky, supporting a collective mood of curious optimism and the joy of learning. The mind reaches naturally toward the broad and meaningful.",
    ("Jupiter", "Mercury", "square"):      "Mercury and Jupiter are in tension in the sky, and the collective mind may be tending toward overconfidence or jumping to conclusions. Checking the details before announcing the vision is wise right now.",
    ("Jupiter", "Mercury", "trine"):       "Mercury and Jupiter are in harmony in the sky, and the collective mind is in a state of generous, broad-ranging intelligence. Ideas expand naturally and communication is both fluent and meaningful.",
    ("Jupiter", "Mercury", "opposition"):  "Mercury and Jupiter are opposed in the sky, and the collective is navigating a tension between careful analysis and the pull toward grand conclusions. Enthusiasm for the big picture may outrun the evidence.",

    # Mercury–Saturn
    ("Mercury", "Saturn", "conjunction"): "Mercury and Saturn are conjunct in the sky, bringing a sobering quality to the collective mind. Thought is careful and serious right now — more preoccupied with what could go wrong than with what might go right.",
    ("Mercury", "Saturn", "sextile"):     "Mercury and Saturn are cooperating in the sky, supporting a collective discipline of mind and the patient application of thought to real problems. Careful analysis and measured communication tend to yield results.",
    ("Mercury", "Saturn", "square"):      "Mercury and Saturn are in tension in the sky, and the collective mind is working against a headwind of doubt or restriction. Communication benefits from patience and precision right now.",
    ("Mercury", "Saturn", "trine"):       "Mercury and Saturn are in harmony in the sky, lending collective thinking a quality of discipline and precision. The mind is a reliable tool and communication is clear and well-structured right now.",
    ("Mercury", "Saturn", "opposition"):  "Mercury and Saturn are opposed in the sky, and the collective is navigating a tension between the flow of ideas and the weight of limitation. Thought may be slowed by doubt or the feeling that nothing is good enough.",

    # Mercury–Uranus
    ("Mercury", "Uranus", "conjunction"): "Mercury and Uranus are conjunct in the sky, electrifying the collective mind with originality and sudden insight. Ideas arrive fast, from unexpected directions, and may be genuinely brilliant right now.",
    ("Mercury", "Uranus", "sextile"):     "Mercury and Uranus are cooperating in the sky, supporting a collective mood of intellectual openness and creative originality. The unusual approach tends to work and new ideas find a receptive audience.",
    ("Mercury", "Uranus", "square"):      "Mercury and Uranus are in tension in the sky, and the collective mind is restless and prone to sudden reversals. Ideas may arrive faster than they can be properly evaluated right now.",
    ("Mercury", "Uranus", "trine"):       "Mercury and Uranus are in harmony in the sky, making the collective mind unusually sharp, original, and open to what has not been thought before. The breakthrough idea is more available than usual.",
    ("Mercury", "Uranus", "opposition"):  "Mercury and Uranus are opposed in the sky, and the collective is navigating a tension between conventional thought and the force of radical new ideas. Established wisdom is being challenged from an unexpected angle.",

    # Mercury–Neptune
    ("Mercury", "Neptune", "conjunction"): "Mercury and Neptune are conjunct in the sky, dissolving the boundaries of the collective mind into something imaginative and sometimes hard to pin down. Inspiration is high but clarity may be elusive for everyone right now.",
    ("Mercury", "Neptune", "sextile"):     "Mercury and Neptune are cooperating in the sky, lending collective thought a gentle imaginative depth. Intuition and logical thought support rather than undermine each other right now.",
    ("Mercury", "Neptune", "square"):      "Mercury and Neptune are in tension in the sky, and the collective mind is susceptible to confusion or the blurring of fact and fantasy. Extra care with what can actually be verified is wise right now.",
    ("Mercury", "Neptune", "trine"):       "Mercury and Neptune are in harmony in the sky, and the collective mind has access to a beautiful blend of imagination and intuition. The poetic and the precise can coexist and inspire each other.",
    ("Mercury", "Neptune", "opposition"):  "Mercury and Neptune are opposed in the sky, and the collective is navigating a tension between clear thought and the dissolving force of imagination. What is real and what is hoped-for may be genuinely hard to tell apart.",

    # Mercury–Pluto
    ("Mercury", "Pluto", "conjunction"): "Mercury and Pluto are conjunct in the sky, turning the collective mind toward intensity and the desire to get to the bottom of things. Thought is penetrating and conversations tend to go deep right now.",
    ("Mercury", "Pluto", "sextile"):     "Mercury and Pluto are cooperating in the sky, supporting a collective capacity for deep thought and the productive exploration of difficult material. The mind is a useful tool for transformation right now.",
    ("Mercury", "Pluto", "square"):      "Mercury and Pluto are in tension in the sky, and the collective mind is pressing against something powerful and resistant. Communication may carry an edge of compulsion — what is said has more weight than usual.",
    ("Mercury", "Pluto", "trine"):       "Mercury and Pluto are in harmony in the sky, giving the collective mind access to depth and penetrating analysis. Profound shared insight is available right now.",
    ("Mercury", "Pluto", "opposition"):  "Mercury and Pluto are opposed in the sky, and the collective is navigating a tension between what is spoken and the deep, often unspoken power dynamics that shape it. The truth beneath the surface is pressing hard.",

    # Venus–Mars
    ("Mars", "Venus", "conjunction"): "Venus and Mars are conjunct in the sky, and the collective atmosphere hums with desire, attraction, and the creative tension between beauty and drive. Love and action, pleasure and initiative are unusually unified right now.",
    ("Mars", "Venus", "sextile"):     "Venus and Mars are cooperating in the sky, creating a collective harmony between desire and action. Attraction and initiative reinforce each other right now — what is wanted and the energy to pursue it are aligned.",
    ("Mars", "Venus", "square"):      "Venus and Mars are in tension in the sky, and the collective atmosphere carries a charge of desire frustrated by urgency, or beauty challenged by force. What is wanted and how it is pursued may not agree.",
    ("Mars", "Venus", "trine"):       "Venus and Mars are in harmony in the sky, and the collective atmosphere is charged with a productive, creative energy between attraction and action. Desire and the drive to pursue it are in an unusually satisfying relationship.",
    ("Mars", "Venus", "opposition"):  "Venus and Mars are opposed in the sky, and the collective is navigating the classic tension between attraction and assertion. This sky weather tends to be charged with desire and the complexity of wanting.",

    # Venus–Jupiter
    ("Jupiter", "Venus", "conjunction"): "Venus and Jupiter are conjunct in the sky — one of the more genuinely pleasurable shared moments available. The collective atmosphere is warm, generous, and open to beauty, abundance, and the goodness of being alive.",
    ("Jupiter", "Venus", "sextile"):     "Venus and Jupiter are cooperating in the sky, supporting a collective mood of easy pleasure and measured good fortune. Social life, creative endeavors, and the simple enjoyment of things tend to go well.",
    ("Jupiter", "Venus", "square"):      "Venus and Jupiter are in tension in the sky, and the collective tendency toward excess or overindulgence is heightened. The desire for pleasure is at risk of outrunning good judgment for everyone right now.",
    ("Jupiter", "Venus", "trine"):       "Venus and Jupiter are in harmony in the sky, and the collective atmosphere is unusually warm, abundant, and open to beauty and good fortune. This is one of the more genuinely pleasant shared sky moments available.",
    ("Jupiter", "Venus", "opposition"):  "Venus and Jupiter are opposed in the sky, and the collective is navigating a tension between the desire for pleasure and the pull toward something larger. Moderation and generosity may need to be consciously balanced.",

    # Venus–Saturn
    ("Saturn", "Venus", "conjunction"): "Venus and Saturn are conjunct in the sky, sobering the collective atmosphere around love and pleasure. The shared air carries a quality of measured commitment, emotional restraint, or the weight of relational responsibility.",
    ("Saturn", "Venus", "sextile"):     "Venus and Saturn are cooperating in the sky, supporting a collective mood of emotional maturity and the quiet satisfaction of love expressed through loyalty. Commitment serves relationships better than grand gestures right now.",
    ("Saturn", "Venus", "square"):      "Venus and Saturn are in tension in the sky, and the collective is navigating a friction between the desire for warmth and beauty and the reality of limitation. Love may feel harder to access right now.",
    ("Saturn", "Venus", "trine"):       "Venus and Saturn are in harmony in the sky, supporting collective love and beauty with a grounding quality of endurance. What is beautiful tends also to be lasting right now.",
    ("Saturn", "Venus", "opposition"):  "Venus and Saturn are opposed in the sky, and the collective is navigating a tension between the longing for love and the weight of obligation. The desire for warmth is being tested against what is actually sustainable.",

    # Venus–Uranus
    ("Uranus", "Venus", "conjunction"): "Venus and Uranus are conjunct in the sky, sending an electrical charge through the collective experience of love and attraction. The unexpected is welcome in relationships and the unusual is appealing right now.",
    ("Uranus", "Venus", "sextile"):     "Venus and Uranus are cooperating in the sky, supporting a collective openness to unexpected beauty and unconventional love. Originality in relationships and aesthetics is rewarded right now.",
    ("Uranus", "Venus", "square"):      "Venus and Uranus are in tension in the sky, and the collective experience of love and attraction is disrupted by the unexpected. Relationships may feel unstable or in need of more freedom than usual.",
    ("Uranus", "Venus", "trine"):       "Venus and Uranus are in harmony in the sky, bringing a collective openness to surprising beauty and unconventional attraction. Love and originality cooperate rather than conflict right now.",
    ("Uranus", "Venus", "opposition"):  "Venus and Uranus are opposed in the sky, and the collective is navigating a tension between the desire for stable love and the force of sudden change. Relationships may need more room to breathe right now.",

    # Venus–Neptune
    ("Neptune", "Venus", "conjunction"): "Venus and Neptune are conjunct in the sky, dissolving the collective experience of love into something idealized, transcendent, and beautifully blurred. The romantic, the spiritual, and the aesthetic are unusually accessible right now.",
    ("Neptune", "Venus", "sextile"):     "Venus and Neptune are cooperating in the sky, lending the collective experience of love a gentle spiritual depth. Compassion and creativity enrich relationships rather than confusing them right now.",
    ("Neptune", "Venus", "square"):      "Venus and Neptune are in tension in the sky, and the collective experience of love is clouded by idealization. Romantic clarity benefits from extra care — the gap between who someone is and who we wish they were is wide right now.",
    ("Neptune", "Venus", "trine"):       "Venus and Neptune are in harmony in the sky, and the collective experience of love and connection is infused with a gentle spiritual grace. Compassion, imagination, and aesthetic sensitivity flow together.",
    ("Neptune", "Venus", "opposition"):  "Venus and Neptune are opposed in the sky, and the collective is navigating a tension between the desire for real love and the pull of idealization. The gap between feeling and fantasy deserves attention right now.",

    # Venus–Pluto
    ("Pluto", "Venus", "conjunction"): "Venus and Pluto are conjunct in the sky, intensifying the collective experience of love and desire into something powerful and transformative. Attraction runs deep and what is wanted can become an obsession right now.",
    ("Pluto", "Venus", "sextile"):     "Venus and Pluto are cooperating in the sky, supporting a collective depth in love and a productive encounter with the more transformative dimensions of desire. Going deeper in relationships tends to reward right now.",
    ("Pluto", "Venus", "square"):      "Venus and Pluto are in tension in the sky, and the collective experience of love and desire is charged with intensity and the difficulty of control. What is wanted may be pursued with more force than is healthy.",
    ("Pluto", "Venus", "trine"):       "Venus and Pluto are in harmony in the sky, deepening the collective experience of love into something genuinely transformative. Desire and depth cooperate and the most meaningful connections are available.",
    ("Pluto", "Venus", "opposition"):  "Venus and Pluto are opposed in the sky, and the collective is navigating a tension between the desire for love and the force of compulsion or the need to control what is most desired.",

    # Mars–Jupiter
    ("Jupiter", "Mars", "conjunction"): "Mars and Jupiter are conjunct in the sky, amplifying the collective with a surge of energy, ambition, and the appetite for bold action. The shared drive is large and optimism fuels it — a good collective moment for brave initiatives.",
    ("Jupiter", "Mars", "sextile"):     "Mars and Jupiter are cooperating in the sky, aligning collective drive with the expansive pull of opportunity. Action taken with confidence tends to open rather than close doors right now.",
    ("Jupiter", "Mars", "square"):      "Mars and Jupiter are in tension in the sky, and the collective appetite for action may be overreaching. The impulse to act big outpaces the wisdom to act carefully — ambition benefits from shared restraint right now.",
    ("Jupiter", "Mars", "trine"):       "Mars and Jupiter are in harmony in the sky, and the collective is moving through a genuinely expansive moment of directed energy. Bold moves tend to work out and momentum builds naturally.",
    ("Jupiter", "Mars", "opposition"):  "Mars and Jupiter are opposed in the sky, and the collective is navigating a tension between the drive to act and the pull of grand expectation. Energy is high but the risk of shared overextension is real.",

    # Mars–Saturn
    ("Mars", "Saturn", "conjunction"): "Mars and Saturn are conjunct in the sky, creating a collective sense of energy meeting resistance. The drive to act is slowed by structure right now — but what is built through this friction tends to be solid.",
    ("Mars", "Saturn", "sextile"):     "Mars and Saturn are cooperating in the sky, supporting a collective ability to apply sustained, disciplined effort. Willpower and structure work together and patient action yields reliable results.",
    ("Mars", "Saturn", "square"):      "Mars and Saturn are in tension in the sky, and the collective atmosphere carries a charge of frustration or blocked energy. The shared impulse to act collides with limit right now.",
    ("Mars", "Saturn", "trine"):       "Mars and Saturn are in harmony in the sky, and the collective is in a moment of disciplined, effective action. Effort is sustained, direction is clear, and the drive to accomplish meets a structure that supports it.",
    ("Mars", "Saturn", "opposition"):  "Mars and Saturn are opposed in the sky, and the collective is navigating a sharp tension between the desire to move forward and the weight of resistance. Force meets limit right now.",

    # Mars–Uranus
    ("Mars", "Uranus", "conjunction"): "Mars and Uranus are conjunct in the sky, and the collective atmosphere is electrically charged with sudden action and the impulse to break from what is established. The unexpected is more likely — and it arrives fast.",
    ("Mars", "Uranus", "sextile"):     "Mars and Uranus are cooperating in the sky, supporting a collective energy of innovative action. The unconventional approach works right now and the drive to do something new is well supported.",
    ("Mars", "Uranus", "square"):      "Mars and Uranus are in tension in the sky, and the collective atmosphere carries a charge of impulsive action and sudden disruption. The unexpected tends to arrive with force right now.",
    ("Mars", "Uranus", "trine"):       "Mars and Uranus are in harmony in the sky, and the collective is in a moment of inspired, original action. The drive to do something genuinely new is well supported and breakthroughs are available to those who move.",
    ("Mars", "Uranus", "opposition"):  "Mars and Uranus are opposed in the sky, and the collective is navigating a high-voltage tension between action and disruption. The force of the unexpected collides with the desire to move forward — flexibility is essential.",

    # Mars–Neptune
    ("Mars", "Neptune", "conjunction"): "Mars and Neptune are conjunct in the sky, dissolving the collective drive into something inspired, confused, or spiritually motivated. Action is infused with idealism but the direction may be harder than usual to pin down.",
    ("Mars", "Neptune", "sextile"):     "Mars and Neptune are cooperating in the sky, supporting a collective capacity to act from intuition and to pursue ideals without being paralyzed by them. The drive and the dream support each other right now.",
    ("Mars", "Neptune", "square"):      "Mars and Neptune are in tension in the sky, and the collective drive is clouded by confusion or misdirection. Action motivated by illusion tends to go sideways right now.",
    ("Mars", "Neptune", "trine"):       "Mars and Neptune are in harmony in the sky, and the collective is in a moment of inspired, compassionate action. The drive is infused with spiritual sensitivity and idealistic action finds its most productive expression.",
    ("Mars", "Neptune", "opposition"):  "Mars and Neptune are opposed in the sky, and the collective is navigating a tension between the will to act and the dissolving force of illusion. Misdirected effort is a real shared risk right now.",

    # Mars–Pluto
    ("Mars", "Pluto", "conjunction"): "Mars and Pluto are conjunct in the sky, and the collective atmosphere is charged with a deep, intense, and sometimes explosive force. The desire for power and transformation is at its most concentrated and the potential for both breakthrough and conflict is high.",
    ("Mars", "Pluto", "sextile"):     "Mars and Pluto are cooperating in the sky, supporting a collective depth of drive and the productive application of transformative power. Effort that cuts to the root tends to be unusually effective right now.",
    ("Mars", "Pluto", "square"):      "Mars and Pluto are in tension in the sky, and the collective atmosphere carries a charge of power struggle and the clash of wills at depth. Force meets deep resistance and conflict can run to extremes right now.",
    ("Mars", "Pluto", "trine"):       "Mars and Pluto are in harmony in the sky, and the collective is in a moment of deep, focused, transformative action. The drive that comes from the root is most available and most effective.",
    ("Mars", "Pluto", "opposition"):  "Mars and Pluto are opposed in the sky, and the collective is navigating an intense tension between assertion and the deeper forces of power. Will collides with what lies beneath — and the result is rarely subtle.",

    # Jupiter–Saturn
    ("Jupiter", "Saturn", "conjunction"): "Jupiter and Saturn are conjunct in the sky — a rare Great Conjunction. The collective is at a threshold between expansion and consolidation, and the structures of a new era are being set. The tension between growth and limits is shaping the world.",
    ("Jupiter", "Saturn", "sextile"):     "Jupiter and Saturn are cooperating in the sky, supporting a collective ability to balance expansion with structure. Growth is possible without overreach and discipline without stagnation — a shared moment of productive balance.",
    ("Jupiter", "Saturn", "square"):      "Jupiter and Saturn are in tension in the sky, and the collective is navigating a friction between the desire to grow and the reality of what limits that growth. The gap between shared ambition and practicality is a social challenge right now.",
    ("Jupiter", "Saturn", "trine"):       "Jupiter and Saturn are in harmony in the sky, and the collective is in a period of sustainable growth — expansion backed by structure, ambition grounded in reality. Long-term projects benefit from the shared conditions.",
    ("Jupiter", "Saturn", "opposition"):  "Jupiter and Saturn are opposed in the sky, and the collective is navigating a major tension between growth and consolidation. The competing demands of expansion and discipline are shaping public life in significant ways.",

    # Jupiter–Uranus
    ("Jupiter", "Uranus", "conjunction"): "Jupiter and Uranus are conjunct in the sky — a significant moment of collective breakthrough and sudden expansion. Unexpected developments are reshaping what is possible, and the sense of sudden liberation is in the shared air.",
    ("Jupiter", "Uranus", "sextile"):     "Jupiter and Uranus are cooperating in the sky, supporting a collective mood of productive innovation. The new idea and the open door tend to arrive together right now.",
    ("Jupiter", "Uranus", "square"):      "Jupiter and Uranus are in tension in the sky, and the collective is navigating a friction between the pull toward freedom and disruption and the demands of what is established. The energy for change outpaces the structures that contain it.",
    ("Jupiter", "Uranus", "trine"):       "Jupiter and Uranus are in harmony in the sky, and the collective is in a moment of expansive, liberating change. Breakthroughs are available and the new tends to be welcomed rather than resisted.",
    ("Jupiter", "Uranus", "opposition"):  "Jupiter and Uranus are opposed in the sky, and the collective is navigating a significant tension between growth and disruption. This sky weather tends to bring sudden, large-scale changes.",

    # Jupiter–Neptune
    ("Jupiter", "Neptune", "conjunction"): "Jupiter and Neptune are conjunct in the sky, dissolving the collective into a rare wave of spiritual expansion and idealism. Imagination and faith are at a collective high — and so is the risk of mass illusion.",
    ("Jupiter", "Neptune", "sextile"):     "Jupiter and Neptune are cooperating in the sky, supporting a collective mood of generous idealism and the gentle expansion of spiritual life. Compassion and vision support each other in productive ways right now.",
    ("Jupiter", "Neptune", "square"):      "Jupiter and Neptune are in tension in the sky, and the collective is susceptible to inflation of ideals or mass confusion. The gap between the shared dream and the reality is becoming undeniable right now.",
    ("Jupiter", "Neptune", "trine"):       "Jupiter and Neptune are in harmony in the sky, and the collective is in a period of heightened spiritual sensitivity and compassionate expansion. The dream and the possible feel unusually close right now.",
    ("Jupiter", "Neptune", "opposition"):  "Jupiter and Neptune are opposed in the sky, and the collective is navigating a significant tension between confident expansion and the dissolving force of illusion. What is inflated eventually meets the truth.",

    # Jupiter–Pluto
    ("Jupiter", "Pluto", "conjunction"): "Jupiter and Pluto are conjunct in the sky — a significant meeting of expansion and deep transformation. The forces of power, growth, and radical change are amplified collectively and what emerges can reshape the landscape for years.",
    ("Jupiter", "Pluto", "sextile"):     "Jupiter and Pluto are cooperating in the sky, supporting a collective capacity to use depth and power productively. The willingness to go deep pays off and transformation can be leveraged for genuine growth.",
    ("Jupiter", "Pluto", "square"):      "Jupiter and Pluto are in tension in the sky, and the collective is navigating a clash between expansion and the forces of power or control. Growth is meeting significant resistance from entrenched power right now.",
    ("Jupiter", "Pluto", "trine"):       "Jupiter and Pluto are in harmony in the sky, and the collective is in a period of unusually powerful, productive transformation. The depth of change and the breadth of growth are aligned — significant shifts tend to work in the long run.",
    ("Jupiter", "Pluto", "opposition"):  "Jupiter and Pluto are opposed in the sky, and the collective is navigating a significant tension between the impulse to expand and the force of power or radical change. This sky weather tends to bring major collective upheavals.",

    # Saturn–Uranus
    ("Saturn", "Uranus", "conjunction"): "Saturn and Uranus are conjunct in the sky — a significant generational moment when the old order and the force of revolution meet. The collective is at a threshold where the established and the radically new must either integrate or collide.",
    ("Saturn", "Uranus", "sextile"):     "Saturn and Uranus are cooperating in the sky, supporting a collective ability to make productive changes within existing structures. Reform is possible without destruction and innovation has a structure to grow within.",
    ("Saturn", "Uranus", "square"):      "Saturn and Uranus are in tension in the sky — a significant and often turbulent sky weather. The collective is navigating a clash between the established order and the force of disruption, and the social friction tends to be palpable.",
    ("Saturn", "Uranus", "trine"):       "Saturn and Uranus are in harmony in the sky, and the collective is in a period where necessary change can happen within existing structures. Reform is achievable and innovation finds practical application.",
    ("Saturn", "Uranus", "opposition"):  "Saturn and Uranus are opposed in the sky — a recurring tension in collective history when the established order faces the most intense pressure for revolutionary change. This sky weather tends to define its era.",

    # Saturn–Neptune
    ("Neptune", "Saturn", "conjunction"): "Saturn and Neptune are conjunct in the sky — a rare meeting of structure and dissolution. The boundary between the real and the imagined is blurred at a societal level as the existing order meets the forces that seek to dissolve or transcend it.",
    ("Neptune", "Saturn", "sextile"):     "Saturn and Neptune are cooperating in the sky, supporting a collective capacity to give form to ideals and bring spiritual vision into practical reality. Dreams can be built and structures can be made more compassionate right now.",
    ("Neptune", "Saturn", "square"):      "Saturn and Neptune are in tension in the sky, and the collective is navigating a significant friction between reality and illusion. Idealistic structures are tested by harsh facts and facts dissolve in the fog of ideology right now.",
    ("Neptune", "Saturn", "trine"):       "Saturn and Neptune are in harmony in the sky, and the collective is in a period where ideals can be given structure and practical life can be infused with genuine spiritual meaning. The dream can be made real.",
    ("Neptune", "Saturn", "opposition"):  "Saturn and Neptune are opposed in the sky — a significant sky moment when the hard edge of reality and the dissolving force of collective illusion confront each other directly. Society tends to be divided between those who want clarity and those who want transcendence.",

    # Saturn–Pluto
    ("Pluto", "Saturn", "conjunction"): "Saturn and Pluto are conjunct in the sky — a rare, heavy, and historically significant moment. The collective is navigating a period of intense restructuring where the existing order is broken down and rebuilt from the foundation. This sky weather is associated with major historical turning points.",
    ("Pluto", "Saturn", "sextile"):     "Saturn and Pluto are cooperating in the sky, supporting a collective ability to use the forces of deep transformation constructively. The work of genuine, lasting change is supported right now.",
    ("Pluto", "Saturn", "square"):      "Saturn and Pluto are in tension in the sky — a significant and often difficult sky weather. The collective is navigating a clash between the existing order and the force of deep, unavoidable transformation. The pressure can be felt across institutions and collective life.",
    ("Pluto", "Saturn", "trine"):       "Saturn and Pluto are in harmony in the sky, and the collective is in a period where deep change and structural stability are aligned. The most difficult transformations tend to yield lasting, if hard-won, results.",
    ("Pluto", "Saturn", "opposition"):  "Saturn and Pluto are opposed in the sky — a historically significant sky moment when the structures of the existing order face direct confrontation with the forces of transformation and upheaval. This tends to be a defining moment in collective history.",

    # Uranus–Neptune
    ("Neptune", "Uranus", "conjunction"): "Uranus and Neptune are conjunct in the sky — an extraordinarily rare generational meeting of revolution and dissolution. The collective is at a point of massive cultural shift where old worldviews dissolve and new ones emerge from the collision of awakening and illusion.",
    ("Neptune", "Uranus", "sextile"):     "Uranus and Neptune are in a long-term cooperative relationship in the sky, supporting collective progress through the gradual integration of spiritual vision and technological innovation. This slow background harmony defines an era of imaginative possibility.",
    ("Neptune", "Uranus", "square"):      "Uranus and Neptune are in a long-term tension in the sky, and the collective is navigating a generational friction between the force of disruption and the dissolving of old ideals. This sky weather defines an era of cultural turbulence.",
    ("Neptune", "Uranus", "trine"):       "Uranus and Neptune are in a long-term harmony in the sky, and the collective is in a period where the force of awakening and the depth of spiritual imagination support each other. This sky weather defines an era of creative and spiritual possibility.",
    ("Neptune", "Uranus", "opposition"):  "Uranus and Neptune are in a long-term opposition in the sky — a rare, generational moment when the force of revolution and the dissolving force of illusion face each other directly. The collective is in an era defined by the tension between awakening and dream.",

    # Uranus–Pluto
    ("Pluto", "Uranus", "conjunction"): "Uranus and Pluto are conjunct in the sky — one of the rarest and most explosive generational moments. The collective is in an era of revolutionary transformation — awakening and the deepest forces of change are aligned and the world is being remade from the ground up.",
    ("Pluto", "Uranus", "sextile"):     "Uranus and Pluto are in a long-term cooperative relationship in the sky, supporting collective innovation and the productive application of transformative power. This era carries the potential for meaningful social progress.",
    ("Pluto", "Uranus", "square"):      "Uranus and Pluto are in a long-term tension in the sky — a defining sky moment for an entire generation. The collective is navigating a clash between the force of revolution and the power of entrenched systems, and the friction between them shapes the era.",
    ("Pluto", "Uranus", "trine"):       "Uranus and Pluto are in a long-term harmony in the sky, and the collective is in a period where the forces of innovation and deep transformation work together productively. This era is defined by meaningful, if gradual, change.",
    ("Pluto", "Uranus", "opposition"):  "Uranus and Pluto are in a long-term opposition in the sky — a rare generational moment when the force of awakening and the force of power confront each other at maximum intensity. This era tends to be defined by its upheavals.",

    # Neptune–Pluto
    ("Neptune", "Pluto", "conjunction"): "Neptune and Pluto are conjunct in the sky — the rarest of all sky moments, occurring only once every ~492 years. The collective is at a threshold of civilizational transformation where the spiritual and the deepest forces of change are unified.",
    ("Neptune", "Pluto", "sextile"):     "Neptune and Pluto are in a long-term cooperative relationship in the sky — a slow background harmony that defines an era of spiritual and transformative potential. The invisible forces that shape civilization are working in the same direction.",
    ("Neptune", "Pluto", "square"):      "Neptune and Pluto are in a long-term tension in the sky, and the collective is navigating a civilizational friction between the forces of spiritual dissolution and deep transformation. This defines an era of profound and sometimes painful cultural upheaval.",
    ("Neptune", "Pluto", "trine"):       "Neptune and Pluto are in a long-term harmony in the sky, and the collective is in a period where the deepest spiritual and transformative forces of civilization are working together. This defines an era of profound, if often invisible, positive change.",
    ("Neptune", "Pluto", "opposition"):  "Neptune and Pluto are in opposition in the sky — an extremely rare and generationally defining moment. The collective is navigating a civilizational tension between the forces of idealism and the forces of power, an era when what is dreamed and what is feared are both at their most intense.",
}


# ── Transit-to-natal aspect interpretations ───────────────────────────────────
# Keyed (transit_planet, natal_planet, aspect) — NOT sorted; direction matters.
# Language: "right now, transiting X is [aspect]ing your natal Y..."
# Fast planets (Sun/Moon/Mercury/Venus/Mars): brief window, immediate feel.
# Slow planets (Jupiter/Saturn/Uranus/Neptune/Pluto): longer arc, structural shift.

TRANSIT_TO_NATAL: dict[tuple[str, str, str], str] = {

    # ── Transiting Sun ────────────────────────────────────────────────────────
    ("Sun", "Sun", "conjunction"):   "Your solar return moment — the Sun is back where it was when you were born. This day carries a potent charge of renewal; intentions set now tend to stick for the year ahead.",
    ("Sun", "Sun", "sextile"):       "The Sun is gently supporting your core identity right now, making it easier to express who you are with clarity and confidence. Small actions that align with your purpose get a quiet boost.",
    ("Sun", "Sun", "square"):        "The transiting Sun is at odds with your natal Sun today, stirring restlessness or mild friction around self-expression. Notice where you feel out of step with your usual rhythm — that tension is information.",
    ("Sun", "Sun", "trine"):         "A natural flow between the current sky and your birth energy makes this one of those days where being yourself feels almost effortless. Good timing for any endeavor that asks you to step forward and shine.",
    ("Sun", "Sun", "opposition"):    "The Sun opposite your natal Sun marks the halfway point of your solar year. Others may mirror something back to you now — relationships highlight where your identity is evolving.",

    ("Sun", "Moon", "conjunction"):  "The Sun is illuminating your natal Moon today, bringing feelings and needs into sharp focus. Emotional patterns you usually run on autopilot become more visible and easier to understand.",
    ("Sun", "Moon", "sextile"):      "Right now the Sun is gently connecting your conscious will with your emotional instincts, making it a good moment for honest self-care and tending to what you genuinely need.",
    ("Sun", "Moon", "square"):       "Today's Sun is pressing on your natal Moon, bringing a subtle tension between what you want to do and what you feel you need. Small frustrations with home or inner comfort are common.",
    ("Sun", "Moon", "trine"):        "The Sun is flowing harmoniously with your natal Moon today, easing the gap between heart and mind. This is a warm, receptive energy — good for nurturing yourself or someone close to you.",
    ("Sun", "Moon", "opposition"):   "The Sun is shining directly across from your natal Moon, creating a full-moon-like pull between public life and private feeling. Something emotional may come to light or reach a natural peak.",

    ("Sun", "Mercury", "conjunction"): "The Sun is fusing with your natal Mercury today, energizing your thinking and communication. A good day to write, present, or have an important conversation — your words carry more vitality than usual.",
    ("Sun", "Mercury", "sextile"):   "Your mind gets a gentle solar charge right now, making it easier to connect ideas and express them clearly. Brief conversations or quick decisions tend to go well under this influence.",
    ("Sun", "Mercury", "square"):    "The Sun is prodding your natal Mercury, which can produce lively but scattered thinking. Watch for communication mix-ups or the urge to talk before fully processing what you mean.",
    ("Sun", "Mercury", "trine"):     "A smooth solar connection to your natal Mercury makes this an excellent window for writing, learning, or any task that needs mental sharpness. Ideas flow and words come easily.",
    ("Sun", "Mercury", "opposition"): "The Sun is highlighting your natal Mercury from the opposite sign, which can sharpen your perspective through contrast. Someone else's viewpoint may challenge — and ultimately refine — your thinking.",

    ("Sun", "Venus", "conjunction"): "The Sun is touching your natal Venus today, brightening your social and aesthetic sensibilities. Pleasure, connection, and beauty feel more accessible — enjoy it without guilt.",
    ("Sun", "Venus", "sextile"):     "A light solar beam on your natal Venus makes today pleasant for socializing, creative work, or simply appreciating what you have. Small gestures of kindness or affection land especially well.",
    ("Sun", "Venus", "square"):      "Today's Sun is nudging your natal Venus, which can stir mild dissatisfaction in relationships or finances. Notice if you are comparing what you have against an ideal rather than seeing it clearly.",
    ("Sun", "Venus", "trine"):       "The Sun is flowing easily through your natal Venus right now, lending a warm, attractive quality to your interactions. Creative projects benefit, and social connections come naturally.",
    ("Sun", "Venus", "opposition"):  "The Sun is illuminating your natal Venus from across the zodiac, putting relationships and values in high relief. What — or who — matters most to you may come into clearer view today.",

    ("Sun", "Mars", "conjunction"):  "The Sun is supercharging your natal Mars today, amplifying drive, confidence, and physical vitality. Channel this surge into purposeful action rather than impulsive reaction.",
    ("Sun", "Mars", "sextile"):      "Right now the Sun is lending easy energy to your natal Mars, making it a good day to start something, tackle a task, or simply move your body with intention.",
    ("Sun", "Mars", "square"):       "The Sun is squaring your natal Mars, which can feel like pressure building in the engine. Frustration or competitive friction may surface — use the tension to fuel focused effort rather than argument.",
    ("Sun", "Mars", "trine"):        "Solar energy is flowing smoothly into your natal Mars today, supporting confident, effective action. You can push toward goals without forcing it — momentum builds on its own.",
    ("Sun", "Mars", "opposition"):   "The Sun is opposing your natal Mars, lighting a tug-of-war between assertion and cooperation. Others may seem to challenge your will; see the friction as a mirror for your own unmet drives.",

    ("Sun", "Jupiter", "conjunction"): "The Sun is meeting your natal Jupiter today, expanding optimism and opening doors. This brief window is excellent for anything that requires faith, vision, or putting yourself forward.",
    ("Sun", "Jupiter", "sextile"):   "A gentle solar connection to your natal Jupiter lifts the mood and encourages a bigger-picture view. Reach a little further than usual today — opportunities respond to initiative.",
    ("Sun", "Jupiter", "square"):    "The Sun is pressing on your natal Jupiter, which can amplify confidence into overconfidence. Watch for promising more than you can deliver or skipping important details in the rush to expand.",
    ("Sun", "Jupiter", "trine"):     "The Sun is flowing through your natal Jupiter, bringing a buoyant, lucky-feeling quality to the day. Generosity, optimism, and forward momentum come naturally — a good time to take a calculated leap.",
    ("Sun", "Jupiter", "opposition"): "The Sun is opposing your natal Jupiter, highlighting the space between ambition and reality. Someone or something external may reflect back where your enthusiasm has outpaced your foundations.",

    ("Sun", "Saturn", "conjunction"): "The Sun is meeting your natal Saturn, which calls you toward seriousness and responsibility today. This isn't a day for shortcuts — it rewards focused effort, structure, and integrity.",
    ("Sun", "Saturn", "sextile"):    "A practical solar connection to your natal Saturn supports disciplined work right now. What you build today has staying power — make use of this steady, no-nonsense energy.",
    ("Sun", "Saturn", "square"):     "The Sun is squaring your natal Saturn, creating pressure around responsibility, authority, or limitation. Obstacles feel heavier today — but they are pointing at something that genuinely needs attention.",
    ("Sun", "Saturn", "trine"):      "The Sun is flowing harmoniously with your natal Saturn, lending a calm, organized quality to the day. Structure feels supportive rather than restrictive, and patient effort yields tangible results.",
    ("Sun", "Saturn", "opposition"): "The Sun is opposing your natal Saturn, putting a spotlight on accountability and long-term obligations. External demands or authority figures may test your resolve — this is a checkpoint, not a punishment.",

    ("Sun", "Uranus", "conjunction"): "The Sun is conjunct your natal Uranus today, sparking sudden insights and a hunger for freedom. Expect the unexpected and stay flexible — this energy rewards authenticity over routine.",
    ("Sun", "Uranus", "sextile"):    "Today brings a mild electric charge from the Sun to your natal Uranus, encouraging creative experimentation and a fresh angle on familiar problems.",
    ("Sun", "Uranus", "square"):     "The Sun is squaring your natal Uranus, which can produce restlessness, disruption, or the sudden urge to break from constraint. Channel the urge to rebel toward genuine innovation rather than just chaos.",
    ("Sun", "Uranus", "trine"):      "An easy solar connection to your natal Uranus makes today friendly to improvisation and originality. Departing from the usual script often leads somewhere surprisingly good right now.",
    ("Sun", "Uranus", "opposition"): "The Sun is opposing your natal Uranus, which can bring abrupt surprises or encounters with people who challenge your worldview. The disruption often carries a liberating message if you stay open.",

    ("Sun", "Neptune", "conjunction"): "The Sun is blending with your natal Neptune today, heightening sensitivity and imagination. Boundaries between self and other feel thinner — creative and spiritual work thrives; guard against escapism.",
    ("Sun", "Neptune", "sextile"):   "A soft solar connection to your natal Neptune gently opens intuition and empathy right now. Pay attention to impressions and dreams; they carry useful information today.",
    ("Sun", "Neptune", "square"):    "The Sun is squaring your natal Neptune, which can blur clarity and invite confusion or self-doubt. Double-check important facts and be cautious about decisions made on wishful thinking.",
    ("Sun", "Neptune", "trine"):     "The Sun is flowing into your natal Neptune, lending a dreamy, inspired quality to the day. Creative, healing, or spiritual work feels especially meaningful and productive.",
    ("Sun", "Neptune", "opposition"): "The Sun is opposing your natal Neptune, which can make it hard to see yourself or a situation clearly. Projection and idealization are hazards — try to ground impressions in observable facts.",

    ("Sun", "Pluto", "conjunction"): "The Sun is fusing with your natal Pluto today, intensifying everything it touches. This is a day for deep work, honest reckoning, or the kind of commitment that permanently changes your direction.",
    ("Sun", "Pluto", "sextile"):     "A subtle solar connection to your natal Pluto adds depth and magnetic quality to your presence today. You can move quietly but effectively toward meaningful transformation.",
    ("Sun", "Pluto", "square"):      "The Sun is squaring your natal Pluto, which amplifies power dynamics, intensity, and the urge to control or transform something. Let go of what you cannot change; focus where your power genuinely operates.",
    ("Sun", "Pluto", "trine"):       "The Sun is flowing through your natal Pluto, supporting deep, purposeful action. You can access reserves of strength and focus that allow for significant progress on what truly matters.",
    ("Sun", "Pluto", "opposition"):  "The Sun is opposing your natal Pluto, putting transformative pressure at the edges of your life. Power struggles or confrontations with what cannot continue as-is may surface — this is evolution in progress.",

    # ── Transiting Moon ───────────────────────────────────────────────────────
    ("Moon", "Sun", "conjunction"):  "The Moon is passing over your natal Sun right now, briefly syncing your feeling nature with your core identity. Moods are especially telling today — they reveal what the self genuinely needs.",
    ("Moon", "Sun", "sextile"):      "The Moon is sending a quick, supportive pulse to your natal Sun, making this a subtly uplifting few hours. Emotional and ego needs are more in agreement than usual.",
    ("Moon", "Moon", "conjunction"): "The Moon has returned to its natal position — your personal monthly lunar return. Emotional attunement is high; this is a good moment to check in with your deeper needs.",
    ("Moon", "Moon", "sextile"):     "The transiting Moon is in easy alignment with your natal Moon, creating a gentle receptivity and emotional ease right now. Small comforts resonate more deeply.",
    ("Moon", "Moon", "square"):      "The Moon is squaring your natal Moon, which can bring a brief mood wobble or friction between what you feel and what you think you should feel. Allow the tension without acting on it.",
    ("Moon", "Moon", "trine"):       "A harmonious lunar return moment — the Moon is in an easy trine to your natal Moon, lending natural emotional flow and a sense of belonging to wherever you are.",
    ("Moon", "Moon", "opposition"):  "The Moon is opposite your natal Moon, which can feel like an emotional tug-of-war between need and response. Relationships reflect your inner state back to you with unusual clarity.",
    ("Moon", "Sun", "square"):       "The Moon is pressing against your natal Sun right now, bringing a brief friction between feeling and will. Notice what emotions are telling you about what you truly want.",
    ("Moon", "Sun", "trine"):        "The Moon is flowing easily with your natal Sun for a few hours, making emotional and conscious intentions work in concert. This is a pleasant, naturally harmonious window.",
    ("Moon", "Sun", "opposition"):   "The Moon is opposite your natal Sun right now, shining an emotional spotlight on your identity. What you feel versus what you project may surface in a telling way.",

    ("Moon", "Mercury", "conjunction"): "The Moon is crossing your natal Mercury, blending feelings with thought. Intuitive insights and emotionally honest communication come easily in this window.",
    ("Moon", "Mercury", "sextile"):  "A quick lunar connection to your natal Mercury makes communication feel natural and warm right now. Good for heartfelt conversations or writing that needs both clarity and feeling.",
    ("Moon", "Mercury", "square"):   "The Moon is squaring your natal Mercury, which can make it hard to separate feelings from facts for a few hours. Wait before sending anything written from a reactive place.",
    ("Moon", "Mercury", "trine"):    "The Moon is flowing through your natal Mercury, making this a receptive window for ideas that blend logic and intuition seamlessly.",
    ("Moon", "Mercury", "opposition"): "The Moon is opposing your natal Mercury, highlighting the gap between what you feel and what you say. Someone's words may land emotionally charged right now — take a breath before responding.",

    ("Moon", "Venus", "conjunction"): "The Moon is meeting your natal Venus, amplifying warmth, affection, and a desire for beauty or pleasure. This brief window is lovely for self-care, creative work, or time with people you love.",
    ("Moon", "Venus", "sextile"):    "A gentle lunar touch on your natal Venus brightens your mood and social ease right now. Small pleasures feel genuinely satisfying.",
    ("Moon", "Venus", "square"):     "The Moon is squaring your natal Venus, which can stir mild emotional dissatisfaction or sensitivity in relationships. Notice if you are craving connection or reassurance — and ask for it honestly.",
    ("Moon", "Venus", "trine"):      "The Moon is flowing into your natal Venus, bringing a warm, sociable quality to these few hours. Love, beauty, and simple enjoyment come naturally.",
    ("Moon", "Venus", "opposition"): "The Moon is opposing your natal Venus, making relationship needs more emotionally charged for a few hours. Desires for closeness may compete with a need for independence.",

    ("Moon", "Mars", "conjunction"): "The Moon is conjunct your natal Mars right now, which can produce a burst of emotional energy, assertiveness, or impatience. Channel it into action rather than reaction.",
    ("Moon", "Mars", "sextile"):     "A quick lunar charge to your natal Mars gives you a mild boost in drive and confidence for a few hours. Good for getting started on something you've been putting off.",
    ("Moon", "Mars", "square"):      "The Moon is squaring your natal Mars, which can bring irritability or emotional urgency. Be conscious of where frustration is building — small triggers can feel larger than they are.",
    ("Moon", "Mars", "trine"):       "The Moon is supporting your natal Mars right now, lending easy courage and physical energy. A good window for assertive action that comes from a clear, non-reactive place.",
    ("Moon", "Mars", "opposition"):  "The Moon is opposing your natal Mars, which can surface emotional tensions around anger, desire, or conflict. What you're feeling and what you're fighting for may need to be examined together.",

    ("Moon", "Jupiter", "conjunction"): "The Moon is passing over your natal Jupiter, briefly expanding your emotional horizons. Optimism rises, generosity flows, and a sense of possibility opens up for these few hours.",
    ("Moon", "Jupiter", "sextile"):  "A lunar touch on your natal Jupiter lifts the mood gently, encouraging generosity and a wider perspective. A good few hours for planning something you believe in.",
    ("Moon", "Jupiter", "square"):   "The Moon is squaring your natal Jupiter, which can make emotions run a bit large or lead to over-promising emotionally. Good feelings are real but may be inflated — enjoy without overcommitting.",
    ("Moon", "Jupiter", "trine"):    "The Moon is flowing through your natal Jupiter, bringing a buoyant, expansive emotional quality to this window. Faith in yourself and others comes naturally.",
    ("Moon", "Jupiter", "opposition"): "The Moon is opposing your natal Jupiter, which can bring a brief tension between what you need emotionally and what you've been reaching for externally. Check that your optimism is grounded in genuine feeling.",

    ("Moon", "Saturn", "conjunction"): "The Moon is passing over your natal Saturn, which can bring a temporary emotional heaviness or a pull toward duty over desire. This window asks for patience rather than comfort-seeking.",
    ("Moon", "Saturn", "sextile"):   "The Moon is connecting gently with your natal Saturn, making this a window where emotional steadiness and practical care come together. Quiet, dependable effort feels satisfying.",
    ("Moon", "Saturn", "square"):    "The Moon is squaring your natal Saturn, which can produce a passing mood of restraint, loneliness, or self-criticism. Be gentle with yourself; this is a brief transit, not a permanent state.",
    ("Moon", "Saturn", "trine"):     "The Moon is in easy alignment with your natal Saturn, lending a calm, grounded quality to your emotional state right now. Responsibilities feel manageable rather than burdensome.",
    ("Moon", "Saturn", "opposition"): "The Moon is opposing your natal Saturn, which can bring feelings of limitation or emotional distance. Old conditioning around worthiness or belonging may surface briefly.",

    ("Moon", "Uranus", "conjunction"): "The Moon is touching your natal Uranus right now, sparking sudden mood shifts, restlessness, or a craving for something different. Expect the unexpected in your emotional world for a few hours.",
    ("Moon", "Uranus", "sextile"):   "A quick lunar connection to your natal Uranus brings a mild excitement or fresh angle to your feelings right now. Creative and intuitive impulses flash brightly in this window.",
    ("Moon", "Uranus", "square"):    "The Moon is squaring your natal Uranus, which can produce emotional unpredictability or sudden irritation. If you feel destabilized, give yourself space rather than reacting impulsively.",
    ("Moon", "Uranus", "trine"):     "The Moon is flowing into your natal Uranus, making this a lively, inventive few hours emotionally. Unusual ideas and spontaneous connection feel genuinely exciting.",
    ("Moon", "Uranus", "opposition"): "The Moon is opposing your natal Uranus, which can bring abrupt emotional surprises or encounters that shake your usual patterns. Stay adaptable — the disruption usually carries insight.",

    ("Moon", "Neptune", "conjunction"): "The Moon is merging with your natal Neptune right now, heightening sensitivity, empathy, and imagination. Boundaries feel thin — protect your energy while staying open to inspiration.",
    ("Moon", "Neptune", "sextile"):  "A soft lunar touch on your natal Neptune gently lifts intuition and creative receptivity right now. Pay attention to subtle impressions and feelings that are hard to name.",
    ("Moon", "Neptune", "square"):   "The Moon is squaring your natal Neptune, which can blur emotional clarity for a few hours. Confusion, hypersensitivity, or wishful feeling are possible — avoid making important decisions in this fog.",
    ("Moon", "Neptune", "trine"):    "The Moon is flowing into your natal Neptune, lending a dreamy, spiritually open quality to these hours. Creative and healing activities flourish; compassion flows easily.",
    ("Moon", "Neptune", "opposition"): "The Moon is opposing your natal Neptune, which can make emotional reality feel slippery or hard to pin down. Watch for projection or over-romanticizing — clarity comes with some distance.",

    ("Moon", "Pluto", "conjunction"): "The Moon is crossing your natal Pluto, briefly intensifying emotional experience and bringing what's usually hidden closer to the surface. Powerful feelings may arise — let them move through rather than suppress.",
    ("Moon", "Pluto", "sextile"):    "A quick lunar connection to your natal Pluto adds emotional depth and subtle magnetism to this window. You can access transformative insight with unusual ease right now.",
    ("Moon", "Pluto", "square"):     "The Moon is squaring your natal Pluto, which can stir intense, compulsive, or buried emotions for a few hours. Power dynamics in close relationships may feel heightened.",
    ("Moon", "Pluto", "trine"):      "The Moon is flowing through your natal Pluto, making it easier to process deep feelings and engage in genuinely transformative emotional work right now.",
    ("Moon", "Pluto", "opposition"): "The Moon is opposing your natal Pluto, surfacing powerful undercurrents in relationships or within yourself. Emotional control struggles are possible — letting go is usually more productive than gripping tighter.",

    # ── Transiting Mercury ────────────────────────────────────────────────────
    ("Mercury", "Sun", "conjunction"): "Transiting Mercury is meeting your natal Sun right now, sharpening your mental focus and giving your voice extra authority. Ideas you express today tend to carry weight.",
    ("Mercury", "Sun", "sextile"):   "Mercury is sending a quick intellectual boost toward your natal Sun, making communication feel natural and your ideas feel aligned with your purpose.",
    ("Mercury", "Sun", "square"):    "Mercury is squaring your natal Sun, which can bring mental restlessness or minor miscommunications. Think before committing — your words may be more scattered than usual.",
    ("Mercury", "Sun", "trine"):     "Mercury is flowing easily with your natal Sun, lending clarity to thought and confidence to expression. A good window for important conversations, proposals, or presentations.",
    ("Mercury", "Sun", "opposition"): "Mercury is opposing your natal Sun, making it a time for intellectual sparring or receiving perspectives that challenge your self-narrative. Listen as much as you speak.",

    ("Mercury", "Moon", "conjunction"): "Transiting Mercury is conjunct your natal Moon, bridging thought and feeling. Emotional truths are easier to articulate right now — journaling or heartfelt conversation is well-starred.",
    ("Mercury", "Moon", "sextile"):  "Mercury is gently supporting your natal Moon, helping you put words to your feelings with more ease than usual. Intuitive messages come through in a form you can actually use.",
    ("Mercury", "Moon", "square"):   "Mercury is squaring your natal Moon, which can make emotions feel noisier than usual or create friction between what you think and what you feel. Avoid over-analyzing every feeling.",
    ("Mercury", "Moon", "trine"):    "Mercury is in easy alignment with your natal Moon, letting mind and heart cooperate smoothly. A good moment for emotionally intelligent decision-making.",
    ("Mercury", "Moon", "opposition"): "Mercury is opposing your natal Moon, making it easier to see your emotional patterns from the outside. Others may verbalize something about you that you recognize as true.",

    ("Mercury", "Mercury", "conjunction"): "Transiting Mercury is back at your natal Mercury — a quick mental reset. Communications tend to feel especially sharp and purposeful during this window.",
    ("Mercury", "Mercury", "sextile"):  "Mercury is supporting your natal Mercury right now, making it a smooth window for learning, writing, or any task that requires clear, organized thinking.",
    ("Mercury", "Mercury", "square"):   "Mercury is squaring your natal Mercury, which can bring mental friction or information overload. Slow down, double-check details, and avoid rushing to conclusions.",
    ("Mercury", "Mercury", "trine"):    "Mercury is trine your natal Mercury, lending excellent mental fluency right now. Complex ideas sort themselves out, and communication flows with precision.",
    ("Mercury", "Mercury", "opposition"): "Mercury is opposing your natal Mercury, which is a good time to get a second opinion or step outside your own perspective. What you hear from others is unusually informative.",

    ("Mercury", "Venus", "conjunction"): "Transiting Mercury is meeting your natal Venus, making your words especially charming and persuasive right now. Negotiations, creative writing, and romantic communication all benefit.",
    ("Mercury", "Venus", "sextile"):   "Mercury is connecting gently with your natal Venus, making this a pleasant window for light social exchange, artful communication, or aesthetic decision-making.",
    ("Mercury", "Venus", "square"):    "Mercury is squaring your natal Venus, which can bring indecision around values or miscommunications in relationships. Take care with financial agreements or romantic words chosen carelessly.",
    ("Mercury", "Venus", "trine"):     "Mercury is flowing into your natal Venus, making your communication warm, graceful, and appealing right now. Good for creative expression, negotiation, or heartfelt correspondence.",
    ("Mercury", "Venus", "opposition"): "Mercury is opposing your natal Venus, putting relationship communication in focus. You may need to say something important — or hear something — about what you value or desire.",

    ("Mercury", "Mars", "conjunction"): "Transiting Mercury is conjunct your natal Mars, sharpening your mind and tongue. Mental energy is high and direct — good for debate, decisive action, or assertive writing.",
    ("Mercury", "Mars", "sextile"):    "Mercury is supporting your natal Mars right now, helping you combine quick thinking with decisive action. Good timing for planning that needs both speed and accuracy.",
    ("Mercury", "Mars", "square"):     "Mercury is squaring your natal Mars, which can make conversations heated or trigger mental impatience. Think before speaking — the urge to win an argument can produce careless words.",
    ("Mercury", "Mars", "trine"):      "Mercury is flowing easily with your natal Mars, giving your thinking a direct, confident edge. Planning, strategy, and assertive communication all benefit right now.",
    ("Mercury", "Mars", "opposition"): "Mercury is opposing your natal Mars, which can bring sharp intellectual friction or debates that reveal real differences. Stay curious rather than combative.",

    ("Mercury", "Jupiter", "conjunction"): "Transiting Mercury is meeting your natal Jupiter, expanding your thinking and making big-picture ideas easier to articulate. Teaching, publishing, or pitching ideas goes especially well.",
    ("Mercury", "Jupiter", "sextile"):   "Mercury is gently boosting your natal Jupiter, encouraging optimistic thinking and broader perspective. A good window for learning, travel planning, or any work that benefits from vision.",
    ("Mercury", "Jupiter", "square"):    "Mercury is squaring your natal Jupiter, which can produce overconfidence in ideas or a tendency to promise more than you can deliver in writing or conversation. Think before you commit.",
    ("Mercury", "Jupiter", "trine"):     "Mercury is flowing into your natal Jupiter right now — an excellent window for learning, communicating complex ideas, and receiving new information that genuinely expands your worldview.",
    ("Mercury", "Jupiter", "opposition"): "Mercury is opposing your natal Jupiter, highlighting the space between what you say and what you mean at scale. Overstatement or unfulfilled promises in communication are the main hazard.",

    ("Mercury", "Saturn", "conjunction"): "Transiting Mercury is conjunct your natal Saturn, lending seriousness and precision to your thinking. This is a good window for detailed planning, editing, or any work that demands rigor.",
    ("Mercury", "Saturn", "sextile"):    "Mercury is supporting your natal Saturn right now, making disciplined mental work feel natural. Deadlines, plans, and technical details come together with satisfying order.",
    ("Mercury", "Saturn", "square"):     "Mercury is squaring your natal Saturn, which can bring mental heaviness, self-censorship, or blocked communication. Be patient with your own thinking; structure helps.",
    ("Mercury", "Saturn", "trine"):      "Mercury is in easy alignment with your natal Saturn, making this a superb window for organized thinking, careful writing, and disciplined communication. Work produced now is solid.",
    ("Mercury", "Saturn", "opposition"): "Mercury is opposing your natal Saturn, which may surface self-doubt in communication or encounters with critical, demanding voices. See the feedback as sharpening, not diminishing, you.",

    ("Mercury", "Uranus", "conjunction"): "Transiting Mercury is meeting your natal Uranus — a lightning-bolt transit for the mind. Expect sudden insights, unconventional ideas, or abrupt changes in plans.",
    ("Mercury", "Uranus", "sextile"):    "Mercury is connecting with your natal Uranus, sparking inventive thinking and a slightly rebellious edge to communication. New and unusual ideas come easily right now.",
    ("Mercury", "Uranus", "square"):     "Mercury is squaring your natal Uranus, which can bring mental excitement that tips into instability. Avoid impulsive decisions or agreements made in a flash of excitement.",
    ("Mercury", "Uranus", "trine"):      "Mercury is flowing through your natal Uranus, making this an excellent window for breakthrough thinking and original communication. The unusual idea is often the right one.",
    ("Mercury", "Uranus", "opposition"): "Mercury is opposing your natal Uranus, which can produce surprising information or a sudden desire to break from conventional thinking. Stay grounded while staying open.",

    ("Mercury", "Neptune", "conjunction"): "Transiting Mercury is meeting your natal Neptune, blending rational thought with imagination and intuition. Creative writing, poetry, and inspired problem-solving flourish — factual precision requires extra care.",
    ("Mercury", "Neptune", "sextile"):    "Mercury is gently connecting with your natal Neptune, opening your mind to subtle impressions and creative possibilities. Artistic or spiritual communication feels natural.",
    ("Mercury", "Neptune", "square"):     "Mercury is squaring your natal Neptune, which can blur the line between fact and wishful thinking. Double-check information and be cautious about communications that feel inspired but vague.",
    ("Mercury", "Neptune", "trine"):      "Mercury is flowing into your natal Neptune, making this a rich window for imaginative thinking, metaphor, and communication that touches something deeper than logic alone.",
    ("Mercury", "Neptune", "opposition"): "Mercury is opposing your natal Neptune, which can make it hard to communicate clearly or see situations without projection. Seek clarity rather than accepting the first impression.",

    ("Mercury", "Pluto", "conjunction"): "Transiting Mercury is meeting your natal Pluto — this is when words become surgical. Research, investigation, deep conversation, and persuasive writing are all intensified.",
    ("Mercury", "Pluto", "sextile"):     "Mercury is connecting with your natal Pluto, giving your thinking and communication a penetrating quality right now. You can get to the root of a problem with unusual ease.",
    ("Mercury", "Pluto", "square"):      "Mercury is squaring your natal Pluto, which can intensify thought or bring obsessive mental loops. Conversations may feel more loaded than expected — be mindful of power dynamics in dialogue.",
    ("Mercury", "Pluto", "trine"):       "Mercury is flowing through your natal Pluto, giving your mind laser-like depth. This is a superb window for research, psychological insight, and transformative communication.",
    ("Mercury", "Pluto", "opposition"):  "Mercury is opposing your natal Pluto, which can bring compulsive thinking or encounters with information that demands a serious reckoning. Truth-telling — even uncomfortable truth — is a theme.",

    # ── Transiting Venus ──────────────────────────────────────────────────────
    ("Venus", "Sun", "conjunction"):  "Transiting Venus is touching your natal Sun, lending warmth, charm, and social magnetism to your presence. This is a pleasant window for pleasure, connection, and anything aesthetic.",
    ("Venus", "Sun", "sextile"):      "Venus is gently supporting your natal Sun right now, making your interactions feel easy and your creative impulses feel welcome. Enjoy the lighter mood.",
    ("Venus", "Sun", "square"):       "Venus is squaring your natal Sun, which can bring a mild tension between desire and self-expression. Financial or relational choices need a second look rather than an impulsive answer.",
    ("Venus", "Sun", "trine"):        "Venus is flowing easily with your natal Sun, one of the nicest transits for social life and creative expression. Beauty, harmony, and connection come naturally right now.",
    ("Venus", "Sun", "opposition"):   "Venus is opposing your natal Sun, heightening the importance of relationships and mirroring back what you most value. What others reflect about you is worth listening to.",

    ("Venus", "Moon", "conjunction"): "Transiting Venus is meeting your natal Moon, amplifying nurturing instincts and a desire for comfort and belonging. This is a genuinely lovely window for self-care and tender connection.",
    ("Venus", "Moon", "sextile"):     "Venus is supporting your natal Moon, making emotional life feel a little softer and more pleasant than usual. Good for sharing affection or simply enjoying a quiet, beautiful moment.",
    ("Venus", "Moon", "square"):      "Venus is squaring your natal Moon, which can stir emotional longing or dissatisfaction in relationships. Notice what you crave and whether it's really what you need.",
    ("Venus", "Moon", "trine"):       "Venus is flowing through your natal Moon, bringing a warm, nurturing quality to your emotional world. This is a naturally happy, contented window.",
    ("Venus", "Moon", "opposition"):  "Venus is opposing your natal Moon, which can bring a pull between personal desire and what relationships ask of you. Feelings about love or home come into sharper relief.",

    ("Venus", "Mercury", "conjunction"): "Transiting Venus is touching your natal Mercury, making your words more charming and your thinking more attuned to beauty and harmony. Excellent for writing, negotiation, or diplomatic conversation.",
    ("Venus", "Mercury", "sextile"):    "Venus is gently connecting with your natal Mercury, lending an easy, pleasant quality to conversation and creative thought. Light social exchanges go smoothly.",
    ("Venus", "Mercury", "square"):     "Venus is squaring your natal Mercury, which can bring indecision or a reluctance to say what needs to be said. Be honest in communication even when you prefer harmony.",
    ("Venus", "Mercury", "trine"):      "Venus is flowing into your natal Mercury, making this an excellent window for charming communication, creative writing, and diplomatic problem-solving.",
    ("Venus", "Mercury", "opposition"): "Venus is opposing your natal Mercury, making it a good time to hear what someone important has to say about beauty, value, or relationship. Listen as generously as you speak.",

    ("Venus", "Venus", "conjunction"): "Transiting Venus is conjunct your natal Venus — a minor but genuinely pleasant personal Venus return. Social grace and aesthetic pleasure are heightened right now.",
    ("Venus", "Venus", "sextile"):     "Venus is sending easy energy to your natal Venus, making this a naturally harmonious window for relationships, art, and financial matters.",
    ("Venus", "Venus", "square"):      "Venus is squaring your natal Venus, which can bring mild friction in relationships or a moment of reconsidering what you truly value. It is a checkpoint, not a crisis.",
    ("Venus", "Venus", "trine"):       "Venus is trine your natal Venus, one of the loveliest minor transits. Enjoy it for what it is — a window of ease, beauty, and warm connection.",
    ("Venus", "Venus", "opposition"):  "Venus is opposing your natal Venus, putting love and values in the spotlight. Relationships may feel both more intense and more revealing than usual.",

    ("Venus", "Mars", "conjunction"):  "Transiting Venus is meeting your natal Mars, igniting attraction, passion, and creative drive. This is a potent window for romance, artistic creation, or any work that requires both desire and action.",
    ("Venus", "Mars", "sextile"):      "Venus is gently supporting your natal Mars, making assertive action feel more appealing and socially smooth right now. Good for pursuing what you want with charm.",
    ("Venus", "Mars", "square"):       "Venus is squaring your natal Mars, which can create tension between desire and restraint — or spark romantic friction. What you want and what's harmonious may need negotiation.",
    ("Venus", "Mars", "trine"):        "Venus is flowing easily with your natal Mars, making this a vibrant, attractive window. Creative work, romance, and any endeavor fueled by enthusiasm are well-supported.",
    ("Venus", "Mars", "opposition"):   "Venus is opposing your natal Mars, putting the push and pull between attraction and assertion into high relief. Relationship intensity — positive or challenging — is heightened.",

    ("Venus", "Jupiter", "conjunction"): "Transiting Venus is meeting your natal Jupiter, one of the most pleasant transits in any person's chart. Abundance, enjoyment, and social luck are all amplified right now.",
    ("Venus", "Jupiter", "sextile"):    "Venus is gently connecting with your natal Jupiter, bringing a light sense of abundance and good fortune to social and financial matters. Small pleasures feel genuinely rich.",
    ("Venus", "Jupiter", "square"):     "Venus is squaring your natal Jupiter, which can encourage over-indulgence or financial overreach. Good feelings are real — just make sure they match what you can actually sustain.",
    ("Venus", "Jupiter", "trine"):      "Venus is flowing through your natal Jupiter — a genuinely lucky window for relationships, creative endeavors, and financial opportunity. Reach a little further than usual.",
    ("Venus", "Jupiter", "opposition"): "Venus is opposing your natal Jupiter, which can bring an excess of pleasant energy that needs grounding. Enjoy but don't overextend in love or spending.",

    ("Venus", "Saturn", "conjunction"): "Transiting Venus is meeting your natal Saturn, which can feel bittersweet — pleasure and duty come together. A relationship may be tested for real depth, or commitment becomes a genuine topic.",
    ("Venus", "Saturn", "sextile"):     "Venus is supporting your natal Saturn right now, making this a good window for solidifying a relationship, honoring a financial commitment, or finding beauty in discipline.",
    ("Venus", "Saturn", "square"):      "Venus is squaring your natal Saturn, which can bring emotional restriction, relational duty, or a feeling that love requires more effort than usual. What survives the pressure is real.",
    ("Venus", "Saturn", "trine"):       "Venus is flowing into your natal Saturn, making lasting commitments feel natural and mutual respect feel beautiful. Serious relationships deepen; practical matters are handled with grace.",
    ("Venus", "Saturn", "opposition"):  "Venus is opposing your natal Saturn, putting the structure and longevity of relationships in focus. What is real and lasting stands up; what has been maintained through inertia may waver.",

    ("Venus", "Uranus", "conjunction"): "Transiting Venus is meeting your natal Uranus, which can bring unexpected attraction, sudden social opportunities, or a compelling urge to break from relational routine.",
    ("Venus", "Uranus", "sextile"):     "Venus is gently connecting with your natal Uranus, bringing a pleasantly surprising quality to social interactions. Something out of the ordinary feels appealing and appropriate right now.",
    ("Venus", "Uranus", "square"):      "Venus is squaring your natal Uranus, which can produce sudden attraction or just as sudden cooling. Don't mistake excitement for depth — give it time before deciding.",
    ("Venus", "Uranus", "trine"):       "Venus is flowing through your natal Uranus, making this an exciting and inventive window for relationships and creative expression. Something unconventional is exactly the right choice.",
    ("Venus", "Uranus", "opposition"):  "Venus is opposing your natal Uranus, which can bring unexpected relationship developments or financial surprises. Stay flexible and don't cling to plans that the moment is already revising.",

    ("Venus", "Neptune", "conjunction"): "Transiting Venus is meeting your natal Neptune, heightening romantic idealism and spiritual sensitivity. This window is exquisite for art, prayer, or deep love — and risky for practical decisions requiring clarity.",
    ("Venus", "Neptune", "sextile"):    "Venus is gently connecting with your natal Neptune, lending a soft, spiritually attuned quality to relationships and creative work. Dreams and beauty feel especially accessible.",
    ("Venus", "Neptune", "square"):     "Venus is squaring your natal Neptune, which can cloud romantic judgment with idealization. Make sure you're seeing people and situations as they are, not as you wish them to be.",
    ("Venus", "Neptune", "trine"):      "Venus is flowing through your natal Neptune — a deeply beautiful transit for art, love, and spiritual devotion. Allow yourself to be moved without losing your footing.",
    ("Venus", "Neptune", "opposition"): "Venus is opposing your natal Neptune, which can blur the line between romantic feeling and illusion. Check your perceptions against reality before making relationship decisions.",

    ("Venus", "Pluto", "conjunction"): "Transiting Venus is meeting your natal Pluto, intensifying love and desire to a degree that can feel transformative or even obsessive. What is touched by this transit leaves a permanent mark.",
    ("Venus", "Pluto", "sextile"):     "Venus is gently connecting with your natal Pluto, adding emotional depth and magnetic appeal to relationships and creative work. Encounters feel more meaningful than usual.",
    ("Venus", "Pluto", "square"):      "Venus is squaring your natal Pluto, which can bring power dynamics into relationships or an intense pull toward something — or someone — that feels fated. Trust the depth, not the compulsion.",
    ("Venus", "Pluto", "trine"):       "Venus is flowing into your natal Pluto, making it possible to experience beauty and love at a genuinely soul-deep level right now. Creative and relational work has lasting impact.",
    ("Venus", "Pluto", "opposition"):  "Venus is opposing your natal Pluto, which can surface jealousy, obsession, or the transformative ending and beginning of a significant relationship cycle.",

    # ── Transiting Mars ───────────────────────────────────────────────────────
    ("Mars", "Sun", "conjunction"):   "Transiting Mars is conjunct your natal Sun, turbocharging your drive and physical energy. This is a potent window for bold action — channel it or risk burning yourself out in reactive frustration.",
    ("Mars", "Sun", "sextile"):       "Mars is supporting your natal Sun right now, giving you a confident, energized edge. Initiative pays off — this is a good window to start something you've been circling.",
    ("Mars", "Sun", "square"):        "Mars is squaring your natal Sun, which can produce friction, impatience, and heightened ego sensitivity. Physical outlet and deliberate pacing help you use this pressure productively.",
    ("Mars", "Sun", "trine"):         "Mars is flowing easily into your natal Sun, giving you sustained, productive energy without the edginess of a hard aspect. Excellent for any ambitious project or physical challenge.",
    ("Mars", "Sun", "opposition"):    "Mars is opposing your natal Sun, which often brings confrontations or competitive dynamics. External friction tends to mirror inner frustration — address both honestly.",

    ("Mars", "Moon", "conjunction"):  "Transiting Mars is meeting your natal Moon, stirring emotional intensity and urgency. Feelings are closer to the surface, and the urge to act on them is strong — take a breath before responding.",
    ("Mars", "Moon", "sextile"):      "Mars is gently supporting your natal Moon, lending emotional courage and a productive restlessness. Good for asserting emotional needs clearly and calmly.",
    ("Mars", "Moon", "square"):       "Mars is squaring your natal Moon, which can bring irritability, emotional reactivity, or domestic friction. Identify the underlying need before responding to the surface trigger.",
    ("Mars", "Moon", "trine"):        "Mars is flowing into your natal Moon, giving emotional life a motivated, purposeful quality. Asserting what you need feels natural and tends to be well-received right now.",
    ("Mars", "Moon", "opposition"):   "Mars is opposing your natal Moon, which can surface anger or conflict rooted in emotional history. Address the feeling underneath the argument to get to something useful.",

    ("Mars", "Mercury", "conjunction"): "Transiting Mars is conjunct your natal Mercury — your mind is sharp, fast, and potentially combative. Excellent for debate, sales, or decisive writing; watch for words that wound without intending to.",
    ("Mars", "Mercury", "sextile"):    "Mars is supporting your natal Mercury, sharpening thinking and lending confidence to communication. Good for making decisions quickly and stating your position clearly.",
    ("Mars", "Mercury", "square"):     "Mars is squaring your natal Mercury, which can bring argumentative energy or mental overload. Slow down in conversation — being right matters less than being understood.",
    ("Mars", "Mercury", "trine"):      "Mars is flowing through your natal Mercury, giving your thinking a direct, decisive edge. Planning, strategy, and assertive communication all hit their mark right now.",
    ("Mars", "Mercury", "opposition"): "Mars is opposing your natal Mercury, which can bring heated debates or verbal confrontations. The friction is useful if you stay curious rather than combative.",

    ("Mars", "Venus", "conjunction"):  "Transiting Mars is meeting your natal Venus, igniting desire and creative passion. Romantic energy is high, and the impulse to pursue what you want is strong — act with awareness.",
    ("Mars", "Venus", "sextile"):      "Mars is gently supporting your natal Venus, making assertive action in love or creative work feel natural and confident. You can pursue what you want without forcing it.",
    ("Mars", "Venus", "square"):       "Mars is squaring your natal Venus, which can create tension between desire and harmony. Romantic friction or financial impulsiveness are the key hazards right now.",
    ("Mars", "Venus", "trine"):        "Mars is flowing through your natal Venus, giving you a magnetism and creative confidence that draws others toward you. A strong window for romance, collaboration, and artistic output.",
    ("Mars", "Venus", "opposition"):   "Mars is opposing your natal Venus, creating a charged push-pull in relationships. Passion is high — and so is the potential for misunderstanding what you or another person actually wants.",

    ("Mars", "Mars", "conjunction"):   "Transiting Mars is back at your natal Mars — your personal Mars return. Drive, ambition, and competitive energy are all at a peak. Begin something you intend to pursue vigorously.",
    ("Mars", "Mars", "sextile"):       "Mars is supporting your natal Mars right now, giving you an energized, capable quality. Physical endurance and willpower are both slightly elevated.",
    ("Mars", "Mars", "square"):        "Mars is squaring your natal Mars, which can produce frustration, overexertion, or conflict that feels pointless in retrospect. Choose your battles consciously.",
    ("Mars", "Mars", "trine"):         "Mars is trine your natal Mars — a clean, productive window where effort translates into results with less friction than usual. Use the momentum.",
    ("Mars", "Mars", "opposition"):    "Mars is opposing your natal Mars, which tends to surface competition, conflict, or the mirroring of your own aggression in others. Reflect on what you're really fighting for.",

    ("Mars", "Jupiter", "conjunction"): "Transiting Mars is meeting your natal Jupiter, amplifying ambition and expanding your sense of what's possible. Bold moves tend to pay off — avoid arrogant overreach.",
    ("Mars", "Jupiter", "sextile"):    "Mars is gently boosting your natal Jupiter, making this a good window for forward-moving action and calculated risk-taking. Confidence is well-founded right now.",
    ("Mars", "Jupiter", "square"):     "Mars is squaring your natal Jupiter, which can produce an excess of ambition or energy that overreaches. The goal is real; the timing and method need more care.",
    ("Mars", "Jupiter", "trine"):      "Mars is flowing through your natal Jupiter, combining drive with luck in a way that rewards initiative. Big goals feel achievable because you are genuinely energized and prepared.",
    ("Mars", "Jupiter", "opposition"): "Mars is opposing your natal Jupiter, which can inflate confidence or make conflict seem more important than the larger goal. Keep perspective on what winning actually costs.",

    ("Mars", "Saturn", "conjunction"): "Transiting Mars is meeting your natal Saturn, creating a potent tension between urgency and caution. When this energy is focused, it builds something lasting — when it frustrates, it simmers as resentment.",
    ("Mars", "Saturn", "sextile"):     "Mars is gently supporting your natal Saturn, making disciplined, energetic work feel satisfying. Progress made now has a quality of real, durable accomplishment.",
    ("Mars", "Saturn", "square"):      "Mars is squaring your natal Saturn, which is one of the more challenging shorter transits — expect blocked progress, authority friction, or physical frustration. Patience over force.",
    ("Mars", "Saturn", "trine"):       "Mars is flowing through your natal Saturn, giving you the rare gift of sustained, disciplined energy. This is excellent for difficult long-term projects that require both drive and perseverance.",
    ("Mars", "Saturn", "opposition"):  "Mars is opposing your natal Saturn, which can surface encounters with authority, delay, or the limits of your own endurance. The challenge is clarifying your sense of purpose, not just pushing harder.",

    ("Mars", "Uranus", "conjunction"): "Transiting Mars is meeting your natal Uranus — a volatile, exciting combination. Sudden breakthroughs and sudden accidents live close together in this window; stay alert and channel energy into innovation.",
    ("Mars", "Uranus", "sextile"):     "Mars is supporting your natal Uranus right now, making bold, unconventional action feel exciting and productive. A good window for creative risks and breaking from routine.",
    ("Mars", "Uranus", "square"):      "Mars is squaring your natal Uranus, which can bring sudden anger, accidents, or impulsive breaks. Stay conscious of the urge to blow things up — it often masks a legitimate desire for freedom.",
    ("Mars", "Uranus", "trine"):       "Mars is flowing into your natal Uranus, giving your initiative a rebellious, inventive quality right now. Doing something differently from how it's always been done produces real results.",
    ("Mars", "Uranus", "opposition"):  "Mars is opposing your natal Uranus, which can bring sudden confrontation or the unexpected disruption of plans. What you can't control can still teach you something useful.",

    ("Mars", "Neptune", "conjunction"): "Transiting Mars is meeting your natal Neptune, blending action with imagination or confusion. Creative and spiritual work can be extraordinary; practical execution needs extra clarity of intention.",
    ("Mars", "Neptune", "sextile"):    "Mars is gently supporting your natal Neptune, making it easier to act on intuition or move toward an idealistic goal. Inspired effort is well-directed right now.",
    ("Mars", "Neptune", "square"):     "Mars is squaring your natal Neptune, which can dissipate energy, blur goals, or make it hard to act decisively. Be clear about your actual objective before committing.",
    ("Mars", "Neptune", "trine"):      "Mars is flowing through your natal Neptune, lending an almost poetic quality to motivated action. Creative, healing, and spiritually aligned work flourishes under this influence.",
    ("Mars", "Neptune", "opposition"): "Mars is opposing your natal Neptune, which can make your efforts feel somehow misdirected or invisible. Clarify your aim and check that you are acting from genuine desire rather than illusion.",

    ("Mars", "Pluto", "conjunction"):  "Transiting Mars is meeting your natal Pluto — one of the most intense shorter transits. Power, drive, and the will to transform all intensify simultaneously. Extraordinary accomplishment and extraordinary destruction are equally possible.",
    ("Mars", "Pluto", "sextile"):      "Mars is gently connecting with your natal Pluto, giving you access to deep reserves of purposeful power right now. You can move an obstacle that has seemed immovable.",
    ("Mars", "Pluto", "square"):       "Mars is squaring your natal Pluto, which can trigger power struggles, obsessive drives, or the sense that something must give. Don't force outcomes — but don't suppress your genuine will either.",
    ("Mars", "Pluto", "trine"):        "Mars is flowing through your natal Pluto, giving your efforts a focused, transformative power. What you work toward now can create lasting structural change in your life.",
    ("Mars", "Pluto", "opposition"):   "Mars is opposing your natal Pluto, which surfaces power dynamics that can no longer be avoided. The clash is usually about something deeper than its apparent subject — look for what needs to change permanently.",

    # ── Transiting Jupiter ────────────────────────────────────────────────────
    ("Jupiter", "Sun", "conjunction"): "Transiting Jupiter is conjunct your natal Sun, opening a major window of expansion, confidence, and opportunity. This year-long passage often marks a period of genuine growth — seize it with intention.",
    ("Jupiter", "Sun", "sextile"):     "Jupiter is sending a supportive beam to your natal Sun right now, making this a period where optimism is well-founded and forward-moving effort pays off.",
    ("Jupiter", "Sun", "square"):      "Jupiter is squaring your natal Sun, which can expand confidence into overconfidence. Opportunities are real but require discernment — don't overextend in ambition, spending, or promises.",
    ("Jupiter", "Sun", "trine"):       "Jupiter is flowing through your natal Sun in one of the most genuinely fortunate transits available. Your natural confidence and external opportunity are aligned — make your move.",
    ("Jupiter", "Sun", "opposition"):  "Jupiter is opposing your natal Sun, which often brings external abundance alongside internal excess. What is genuinely yours will expand; what belongs to others will become clearer.",

    ("Jupiter", "Moon", "conjunction"): "Transiting Jupiter is meeting your natal Moon, expanding your emotional world and bringing a sense of abundance to home and family life. Generosity and optimism feel effortless right now.",
    ("Jupiter", "Moon", "sextile"):    "Jupiter is supporting your natal Moon, gently expanding your emotional capacity and making nurturing feel natural and rewarding. A good period for home life and emotional investment.",
    ("Jupiter", "Moon", "square"):     "Jupiter is squaring your natal Moon, which can make emotions run large or lead to over-giving. Be generous without losing your own boundaries or center.",
    ("Jupiter", "Moon", "trine"):      "Jupiter is flowing into your natal Moon, making this a genuinely comfortable and expansive period emotionally. Home life and family tend to flourish; inner contentment is real.",
    ("Jupiter", "Moon", "opposition"): "Jupiter is opposing your natal Moon, expanding emotional sensitivity and highlighting the relationship between personal needs and what you give to others. Find where you can receive more graciously.",

    ("Jupiter", "Mercury", "conjunction"): "Transiting Jupiter is conjunct your natal Mercury, broadening your thinking and making it a superb period for learning, publishing, teaching, and any form of large-scale communication.",
    ("Jupiter", "Mercury", "sextile"):    "Jupiter is gently expanding your natal Mercury, making this a good period for study, travel communication, and putting your ideas in front of a wider audience.",
    ("Jupiter", "Mercury", "square"):     "Jupiter is squaring your natal Mercury, which can produce mental overextension or the tendency to promise more than you deliver in writing or speech. Think in smaller, concrete steps.",
    ("Jupiter", "Mercury", "trine"):      "Jupiter is flowing through your natal Mercury, making this an excellent period for big ideas that are also well-expressed. Teaching, writing, and learning all benefit from the expansive mental energy.",
    ("Jupiter", "Mercury", "opposition"): "Jupiter is opposing your natal Mercury, putting the gap between broad vision and practical detail in focus. What you say may be grand; make sure it has a foundation.",

    ("Jupiter", "Venus", "conjunction"): "Transiting Jupiter is meeting your natal Venus — one of the most enjoyable transits available. Relationships, creativity, and financial life all tend to expand and improve during this period.",
    ("Jupiter", "Venus", "sextile"):    "Jupiter is gently supporting your natal Venus, bringing a pleasant, abundant quality to social and creative life. Small blessings accumulate in ways that feel genuinely good.",
    ("Jupiter", "Venus", "square"):     "Jupiter is squaring your natal Venus, which can encourage over-indulgence in pleasure or financial excess. Enjoy the abundance without losing sight of what is actually sustainable.",
    ("Jupiter", "Venus", "trine"):      "Jupiter is flowing through your natal Venus, making this a rich period for love, art, and financial well-being. Reach for more than feels safe — the support is there.",
    ("Jupiter", "Venus", "opposition"): "Jupiter is opposing your natal Venus, expanding relationship experiences and financial awareness simultaneously. What you truly value may turn out to be larger — or different — than you assumed.",

    ("Jupiter", "Mars", "conjunction"): "Transiting Jupiter is meeting your natal Mars, amplifying drive, ambition, and physical energy. This is a time for bold initiative and expansion — just ensure the plan can hold the scale.",
    ("Jupiter", "Mars", "sextile"):    "Jupiter is supporting your natal Mars, lending a confident, expansive quality to your efforts right now. Things that require initiative and sustained energy tend to go well.",
    ("Jupiter", "Mars", "square"):     "Jupiter is squaring your natal Mars, which can produce restless energy or actions that overshoot the mark. Direct the drive toward a clearly defined target.",
    ("Jupiter", "Mars", "trine"):      "Jupiter is flowing into your natal Mars, combining ambition with luck in a way that makes forward momentum feel both natural and well-timed.",
    ("Jupiter", "Mars", "opposition"): "Jupiter is opposing your natal Mars, which can amplify competitive energy or make conflict feel consequential. Keep the long-term goal in view rather than winning the immediate skirmish.",

    ("Jupiter", "Jupiter", "conjunction"): "Transiting Jupiter has returned to its natal position — your Jupiter return, arriving roughly every 12 years. This is a major reset in faith, vision, and opportunity that shapes the coming decade.",
    ("Jupiter", "Jupiter", "sextile"):    "Jupiter is in easy alignment with your natal Jupiter, reinforcing the areas of life where growth naturally wants to happen. A good period for expanding projects already in motion.",
    ("Jupiter", "Jupiter", "square"):     "Jupiter is squaring its natal position, marking a turning-point year where early Jupiter return themes are tested. What expanded easily now needs more careful tending.",
    ("Jupiter", "Jupiter", "trine"):      "Jupiter is trine your natal Jupiter, a period of genuine flow in areas of growth and abundance. What you set in motion now has an unusual ease of momentum.",
    ("Jupiter", "Jupiter", "opposition"): "Jupiter is opposing its natal position, the halfway point of the Jupiter cycle. Where has growth actually taken you? What has expanded needs now to be given meaningful form.",

    ("Jupiter", "Saturn", "conjunction"): "Transiting Jupiter is meeting your natal Saturn, opening up the structures and commitments of your life to growth. Old limitations can become platforms for expansion during this period.",
    ("Jupiter", "Saturn", "sextile"):    "Jupiter is gently supporting your natal Saturn, making disciplined effort feel rewarded and long-term structures more expansive. Progress is steady and real.",
    ("Jupiter", "Saturn", "square"):     "Jupiter is squaring your natal Saturn, which creates tension between your desire for growth and the limits that have defined you. The push is worth it — just don't promise more than the structure can hold.",
    ("Jupiter", "Saturn", "trine"):      "Jupiter is flowing into your natal Saturn, making this a particularly productive period for structured expansion — you can grow steadily into something genuinely larger without losing your foundations.",
    ("Jupiter", "Saturn", "opposition"): "Jupiter is opposing your natal Saturn, putting the tension between vision and limitation in front of you. What has felt like a ceiling may actually be a challenge to outgrow.",

    ("Jupiter", "Uranus", "conjunction"): "Transiting Jupiter is meeting your natal Uranus, which can bring sudden, exciting breakthroughs or a radical shift in your sense of what is possible. Embrace the unexpected development.",
    ("Jupiter", "Uranus", "sextile"):    "Jupiter is supporting your natal Uranus, expanding your freedom and making unconventional choices feel not just acceptable but well-timed. Innovation pays off right now.",
    ("Jupiter", "Uranus", "square"):     "Jupiter is squaring your natal Uranus, amplifying the urge to break free in ways that may overshoot what is actually needed. Revolutionary energy is real — point it thoughtfully.",
    ("Jupiter", "Uranus", "trine"):      "Jupiter is flowing through your natal Uranus — a spectacular window for breakthroughs, inventions, and liberation from outdated constraints. The unusual path is often the right one.",
    ("Jupiter", "Uranus", "opposition"): "Jupiter is opposing your natal Uranus, which can bring sudden external opportunities — or disruptions — that force a reevaluation of your values and direction.",

    ("Jupiter", "Neptune", "conjunction"): "Transiting Jupiter is meeting your natal Neptune, expanding spiritual sensitivity and creative imagination. This period can bring peak inspirational experiences — keep one foot in practical reality.",
    ("Jupiter", "Neptune", "sextile"):    "Jupiter is gently supporting your natal Neptune, opening doors to creative, spiritual, and healing work. Vision is elevated and the effort to pursue it feels meaningful.",
    ("Jupiter", "Neptune", "square"):     "Jupiter is squaring your natal Neptune, which can inflate idealism or blur the line between genuine opportunity and wishful thinking. Seek concrete grounding for expanded dreams.",
    ("Jupiter", "Neptune", "trine"):      "Jupiter is flowing through your natal Neptune — a period of heightened inspiration, spiritual expansion, and creative breakthrough. What you imagine now has unusual power to manifest.",
    ("Jupiter", "Neptune", "opposition"): "Jupiter is opposing your natal Neptune, expanding illusions as readily as ideals. Be honest about what you believe versus what you wish were true in your larger commitments.",

    ("Jupiter", "Pluto", "conjunction"): "Transiting Jupiter is meeting your natal Pluto — a potent expansion of personal power, ambition, and the desire to have meaningful impact. This period can produce major life transformations.",
    ("Jupiter", "Pluto", "sextile"):    "Jupiter is supporting your natal Pluto, making deep transformation feel not only possible but well-timed. You can reach into reserved power and use it purposefully right now.",
    ("Jupiter", "Pluto", "square"):     "Jupiter is squaring your natal Pluto, which amplifies power drives and can intensify control dynamics. Transform yourself first before trying to transform the situation.",
    ("Jupiter", "Pluto", "trine"):      "Jupiter is flowing through your natal Pluto, expanding your capacity for genuine transformation and meaningful impact. What you build now carries unusual depth and lasting consequence.",
    ("Jupiter", "Pluto", "opposition"): "Jupiter is opposing your natal Pluto, which can surface the tension between personal power and external forces that want to reshape your life. Real growth requires releasing something significant.",

    # ── Transiting Saturn ─────────────────────────────────────────────────────
    ("Saturn", "Sun", "conjunction"):  "Transiting Saturn is conjunct your natal Sun — the Saturn passage through your solar identity. This multi-year influence asks you to take your sense of self seriously, strip away pretense, and build something real.",
    ("Saturn", "Sun", "sextile"):      "Saturn is sending a steady, supportive signal to your natal Sun, making this a period where disciplined effort and genuine authenticity are quietly rewarded.",
    ("Saturn", "Sun", "square"):       "Saturn is squaring your natal Sun, one of the more demanding chapters in the Saturn cycle. External pressure and internal doubt are working in tandem to clarify who you actually are beneath the roles you play.",
    ("Saturn", "Sun", "trine"):        "Saturn is flowing into your natal Sun, making this a period of calm, productive authority. Responsibilities feel manageable, goals feel reachable, and effort builds on itself with unusual solidity.",
    ("Saturn", "Sun", "opposition"):   "Saturn is opposing your natal Sun — the halfway point of the Saturn cycle begun at the conjunction. Relationships and external demands are the mirrors now; accountability arrives from outside.",

    ("Saturn", "Moon", "conjunction"): "Transiting Saturn is conjunct your natal Moon, pressing on emotional life with unusual weight. This can feel lonely or heavy, but it also invites a profound maturation of your relationship with need and feeling.",
    ("Saturn", "Moon", "sextile"):     "Saturn is supporting your natal Moon with steady, grounding energy. Emotional commitments made during this period tend to be durable and genuinely felt.",
    ("Saturn", "Moon", "square"):      "Saturn is squaring your natal Moon, which can bring emotional restriction, family strain, or a sense of carrying too much alone. The invitation is to clarify what you actually owe — and to whom.",
    ("Saturn", "Moon", "trine"):       "Saturn is flowing through your natal Moon, lending emotional steadiness and the ability to care for others without losing yourself. A quietly strong period for home and family life.",
    ("Saturn", "Moon", "opposition"):  "Saturn is opposing your natal Moon, putting the balance between personal need and public duty in uncomfortable relief. What you have been suppressing emotionally asks for honest attention.",

    ("Saturn", "Mercury", "conjunction"): "Transiting Saturn is conjunct your natal Mercury — a serious, focused period for the mind. Depth of thought is rewarded; scattered thinking is pruned. Excellent for writing, research, or any disciplined intellectual project.",
    ("Saturn", "Mercury", "sextile"):    "Saturn is supporting your natal Mercury, making this a productive window for structured thinking and careful communication. What you commit to in writing now tends to hold.",
    ("Saturn", "Mercury", "square"):     "Saturn is squaring your natal Mercury, which can produce mental heaviness, self-censorship, or blocked communication. Patience with the slow, careful thought pays off better than forcing output.",
    ("Saturn", "Mercury", "trine"):      "Saturn is flowing through your natal Mercury, making this an excellent period for serious intellectual work, precise writing, and communication that builds trust through clarity.",
    ("Saturn", "Mercury", "opposition"): "Saturn is opposing your natal Mercury, surfacing critical feedback or demanding that your ideas prove their worth. The pressure, though uncomfortable, sharpens what matters.",

    ("Saturn", "Venus", "conjunction"): "Transiting Saturn is conjunct your natal Venus, which can bring a sober, sometimes challenging period in relationships and finances. What is real and lasting is being distinguished from what was held by momentum alone.",
    ("Saturn", "Venus", "sextile"):    "Saturn is gently supporting your natal Venus, making this a period where committed relationships deepen and financial planning pays off. Love that endures is being built right now.",
    ("Saturn", "Venus", "square"):     "Saturn is squaring your natal Venus, which can create emotional distance, relational duty, or financial strain. What you most need may feel hard to ask for — but honest request is the path.",
    ("Saturn", "Venus", "trine"):      "Saturn is flowing through your natal Venus, supporting lasting commitments in love and finances. Relationships that have been tested are now rewarded with genuine depth.",
    ("Saturn", "Venus", "opposition"): "Saturn is opposing your natal Venus, putting the weight of commitment and the question of what you truly value at the center of relationship experience. Accountability in love arrives from outside.",

    ("Saturn", "Mars", "conjunction"): "Transiting Saturn is conjunct your natal Mars — a long, demanding alignment between will and restraint. Energy meets structure: raw drive is being shaped into something that can actually last.",
    ("Saturn", "Mars", "sextile"):    "Saturn is supporting your natal Mars with focused, disciplined energy. Effort applied in a sustained, structured way produces results that feel genuinely solid.",
    ("Saturn", "Mars", "square"):     "Saturn is squaring your natal Mars, which can produce blocked energy, authority friction, or frustration with the pace of progress. Patience and targeted effort work better than force.",
    ("Saturn", "Mars", "trine"):      "Saturn is flowing into your natal Mars — a rare alignment where drive and discipline operate in harmony. Sustained, purposeful effort during this period can reshape the structures of your life.",
    ("Saturn", "Mars", "opposition"): "Saturn is opposing your natal Mars, which surfaces tension between what you want to do and what external limits or authority will allow. The long view matters more than the immediate win.",

    ("Saturn", "Jupiter", "conjunction"): "Transiting Saturn is meeting your natal Jupiter, tempering optimism with realism. This is a period for sorting genuine opportunity from wishful thinking and building what you believe in on real foundations.",
    ("Saturn", "Jupiter", "sextile"):    "Saturn is gently supporting your natal Jupiter, making this a period where disciplined pursuit of a meaningful goal moves forward at a slow but steady and real pace.",
    ("Saturn", "Jupiter", "square"):     "Saturn is squaring your natal Jupiter — where the limits of optimism become visible. Dreams are being tested; what survives the test is worth pursuing with renewed seriousness.",
    ("Saturn", "Jupiter", "trine"):      "Saturn is flowing through your natal Jupiter in a way that allows for responsible expansion. Growth during this period is real because it is being built on ground that can hold it.",
    ("Saturn", "Jupiter", "opposition"): "Saturn is opposing your natal Jupiter, putting the tension between what you have aspired toward and what you have actually built in front of you. Honest accounting opens the next chapter.",

    ("Saturn", "Saturn", "conjunction"): "Transiting Saturn has returned to its natal position — your Saturn return, arriving roughly every 29 years. This is one of the most significant transits in adult life, calling for a full accounting of who you are and what you will build next.",
    ("Saturn", "Saturn", "sextile"):    "Saturn is in easy alignment with your natal Saturn, a quieter but productive period for consolidating structures and taking responsibility seriously. Progress is steady.",
    ("Saturn", "Saturn", "square"):     "Saturn is squaring its natal position — a turning point in the Saturn cycle. What you built at the last return is being tested. Reinforce what is sound; release what has served its purpose.",
    ("Saturn", "Saturn", "trine"):      "Saturn is trine its natal position, making this a period where your relationship with responsibility, structure, and long-term commitment flows with unusual ease.",
    ("Saturn", "Saturn", "opposition"): "Saturn is opposing its natal position — the midpoint of the Saturn cycle. You are accountable to a version of yourself that made promises some years ago. Where do they stand?",

    ("Saturn", "Uranus", "conjunction"): "Transiting Saturn is meeting your natal Uranus, pressing the tension between security and freedom into sharp focus. This multi-year passage requires innovating within real constraints.",
    ("Saturn", "Uranus", "sextile"):    "Saturn is gently supporting your natal Uranus, making this a period where innovation and structure can actually work together. Unconventional moves made carefully tend to hold.",
    ("Saturn", "Uranus", "square"):     "Saturn is squaring your natal Uranus, creating tension between the desire for liberation and the weight of existing structure. Change is needed but recklessness is costly — find the disciplined path to freedom.",
    ("Saturn", "Uranus", "trine"):      "Saturn is flowing into your natal Uranus, making this a period where you can build something genuinely new without dismantling everything first. Creative innovation with lasting foundations is possible.",
    ("Saturn", "Uranus", "opposition"): "Saturn is opposing your natal Uranus, putting the conflict between your need for freedom and the demands of obligation at the center of this period. Neither can fully win — integration is the work.",

    ("Saturn", "Neptune", "conjunction"): "Transiting Saturn is conjunct your natal Neptune, pressing your ideals against reality in a sustained and sometimes disorienting way. What you believe is being tested; what survives is more than belief.",
    ("Saturn", "Neptune", "sextile"):    "Saturn is gently grounding your natal Neptune, making it easier to give practical form to your spiritual or creative vision. Dreams are finding their feet.",
    ("Saturn", "Neptune", "square"):     "Saturn is squaring your natal Neptune, which can dissolve illusions in ways that feel painful but ultimately clarifying. Where are you living in a story that doesn't match the facts?",
    ("Saturn", "Neptune", "trine"):      "Saturn is flowing through your natal Neptune, allowing creative and spiritual work to become practically meaningful. What you believe can now be expressed in a form that lasts.",
    ("Saturn", "Neptune", "opposition"): "Saturn is opposing your natal Neptune, calling you to account for where fantasy and reality have been confused. The discomfort of clarity is more useful than the comfort of illusion.",

    ("Saturn", "Pluto", "conjunction"): "Transiting Saturn is conjunct your natal Pluto — a rare, long alignment that brings deep transformation under deliberate pressure. What has been buried is meeting the surface; what needs to die will; what is essential will survive.",
    ("Saturn", "Pluto", "sextile"):    "Saturn is quietly supporting your natal Pluto, making this a period where deep, sustained work toward genuine transformation can proceed at a manageable pace.",
    ("Saturn", "Pluto", "square"):     "Saturn is squaring your natal Pluto, surfacing power struggles, compulsive patterns, or the places in your life where control is being exercised beyond its healthy scope. Something needs to fundamentally change.",
    ("Saturn", "Pluto", "trine"):      "Saturn is flowing through your natal Pluto in a way that allows deep transformation to proceed with unusual steadiness. What you rebuild now will be both powerful and durable.",
    ("Saturn", "Pluto", "opposition"): "Saturn is opposing your natal Pluto, which can surface encounters with institutional power, collective transformation, or the limits of personal control. The long arc of your life is being reshaped.",

    # ── Transiting Uranus ─────────────────────────────────────────────────────
    ("Uranus", "Sun", "conjunction"):  "Transiting Uranus is conjunct your natal Sun — a once-in-84-year alignment that often signals a radical reinvention of identity and purpose. What you thought you were is making room for who you actually need to become.",
    ("Uranus", "Sun", "sextile"):      "Uranus is sending an innovative beam to your natal Sun over a multi-year period, offering sustained opportunities to express yourself in freer, more authentic ways.",
    ("Uranus", "Sun", "square"):       "Uranus is squaring your natal Sun in a slow transit that brings disruption, restlessness, and the urgent need for authenticity. The life you've been living may no longer feel like your own.",
    ("Uranus", "Sun", "trine"):        "Uranus is flowing into your natal Sun over a multi-year period, supporting authentic self-expression and gradual liberation from roles that have outgrown you.",
    ("Uranus", "Sun", "opposition"):   "Uranus is opposing your natal Sun — a period often called the mid-life awakening, arriving in the mid-40s. External disruptions mirror the inner need for radical authenticity.",

    ("Uranus", "Moon", "conjunction"): "Transiting Uranus is conjunct your natal Moon over an extended period, shaking up your emotional foundations and domestic life in ways that demand a new relationship with need, belonging, and feeling.",
    ("Uranus", "Moon", "sextile"):     "Uranus is gently connecting with your natal Moon over time, opening new emotional possibilities and refreshing your relationship with home and belonging.",
    ("Uranus", "Moon", "square"):      "Uranus is squaring your natal Moon in a slow transit that can bring sudden emotional upheaval, unexpected changes in home or family life, and a hunger for emotional freedom.",
    ("Uranus", "Moon", "trine"):       "Uranus is flowing through your natal Moon over an extended period, making emotional innovation feel natural and beneficial. Old patterns of need and response are being refreshed.",
    ("Uranus", "Moon", "opposition"):  "Uranus is opposing your natal Moon, which can bring abrupt changes in domestic life or emotional experience that feel disorienting but ultimately liberating.",

    ("Uranus", "Mercury", "conjunction"): "Transiting Uranus is conjunct your natal Mercury over a multi-year period — a sustained electric charge to your thinking. Original ideas, sudden insights, and unconventional communication define this chapter.",
    ("Uranus", "Mercury", "sextile"):    "Uranus is gently supporting your natal Mercury with an innovative charge over time. New ideas and ways of thinking arrive with unusual regularity during this period.",
    ("Uranus", "Mercury", "square"):     "Uranus is squaring your natal Mercury in an extended passage that can make thinking erratic, communication surprising, or the mind eager to overturn what it previously believed.",
    ("Uranus", "Mercury", "trine"):      "Uranus is flowing through your natal Mercury over time, making this a period of genuine intellectual breakthrough and original communication. Think further than usual.",
    ("Uranus", "Mercury", "opposition"): "Uranus is opposing your natal Mercury, bringing new and often disruptive information that challenges how you think. The disruption points toward a needed update in perspective.",

    ("Uranus", "Venus", "conjunction"): "Transiting Uranus is conjunct your natal Venus over a multi-year period, revolutionizing your experience of love and what you value. Relationships that cannot accommodate your growing need for freedom may not survive.",
    ("Uranus", "Venus", "sextile"):    "Uranus is gently opening your natal Venus to new relational and creative possibilities over time. Unexpected connections and innovative ways of expressing love arise.",
    ("Uranus", "Venus", "square"):     "Uranus is squaring your natal Venus in a slow transit that can destabilize existing relationships or attract sudden and unconventional new ones. What feels like disruption is clarifying what you truly value.",
    ("Uranus", "Venus", "trine"):      "Uranus is flowing into your natal Venus, refreshing your relationship with love, creativity, and pleasure over an extended period. Innovation in these areas feels exciting and sustainable.",
    ("Uranus", "Venus", "opposition"): "Uranus is opposing your natal Venus, which can bring sudden relationship changes or revelations about what you truly want. Freedom and intimacy are working out a new arrangement.",

    ("Uranus", "Mars", "conjunction"): "Transiting Uranus is meeting your natal Mars over a multi-year period, electrifying your drive and making conventional channels feel too small. Bold, innovative action — and its risks — define this chapter.",
    ("Uranus", "Mars", "sextile"):    "Uranus is gently supporting your natal Mars, making this a period where unconventional effort and creative initiative find real traction.",
    ("Uranus", "Mars", "square"):     "Uranus is squaring your natal Mars in a slow, potentially disruptive transit. Anger, frustration, or the urge to break free may build suddenly. Direct the energy into deliberate innovation rather than impulsive break.",
    ("Uranus", "Mars", "trine"):      "Uranus is flowing through your natal Mars over an extended period, giving your drive a brilliantly unconventional quality. Breakthroughs in effort come from doing what has never been done before.",
    ("Uranus", "Mars", "opposition"): "Uranus is opposing your natal Mars, which can bring sudden confrontation with forces that challenge your will. The lesson is in finding freedom within the friction rather than against it.",

    ("Uranus", "Jupiter", "conjunction"): "Transiting Uranus is meeting your natal Jupiter, which can bring a sudden expansion of opportunity or a radical revision of your sense of what is possible. Think beyond your previous definition of lucky.",
    ("Uranus", "Jupiter", "sextile"):    "Uranus is gently supporting your natal Jupiter over time, opening inventive and unconventional channels for growth and opportunity. Something unexpected turns out to be the right path.",
    ("Uranus", "Jupiter", "square"):     "Uranus is squaring your natal Jupiter, amplifying the urge to break from what has limited your expansion. Avoid reckless leaps while pursuing genuine liberation.",
    ("Uranus", "Jupiter", "trine"):      "Uranus is flowing into your natal Jupiter, making this a genuinely lucky, inventive period for growth. The unexpected route is often the most rewarding one.",
    ("Uranus", "Jupiter", "opposition"): "Uranus is opposing your natal Jupiter, which can bring sudden opportunity alongside sudden reversals. The gift may arrive disguised as disruption.",

    ("Uranus", "Saturn", "conjunction"): "Transiting Uranus is conjunct your natal Saturn, forcing freedom and structure into direct encounter. This multi-year transit can dismantle outdated systems or make existing ones innovate profoundly.",
    ("Uranus", "Saturn", "sextile"):    "Uranus is gently loosening your natal Saturn over time, making it possible to reform your structures with creativity rather than just maintain them.",
    ("Uranus", "Saturn", "square"):     "Uranus is squaring your natal Saturn — a slow, persistent friction between the need for change and the weight of existing structure. Reform rather than revolution tends to yield better results.",
    ("Uranus", "Saturn", "trine"):      "Uranus is flowing through your natal Saturn, allowing existing structures to be innovated and refreshed rather than simply maintained. What was rigid becomes adaptive.",
    ("Uranus", "Saturn", "opposition"): "Uranus is opposing your natal Saturn, which can bring sudden encounters with authority or the collapse of structures that were too rigid to bend. What can adapt will survive and grow.",

    ("Uranus", "Uranus", "conjunction"): "Transiting Uranus has returned to its natal position — your Uranus return, arriving around age 84. A life-review of authenticity, freedom, and the choices made in service of genuine self-expression.",
    ("Uranus", "Uranus", "sextile"):    "Uranus is in easy alignment with your natal Uranus, a period that opens mild but genuine opportunities for innovation, freedom, and authenticity in daily life.",
    ("Uranus", "Uranus", "square"):     "Uranus is squaring its natal position — a turning point in the 84-year cycle. Authenticity, freedom, and originality are being called to a new level of expression.",
    ("Uranus", "Uranus", "trine"):      "Uranus is trine your natal Uranus, which makes this a period of natural alignment between the person you are and the freedom you need. Inventive choices tend to succeed.",
    ("Uranus", "Uranus", "opposition"): "Uranus is opposing its natal position — the mid-life Uranus opposition, arriving around age 42. The most significant Uranian transit of adult life: who are you beyond the roles you've accumulated?",

    ("Uranus", "Neptune", "conjunction"): "Transiting Uranus is meeting your natal Neptune in a generational alignment. Old spiritual or collective ideals may be disrupted; new and more authentic visions emerge from the break.",
    ("Uranus", "Neptune", "sextile"):    "Uranus is gently opening your natal Neptune over time, inviting creative and spiritual renovation that feels both liberating and inspired.",
    ("Uranus", "Neptune", "square"):     "Uranus is squaring your natal Neptune in a slow transit that can dissolve long-held spiritual assumptions or creative ideals in ways that are disorienting but ultimately clarifying.",
    ("Uranus", "Neptune", "trine"):      "Uranus is flowing into your natal Neptune, bringing inspired innovation to your spiritual, creative, or compassionate impulses over an extended period.",
    ("Uranus", "Neptune", "opposition"): "Uranus is opposing your natal Neptune, bringing external disruption to long-cherished ideals or spiritual frameworks. What is genuinely true will hold; what was illusion will not.",

    ("Uranus", "Pluto", "conjunction"): "Transiting Uranus is meeting your natal Pluto in a generational alignment that can catalyze radical, collective transformation through the most personal dimensions of your life.",
    ("Uranus", "Pluto", "sextile"):    "Uranus is gently supporting your natal Pluto over time, making deep transformation feel innovative rather than catastrophic. Change happens organically.",
    ("Uranus", "Pluto", "square"):     "Uranus is squaring your natal Pluto — a slow, intense transit associated with radical collective and personal upheaval. Power structures are being broken open; authenticity demands transformation.",
    ("Uranus", "Pluto", "trine"):      "Uranus is flowing through your natal Pluto over an extended period, making deep transformation feel evolutionary and inventive rather than violent.",
    ("Uranus", "Pluto", "opposition"): "Uranus is opposing your natal Pluto, which can surface the tension between freedom and power in significant ways. What must transform is now in direct contact with what would prefer to remain as-is.",

    # ── Transiting Neptune ────────────────────────────────────────────────────
    ("Neptune", "Sun", "conjunction"):  "Transiting Neptune is conjunct your natal Sun — a multi-year spiritual passage that can dissolve the ego's certainties and open a profound sensitivity to something larger. Identity becomes porous, which is both the gift and the risk.",
    ("Neptune", "Sun", "sextile"):      "Neptune is sending a gentle spiritual current to your natal Sun over time, softening the ego's edges and inviting a more inspired, compassionate expression of self.",
    ("Neptune", "Sun", "square"):       "Neptune is squaring your natal Sun in a slow transit that can blur self-definition and invite confusion, self-deception, or a deep spiritual seeking. Be honest about where the fog is your own creation.",
    ("Neptune", "Sun", "trine"):        "Neptune is flowing into your natal Sun over a multi-year period, lending a transcendent, creative, and spiritually sensitive quality to your identity and self-expression.",
    ("Neptune", "Sun", "opposition"):   "Neptune is opposing your natal Sun, dissolving the boundary between who you are and who others project onto you. Clarity about identity becomes essential precisely because it is elusive.",

    ("Neptune", "Moon", "conjunction"): "Transiting Neptune is conjunct your natal Moon — a long, deeply sensitive passage. Emotional boundaries thin almost to transparency; compassion and spiritual experience open; confusion and escapism are the shadow side.",
    ("Neptune", "Moon", "sextile"):     "Neptune is gently supporting your natal Moon over time, opening your emotional life to deeper empathy, spiritual sensitivity, and creative feeling.",
    ("Neptune", "Moon", "square"):      "Neptune is squaring your natal Moon in a slow transit that can blur emotional boundaries, invite confusion about what you feel, or pull toward escapist comfort. What are you avoiding feeling?",
    ("Neptune", "Moon", "trine"):       "Neptune is flowing through your natal Moon, making this a period of deep emotional receptivity, creative inspiration, and spiritual sensitivity in the realm of feeling and belonging.",
    ("Neptune", "Moon", "opposition"):  "Neptune is opposing your natal Moon, which can make emotional reality feel dreamlike or hard to grasp. Projection and idealization in close relationships need compassionate examination.",

    ("Neptune", "Mercury", "conjunction"): "Transiting Neptune is conjunct your natal Mercury — a long, sometimes disorienting transit that softens rational thinking and opens extraordinary creative, intuitive, and spiritual channels.",
    ("Neptune", "Mercury", "sextile"):    "Neptune is gently supporting your natal Mercury over time, inspiring creative writing, intuitive communication, and a more poetic way of thinking.",
    ("Neptune", "Mercury", "square"):     "Neptune is squaring your natal Mercury in a slow transit that can blur mental clarity, invite confusion, or make concentration elusive. Creative and spiritual thinking flourish; factual precision needs extra care.",
    ("Neptune", "Mercury", "trine"):      "Neptune is flowing into your natal Mercury over a multi-year period, making this a time of extraordinary imaginative, poetic, and spiritually attuned communication.",
    ("Neptune", "Mercury", "opposition"): "Neptune is opposing your natal Mercury, which can make it hard to know what you actually think versus what you've absorbed from the emotional atmosphere around you. Clarity is a discipline.",

    ("Neptune", "Venus", "conjunction"): "Transiting Neptune is conjunct your natal Venus — a long transit that elevates love and creativity to spiritual heights while dissolving practical boundaries. Idealization is the shadow; transcendent connection is the gift.",
    ("Neptune", "Venus", "sextile"):    "Neptune is gently opening your natal Venus over time to more refined, spiritually attuned love and creative expression.",
    ("Neptune", "Venus", "square"):     "Neptune is squaring your natal Venus in a slow transit that can cloud romantic judgment with idealization or cause financial decisions to drift from reality. See love and money as they are.",
    ("Neptune", "Venus", "trine"):      "Neptune is flowing through your natal Venus over a multi-year period, making love, art, and beauty feel genuinely transcendent. The highest expression of compassionate love is possible.",
    ("Neptune", "Venus", "opposition"): "Neptune is opposing your natal Venus, which can blur the line between genuine love and romantic fantasy. Grounding the heart in honesty protects the relationship.",

    ("Neptune", "Mars", "conjunction"): "Transiting Neptune is conjunct your natal Mars — a long, often confusing transit for will and action. Drive disperses or becomes spiritually redirected; passive acceptance and inspired sacrifice are the extremes.",
    ("Neptune", "Mars", "sextile"):    "Neptune is gently supporting your natal Mars over time, allowing inspired, idealistic action to be effective. Moving toward something you believe in deeply is well-supported.",
    ("Neptune", "Mars", "square"):     "Neptune is squaring your natal Mars in a slow transit that can dissipate energy or make goals feel unclear. Acting on genuine conviction rather than wishful impulse is essential.",
    ("Neptune", "Mars", "trine"):      "Neptune is flowing into your natal Mars, making purposeful action aligned with a larger vision feel natural. Creative and spiritually motivated effort is especially effective.",
    ("Neptune", "Mars", "opposition"): "Neptune is opposing your natal Mars, which can make it hard to know what you are actually fighting for. Reconnect with genuine conviction before expending energy.",

    ("Neptune", "Jupiter", "conjunction"): "Transiting Neptune is meeting your natal Jupiter — a long transit that can expand spiritual and creative vision to extraordinary proportions. Inspiration is immense; keep one foot in discernible reality.",
    ("Neptune", "Jupiter", "sextile"):    "Neptune is gently supporting your natal Jupiter over time, expanding spiritual and creative horizons with idealistic but genuine possibility.",
    ("Neptune", "Jupiter", "square"):     "Neptune is squaring your natal Jupiter, which can expand illusion as readily as vision. Where is your optimism outpacing honest assessment of facts?",
    ("Neptune", "Jupiter", "trine"):      "Neptune is flowing through your natal Jupiter — a period of expansive spiritual imagination and inspired generosity. What you believe in deeply can grow into something transcendent.",
    ("Neptune", "Jupiter", "opposition"): "Neptune is opposing your natal Jupiter, inflating idealism beyond what reality can comfortably hold. The wisdom is in knowing which beliefs to keep and which to release.",

    ("Neptune", "Saturn", "conjunction"): "Transiting Neptune is conjunct your natal Saturn, dissolving structures that have provided definition and security. What is genuinely real will hold; what was maintained through habit or fear will soften away.",
    ("Neptune", "Saturn", "sextile"):    "Neptune is gently connecting with your natal Saturn, helping you give spiritual or creative vision a workable form over time.",
    ("Neptune", "Saturn", "square"):     "Neptune is squaring your natal Saturn in a slow transit that can dissolve hard-won structures or undermine confidence in what you have built. Which limits are real and which are imagined?",
    ("Neptune", "Saturn", "trine"):      "Neptune is flowing into your natal Saturn, making this a period where spiritual depth and practical structure can support each other in a genuinely productive way.",
    ("Neptune", "Saturn", "opposition"): "Neptune is opposing your natal Saturn, putting the tension between material form and spiritual dissolution at the center of an extended chapter. What still has real meaning?",

    ("Neptune", "Uranus", "conjunction"): "Transiting Neptune is meeting your natal Uranus in a generational configuration. Collective dreams and ideals are reshaping the territory of freedom and innovation.",
    ("Neptune", "Uranus", "sextile"):    "Neptune is gently supporting your natal Uranus over time, opening a channel where intuition and innovation work together rather than in opposition.",
    ("Neptune", "Uranus", "square"):     "Neptune is squaring your natal Uranus in a slow transit that can blur the line between liberation and escape. Is the freedom you're pursuing real, or is it avoidance in disguise?",
    ("Neptune", "Uranus", "trine"):      "Neptune is flowing through your natal Uranus, lending an inspired, visionary quality to the Uranian themes of freedom, originality, and change over time.",
    ("Neptune", "Uranus", "opposition"): "Neptune is opposing your natal Uranus, bringing collective idealism into tension with the need for authentic individual freedom. What does real liberation actually require?",

    ("Neptune", "Neptune", "conjunction"): "Transiting Neptune is conjunct its natal position — your Neptune return, arriving around age 165 and never actually experienced. In practice, Neptune opposing or squaring itself (earlier in life) is the relevant transit.",
    ("Neptune", "Neptune", "sextile"):    "Neptune is in easy alignment with your natal Neptune, a period of gentle spiritual and creative opening. Imagination and compassion flow with quiet ease.",
    ("Neptune", "Neptune", "square"):     "Neptune is squaring its natal position — a significant generational transit in midlife that invites a reckoning with illusions, ideals, and the gap between vision and lived reality.",
    ("Neptune", "Neptune", "trine"):      "Neptune is trine its natal position, making this a period of natural spiritual and creative flow. Long-held dreams may find quiet but meaningful expression.",
    ("Neptune", "Neptune", "opposition"): "Neptune is opposing its natal position — a generational transit arriving around age 84 that can be a profoundly spiritual or dissolving chapter of late life.",

    ("Neptune", "Pluto", "conjunction"): "Transiting Neptune is meeting your natal Pluto — a generational alignment that occurs very rarely and speaks to collective forces of dissolution and transformation far larger than any individual life.",
    ("Neptune", "Pluto", "sextile"):    "Neptune is gently supporting your natal Pluto in a generational alignment, opening space for idealistic, deeply felt transformation to unfold slowly and meaningfully.",
    ("Neptune", "Pluto", "square"):     "Neptune is squaring your natal Pluto in a rare generational transit. Collective dissolution and transformation are pressing on the structures of power and meaning in deep and sustained ways.",
    ("Neptune", "Pluto", "trine"):      "Neptune is flowing into your natal Pluto in a generational alignment that opens spiritual depth and collective transformation to a period of quiet but profound unfolding.",
    ("Neptune", "Pluto", "opposition"): "Neptune is opposing your natal Pluto — one of the rarest generational alignments. Forces of dissolution and transformation are in profound tension at the collective level.",

    # ── Transiting Pluto ──────────────────────────────────────────────────────
    ("Pluto", "Sun", "conjunction"):   "Transiting Pluto is conjunct your natal Sun — one of the most transformative transits possible. Identity is being stripped to its core, rebuilt from what is most essential, most real, most yours. This is not a small chapter.",
    ("Pluto", "Sun", "sextile"):       "Pluto is sending a quiet but powerful signal to your natal Sun over years, enabling deep, purposeful self-transformation at a pace you can absorb.",
    ("Pluto", "Sun", "square"):        "Pluto is squaring your natal Sun in a long, intense transit. External forces and internal compulsions are pressing your identity to reveal what it's actually made of. Real power emerges through honest surrender.",
    ("Pluto", "Sun", "trine"):         "Pluto is flowing into your natal Sun over a multi-year period, supporting deep personal transformation that feels evolutionary rather than violent. You are becoming more of who you were always meant to be.",
    ("Pluto", "Sun", "opposition"):    "Pluto is opposing your natal Sun — a sustained encounter with transformative power arriving from outside. Relationships and external forces are the catalysts for a profound reckoning with identity.",

    ("Pluto", "Moon", "conjunction"):  "Transiting Pluto is conjunct your natal Moon in a long, emotionally intense transit. Deep unconscious material surfaces; family patterns, grief, and the roots of emotional life are being transformed from the foundation.",
    ("Pluto", "Moon", "sextile"):      "Pluto is gently supporting your natal Moon over time, enabling deep emotional transformation that proceeds at a sustainable pace. Old patterns of feeling give way to more authentic ones.",
    ("Pluto", "Moon", "square"):       "Pluto is squaring your natal Moon in a sustained, emotionally demanding transit. Buried feelings, family wounds, and unconscious compulsions are surfacing for honest examination and release.",
    ("Pluto", "Moon", "trine"):        "Pluto is flowing through your natal Moon, allowing deep emotional renewal to happen gradually and purposefully. What has been carried unconsciously is being acknowledged and transformed.",
    ("Pluto", "Moon", "opposition"):   "Pluto is opposing your natal Moon in an extended transit that can surface power struggles in intimate relationships or the forced confrontation of deep emotional patterns. What cannot remain hidden is coming to light.",

    ("Pluto", "Mercury", "conjunction"): "Transiting Pluto is conjunct your natal Mercury — a long transit that transforms how you think, what you say, and what you are willing to know. Communication and investigation reach an unusual depth and power.",
    ("Pluto", "Mercury", "sextile"):    "Pluto is gently deepening your natal Mercury over time, enabling penetrating insight and the willingness to investigate what lies beneath the obvious.",
    ("Pluto", "Mercury", "square"):     "Pluto is squaring your natal Mercury in an extended transit that can produce obsessive thinking, forced revelation of what was hidden, or the need to completely rebuild your intellectual framework.",
    ("Pluto", "Mercury", "trine"):      "Pluto is flowing through your natal Mercury over time, making this a period of profound intellectual depth, investigative skill, and transformative communication.",
    ("Pluto", "Mercury", "opposition"): "Pluto is opposing your natal Mercury, which can bring encounters with information or perspectives that permanently change how you see things. Truth is the only useful response.",

    ("Pluto", "Venus", "conjunction"):  "Transiting Pluto is conjunct your natal Venus — a long, potentially transformative chapter in love and values. What you desire, what you are worth, and what you will accept in relationship are all being remade.",
    ("Pluto", "Venus", "sextile"):      "Pluto is gently deepening your natal Venus over time, enriching your experience of love and beauty with a layer of transformative meaning.",
    ("Pluto", "Venus", "square"):       "Pluto is squaring your natal Venus in a sustained transit that can intensify relationship dynamics, surface jealousy or power struggles, or force a reckoning with what you genuinely value.",
    ("Pluto", "Venus", "trine"):        "Pluto is flowing into your natal Venus over years, enabling love and creative expression to be transformed at a soul level without violence. Depth and beauty are working together.",
    ("Pluto", "Venus", "opposition"):   "Pluto is opposing your natal Venus in a long, intense transit. Relationship dynamics involving power, desire, and transformation are at the center of an extended and significant chapter.",

    ("Pluto", "Mars", "conjunction"):   "Transiting Pluto is conjunct your natal Mars — a rare, long alignment of will and transformation. Primal power is available; how it is directed determines whether this period produces extraordinary accomplishment or destruction.",
    ("Pluto", "Mars", "sextile"):       "Pluto is gently supporting your natal Mars over time, providing access to deep, sustained reserves of purposeful power. You can move what seemed immovable.",
    ("Pluto", "Mars", "square"):        "Pluto is squaring your natal Mars in a slow, intense transit. Power struggles, compulsive drives, and the transformation of how you use your will are central themes. Depth, not force, is what works.",
    ("Pluto", "Mars", "trine"):         "Pluto is flowing through your natal Mars over an extended period, enabling purposeful, transformative action that leaves lasting structural change in its wake.",
    ("Pluto", "Mars", "opposition"):    "Pluto is opposing your natal Mars in a long, demanding transit. Power dynamics that have been building must now be honestly confronted. The willingness to transform is the only real power available.",

    ("Pluto", "Jupiter", "conjunction"): "Transiting Pluto is meeting your natal Jupiter — a rare, potent alignment of transformation and expansion. Your sense of what is possible and what you believe are being fundamentally remade.",
    ("Pluto", "Jupiter", "sextile"):    "Pluto is quietly supporting your natal Jupiter over time, allowing expansion of the kind that is built on something genuinely real and deeply understood.",
    ("Pluto", "Jupiter", "square"):     "Pluto is squaring your natal Jupiter in a slow, powerful transit. The desire for growth is intense; what you are being asked to transform may be your most fundamental assumptions about meaning and possibility.",
    ("Pluto", "Jupiter", "trine"):      "Pluto is flowing into your natal Jupiter over time, enabling transformation and growth to work together in a way that is both deep and expansive.",
    ("Pluto", "Jupiter", "opposition"): "Pluto is opposing your natal Jupiter — a long encounter with the gap between ambitious vision and the power required to truly transform. What must you give up to genuinely grow?",

    ("Pluto", "Saturn", "conjunction"): "Transiting Pluto is conjunct your natal Saturn — a rare, generational-scale transit that dismantles and rebuilds the deepest structures of your life. What has outlasted its purpose is being cleared for what is essential.",
    ("Pluto", "Saturn", "sextile"):    "Pluto is gently supporting your natal Saturn over time, enabling the gradual transformation of structures and commitments in ways that are durable rather than violent.",
    ("Pluto", "Saturn", "square"):     "Pluto is squaring your natal Saturn in a slow, demanding transit. Power and structure are in direct conflict; what does not serve its genuine purpose is being dismantled under unusual pressure.",
    ("Pluto", "Saturn", "trine"):      "Pluto is flowing through your natal Saturn over an extended period, allowing deep transformation of your structures, commitments, and relationship with authority to occur at a sustainable pace.",
    ("Pluto", "Saturn", "opposition"): "Pluto is opposing your natal Saturn, surfacing an extended encounter with the limits of what you have built and the transformative forces that press against those limits.",

    ("Pluto", "Uranus", "conjunction"): "Transiting Pluto is meeting your natal Uranus — a generational alignment associated with radical collective transformation breaking open the structures of freedom and innovation.",
    ("Pluto", "Uranus", "sextile"):    "Pluto is gently supporting your natal Uranus over time, enabling deep transformation of the Uranian themes — freedom, originality, and revolution — at a manageable pace.",
    ("Pluto", "Uranus", "square"):     "Pluto is squaring your natal Uranus in a rare, slow transit. Radical transformation and systemic rupture of freedom-constraining structures are the themes of this long chapter.",
    ("Pluto", "Uranus", "trine"):      "Pluto is flowing into your natal Uranus in a generational alignment that allows deep transformation of social and personal structures of freedom to proceed organically.",
    ("Pluto", "Uranus", "opposition"): "Pluto is opposing your natal Uranus — a generational transit that places transformative power in direct tension with the need for radical freedom. Collective and personal structures are under extraordinary pressure.",

    ("Pluto", "Neptune", "conjunction"): "Transiting Pluto is meeting your natal Neptune — one of the rarest and most generational alignments, speaking to the dissolution and transformation of the deepest collective ideals and spiritual frameworks.",
    ("Pluto", "Neptune", "sextile"):    "Pluto is gently supporting your natal Neptune in a long generational alignment. Collective transformation and spiritual evolution are working together at the largest possible scale.",
    ("Pluto", "Neptune", "square"):     "Pluto is squaring your natal Neptune — a rare, slow generational transit. Deep spiritual or collective ideals are being broken open and transformed from the core.",
    ("Pluto", "Neptune", "trine"):      "Pluto is flowing into your natal Neptune in a generational alignment that allows the deepest spiritual and creative visions to be transformed into something enduring.",
    ("Pluto", "Neptune", "opposition"): "Pluto is opposing your natal Neptune — a rare generational alignment where transformative power and spiritual dissolution are in direct, sustained tension.",

    ("Pluto", "Pluto", "conjunction"):  "Transiting Pluto is conjunct its natal position — your Pluto return, arriving around age 248. No human lives to experience it; nations and civilizations do. For individuals, the relevant Pluto transits are to other natal planets.",
    ("Pluto", "Pluto", "sextile"):      "Pluto is in easy alignment with its natal position — a generational transit that subtly supports deep, evolutionary transformation at the collective level.",
    ("Pluto", "Pluto", "square"):       "Pluto is squaring its natal position — a significant generational transit that marks a turning point in collective power structures, arriving for each generation in late adolescence or early adulthood.",
    ("Pluto", "Pluto", "trine"):        "Pluto is trine its natal position — a generational alignment that allows deep collective transformation to proceed with unusual ease and purposefulness.",
    ("Pluto", "Pluto", "opposition"):   "Pluto is opposing its natal position — a generational transit associated with radical collective transformation and the confrontation of accumulated power structures.",

    # ── Transit planets to natal Angles ───────────────────────────────────────
    # ASC: self-presentation, body, how you meet the world
    # DSC: relationships, partners, one-on-one encounters
    # MC:  career, public reputation, life direction
    # IC:  home, roots, private foundation, ancestry

    # Transiting Sun → Angles
    ("Sun", "ASC", "conjunction"):  "The Sun is crossing your Ascendant, putting you squarely in the spotlight. Your presence feels especially vital and visible right now — make the most of any public-facing moment.",
    ("Sun", "ASC", "sextile"):      "The Sun is sending supportive energy to your Ascendant, making it easy to project confidence and warmth. Others see you at your natural best in this window.",
    ("Sun", "ASC", "square"):       "The Sun is squaring your Ascendant, creating mild friction between how you want to show up and what the moment seems to demand. Adjust your style rather than forcing your usual approach.",
    ("Sun", "ASC", "trine"):        "The Sun is flowing into your Ascendant, lending natural vitality and magnetism to your presence. A good window for introductions, appearances, or any situation where first impressions count.",
    ("Sun", "ASC", "opposition"):   "The Sun is on your Descendant, shining a light on one-on-one relationships. Significant others — romantic or professional — are especially visible in your life right now.",

    ("Sun", "DSC", "conjunction"):  "The Sun is conjunct your Descendant, illuminating your relationship axis. A key partnership comes into focus — what you need from others and what you offer is unusually clear right now.",
    ("Sun", "DSC", "sextile"):      "The Sun is gently supporting your Descendant, making collaboration and relational warmth flow easily. Partnerships benefit from this light, open energy.",
    ("Sun", "DSC", "square"):       "The Sun is squaring your Descendant, which can surface tension in close partnerships or highlight where your needs and a partner's needs are misaligned. Honest negotiation works better than avoidance.",
    ("Sun", "DSC", "trine"):        "The Sun is flowing toward your Descendant, enriching partnerships with warmth and clarity. A good window for deepening a significant relationship or formalizing a collaboration.",
    ("Sun", "DSC", "opposition"):   "The Sun is on your Ascendant, turning the focus back onto you — how you present yourself directly affects your key relationships right now.",

    ("Sun", "MC", "conjunction"):   "The Sun is conjunct your Midheaven — one of the most career-activating transits possible. Your reputation, ambitions, and public role are illuminated. Visibility is high; show your best work.",
    ("Sun", "MC", "sextile"):       "The Sun is supporting your Midheaven right now, making professional effort feel recognized and purposeful. A good window for career conversations or advancing an important goal.",
    ("Sun", "MC", "square"):        "The Sun is squaring your Midheaven, creating pressure between your public ambitions and personal life. Something is asking you to reconcile what you show the world with what you actually want.",
    ("Sun", "MC", "trine"):         "The Sun is flowing into your Midheaven, making this an excellent window for professional advancement, public presentation, or any work that benefits from external visibility.",
    ("Sun", "MC", "opposition"):    "The Sun is opposite your Midheaven — on your IC — turning attention toward home and private life. Career and family may feel in competition; the inner life needs as much sunlight as the outer one.",

    ("Sun", "IC", "conjunction"):   "The Sun is on your IC, illuminating your roots, home, and private foundation. This is a time to tend to what nourishes you privately — family, home, and inner life all come into focus.",
    ("Sun", "IC", "sextile"):       "The Sun is gently supporting your IC, making home life feel warm and purposeful. A good window for family connection, domestic projects, or reconnecting with your roots.",
    ("Sun", "IC", "square"):        "The Sun is squaring your IC, which can create friction between career demands and home life, or stir questions about where you truly belong.",
    ("Sun", "IC", "trine"):         "The Sun is flowing into your IC, lending a nurturing, settled quality to home and family life. What grounds you privately is being quietly nourished.",
    ("Sun", "IC", "opposition"):    "The Sun is opposite your IC — on your Midheaven — pulling focus outward toward career and public life. Home and private needs may feel temporarily eclipsed.",

    # Transiting Moon → Angles
    ("Moon", "ASC", "conjunction"): "The Moon is crossing your Ascendant, making you more emotionally visible than usual. Others pick up easily on what you're feeling — authenticity serves you better than a composed front right now.",
    ("Moon", "ASC", "sextile"):     "The Moon is gently connecting with your Ascendant, lending a warm, approachable quality to your presence for these few hours. Social interactions feel naturally easy.",
    ("Moon", "ASC", "square"):      "The Moon is squaring your Ascendant, which can create a subtle mismatch between your inner mood and the face you present. Give yourself permission to feel without performing.",
    ("Moon", "ASC", "trine"):       "The Moon is flowing into your Ascendant right now, making your emotional presence feel safe and inviting to others. Connection comes naturally in this window.",
    ("Moon", "ASC", "opposition"):  "The Moon is opposite your Ascendant — on your Descendant — bringing emotional attunement to your relationships for a few hours. You feel others' needs keenly and they feel yours.",

    ("Moon", "DSC", "conjunction"): "The Moon is on your Descendant, heightening emotional sensitivity in one-on-one relationships. Feelings about a key partner — or the need for closeness itself — come sharply to the surface.",
    ("Moon", "DSC", "sextile"):     "The Moon is supporting your Descendant, making relational exchanges feel emotionally fluid and warm for a few hours. A good window for heartfelt conversation with someone important.",
    ("Moon", "DSC", "square"):      "The Moon is squaring your Descendant, which can stir emotional friction in partnerships or surface unspoken needs. Be honest rather than managing the other person's comfort.",
    ("Moon", "DSC", "trine"):       "The Moon is flowing into your Descendant, making this a naturally harmonious window for close relationships. Emotional openness between you and a partner or collaborator comes easily.",
    ("Moon", "DSC", "opposition"):  "The Moon is opposite your Descendant — on your Ascendant — which can make your own emotional state feel louder than what partners are bringing. Check the balance.",

    ("Moon", "MC", "conjunction"):  "The Moon is crossing your Midheaven, briefly putting your emotional state on public display. How you feel is visible in your professional life right now — authenticity is an asset.",
    ("Moon", "MC", "sextile"):      "The Moon is gently supporting your Midheaven, making career effort feel emotionally meaningful for a few hours. Public interactions benefit from your natural warmth.",
    ("Moon", "MC", "square"):       "The Moon is squaring your Midheaven, which can bring tension between professional demands and emotional needs. Noticing what you actually feel beneath the role is the useful work here.",
    ("Moon", "MC", "trine"):        "The Moon is flowing into your Midheaven right now, making professional engagement feel emotionally satisfying. Your public presence carries genuine warmth and draws people toward you.",
    ("Moon", "MC", "opposition"):   "The Moon is opposite your Midheaven — on your IC — pulling emotional energy toward home and private life for a few hours. The need for comfort and withdrawal is temporarily stronger than the pull of public ambition.",

    ("Moon", "IC", "conjunction"):  "The Moon is at your IC — the deepest point of the chart. Emotional needs around home, family, and belonging are at their most acute. Tending to your inner life is exactly the right priority.",
    ("Moon", "IC", "sextile"):      "The Moon is gently supporting your IC, making home feel like a genuine refuge and family connections feel easy and nourishing for a few hours.",
    ("Moon", "IC", "square"):       "The Moon is squaring your IC, which can surface tension between the demands of the outer world and the emotional pull of home and private life.",
    ("Moon", "IC", "trine"):        "The Moon is flowing into your IC right now, making the private, domestic side of life feel comforting and emotionally complete. A good few hours for home, rest, or family.",
    ("Moon", "IC", "opposition"):   "The Moon is opposite your IC — on your Midheaven — briefly pulling focus outward. Emotional energy is spent on public roles, while the private self waits quietly.",

    # Transiting Mercury → Angles
    ("Mercury", "ASC", "conjunction"): "Mercury is crossing your Ascendant, sharpening how you come across and what you lead with in conversation. Your mind is on display — a good time to articulate ideas you've been developing.",
    ("Mercury", "ASC", "sextile"):     "Mercury is supporting your Ascendant right now, making communication feel natural and your personal style feel intellectually engaging. Introductions and networking go well.",
    ("Mercury", "ASC", "square"):      "Mercury is squaring your Ascendant, which can make it hard to say exactly what you mean or have it land the way you intend. Take an extra moment before speaking.",
    ("Mercury", "ASC", "trine"):       "Mercury is flowing into your Ascendant, making your communication style especially appealing and clear right now. What you say and how you say it feel well-matched.",
    ("Mercury", "ASC", "opposition"):  "Mercury is opposite your Ascendant — on your Descendant — emphasizing dialogue and information exchange in relationships. Listening actively to a partner's perspective is especially productive.",

    ("Mercury", "DSC", "conjunction"): "Mercury is on your Descendant, activating communication within close partnerships. Important conversations about a relationship's terms, direction, or needs are well-timed right now.",
    ("Mercury", "DSC", "sextile"):     "Mercury is gently supporting your Descendant, making relational communication feel easy and productive. A good window for discussion, negotiation, or simply catching up with a significant person.",
    ("Mercury", "DSC", "square"):      "Mercury is squaring your Descendant, which can bring miscommunication or intellectual friction in partnerships. Say what you mean and invite the same in return.",
    ("Mercury", "DSC", "trine"):       "Mercury is flowing into your Descendant, making conversation with partners flow easily and productively. Contracts, agreements, and honest exchanges are all well-supported.",
    ("Mercury", "DSC", "opposition"):  "Mercury is opposite your Descendant — on your Ascendant — making your own voice especially prominent. Make sure you're leaving room for the other person to be heard.",

    ("Mercury", "MC", "conjunction"):  "Mercury is conjunct your Midheaven, making this an excellent window for professional communication, presentations, or any public-facing intellectual work. Your ideas carry weight right now.",
    ("Mercury", "MC", "sextile"):      "Mercury is supporting your Midheaven, making career communications feel well-timed and well-received. A good window for proposals, reports, or any important professional exchange.",
    ("Mercury", "MC", "square"):       "Mercury is squaring your Midheaven, which can bring mental pressure around career decisions or communication with authority figures. Think carefully before committing to a public position.",
    ("Mercury", "MC", "trine"):        "Mercury is flowing into your Midheaven, making professional communication especially sharp and effective right now. Ideas land well and the mind serves ambition seamlessly.",
    ("Mercury", "MC", "opposition"):   "Mercury is opposite your Midheaven — on your IC — which can turn mental energy toward home, family history, or private reflection rather than outward ambition. Useful for internal processing.",

    ("Mercury", "IC", "conjunction"):  "Mercury is at your IC, stimulating thought and conversation around home, family, and your private foundations. Planning around domestic matters or processing family history comes naturally.",
    ("Mercury", "IC", "sextile"):      "Mercury is gently supporting your IC, making family communication feel easy and domestic planning feel clear-headed. A good window for home-related decisions.",
    ("Mercury", "IC", "square"):       "Mercury is squaring your IC, which can bring mental restlessness around home life or difficult conversations within the family. Patience and clarity of intention help.",
    ("Mercury", "IC", "trine"):        "Mercury is flowing into your IC, making this a good window for thoughtful domestic planning, meaningful family conversations, or reconnecting intellectually with your roots.",
    ("Mercury", "IC", "opposition"):   "Mercury is opposite your IC — on your Midheaven — directing mental energy outward toward career and public life. Home and family are temporarily on the back burner of your thinking.",

    # Transiting Venus → Angles
    ("Venus", "ASC", "conjunction"):  "Venus is crossing your Ascendant, lending personal charm, warmth, and aesthetic appeal to your presence. Others are drawn to you naturally right now — a wonderful window for social events or creative self-expression.",
    ("Venus", "ASC", "sextile"):      "Venus is gently supporting your Ascendant, making you easy to like and pleasant to be around. Social and creative opportunities come through your natural charm.",
    ("Venus", "ASC", "square"):       "Venus is squaring your Ascendant, which can bring a mild tension between how you want to appear and what actually feels comfortable. Vanity or people-pleasing can surface — stay genuine.",
    ("Venus", "ASC", "trine"):        "Venus is flowing into your Ascendant, making this one of the nicest windows for social connection and creative self-presentation. You feel good in your skin and others respond in kind.",
    ("Venus", "ASC", "opposition"):   "Venus is opposite your Ascendant — on your Descendant — making beauty and affection a theme in your closest relationships. Love, aesthetics, and relational harmony come into sharp focus.",

    ("Venus", "DSC", "conjunction"):  "Venus is conjunct your Descendant, making this a peak window for romantic connection and partnership harmony. A relationship deepens, a new attraction begins, or existing bonds feel especially beautiful.",
    ("Venus", "DSC", "sextile"):      "Venus is supporting your Descendant, making partnership feel warm and mutually appreciative right now. A good window for smoothing rough edges in a relationship or deepening collaborative bonds.",
    ("Venus", "DSC", "square"):       "Venus is squaring your Descendant, which can surface tension between what you desire in a relationship and what the partnership currently offers. Honest discussion of values serves well here.",
    ("Venus", "DSC", "trine"):        "Venus is flowing into your Descendant, making close relationships feel especially harmonious and beautiful right now. Love is easy, collaboration is pleasant, and the give-and-take feels balanced.",
    ("Venus", "DSC", "opposition"):   "Venus is opposite your Descendant — on your Ascendant — turning personal charm inward. How you feel about yourself is the determining factor in how relationships feel right now.",

    ("Venus", "MC", "conjunction"):   "Venus is conjunct your Midheaven, one of the best transits for professional reputation and public appeal. Artistic work, social visibility, and career advancement all benefit from this graceful energy.",
    ("Venus", "MC", "sextile"):       "Venus is supporting your Midheaven, lending a pleasing quality to your professional interactions and public persona. Career efforts that require diplomacy or aesthetic sensibility flourish.",
    ("Venus", "MC", "square"):        "Venus is squaring your Midheaven, which can create tension between the desire for ease and the demands of professional ambition. Social niceties may not be enough — real effort is still required.",
    ("Venus", "MC", "trine"):         "Venus is flowing into your Midheaven, making your public presence attractive and your professional interactions pleasant. Creative careers, client work, and anything requiring social grace are especially well-supported.",
    ("Venus", "MC", "opposition"):    "Venus is opposite your Midheaven — on your IC — turning affection and beauty toward home and private life. The people and places that comfort you privately feel especially precious right now.",

    ("Venus", "IC", "conjunction"):   "Venus is at your IC, warming the home and private life with affection and beauty. A wonderful window for domestic pleasures, family harmony, and tending to what nourishes you at the root.",
    ("Venus", "IC", "sextile"):       "Venus is gently supporting your IC, making home feel like a place of beauty and comfort. Family relationships benefit from a gentle, appreciative tone.",
    ("Venus", "IC", "square"):        "Venus is squaring your IC, which can bring mild tension between the desire for domestic harmony and underlying family dynamics that need addressing. Surface sweetness won't resolve deeper friction.",
    ("Venus", "IC", "trine"):         "Venus is flowing into your IC, making home and family life feel genuinely pleasant and nourishing. A good window for beautifying your space or deepening family bonds.",
    ("Venus", "IC", "opposition"):    "Venus is opposite your IC — on your Midheaven — directing charm and beauty outward into the public world. Home life is temporarily in the background of your affections.",

    # Transiting Mars → Angles
    ("Mars", "ASC", "conjunction"):  "Mars is crossing your Ascendant, charging your physical presence with drive and assertiveness. You project energy and confidence easily now — channel it into purposeful action rather than letting it spill as aggression.",
    ("Mars", "ASC", "sextile"):      "Mars is supporting your Ascendant, giving you a confident, energized quality in how you come across. A good window to initiate something that requires personal boldness.",
    ("Mars", "ASC", "square"):       "Mars is squaring your Ascendant, which can produce friction between your drive and how others receive it. You may come across as more forceful than intended — adjust your approach without softening your intent.",
    ("Mars", "ASC", "trine"):        "Mars is flowing into your Ascendant, making you feel capable and assertive in exactly the right measure. Physical energy and personal presence are both high and well-directed.",
    ("Mars", "ASC", "opposition"):   "Mars is opposite your Ascendant — on your Descendant — activating the relationship axis with competitive or passionate energy. A significant encounter, confrontation, or intense connection is likely.",

    ("Mars", "DSC", "conjunction"):  "Mars is on your Descendant, bringing energy and possible tension into close partnerships. This can ignite passion or spark conflict — either way, something latent in a key relationship comes to a head.",
    ("Mars", "DSC", "sextile"):      "Mars is gently supporting your Descendant, making assertive partnership communication feel productive. A good window for moving a shared goal forward with confidence.",
    ("Mars", "DSC", "square"):       "Mars is squaring your Descendant, which can stir conflict or competitive friction in close relationships. The underlying issue is usually about unmet needs — address those rather than the argument.",
    ("Mars", "DSC", "trine"):        "Mars is flowing into your Descendant, giving partnerships an energized, forward-moving quality. Collaborative drive is high; what you build together now benefits from motivated, clear-eyed effort.",
    ("Mars", "DSC", "opposition"):   "Mars is opposite your Descendant — on your Ascendant — charging your personal presence. The energy is yours to direct; whether it serves or harms your relationships depends on how consciously you wield it.",

    ("Mars", "MC", "conjunction"):   "Mars is conjunct your Midheaven — a potent career transit. Ambition, drive, and willingness to compete are all amplified. This is a window for bold professional moves, but avoid burning bridges in the process.",
    ("Mars", "MC", "sextile"):       "Mars is supporting your Midheaven, lending confident momentum to career pursuits. A good window for pushing a professional project forward or making your ambitions visible.",
    ("Mars", "MC", "square"):        "Mars is squaring your Midheaven, creating tension between your drives and your professional situation. Frustration with authority or slow progress can be channeled into productive restructuring.",
    ("Mars", "MC", "trine"):         "Mars is flowing into your Midheaven, giving your career ambitions a direct, energized quality. Forward movement comes naturally; the effort you put in now tends to produce real professional results.",
    ("Mars", "MC", "opposition"):    "Mars is opposite your Midheaven — on your IC — driving energy toward home and private life. Ambition turns inward; domestic projects or family conflicts may demand the same intensity usually reserved for career.",

    ("Mars", "IC", "conjunction"):   "Mars is at your IC, stirring energy — and possibly conflict — in the domestic and private sphere. Family tensions may surface, or you may find the drive to tackle long-avoided home projects.",
    ("Mars", "IC", "sextile"):       "Mars is gently energizing your IC, making this a good window for home improvements, family initiatives, or addressing something in your private life that has needed attention.",
    ("Mars", "IC", "square"):        "Mars is squaring your IC, which can produce domestic friction or inner restlessness around your sense of belonging. Anger rooted in home or family history may need conscious acknowledgment.",
    ("Mars", "IC", "trine"):         "Mars is flowing into your IC, making it easier to take decisive action on home and family matters. Domestic energy is high and productive.",
    ("Mars", "IC", "opposition"):    "Mars is opposite your IC — on your Midheaven — driving ambition outward and possibly creating tension with home life. Career and domestic needs are competing for the same energy.",

    # Transiting Jupiter → Angles
    ("Jupiter", "ASC", "conjunction"):  "Jupiter is conjunct your Ascendant, expanding your presence and opening a window of genuine opportunity in how you move through the world. This transit often coincides with growth in confidence, visibility, and physical vitality.",
    ("Jupiter", "ASC", "sextile"):      "Jupiter is supporting your Ascendant, making your social presence feel open and fortunate. Opportunities arrive naturally through the way you show up — stay present and say yes.",
    ("Jupiter", "ASC", "square"):       "Jupiter is squaring your Ascendant, which can expand confidence into overreach. New possibilities are real, but taking on more than you can comfortably carry is the main hazard.",
    ("Jupiter", "ASC", "trine"):        "Jupiter is flowing into your Ascendant, making this a genuinely expansive window for personal growth, public connection, and forward-moving opportunity that fits your authentic self.",
    ("Jupiter", "ASC", "opposition"):   "Jupiter is opposite your Ascendant — on your Descendant — expanding your relationship world. Significant partnerships grow, new alliances form, and the benefits of collaboration are especially apparent.",

    ("Jupiter", "DSC", "conjunction"):  "Jupiter is conjunct your Descendant, expanding the relationship sphere in meaningful ways. A partnership grows significantly, a beneficial new connection arrives, or existing collaborations open to new possibility.",
    ("Jupiter", "DSC", "sextile"):      "Jupiter is gently supporting your Descendant, making partnership and collaboration feel generative and mutually beneficial. A good window for deepening important relationships.",
    ("Jupiter", "DSC", "square"):       "Jupiter is squaring your Descendant, which can expand relationship expectations beyond what is realistic. Optimism about a partnership needs checking against honest assessment.",
    ("Jupiter", "DSC", "trine"):        "Jupiter is flowing into your Descendant, making this an excellent period for partnerships, legal agreements, and any significant one-on-one collaboration that benefits from growth and goodwill.",
    ("Jupiter", "DSC", "opposition"):   "Jupiter is opposite your Descendant — on your Ascendant — expanding personal confidence and presence. The self is growing; ensure that growth enriches rather than overwhelms your relationships.",

    ("Jupiter", "MC", "conjunction"):   "Jupiter is conjunct your Midheaven — one of the most significant career transits possible. Professional expansion, recognition, and new opportunity are all amplified. This is a genuine peak for public life.",
    ("Jupiter", "MC", "sextile"):       "Jupiter is supporting your Midheaven, opening doors in career and public life with quiet but real good fortune. Move toward what you want professionally — the climate is genuinely receptive.",
    ("Jupiter", "MC", "square"):        "Jupiter is squaring your Midheaven, which can produce overconfidence in career matters or promises that outpace what you can deliver. Keep ambition grounded in what is actually achievable.",
    ("Jupiter", "MC", "trine"):         "Jupiter is flowing into your Midheaven, making this an excellent window for professional advancement, recognition, and public expansion. The effort you've put in is ready to be rewarded.",
    ("Jupiter", "MC", "opposition"):    "Jupiter is opposite your Midheaven — on your IC — expanding home, family, and private foundations. Domestic life grows or improves; inner resources are being enriched even if outer ambition is quieter.",

    ("Jupiter", "IC", "conjunction"):   "Jupiter is at your IC, bringing expansion and improvement to your home, family, and private foundations. This can mean a literal move, a growing family, or a profound deepening of your sense of belonging.",
    ("Jupiter", "IC", "sextile"):       "Jupiter is gently expanding your IC, making home life feel more spacious, generous, and supportive. A good window for family investment or strengthening your domestic foundation.",
    ("Jupiter", "IC", "square"):        "Jupiter is squaring your IC, which can bring growth in the private sphere that strains existing structures — a bigger home that is also a bigger responsibility, for example. Expand with care.",
    ("Jupiter", "IC", "trine"):         "Jupiter is flowing into your IC, making this a naturally abundant time for home, family, and the private life that sustains everything else. Roots grow deeper; the foundation becomes more generous.",
    ("Jupiter", "IC", "opposition"):    "Jupiter is opposite your IC — on your Midheaven — expanding public life and career. Home may temporarily feel less central as the outer world offers more opportunity than usual.",

    # Transiting Saturn → Angles
    ("Saturn", "ASC", "conjunction"):  "Saturn is conjunct your Ascendant — a significant, multi-year passage. Your identity, body, and the way you meet the world are being tested and ultimately strengthened. Maturity and authenticity become non-negotiable.",
    ("Saturn", "ASC", "sextile"):      "Saturn is supporting your Ascendant with quiet steadiness, making this a period where disciplined self-presentation and consistent effort earn gradual recognition.",
    ("Saturn", "ASC", "square"):       "Saturn is squaring your Ascendant, which can feel like a period of self-doubt or external pressure on how you show up. The friction points toward where greater authenticity or discipline is needed.",
    ("Saturn", "ASC", "trine"):        "Saturn is flowing into your Ascendant, lending a calm authority to your presence. How you carry yourself earns respect naturally, and responsibility feels manageable rather than burdensome.",
    ("Saturn", "ASC", "opposition"):   "Saturn is opposite your Ascendant — on your Descendant — placing the weight of accountability on close partnerships. Relationships that lack real foundations are being tested; those that are solid are deepened.",

    ("Saturn", "DSC", "conjunction"):  "Saturn is conjunct your Descendant, bringing serious attention to close partnerships. Relationships are tested for real depth — what is genuine deepens; what was held together by inertia may end.",
    ("Saturn", "DSC", "sextile"):      "Saturn is gently supporting your Descendant, making this a period where commitment in relationships is natural and rewarding. Long-term partnerships are built on firmer ground.",
    ("Saturn", "DSC", "square"):       "Saturn is squaring your Descendant, which can bring strain, distance, or hard accountability in significant relationships. What needs to be said or renegotiated can no longer be avoided.",
    ("Saturn", "DSC", "trine"):        "Saturn is flowing into your Descendant, supporting lasting relational commitments. Partnerships formed or deepened now are built on genuine mutual understanding and respect.",
    ("Saturn", "DSC", "opposition"):   "Saturn is opposite your Descendant — on your Ascendant — putting pressure on how you carry yourself rather than directly on your relationships. Your own discipline and authenticity are the key variables.",

    ("Saturn", "MC", "conjunction"):   "Saturn is conjunct your Midheaven — a defining career transit. Ambitions are tested against reality; what you are genuinely capable of is being clarified. The rewards of sustained effort, over years, may now arrive.",
    ("Saturn", "MC", "sextile"):       "Saturn is gently supporting your Midheaven, making structured career effort feel rewarded and purposeful. Professional progress is quiet but durable.",
    ("Saturn", "MC", "square"):        "Saturn is squaring your Midheaven, placing real pressure on career direction and public reputation. External obstacles or authority friction are pointing at where your professional foundations need reinforcing.",
    ("Saturn", "MC", "trine"):         "Saturn is flowing into your Midheaven, making disciplined professional effort translate into lasting achievement. A good window for building something in your public life that will endure.",
    ("Saturn", "MC", "opposition"):    "Saturn is opposite your Midheaven — on your IC — placing accountability on home and private foundations. What has been neglected in your inner life or family situation is now asking for serious attention.",

    ("Saturn", "IC", "conjunction"):   "Saturn is at your IC, pressing on your most private foundations — home, family, and the psychological roots of your sense of self. This is a serious passage that asks what you are truly built on.",
    ("Saturn", "IC", "sextile"):       "Saturn is gently supporting your IC, making this a good period for solidifying your domestic situation and taking quiet, durable responsibility for your private life.",
    ("Saturn", "IC", "square"):        "Saturn is squaring your IC, which can bring pressure from family history, home instability, or an unresolved sense of not-belonging. The invitation is to honestly examine your foundations.",
    ("Saturn", "IC", "trine"):         "Saturn is flowing into your IC, making it easier to build a stable, lasting private foundation. Domestic structures that are put in place now tend to hold.",
    ("Saturn", "IC", "opposition"):    "Saturn is opposite your IC — on your Midheaven — directing its weight toward career and public life. Private life is simplified while outer structures and responsibilities demand full attention.",

    # Transiting Uranus → Angles
    ("Uranus", "ASC", "conjunction"):  "Uranus is conjunct your Ascendant over a multi-year period — a radical reinvention of identity, appearance, and how you meet the world. Who you have been presenting yourself as no longer fits; who you are becoming is still taking shape.",
    ("Uranus", "ASC", "sextile"):      "Uranus is supporting your Ascendant over time, opening space for a freer, more authentic self-expression. Changes in your personal style or public identity feel liberating rather than destabilizing.",
    ("Uranus", "ASC", "square"):       "Uranus is squaring your Ascendant in an extended transit that can feel like the ground shifting under your sense of self. External disruptions mirror the need for a more authentic way of showing up.",
    ("Uranus", "ASC", "trine"):        "Uranus is flowing into your Ascendant over a multi-year period, allowing originality and authenticity to become natural features of how you present yourself in the world.",
    ("Uranus", "ASC", "opposition"):   "Uranus is opposite your Ascendant — on your Descendant — bringing sudden or unusual relationship developments over an extended period. Freedom, individuality, and the need for space are themes in significant partnerships.",

    ("Uranus", "DSC", "conjunction"):  "Uranus is conjunct your Descendant over a multi-year period, disrupting and reinventing your relationship sphere. Existing partnerships change dramatically or end; new and unconventional connections arrive.",
    ("Uranus", "DSC", "sextile"):      "Uranus is gently supporting your Descendant over time, bringing fresh, inventive energy into relationships. Unusual connections and new collaborative possibilities open up.",
    ("Uranus", "DSC", "square"):       "Uranus is squaring your Descendant in a slow transit that can unsettle close partnerships or trigger sudden changes in relationship status. Freedom and commitment are working out a new arrangement.",
    ("Uranus", "DSC", "trine"):        "Uranus is flowing into your Descendant, allowing relationships to become more authentic and free over time. The best partnerships during this period are those that can hold both intimacy and independence.",
    ("Uranus", "DSC", "opposition"):   "Uranus is opposite your Descendant — on your Ascendant — charging your identity with the urge for radical authenticity. Relationships feel the downstream effects of your own need to break from old patterns.",

    ("Uranus", "MC", "conjunction"):   "Uranus is conjunct your Midheaven — a career-disrupting, potentially career-liberating transit. Your professional direction undergoes sudden or radical change. What once felt like the right path may give way to something entirely unexpected.",
    ("Uranus", "MC", "sextile"):       "Uranus is supporting your Midheaven over time, bringing innovative opportunities into your career and encouraging unconventional paths to professional growth.",
    ("Uranus", "MC", "square"):        "Uranus is squaring your Midheaven in a slow transit that can bring unexpected disruptions to career or public reputation. The instability points toward needed change in your professional direction.",
    ("Uranus", "MC", "trine"):         "Uranus is flowing into your Midheaven over an extended period, allowing career innovation and authentic professional direction to develop without forcing a complete break from what came before.",
    ("Uranus", "MC", "opposition"):    "Uranus is opposite your Midheaven — on your IC — bringing sudden changes in home and private life that ripple outward. The foundations are shifting; the outer edifice of career and reputation responds in turn.",

    ("Uranus", "IC", "conjunction"):   "Uranus is at your IC over an extended period, disrupting home, family, and your deepest sense of belonging. Unexpected moves, family upheaval, or a radical re-rooting of your private life are common.",
    ("Uranus", "IC", "sextile"):       "Uranus is gently supporting your IC over time, opening new and freer possibilities for your home life and family structure. Domestic innovation feels exciting rather than unsettling.",
    ("Uranus", "IC", "square"):        "Uranus is squaring your IC in a slow transit that can unsettle home and family life or prompt a sudden reassessment of where — and with whom — you truly belong.",
    ("Uranus", "IC", "trine"):         "Uranus is flowing into your IC, making this an extended period of refreshing and reinventing your private foundations in ways that feel liberating rather than destabilizing.",
    ("Uranus", "IC", "opposition"):    "Uranus is opposite your IC — on your Midheaven — bringing radical change to public and professional life. The domestic sphere becomes quieter and more uncertain as the career axis undergoes its revolution.",

    # Transiting Neptune → Angles
    ("Neptune", "ASC", "conjunction"):  "Neptune is conjunct your Ascendant over a multi-year period, dissolving the edges of your identity and opening you to unusual sensitivity and spiritual permeability. Who you are becomes harder to define — and more expansive for it.",
    ("Neptune", "ASC", "sextile"):      "Neptune is gently connecting with your Ascendant over time, lending a spiritually attuned, compassionate quality to your presence. Others experience you as unusually empathetic and inspiring.",
    ("Neptune", "ASC", "square"):       "Neptune is squaring your Ascendant in a slow transit that can blur your sense of self or make it hard to know how you're coming across. Be wary of projection and idealization in how you present yourself.",
    ("Neptune", "ASC", "trine"):        "Neptune is flowing into your Ascendant over a multi-year period, making your personal presence more imaginative, spiritually open, and compassionate. Artistic and healing work flourish through how you show up.",
    ("Neptune", "ASC", "opposition"):   "Neptune is opposite your Ascendant — on your Descendant — dissolving boundaries in close relationships. The line between self and other becomes thin; clarity about what you project onto partners is essential.",

    ("Neptune", "DSC", "conjunction"):  "Neptune is conjunct your Descendant over a multi-year period, bringing idealism, spiritual depth, or confusion into close partnerships. Relationships may feel fated, transcendent — or require careful reality-testing.",
    ("Neptune", "DSC", "sextile"):      "Neptune is gently supporting your Descendant over time, inspiring compassionate, spiritually attuned connection in relationships. A meaningful partnership may feel almost soulmate-like.",
    ("Neptune", "DSC", "square"):       "Neptune is squaring your Descendant in a slow transit that can cloud relationship reality with idealization or confusion. See partners as they genuinely are, not as you wish or fear them to be.",
    ("Neptune", "DSC", "trine"):        "Neptune is flowing into your Descendant, making this an extended period of deep, spiritually attuned connection in partnerships. The highest form of compassionate love is accessible in close relationships right now.",
    ("Neptune", "DSC", "opposition"):   "Neptune is opposite your Descendant — on your Ascendant — dissolving the ego's clarity about identity. Relationships reflect back where your self-concept has become permeable or unclear.",

    ("Neptune", "MC", "conjunction"):   "Neptune is conjunct your Midheaven over a multi-year period, dissolving clarity about career direction and public identity. Confusion about purpose is real — but so is the opening toward a more spiritually meaningful vocation.",
    ("Neptune", "MC", "sextile"):       "Neptune is gently supporting your Midheaven, inspiring creative and spiritually aligned career work over time. A vocation with genuine meaning becomes more accessible.",
    ("Neptune", "MC", "square"):        "Neptune is squaring your Midheaven in a slow transit that can blur career goals or undermine public reputation through confusion or wishful thinking. Grounding your professional vision in concrete steps is essential.",
    ("Neptune", "MC", "trine"):         "Neptune is flowing into your Midheaven, making this a period where creative, healing, or spiritually meaningful work can be genuinely recognized and rewarded in the public sphere.",
    ("Neptune", "MC", "opposition"):    "Neptune is opposite your Midheaven — on your IC — dissolving private foundations in ways that are hard to name. Inner life becomes deeply fluid; the outer professional identity compensates by hardening or drifting.",

    ("Neptune", "IC", "conjunction"):   "Neptune is at your IC over a long period, dissolving the fixed sense of home, family, and roots. What once felt like solid ground becomes more fluid — spiritually rich and sometimes disorienting.",
    ("Neptune", "IC", "sextile"):       "Neptune is gently supporting your IC over time, opening your home and family life to greater compassion, imagination, and spiritual nourishment.",
    ("Neptune", "IC", "square"):        "Neptune is squaring your IC in a slow transit that can blur boundaries in family life or make the private foundations of your existence feel unstable. What is genuinely nourishing, and what is illusion?",
    ("Neptune", "IC", "trine"):         "Neptune is flowing into your IC, making home and family life feel spiritually nourishing and compassionately held over an extended period. The inner life becomes a genuine sanctuary.",
    ("Neptune", "IC", "opposition"):    "Neptune is opposite your IC — on your Midheaven — dissolving certainty about career and public direction. The outer world becomes misty as the inner private life asks for deeper spiritual honesty.",

    # Transiting Pluto → Angles
    ("Pluto", "ASC", "conjunction"):   "Pluto is conjunct your Ascendant in a rare, long transit — a total transformation of identity, body, and how you meet the world. Who you were before is being dismantled to make room for who you are becoming. The process is not gentle, but it is essential.",
    ("Pluto", "ASC", "sextile"):       "Pluto is gently supporting your Ascendant over time, enabling deep personal transformation to unfold at a sustainable pace. Your identity is evolving from the inside out.",
    ("Pluto", "ASC", "square"):        "Pluto is squaring your Ascendant in a slow, powerful transit. External events and internal pressure combine to force a fundamental change in how you carry yourself in the world. What is not genuinely you cannot survive this passage.",
    ("Pluto", "ASC", "trine"):         "Pluto is flowing into your Ascendant over a multi-year period, supporting a deep and purposeful transformation of identity and self-presentation. You emerge from this period more fully and authentically yourself.",
    ("Pluto", "ASC", "opposition"):    "Pluto is opposite your Ascendant — on your Descendant — bringing transformative forces through close relationships. Someone or something in your relationship sphere is the catalyst for a fundamental change in who you are.",

    ("Pluto", "DSC", "conjunction"):   "Pluto is conjunct your Descendant over an extended period, transforming your relationship sphere from the ground up. Significant partnerships end or are profoundly remade; the kinds of people and bonds you attract are fundamentally changing.",
    ("Pluto", "DSC", "sextile"):       "Pluto is gently deepening your Descendant over time, enriching close partnerships with unusual depth and transformative possibility.",
    ("Pluto", "DSC", "square"):        "Pluto is squaring your Descendant in a slow, intense transit. Power dynamics in close relationships are surfacing and demanding honest reckoning. What does not serve genuine mutual growth is being dismantled.",
    ("Pluto", "DSC", "trine"):         "Pluto is flowing into your Descendant, enabling deep and lasting transformation in close partnerships over time. Relationships that survive this period are profoundly real.",
    ("Pluto", "DSC", "opposition"):    "Pluto is opposite your Descendant — on your Ascendant — driving transformation through the self. The changes in who you are inevitably reshape who and what you attract in relationship.",

    ("Pluto", "MC", "conjunction"):    "Pluto is conjunct your Midheaven — a rare, defining career transit. Professional life is being stripped down and rebuilt from what is most essential and powerful. The public role you emerge with is fundamentally different from the one you entered with.",
    ("Pluto", "MC", "sextile"):        "Pluto is gently supporting your Midheaven over time, enabling deep, purposeful transformation in career and public life at a pace that can be absorbed and integrated.",
    ("Pluto", "MC", "square"):         "Pluto is squaring your Midheaven in a slow, demanding transit. Career structures, public reputation, or your relationship with authority are under intense pressure. What is most authentic about your ambitions is all that will remain.",
    ("Pluto", "MC", "trine"):          "Pluto is flowing into your Midheaven over an extended period, enabling a profound and lasting transformation of your career direction and public identity. What you build now in professional life carries unusual depth and consequence.",
    ("Pluto", "MC", "opposition"):     "Pluto is opposite your Midheaven — on your IC — bringing transformative pressure to home, family, and private foundations. The roots must be renegotiated before the outer structure of career and reputation can be genuinely renewed.",

    ("Pluto", "IC", "conjunction"):    "Pluto is at your IC in a rare, long transit, transforming your most private foundations — home, family history, and the psychological roots of your sense of self. What has been buried in the family lineage is surfacing for reckoning and release.",
    ("Pluto", "IC", "sextile"):        "Pluto is gently supporting your IC over time, enabling deep transformation of home and family life in ways that feel purposeful rather than catastrophic.",
    ("Pluto", "IC", "square"):         "Pluto is squaring your IC in a slow, powerful transit. Home instability, family upheaval, or the forced confrontation of deep psychological roots are themes. What was hidden in the foundations is now impossible to ignore.",
    ("Pluto", "IC", "trine"):          "Pluto is flowing into your IC over an extended period, allowing the deepest private foundations of your life to be transformed in ways that are lasting and genuinely healing.",
    ("Pluto", "IC", "opposition"):     "Pluto is opposite your IC — on your Midheaven — directing transformative pressure at career and public life. The private sphere must release old power structures before the public one can be genuinely rebuilt.",

    # ── Transit planets to natal Nodes ────────────────────────────────────────
    # North Node: soul's growth direction, evolutionary purpose
    # South Node: past-life comfort zone, ingrained habits, karmic inheritance

    # Transiting Sun → Nodes
    ("Sun", "North Node", "conjunction"):  "The Sun is crossing your North Node, directly activating your soul's growth direction. Identity and destiny are briefly aligned — encounters or opportunities that arise now have a way of pointing you toward who you are becoming rather than who you have been.",
    ("Sun", "North Node", "sextile"):      "The Sun is sending supportive light to your North Node, making it easy to take steps toward your evolutionary purpose. Opportunities that feel both comfortable and forward-moving are available; this window favors progress without force.",
    ("Sun", "North Node", "square"):       "The Sun is squaring your North Node, creating productive friction between current self-expression and your soul's growth direction. The tension may signal that how you are showing up needs to shift before forward movement becomes clear.",
    ("Sun", "North Node", "trine"):        "The Sun is flowing naturally into your North Node, lending clarity and ease to forward movement. Identity and growth direction are aligned, making this a good window for choices that move you toward your purpose rather than toward familiar comfort.",
    ("Sun", "North Node", "opposition"):   "The Sun is opposite your North Node — sitting on your South Node — illuminating the familiar territory of past patterns and old self-expression. Old habits of identity surface; the contrast with where you are growing toward becomes especially visible.",

    ("Sun", "South Node", "conjunction"):  "The Sun is crossing your South Node, bringing the familiar territory of past comfort zones into the light. Old strengths and ingrained patterns of self-expression resurface — a moment for recognizing what has served its purpose and what may be holding growth back.",
    ("Sun", "South Node", "sextile"):      "The Sun is gently supporting your South Node, making past gifts and familiar approaches feel accessible. Draw on established strengths while staying open to the forward-facing calls that sit just beyond the comfortable.",
    ("Sun", "South Node", "square"):       "The Sun is squaring your South Node, creating friction between who you want to be and the gravitational pull of old familiar patterns. The tension is useful — it names what needs to shift for genuine forward movement.",
    ("Sun", "South Node", "trine"):        "The Sun is flowing easily into your South Node, making old gifts and comfortable self-expression feel natural. The ease is genuine, but what is most comfortable may not be where the most growth is available right now.",
    ("Sun", "South Node", "opposition"):   "The Sun is opposite your South Node — sitting on your North Node — pulling identity toward its evolutionary edge. What you are becoming is more available than what you have been; the familiar feels distant while the unfamiliar feels strangely right.",

    # Transiting Moon → Nodes
    ("Moon", "North Node", "conjunction"):  "The Moon is crossing your North Node, stirring emotional activation around your soul's growth direction. Feelings and instincts may briefly point you toward what you are evolving into rather than what has always felt safe and familiar.",
    ("Moon", "North Node", "sextile"):      "The Moon is supporting your North Node with an easy emotional current. Feelings that point toward growth rather than comfort are available — following an instinct toward the new feels unusually natural in this window.",
    ("Moon", "North Node", "square"):       "The Moon is squaring your North Node, creating brief emotional friction between what feels instinctively safe and where your soul is calling you. The discomfort is temporary and informative — it names where emotional habit meets evolutionary necessity.",
    ("Moon", "North Node", "trine"):        "The Moon is flowing naturally into your North Node, giving emotional momentum to forward movement. Instincts and feelings briefly align with your growth direction, making it easier than usual to move toward what your life is asking of you.",
    ("Moon", "North Node", "opposition"):   "The Moon is opposite your North Node — touching your South Node — stirring up emotional comfort-seeking and familiar instinctive patterns. Old feelings are prominent right now; the invitation is ultimately to keep moving forward rather than retreating into the known.",

    ("Moon", "South Node", "conjunction"):  "The Moon is crossing your South Node, dredging up deeply familiar emotional patterns and instincts from the past. Old comfort-seeking behaviors and habitual feelings surface — a moment for recognition rather than indulgence of what no longer serves growth.",
    ("Moon", "South Node", "sextile"):      "The Moon is supporting your South Node with gentle emotional ease. Past emotional patterns and familiar comforts are accessible — useful in moderation, and worth noticing when they substitute for the harder work of genuine development.",
    ("Moon", "South Node", "square"):       "The Moon is squaring your South Node, creating brief emotional friction with ingrained patterns. Something about a habitual emotional response or comfort-seeking behavior is being nudged — the tension is pointing at what needs to shift.",
    ("Moon", "South Node", "trine"):        "The Moon is flowing into your South Node, making familiar emotional territory feel especially comfortable and safe. The ease is real, but so is the risk of defaulting to old patterns; the invitation is to enjoy the comfort without letting it substitute for growth.",
    ("Moon", "South Node", "opposition"):   "The Moon is opposite your South Node — touching your North Node — giving emotional momentum to your growth direction. The pull toward the new is stronger than usual; what feels instinctively safe and what your soul is growing toward are briefly in productive tension.",

    # Transiting Mercury → Nodes
    ("Mercury", "North Node", "conjunction"):  "Mercury is crossing your North Node, activating the mind in service of your soul's growth direction. Conversations, ideas, or information that arrive now have a way of orienting you forward — pay close attention to what gets said or thought in this window.",
    ("Mercury", "North Node", "sextile"):      "Mercury is sending supportive mental energy to your North Node, making it easy to think and speak in ways that serve your growth direction. A good window for conversations that open doors or ideas that point meaningfully toward what you are becoming.",
    ("Mercury", "North Node", "square"):       "Mercury is squaring your North Node, creating mild friction between how you think and where your soul is calling you to grow. A thought pattern, conversational habit, or belief may need to be revised before forward movement becomes clear.",
    ("Mercury", "North Node", "trine"):        "Mercury is flowing naturally into your North Node, aligning thought and communication with your growth direction. Ideas that feel both genuine and forward-pointing are available; conversations in this window can open real progress.",
    ("Mercury", "North Node", "opposition"):   "Mercury is opposite your North Node, sitting on your South Node, surfacing old mental habits and familiar ways of thinking. Ingrained ideas and past communication patterns are prominent — moving forward often requires a deliberate shift in perspective.",

    ("Mercury", "South Node", "conjunction"):  "Mercury is crossing your South Node, bringing familiar mental patterns, old ideas, and habitual ways of communicating to the surface. Past perspectives and comfortable thinking styles are easy to access — useful for recognizing what has crystallized into habit rather than genuine understanding.",
    ("Mercury", "South Node", "sextile"):      "Mercury is gently supporting your South Node, making past knowledge and familiar ways of thinking easy to draw on. Use what you know well while staying open to information that may not fit neatly into existing frameworks.",
    ("Mercury", "South Node", "square"):       "Mercury is squaring your South Node, creating friction between present communication and past mental patterns. An old way of thinking or speaking may be getting in the way of something new — the tension is useful for naming it.",
    ("Mercury", "South Node", "trine"):        "Mercury is flowing easily into your South Node, making established ideas and comfortable communication styles feel effortless. The gift is real access to accumulated knowledge; the risk is mistaking familiarity for adequacy.",
    ("Mercury", "South Node", "opposition"):   "Mercury is opposite your South Node — touching your North Node — lending fresh thinking and forward-oriented communication to this window. Ideas that feel new or slightly unfamiliar may carry the most useful direction right now.",

    # Transiting Venus → Nodes
    ("Venus", "North Node", "conjunction"):  "Venus is crossing your North Node, bringing love, beauty, and relational connection into direct contact with your soul's growth direction. Meaningful encounters or new values that feel both attractive and forward-pointing are especially available in this window.",
    ("Venus", "North Node", "sextile"):      "Venus is supporting your North Node with easy relational and aesthetic energy. Connections that feel genuine and growth-oriented flow naturally — a good window for opening to love or beauty that actually serves your evolution rather than just comfort.",
    ("Venus", "North Node", "square"):       "Venus is squaring your North Node, creating friction between what feels pleasurable or relationally comfortable and where your soul is calling you to grow. A relationship, value, or attachment may be gently tested against your larger life direction.",
    ("Venus", "North Node", "trine"):        "Venus is flowing naturally into your North Node, making relational warmth and forward movement feel aligned. Connections made or deepened in this window tend to support growth rather than reinforce familiar patterns — love and destiny feel briefly in step.",
    ("Venus", "North Node", "opposition"):   "Venus is opposite your North Node — touching your South Node — drawing attention to familiar relational patterns and comfort-seeking in love. Old attachment styles are prominent; the invitation is toward more evolving forms of connection.",

    ("Venus", "South Node", "conjunction"):  "Venus is crossing your South Node, illuminating familiar relational patterns and past-life values around love and beauty. Old attachments, ingrained tastes, and comfortable ways of relating resurface — a moment for recognizing what has calcified into habit in your relationship world.",
    ("Venus", "South Node", "sextile"):      "Venus is gently supporting your South Node, making past relational gifts and familiar ways of connecting feel accessible and pleasant. Draw on genuine relational warmth while remaining open to how love and values are being asked to grow.",
    ("Venus", "South Node", "square"):       "Venus is squaring your South Node, generating friction between comfort in love and the need for relational growth. An old pattern in how you relate or attract may be creating drag — the friction is pointing at it.",
    ("Venus", "South Node", "trine"):        "Venus is flowing into your South Node, making familiar relationship patterns and comfortable pleasures feel effortless and appealing. The ease is genuine, but the invitation is to notice when comfortable love substitutes for the more demanding work of growth.",
    ("Venus", "South Node", "opposition"):   "Venus is opposite your South Node — touching your North Node — pulling love, values, and relational style toward their growing edge. What the soul is learning about connection may feel slightly unfamiliar; that discomfort is the signal that real growth is underway.",

    # Transiting Mars → Nodes
    ("Mars", "North Node", "conjunction"):  "Mars is crossing your North Node, delivering a surge of drive and initiative directly into your soul's growth direction. Energy for action is available, and actions taken now have a way of orienting life forward. Move deliberately rather than reactively.",
    ("Mars", "North Node", "sextile"):      "Mars is supporting your North Node with easy active energy, making it straightforward to take steps toward your growth direction. Effort toward forward-facing goals meets less resistance than usual — a useful window for pushing through inertia.",
    ("Mars", "North Node", "square"):       "Mars is squaring your North Node, generating friction between how you are currently asserting yourself and where your soul is growing. Old action patterns may be getting in the way; the tension is naming where drive and direction need to be realigned.",
    ("Mars", "North Node", "trine"):        "Mars is flowing naturally into your North Node, aligning physical drive with your evolutionary direction. Action taken in this window tends to advance your soul's purpose rather than reinforce comfortable habit — a good period for decisive forward movement.",
    ("Mars", "North Node", "opposition"):   "Mars is opposite your North Node, sitting on your South Node, activating familiar patterns of assertion and old fighting styles. Notice what gets triggered and whether those habitual responses still serve where you are going.",

    ("Mars", "South Node", "conjunction"):  "Mars is crossing your South Node, stirring up deeply ingrained patterns of drive, assertion, and conflict from the past. Old ways of fighting, pushing, or seeking what you want resurface with force — a moment to examine whether those strategies are still appropriate or just familiar.",
    ("Mars", "South Node", "sextile"):      "Mars is gently supporting your South Node, making past action patterns and familiar assertive styles feel accessible and effective. Old strengths in initiative are available for current tasks, though the invitation remains toward new ways of moving through the world.",
    ("Mars", "South Node", "square"):       "Mars is squaring your South Node, generating friction with old patterns of assertion or impulsivity. A habitual way of fighting or pushing may be creating unnecessary resistance — the tension is pointing at what needs to be released or transformed.",
    ("Mars", "South Node", "trine"):        "Mars is flowing easily into your South Node, making old assertive patterns and familiar drives feel natural and effective. Past strengths are accessible — genuinely useful, though worth questioning whether the old approach still fits the current situation.",
    ("Mars", "South Node", "opposition"):   "Mars is opposite your South Node — touching your North Node — directing drive and initiative toward your soul's growing edge. Energy is available for genuine forward movement, and actions taken in this window can meaningfully advance your evolutionary direction.",

    # Transiting Jupiter → Nodes
    ("Jupiter", "North Node", "conjunction"):  "Jupiter is crossing your North Node in a significant alignment of expansion and soul purpose. Growth and opportunity arrive through paths that are genuinely forward-facing rather than merely comfortable — this is a meaningful window for movement toward your larger life direction.",
    ("Jupiter", "North Node", "sextile"):      "Jupiter is supporting your North Node with easy expansive energy, opening doors that lead toward your growth direction. Opportunities feel available without excessive effort — a good window to say yes to possibilities that feel both promising and forward-pointing.",
    ("Jupiter", "North Node", "square"):       "Jupiter is squaring your North Node, creating friction between the desire for expansion and your soul's actual growth direction. The urge to grow may be real, but the direction or method may need recalibration before the expansion serves genuine purpose.",
    ("Jupiter", "North Node", "trine"):        "Jupiter is flowing generously into your North Node, making expansion and forward movement feel natural and abundant. Good fortune that arrives in this window tends to support your evolutionary path — the luck is real, and it is pointing somewhere worth following.",
    ("Jupiter", "North Node", "opposition"):   "Jupiter is opposite your North Node, touching your South Node, expanding familiar territory, old beliefs, and past-life abundance. The gifts are real but may reinforce comfort over growth; the invitation is toward forward-facing expansion rather than simply more of what is already known.",

    ("Jupiter", "South Node", "conjunction"):  "Jupiter is crossing your South Node, expanding and amplifying past-life gifts, old belief systems, and familiar forms of abundance. The resources of the past feel especially available — valuable when used as foundations for growth, potentially limiting when they become the destination.",
    ("Jupiter", "South Node", "sextile"):      "Jupiter is gently supporting your South Node, making past gifts, skills, and familiar abundance feel generous and accessible. Old knowledge and ingrained wisdom are easy to draw on; use them as springboards for new development rather than resting places.",
    ("Jupiter", "South Node", "square"):       "Jupiter is squaring your South Node, creating friction with old belief systems, past abundance, or ingrained optimism. A comfortable but limiting worldview may be generating tension; the expansion being called for requires leaving some familiar philosophical ground behind.",
    ("Jupiter", "South Node", "trine"):        "Jupiter is flowing easily into your South Node, amplifying past gifts, old wisdom, and familiar forms of good fortune. Genuine abundance is available through established channels — enjoyable and real, though the most meaningful growth often lives just beyond what has always worked.",
    ("Jupiter", "South Node", "opposition"):   "Jupiter is opposite your South Node — touching your North Node — directing expansion and optimism toward your soul's growing edge. The most meaningful opportunity right now is likely the one that feels less familiar, slightly bigger than comfortable, and genuinely forward-facing.",

    # Transiting Saturn → Nodes
    ("Saturn", "North Node", "conjunction"):  "Saturn is crossing your North Node in a sobering activation of your soul's growth direction. This transit asks you to build seriously toward your evolutionary purpose — not through inspiration alone, but through discipline, patience, and willingness to do the work growth actually requires.",
    ("Saturn", "North Node", "sextile"):      "Saturn is supporting your North Node with steady, structured energy. Effort applied toward your growth direction in this window tends to build something lasting — the work may be unglamorous, but the foundation being laid is solid.",
    ("Saturn", "North Node", "square"):       "Saturn is squaring your North Node, applying serious pressure to the gap between where you are and where your soul is growing. Obligations or reality checks are forcing a reckoning with your evolutionary direction — the friction is demanding genuine maturity.",
    ("Saturn", "North Node", "trine"):        "Saturn is flowing steadily into your North Node, lending discipline and structural support to your growth direction. Efforts made now toward your soul's purpose are likely to produce durable results — a good window for serious, long-term investment in what you are becoming.",
    ("Saturn", "North Node", "opposition"):   "Saturn is opposite your North Node, sitting on your South Node, bringing its weight down on old karmic obligations, past structures, and inherited limitations. What has been carried too long from the past may be making forward movement genuinely difficult; something needs to be put down.",

    ("Saturn", "South Node", "conjunction"):  "Saturn is crossing your South Node in a significant karmic activation. Old obligations, past structures, and inherited limitations are being confronted directly. This transit often marks a reckoning with what has been carried too long — duties completed, old patterns formalized and then released.",
    ("Saturn", "South Node", "sextile"):      "Saturn is gently supporting your South Node, making past discipline, old structures, and familiar responsibilities feel manageable and useful. Past competence and ingrained work ethics are available — apply them deliberately while staying open to which structures still deserve to be built upon.",
    ("Saturn", "South Node", "square"):       "Saturn is squaring your South Node, applying friction to old structures, inherited obligations, and familiar ways of taking responsibility. A pattern of duty or limitation that has outlived its usefulness is being pressured — the discomfort is pointing at what needs to be restructured or released.",
    ("Saturn", "South Node", "trine"):        "Saturn is flowing into your South Node, making old disciplines and inherited competence feel dependable and accessible. Past mastery is available as a genuine resource — the key is using it to build forward rather than simply to reproduce the familiar.",
    ("Saturn", "South Node", "opposition"):   "Saturn is opposite your South Node — touching your North Node — applying its demanding energy to your soul's growing edge. The invitation is to take your growth direction as seriously as you have historically taken your obligations: with structure, commitment, and willingness to do the work.",

    # Transiting Uranus → Nodes
    ("Uranus", "North Node", "conjunction"):  "Uranus is crossing your North Node in a sudden, destabilizing activation of your soul's growth direction. Unexpected changes or awakenings may arrive that, though unsettling, are oriented toward genuine evolution. The faster you release the old, the more clearly the new direction becomes.",
    ("Uranus", "North Node", "sextile"):      "Uranus is supporting your North Node with liberating, innovative energy, opening unexpected pathways toward your growth direction. Original thinking and unconventional moves can advance your evolution now — a good window to experiment with something genuinely new.",
    ("Uranus", "North Node", "square"):       "Uranus is squaring your North Node, delivering sudden friction between stability and your soul's evolutionary direction. Disruptions may feel destabilizing, but they are forcing a confrontation with what needs to change before genuine forward movement is possible.",
    ("Uranus", "North Node", "trine"):        "Uranus is flowing freely into your North Node, bringing a liberating current of change into alignment with your growth direction. The unusual and unexpected can carry you forward right now — the changes may feel surprisingly right.",
    ("Uranus", "North Node", "opposition"):   "Uranus is opposite your North Node, sitting on your South Node, disrupting old comfort zones, past rebellions, and familiar unconventionalities. The disruption is loosening the grip of whatever has been holding you in the past, even when the path forward isn't yet clear.",

    ("Uranus", "South Node", "conjunction"):  "Uranus is crossing your South Node, suddenly destabilizing old patterns, past-life rebellions, and familiar forms of independence. What has been the source of your sense of originality is being shaken loose — liberating in the long run, disorienting in the short.",
    ("Uranus", "South Node", "sextile"):      "Uranus is gently activating your South Node, making past innovations and familiar forms of originality feel fresh and accessible. Old unconventional gifts are available without major disruption — a good window for applying originality in service of forward movement.",
    ("Uranus", "South Node", "square"):       "Uranus is squaring your South Node, generating sudden friction with ingrained patterns of rebellion or disruption. An old way of being unconventional may itself be creating instability; the tension is pointing at what needs to evolve in how you relate to change.",
    ("Uranus", "South Node", "trine"):        "Uranus is flowing into your South Node, liberating old patterns of originality and making past-life independence feel easy and electric. The access to unconventional thinking is real — direct that energy forward rather than into the same comfortable forms of rebellion.",
    ("Uranus", "South Node", "opposition"):   "Uranus is opposite your South Node — on your North Node — bringing sudden awakening energy into contact with your soul's growth direction. Disruptions may feel abrupt, but they have a way of pointing exactly toward where genuine evolution is waiting.",

    # Transiting Neptune → Nodes
    ("Neptune", "North Node", "conjunction"):  "Neptune is crossing your North Node in a slow, dissolving activation of your soul's growth direction. Spiritual sensitivity and a longing for meaning are being woven into your evolutionary path — though the direction may feel unclear for a time before it becomes genuinely luminous.",
    ("Neptune", "North Node", "sextile"):      "Neptune is gently supporting your North Node, opening a spiritual current that aligns with your growth direction. Intuition and compassion are available in service of your soul's purpose right now — follow the feeling of genuine meaning over logical certainty.",
    ("Neptune", "North Node", "square"):       "Neptune is squaring your North Node, dissolving clarity around your growth direction. Confusion or disillusionment may cloud the path forward, but the fog is purposeful — it is dissolving what was mistaken for the goal before the real one comes into focus.",
    ("Neptune", "North Node", "trine"):        "Neptune is flowing gently into your North Node, giving a spiritual, intuitive quality to forward movement. The path ahead feels less rational and more felt — dreams, synchronicities, and quiet knowing are pointing the way with unusual clarity.",
    ("Neptune", "North Node", "opposition"):   "Neptune is opposite your North Node, touching your South Node, suffusing familiar spiritual patterns and past-life longings with a dissolving quality. Old ideals and spiritual comforts may be dissolving, which, though disorienting, opens space for a more genuine spiritual direction.",

    ("Neptune", "South Node", "conjunction"):  "Neptune is crossing your South Node in a long, dissolving activation of past-life spiritual patterns and deep karmic longings. What has been carried from before — spiritual gifts and spiritual wounds alike — is being gently dissolved. The process is gradual and not always comfortable.",
    ("Neptune", "South Node", "sextile"):      "Neptune is gently supporting your South Node, making past spiritual gifts and familiar forms of compassion accessible in a soft, flowing way. Past-life sensitivity is available — draw on it without retreating into old forms of escapism or idealization.",
    ("Neptune", "South Node", "square"):       "Neptune is squaring your South Node, generating gentle but persistent friction with old spiritual patterns or ingrained forms of self-dissolution. Something about the old way of seeking transcendence may be creating confusion — clarity and discernment are being asked for.",
    ("Neptune", "South Node", "trine"):        "Neptune is flowing easily into your South Node, making past spiritual gifts and familiar forms of sensitivity feel natural and available. Old spiritual ease is accessible — let it serve genuine compassion and forward-moving spirituality rather than retreat and diffusion.",
    ("Neptune", "South Node", "opposition"):   "Neptune is opposite your South Node — touching your North Node — drawing spiritual sensitivity into contact with the soul's growing edge. What is dissolving in the familiar may be exactly what needs to dissolve so that something more genuinely spiritual can take its place.",

    # Transiting Pluto → Nodes
    ("Pluto", "North Node", "conjunction"):  "Pluto is crossing your North Node in a profound and rarely experienced transit. A deep, irreversible transformation is being applied directly to your soul's growth direction. What you are becoming is being forged under genuine pressure — the old self cannot survive what the new direction requires.",
    ("Pluto", "North Node", "sextile"):      "Pluto is gently supporting your North Node, offering the power of transformation in service of your growth direction. Deep change is available without catastrophic disruption — a good window for deliberate shedding of what no longer serves your soul's forward path.",
    ("Pluto", "North Node", "square"):       "Pluto is squaring your North Node, applying deep, relentless pressure to the gap between the old self and the soul's growing edge. What stands in the way of your evolution is being confronted at a fundamental level — resistance only intensifies what transformation will eventually accomplish anyway.",
    ("Pluto", "North Node", "trine"):        "Pluto is flowing powerfully into your North Node, aligning depth and transformation with your growth direction. The change available now is not superficial — what shifts in this window tends to be lasting and oriented toward genuine soul development.",
    ("Pluto", "North Node", "opposition"):   "Pluto is opposite your North Node, sitting on your South Node, targeting the deep roots of past-life patterns and buried soul material. The transformation happening underground is ultimately clearing the ground for who you are meant to become.",

    ("Pluto", "South Node", "conjunction"):  "Pluto is crossing your South Node in a rare and profound karmic excavation. Deep past-life material, buried compulsions, and inherited soul-level patterns are being forced to the surface for confrontation and transformation. This is not a comfortable transit, but it is a thoroughly clearing one.",
    ("Pluto", "South Node", "sextile"):      "Pluto is gently supporting your South Node, offering an opportunity to consciously transform past-life patterns and old compulsions. Profound depth is accessible without catastrophic disruption — a deliberate approach to clearing old material can be unusually effective right now.",
    ("Pluto", "South Node", "square"):       "Pluto is squaring your South Node, driving deep friction into past-life patterns and entrenched soul-level material. Something buried and long-carried is being brought to the surface with significant force — what is erupting is asking to be transformed, not suppressed.",
    ("Pluto", "South Node", "trine"):        "Pluto is flowing into your South Node, bringing deep transformative energy into alignment with past-life material. Old patterns and ingrained soul-level habits can be consciously transformed in this window — the depth is available and the process, though demanding, flows with unusual clarity.",
    ("Pluto", "South Node", "opposition"):   "Pluto is opposite your South Node — on your North Node — directing its transformative power toward your soul's growing edge. What is being destroyed in the underground of who you have been is exactly what needs to go so that the soul can move toward its genuine destination.",
}

# ── Lookup helpers ────────────────────────────────────────────────────────────

def natal_aspect_text(p1: str, p2: str, aspect: str) -> str:
    return NATAL_ASPECT.get((*sorted([p1, p2]), aspect), "")


def planet_in_sign_text(planet: str, sign: str) -> str:
    return PLANET_IN_SIGN.get((planet, sign), "")


def planet_in_house_text(planet: str, house: int) -> str:
    return PLANET_IN_HOUSE.get((planet, house), "")


def transit_in_sign_text(planet: str, sign: str) -> str:
    return TRANSIT_IN_SIGN.get((planet, sign), "")


def sky_aspect_text(p1: str, p2: str, aspect: str) -> str:
    return SKY_ASPECT.get((*sorted([p1, p2]), aspect), "")


def transit_to_natal_text(transit_planet: str, natal_planet: str, aspect: str) -> str:
    return TRANSIT_TO_NATAL.get((transit_planet, natal_planet, aspect), "")
