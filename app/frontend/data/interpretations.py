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


# ── Lookup helpers ────────────────────────────────────────────────────────────

def natal_aspect_text(p1: str, p2: str, aspect: str) -> str:
    return NATAL_ASPECT.get((*sorted([p1, p2]), aspect), "")


def planet_in_sign_text(planet: str, sign: str) -> str:
    return PLANET_IN_SIGN.get((planet, sign), "")


def planet_in_house_text(planet: str, house: int) -> str:
    return PLANET_IN_HOUSE.get((planet, house), "")
