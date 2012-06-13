# -*- coding: utf-8 -*-
from bottu import flags

def faq(env, key):
    result = env.get(key, None)
    if result:
        env.msg("%s: %s" % (key, result))
    else:
        env.msg("%s: No entry found, try !listfaq to see a list of entries." % key)

def addfaq(env, key, value):
    if env.store(key, ' '.join(value)):
        env.msg("%s added" % key)
    else:
        env.msg("Failed to add %s :(" % key)

def delfaq(env, key):
    if env.delete(key):
        env.msg("%s deleted" % key)
    else:
        env.msg("Failed to delete %s :(" % key)


def listfaq(env):
    keys = env.keys()
    env.msg("FAQ entries: %s" % (', '.join(keys) if keys else 'No entries yet'))

def register(app, conf):
    plugin = app.add_plugin('FAQ')
    addfaq_perm = plugin.add_permission('addfaq', default=flags.OPERATOR)
    delfaq_perm = plugin.add_permission('delfaq', default=flags.VOICE)

    faq_cmd = plugin.add_command('faq', 'Show a FAQ entry')
    faq_cmd.add_argument('key')
    faq_cmd.bind(faq)

    addfaq_cmd = plugin.add_command('addfaq', 'Add a FAQ entry')
    addfaq_cmd.add_argument('key')
    addfaq_cmd.add_argument('value', nargs='+')
    addfaq_cmd.guard(addfaq_perm)
    addfaq_cmd.bind(addfaq)

    delfaq_cmd = plugin.add_command('delfaq', 'Remove a FAQ entry')
    delfaq_cmd.add_argument('key')
    delfaq_cmd.guard(delfaq_perm)
    delfaq_cmd.bind(delfaq)

    listfaq_cmd = plugin.add_command('listfaq', 'List all FAQ entries')
    listfaq_cmd.bind(listfaq)
