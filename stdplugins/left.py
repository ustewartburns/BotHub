"""COMMAND : .left"""

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("left"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Why Are Some People Left-Handed?\n\n`Being a righty or a lefty could be linked to variations in a network of genes that influence right or left asymmetries in the body and brain.\n\nFor the left-handed people of the world, life isn’t easy.\nThroughout much of history, massive stigmas attached to left-handedness meant they were singled out as everything from unclean to witches.\nIn Medieval times, writing with your left-hand was a surefire way to be accused of being possessed by the devil; after all, the devil himself was thought to be a lefty.\nThe world has gotten progressively more accepting of left-handed folk,\nbut there are still some undeniable bummers associated with a left-handed proclivity: desks and spiral notebooks pose a constant battle,\nscissors are all but impossible to use and–according to some studies–life-expectancy might be lower than for right-handed people.\n\nWhat makes humanity’s bias against lefties all the more unfair is that left-handed people are born that way.\nIn fact, scientists have speculated for years that a single gene could control a left-right preference in humans.\nUnfortunately, they just couldn’t pinpoint exactly where the gene might lie.\n\nNow, in a paper published SEPTEMBER 12, 2013 in PLOS Genetics a group of researchers have identified a network of genes that relate to handedness in humans.\nWhat’s more, they’ve linked this preference to the development of asymmetry in the body and the brain.\n\nIn previous studies, the researchers observed that patients with dyslexia exhibited a correlation between the gene PCSK6 and handedness.\nBecause every gene has two copies (known as alleles), every gene has two chances for mutation;\nwhat the researches found was that dyslexic patients with more variance in PCSK6–meaning that one or both of their PSCK6 alleles had mutated–were more likely to be right-handed.\n\nThe research team found this especially interesting, because they knew that PCSK6 was a gene directly associated with the development of left-right asymmetry in the body.\nThey weren’t sure why this would present itself only in dyslexic patients, as dyslexia and handedness are not related.\nSo the team expanded the study to include more than 2,600 people who don’t have dyslexia.\n\nThe study found that PCSK6 didn’t work alone in affecting handedness in the general population.\nOther genes, also responsible for creating left-right asymmetry in the body, were strongly associated with handedness.\nLike PCSK6, the effect that these genes have on handedness depends on how many mutations the alleles undergo.\nEach gene has the potential for mutation–the more mutations a person has in any one direction (toward right handedness or left handedness)\nthe more likely they are to use that hand as their dominant hand, or so the researchers speculate.\n\nThe hypothesis is a logical response to a key question:\n If handedness is genetic and if right-handedness is such a dominant trait, why hasn’t left-handedness been forced out of the genetic pool?\nIn reality, the research suggests that handedness could be more subtle than simple “dominant” or “recessive” traits–a whole host of genes might play significant roles.\n\nWhat’s especially exciting is that these genes all relate to the development of left-right asymmetry in the body and brain,\ncreating a strong case for correlation between the development of this symmetry and the development of handedness.\nDisrupting any of these genes could lead to serious physical asymmetry,\nlike situs inversus, a condition where the body’s organs are reversed (heart on the right side of the body, for example).\nIn mice, the disruption of PCSK6 resulted in serious abnormal positioning of organs in their bodies.\n\nIf physical asymmetry is related to handedness, then people with situs inversus should favor one hand more often than what you’d find in the general population.\nStudies show that this isn’t the case–individuals with this condition mirror the general population’s split in handedness–leading the researchers to postulate that while these genes certainly influence handedness,\nthere might be other mechanisms in the body that compensate for handedness in the event of major physiological asymmetries.\n\nOther animals, such as polar bears or chimpanzees, also have handedness\n–-chimpanzees have been known to prefer one hand to the other when using tools or looking for food,\nbut the split within a population hangs around 50/50.\nHumans are the only species that show a truly distinct bias toward one hand or the other:\na 90/10 right/left split throughout the population.\n\nOne predominant hypothesis for this bias relates to another distinct human trait: language ability.\nLanguage ability is split between the different hemispheres of the brain,\nmuch like handedness, which suggests that handedness became compartmentalized along with language ability,\nFor most, the parts of the brain that govern language are are present in the left-side of the brain–these people tend to be right-handed.\nThe few that have language skills focused in the right side of the brain tend to be left-handed.\n\nHowever, William Brandler, a PhD student at Oxford University and the paper’s lead author, isn’t convinced that this theory holds much stock,\nas correlations between language and handedness in research aren’t well established.\nBrandler is more interested in learning how the permutations and combinations of genetic mutations play into humans’ likelihood to be right-handed.\n“Through understanding the genetics of handedness, we might be able to understand how it evolved,”\nhe says. “Once we have the full picture of all the genes involved,\nand how they interact with other genes,\nwe might be able to understand how and why there is such a bias.”\n\nAnd he’s confident that even if environmental factors (like the continued hatred of lefties by two-thirds of the world) place pressure on handedness,\nany baseline bias still boils down to genetics.\n“People think it’s just an environmental thing, but you’ve got to think, why is there that initial bias in the first place,\nand why do you see that bias across all societies?\nWhy aren’t there societies where you see a bias to the left?” Brandler asks.\n“There is a genetic component to handedness, hundreds of different genetic variants,\nand each one might push you one way or the other,\nand it’s the type of variance, along with the environment you’re in\nand the pressures acting on you, which affect your handedness.”\n\nBut until a larger population can be tested–hundreds of thousands,\nby Brandler’s estimates–a full genetic map of what controls handedness\nand why our population isn’t evenly split between righties and lefties can’t be determined.\n“It’s going to take a bit of time before these materialize—but it will happen,” Brandler says.\n“There’s been a whole revolution in genetics such that, in a few years time,\nwe’re really going to start to understand the genetic basis of complex traits.”\n\nThe former President United States Barack Obama is left-handed, as well as at least six former presidents.\n\n`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
